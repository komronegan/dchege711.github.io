import feedparser 
from pprint import pprint
import html2text
import smmry_client

google_developers_rss = "http://googledevelopers.blogspot.com/atom.xml"

rss_matcher = {
    "google_developers": google_developers_rss
}

# Initialize the html to plain text converter
h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True 


def get_new_stories(blog_name):
    try:
        entries = feedparser.parse(rss_matcher[blog_name])["entries"]
    except KeyError:
        raise KeyError("The provided blog name doesn't match any on file")
    
    """
    Available keys
    'id', 'guidislink', 'link', 'published', 'published_parsed', 'updated', 
    'updated_parsed', 'tags', 'title', 'title_detail', 'content', 'summary', 
    'links', 'authors', 'author_detail', 'href', 'author', 'gd_image', 
    'media_thumbnail', 'thr_total', 'feedburner_origlink'
    """
    
    link = entries[1]["link"]
    title = entries[1]["title"]
    content = h.handle(entries[1]["content"][0]["value"])
    summary = smmry_client.get_summary(content, blog_name)

def main():
    get_new_stories("google_developers")
    
if __name__ == "__main__":
    main()
