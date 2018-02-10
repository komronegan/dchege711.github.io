import requests
import json
import os
from pprint import pprint

SMMRY_API_KEY = os.environ["SMMRY_API_KEY"]

def get_summary(text, num_sentences=4, num_keywords=5):
    r = requests.post(
        "https://api.smmry.com",
        params = { 
            "SM_API_KEY": SMMRY_API_KEY,
            "SM_LENGTH": num_sentences,
            "sm_api_input": text,
            "SM_KEYWORD_COUNT": num_keywords
        },
        data = json.dumps(text)
    )
    
    pprint(json.loads(r.text))
    
    return r
    
