import requests
import json
import os
from pprint import pprint
from google.cloud import storage, exceptions
import config
from datetime import timedelta

# Initialize the Google Cloud Client at the first invocation of this script.
storage_client = storage.Client()
try:
    bucket = storage_client.get_bucket("temp_storage_for_smmry_docs")
except exceptions.NotFound:
    bucket = storage_client.create_bucket("temp_storage_for_smmry_docs")

def get_summary(text_to_summarized, blog_name, num_sentences=7, num_keywords=5):
    """
    Get a summary of a block of text from SMMRY's API 
    
    param(s):
    text_to_summarized  (str)   The text that should be summarized
    blog_name           (str)   The name of the original blog.
    num_sentences       (int)   Number of sentences to be included in the summary 
    num_keywords        (int)   Number of keywords to be extracted from the text
    
    return(s):
    True and a string containing the summary if the request is successful.
    False and a string containing the error message if request is unsuccessful.
     
    """
    
    html_file_name = write_to_html(text_to_summarized, html_name=blog_name+".html")
    html_url = get_html_url(html_file_name)
    
    r = requests.post(
        "https://api.smmry.com",
        params = { 
            "SM_API_KEY": config.SMMRY_API_KEY,
            "SM_LENGTH": num_sentences,
            "SM_KEYWORD_COUNT": num_keywords,
            "SM_URL": html_url
        }
    )
    
    response_as_json = json.loads(r.text)
    try:
        return True, response_as_json["sm_api_message"]
    else:
        return False, response_as_json["sm_api_message"]
    
def write_to_html(data, html_name="content.html"):
    """
    Create a .html file with the blog post's contents as the body.
    Return the filename of this html file.
    
    param(s):
    data        (str)   e.g. "Introduction to Tensorflow..."
    html_name   (str)   e.g. "desired_html_file.html"
    
    return(s):
    html_name   (str)   Same as the incoming html_name, but a file also exists
                        in the same directory.
                        
    """
    output_file = open(html_name, 'w')
    output_file.write("<!DOCTYPE html><html><body><p>")
    output_file.write(data)
    output_file.write("</p></body></html>")
    
    return html_name

def get_html_url(html_file_name):
    """
    Upload the html to Google Cloud Storage and returns the public url of the item.
    Necessary because SMMRY's API for receiving blocks of texts isn't working.
    
    param(s):
    html_file   (str)   Must exist in current directory. e.g. "google_blog.html"
    
    return(s):
    url         (str)   The publicly accesible url of the html file.
    
    """
    file_blob = storage.blob.Blob(html_file_name, bucket)
    file_blob.upload_from_file(
        open(html_file, "rb"),
        content_type="text/html"
    )
    file_blob.make_public()
    return file_blob.public_url
    
