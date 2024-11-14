import MeCab
import os

# ディレクトリの変更
os.chdir('/workspaces/Markov/Markov-Takkun')

mecab = MeCab.Tagger("-r /etc/mecabrc -Owakati")

# テキストファイルから内容を読み込み、形態素解析を実行
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 形態素解析を実行して、結果をスペース区切りでリスト化
tokens = mecab.parse(text).split()

# 形態素解析結果を表示
print("形態素解析結果:", tokens)

# トークンリストをスペース区切りの文字列に変換してファイルに書き込み
with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(' '.join(tokens))  # トークンをスペースで区切って書き込む

print("形態素解析結果がoutput.txtに保存されました。")