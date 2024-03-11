from data import get_data
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.preprocessing import MinMaxScaler

words = [
    'stick',
    'shift',
    'bone',
    'hide',
    'blank',
    'block',
    'space',
    'ball',
    'obscure',
    'command',
    'flake',
    'cover',
    'control',
    'forget',
    'Frisbee',
    'option'
]

data = []
words = tqdm(words)

for word in words:
    words.set_description(word)
    for sense in get_data(word):
        data.append(sense)
        
senses = [f"{d['word']}#{d['sense_id']}" for d in data]
vectors = [d['vector'] for d in data]

X = np.vstack(vectors)
scaler = MinMaxScaler()
tsne = TSNE(perplexity=(len(vectors) - 1)).fit_transform(X)
tsne = scaler.fit_transform(tsne)

plt.scatter(*tsne.T.reshape(2, -1))

for i, label in enumerate(senses):
    x = tsne[i][0]
    y = tsne[i][1]
    plt.text(x, y, label)

plt.show()