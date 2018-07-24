import requests

from xiaohongshu_sel import get_detailed

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
}
session = requests.Session()
session.headers.update(headers)

payload = {'page_size': '50', 'oid': 'cosmetics', 'page': 1}
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

session.close()
print(id_list)
print(len(id_list))
