from collections import defaultdict
import numpy as np

def co_occurrence(sentences, window_size, min_edges):
    d = defaultdict(int)
    vocab = set()
    for text in sentences:
        text = text.lower().split()
        for i in range(len(text)):
            token = text[i]
            vocab.add(token)  # add to vocab
            next_token = text[i+1 : i+1+window_size]
            for t in next_token:
                key = tuple( sorted([t, token]) )
                d[key] += 1
    
    vocab = sorted(vocab) # sort vocab
    df = pd.DataFrame(data=np.zeros((len(vocab), len(vocab)), dtype=np.int16),
                      index=vocab,
                      columns=vocab)
    for key, value in d.items():
        df.at[key[0], key[1]] = value
        df.at[key[1], key[0]] = value
    
    df = df.stack().reset_index()
    df = df[df[0]>=min_edges]
    
    df = df[~(np.triu(df.level_0.values[:,None] == df.level_1.values)).any(0)].sort_values(0, ascending = False)
    
    return df
