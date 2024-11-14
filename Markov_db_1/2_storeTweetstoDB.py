# https://qiita.com/ichi_zamurai/items/60d2480edcb68a76aeb6
# https://zenn.dev/hg/articles/4cf2dbc432621e
# から引用,変更
# ーーーーーーーーーーーーーーーーーーーーーーー
# cd指定したか？？？？？
# ーーーーーーーーーーーーーーーーーーーーーーー
from PrepareChain import PrepareChain
from tqdm import tqdm
import os

# ディレクトリの変更
os.chdir('/workspaces/Markov/Markov_db_1')

def storeTweetstoDB():
    
    with open('tweets.txt', 'r', encoding='utf-8') as f:
        tweets = [line.strip() for line in f]

    print(len(tweets))

    chain = PrepareChain(tweets[0])
    triplet_freqs = chain.make_triplet_freqs()
    chain.save(triplet_freqs, True)

    for i in tqdm(tweets[1:]):
        chain = PrepareChain(i)
        triplet_freqs = chain.make_triplet_freqs()
        chain.save(triplet_freqs, False)

if __name__ == '__main__':
    storeTweetstoDB()