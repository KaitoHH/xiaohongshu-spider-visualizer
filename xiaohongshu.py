import os

import redis
import requests
from bs4 import BeautifulSoup as Soup

from app import app

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
}
session = requests.Session()
session.headers.update(headers)

red = redis.StrictRedis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379/1'))


@app.task
def get_detailed(item_id, title, likes, user_id):
    ret_code = 0
    content = None
    item_url = 'https://www.xiaohongshu.com/discovery/item/' + item_id
    item_html = session.get(item_url)
    soup = Soup(item_html.text, 'html.parser')
    div = soup.find("div", class_="content")
    if div:
        content = div.text
        ret_code = 1
    red.hmset('item:' + item_id, {'title': title, 'content': content, 'likes': likes, 'user_id': user_id})
    print(item_id)
    return ret_code
