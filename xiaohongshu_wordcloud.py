import csv

import jieba.analyse
from wordcloud import WordCloud

text = ''
with open('xiaohongshu.csv', encoding='utf-8') as file:
    count = 0
    for line in csv.reader(file):
        count += 1
        print(count)
        content = line[9]
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=False, allowPOS=('n'))
        text += ' '.join(tags) + ' '
        # cut_list = pseg.cut(content)
        # for word, flag in cut_list:
        #     if 'n' in flag:
        #         text += word + ' '

print(text)
wordcloud = WordCloud(font_path='font/msyh.ttc', width=1920, height=1080).generate(text)

image = wordcloud.to_image()
image.save('wordcloud.png')
image.show()
