"""
Get new content from the Google Developers Blog.

Side Note: The guys at Google are kind enough to provide an XML file :-)

"""

import feedparser
import datetime

def get_new_posts(relevant_day):
    """
    Return a list of all the posts made on the specified day.
    
    params(s):
    date    (datetime.date)     Day for which the blog posts should be obtained
    
    return(s):
    List of dicts, each having the keys: title, publication_date, content, url
    
    """
    google_developers_rss = "http://googledevelopers.blogspot.com/atom.xml"
    try:
        entries = feedparser.parse(google_developers_rss)["entries"]
    except KeyError:
        raise KeyError("The provided blog name doesn't match any on file")
    
    """
    Available keys
    'id', 'guidislink', 'link', 'published', 'published_parsed', 'updated', 
    'updated_parsed', 'tags', 'title', 'title_detail', 'content', 'summary', 
    'links', 'authors', 'author_detail', 'href', 'author', 'gd_image', 
    'media_thumbnail', 'thr_total', 'feedburner_origlink'
    """
    
    # link = entries[1]["link"]
    # title = entries[1]["title"]
    # content = h.handle(entries[1]["content"][0]["value"])
    
    for entry in entries:
        print(entry["published"])
