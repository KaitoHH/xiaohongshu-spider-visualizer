import requests

from xiaohongshu import get_detailed, headers

session = requests.Session()
session.headers.update(headers)

payload = {'page_size': '20', 'oid': 'recommend', 'page': 1}
page = 0
id_list = []
while True:
    page += 1
    payload['page'] = page
    print('page =', page)
    r = session.get('https://www.xiaohongshu.com/web_api/sns/v2/homefeed/notes', params=payload)
    response = r.json()
    if not response['data']:
        break
    for item in response['data']:
        id_list.append(item['id'])
        get_detailed.delay(item['id'], item['desc'], item['likes'], item['user']['id'])
