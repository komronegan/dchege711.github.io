from pprint import pprint
import html2text
import datetime

import smmry_client
import google_developers 

blog_script_matcher = {
    "google_developers": google_developers
}

# Initialize the html to plain text converter globally
h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True 
h.ignore_tables = True

def get_new_posts(blog_name):
    
    relevant_day = get_day("yesterday")
    try:
        new_posts = blog_script_matcher[blog_name].get_new_posts(relevant_day)
    except KeyError:
        raise KeyError("The provided blog name doesn't match any on file")
    
    # for post in new_posts:
        # print(post["title"], post["publication_date"])
        # content = h.handle(post["content"])
        # summary = smmry_client.get_summary(content, blog_name)
    
def get_day(desired_day):
    today = datetime.date.today()
    
    if desired_day == "today":
        return today
    elif desired_day == "yesterday":
        return today - datetime.timedelta(days=1)
    else:
        raise ValueError("Unsupported query was made.")

def main():
    get_new_posts("google_developers")
    
if __name__ == "__main__":
    main()
