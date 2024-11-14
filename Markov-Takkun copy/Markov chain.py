import random
import os

# ディレクトリの変更
os.chdir('/workspaces/Markov/Markov-Takkun copy')

# 出力ファイル（output.txt）を読み込み
with open("output.txt", "r", encoding="utf-8") as file:
    text = file.read()

# スペース区切りでトークン化
tokens = text.split()

# マルコフ連鎖のための遷移辞書を作成
markov_chain = {}

# トークンペアを使って遷移確率を計算
for i in range(len(tokens) - 1):
    current_word = tokens[i]
    next_word = tokens[i + 1]
    
    if current_word not in markov_chain:
        markov_chain[current_word] = []
    
    markov_chain[current_word].append(next_word)

# 次に来る単語を予測する関数
def generate_text(start_word, length=100):
    current_word = start_word
    result = [current_word]
    
    while len(result) < length:  # 指定された長さに満たない場合
        if current_word not in markov_chain:
            break
        next_word = random.choice(markov_chain[current_word])
        result.append(next_word)
        current_word = next_word

        # 文の終わりを判定する条件
        if next_word in ['。', '！', '？']:  # 文末の句読点で終了
            break
    
    # 空白を削除
    return ''.join(result)

# 最初の単語をランダムに選択
start_word = random.choice(tokens)

# 生成するテキストの長さ
text_length = 100  # 100単語分

# テキスト生成
generated_text = generate_text(start_word, text_length)

# 結果を表示
print("生成されたテキスト:")
print(generated_text)

# 生成したテキストをファイルに保存
with open("generated_text.txt", "w", encoding="utf-8") as output_file:
    output_file.write(generated_text)

print("生成されたテキストがgenerated_text.txtに保存されました。")
