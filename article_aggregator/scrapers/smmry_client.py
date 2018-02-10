import requests
import json
import os
from pprint import pprint
from google.cloud import storage, exceptions
import config
from datetime import timedelta

# Initialize the Google Cloud Client 
storage_client = storage.Client()
try:
    bucket = storage_client.get_bucket("temp_storage_for_smmry_docs")
except exceptions.NotFound:
    bucket = storage_client.create_bucket("temp_storage_for_smmry_docs")

def get_summary(text, blog_name, num_sentences=7, num_keywords=5):
    html_file = write_to_html(text, html_name=blog_name+".html")
    html_url = get_html_url(html_file, blog_name)
    print(html_url)
    
    r = requests.post(
        "https://api.smmry.com",
        params = { 
            "SM_API_KEY": config.SMMRY_API_KEY,
            "SM_LENGTH": num_sentences,
            "SM_KEYWORD_COUNT": num_keywords,
            "SM_URL": html_url
        },
        data = json.dumps(text)
    )
    
    pprint(json.loads(r.text))
    
    return r
    
def write_to_html(data, html_name="content"):
    output_file = open(html_name, 'w')
    html_content = """
    <!DOCTYPE html>
    <html>
    <body>
    <p>
    
    """
    output_file.write("<!DOCTYPE html><html><body><p>")
    output_file.write(data)
    output_file.write("</p></body></html>")
    
    return html_name

def get_html_url(html_file, blog_name):
    file_blob = storage.blob.Blob(blog_name, bucket)
    file_blob.upload_from_file(
        open(html_file, "rb"),
        content_type="text/html"
    )
    file_blob.make_public()
    return file_blob.public_url
    
