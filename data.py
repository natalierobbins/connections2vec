from nltk.corpus import wordnet as wn
import sqlite3
import numpy as np


con = sqlite3.connect('./maps.sqlite3')


def get_senses(word):
    curs = con.execute("SELECT senses FROM senses WHERE word = ?", (word,))
    senses, = curs.fetchone()
    return senses.split(' ')


def get_key(sense):
    curs = con.execute("SELECT key FROM keys WHERE sense = ?", (sense,))
    key, = curs.fetchone()
    return key


def get_vector(sense):
    curs = con.execute("SELECT vector FROM vectors WHERE sense = ?", (sense,))
    vector, = curs.fetchone()
    return np.array(vector.split(' '), dtype=np.float32)
  

def get_data(word):
    senses = get_senses(word)
    data = []
    for sense in senses:
        word = sense.split('#')[0]
        id = sense.split('#')[1]
        synset = wn.synset_from_sense_key(get_key(sense))
        vector = get_vector(sense)
        data.append({
            'word': word,
            'sense_id': id,
            'pos': synset.pos(),
            'definition': synset.definition(),
            'vector': vector
        })
    return data