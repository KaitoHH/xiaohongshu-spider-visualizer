import os
import time

import redis
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from app import app

options = Options()
# options.add_argument('headless')
# options.add_argument('no-sandbox')
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(options=options)
browser.maximize_window()
wait = WebDriverWait(browser, 20)

red = redis.StrictRedis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379/1'))


@app.task
def get_detailed(item_id, title, likes=None, user_id=None):
    print(item_id)
    item_url = 'https://www.xiaohongshu.com/discovery/item/' + item_id
    browser.get(item_url)
    time.sleep(2)
    content = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'content'))).text
    # content = browser.find_element_by_class_name('content').text
    likes = browser.find_element_by_class_name('like').text
    comments = browser.find_element_by_class_name('comment').text
    stars = browser.find_element_by_class_name('star').text
    notes = browser.find_element_by_class_name('note').text
    fans = browser.find_element_by_class_name('fans').text
    collect = browser.find_element_by_class_name('collect').text
    red.hmset('item:' + item_id,
              {'title': title, 'content': content, 'likes': likes, 'comments': comments, 'stars': stars, 'notes': notes,
               'fans': fans, 'collect': collect, 'user_id': user_id})
    return title, content, likes, comments, stars, notes, fans, collect, user_id


if __name__ == '__main__':
    print(get_detailed('5b51d0fd07ef1c6ba98285cd', 'title'))
