# https://qiita.com/ichi_zamurai/items/60d2480edcb68a76aeb6
# https://zenn.dev/hg/articles/4cf2dbc432621e
# から引用,変更
from GenerateText import GenerateText

with open('generated_tweets.txt', 'w', encoding='utf-8') as f:
    for _ in range(100):
        generator = GenerateText()
        tweet = generator.generate()
        f.write(f'{tweet}\n')