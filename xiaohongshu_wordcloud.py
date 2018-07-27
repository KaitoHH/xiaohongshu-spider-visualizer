import csv

import jieba.analyse
import numpy as np
from PIL import Image
from wordcloud import WordCloud

text = ''
with open('xiaohongshu.csv', encoding='utf-8') as file:
    count = 0
    for line in csv.reader(file):
        count += 1
        print(count)
        # if count > 100:
        #     break
        content = line[9]
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=False, allowPOS=('n'))
        text += ' '.join(tags) + ' '
        # cut_list = pseg.cut(content)
        # for word, flag in cut_list:
        #     if 'n' in flag:
        #         text += word + ' '

print(text)

mask = np.array(Image.open('mask.png'))

wordcloud = WordCloud(background_color='white', mask=mask, font_path='font/msyh.ttc',
                      color_func=lambda *args, **kwargs: (0xff, 0x28, 0x43),
                      # contour_width=2,
                      # contour_color='#ff8f8f',
                      max_words=1000,
                      scale=3).generate(text)

image = wordcloud.to_image()
wordcloud.to_file('wordcloud.png')
image.show()
