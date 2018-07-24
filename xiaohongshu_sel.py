from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from app import app

options = Options()
options.add_argument('headless')
options.add_argument('no-sandbox')
browser = webdriver.Chrome(options=options)
browser.maximize_window()
wait = WebDriverWait(browser, 10)


@app.task
def get_detailed(item_id, title, likes=None, user_id=None):
    item_url = 'https://www.xiaohongshu.com/discovery/item/' + item_id
    browser.get(item_url)

    content = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'content'))).text
    # content = browser.find_element_by_class_name('content').text
    likes = browser.find_element_by_class_name('like').text
    comments = browser.find_element_by_class_name('comment').text
    stars = browser.find_element_by_class_name('star').text
    notes = browser.find_element_by_class_name('note').text
    fans = browser.find_element_by_class_name('fans').text
    collect = browser.find_element_by_class_name('collect').text
    return title, content, likes, comments, stars, notes, fans, collect, user_id


if __name__ == '__main__':
    print(get_detailed('5b51d0fd07ef1c6ba98285cd', 'title'))
