# https://qiita.com/ichi_zamurai/items/60d2480edcb68a76aeb6
# から引用,変更
import MeCab
import re
import os

# ディレクトリの変更
os.chdir('/workspaces/Markov/Markov_db_1')

text = open("./0_start.txt","r").read()

# Replace Bad Symbols for markovify to function
# Refer: https://github.com/jsvine/markovify/issues/84
table = str.maketrans({
        # '\n': '',
        # '\r': '',
        '(': '（',
        ')': '）',
        '[': '［',
        ']': '］',
        '"':'”',
        "'":"’",
    })
text = text.translate(table).split()
# url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
url_pattern = r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"


for i in range(10): # remove()を使ってるから10回くらいやると綺麗になった
    for line in text:
        if re.match(url_pattern, line): # URL
            text.remove(line)
        elif bool(re.search(r'[a-zA-Z0-9]', line)):
            text.remove(line)
        elif re.match('^@.*', line):
            text.remove(line)
        elif re.match('.*,$', line):
            text.remove(line)
        elif re.match('^#.*', line):
            text.remove(line)
        elif re.match('RT', line):
            text.remove(line)

# Parse text using MeCab
# m = MeCab.Tagger('-r /etc/mecabrc -Owakati')
# 辞書を使用（新しいの）
m = MeCab.Tagger('-r /etc/mecabrc -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd -Owakati')

# -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd
f = open('./tweets.txt', 'w')
for line in text:
    splited_line = m.parse(line)
    f.write(str(splited_line))
f.close()
