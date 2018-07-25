import csv
import os

import redis

red = redis.StrictRedis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379/1'))


def decode(bytes_):
    return bytes_.decode('utf-8')


with open('xiaohongshu.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for key in red.keys('item*'):
        item = red.hgetall(key)
        row = [key[5:], item[b'title'], item[b'user_id'], item[b'likes'], item[b'comments'], item[b'stars'],
               item[b'notes'], item[b'fans'], item[b'collect'], item[b'content']]
        row = list(map(decode, row))
        print(row)
        writer.writerow(row)
