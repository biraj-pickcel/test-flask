from flask import request

from app.helpers.apify import start_crawling
from app.utils.validation import is_valid_url

def crawl():
    try:
        data = request.get_json()
    except:
        return {"success": False, "message": "provide a valid json"}
    
    url = data.get('url')
    if not url or not is_valid_url(url):
        return {"success": False, "message": "provide a valid URL"}, 400
    
    start_crawling(url)
    
    return {"success": True, "message": "crawl started"}