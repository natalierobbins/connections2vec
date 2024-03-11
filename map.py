import json
import sqlite3
from tqdm import tqdm

def sense_to_vector(line):
    line = line.split(' ')
    key = line[0]
    val = [float(num) for num in line[1:]]
    return (key, val)

def word_to_sense(line):
    line = line.split('\t')
    key = line[0]
    val = line[1].split(' ')
    return (key, val)

def sense_to_key(line):
    line = line.split('\t')
    key = line[0]
    val = line[1]
    return (key, val)

map_funcs = {
    'word_to_sense.json': word_to_sense,
    'sense_to_key.json': sense_to_key,
    'sense_to_vector.json': sense_to_vector
}

tables = {
    'sense_key_map': {
        'table': 'keys',
        'key': 'sense',
        'value': 'key'
    },
    'sense_list': {
        'table': 'senses',
        'key': 'word',
        'value': 'senses'
    },
    'wn_sense_vectors': {
        'table': 'vectors',
        'key': 'sense',
        'value': 'vector'
    }
}

def generate(input):
    con = sqlite3.connect('maps.sqlite3')
    with open(f"{input}.txt", 'r') as f:
        input = f.read()
    
    for line in tqdm(input.split('\n')[1:-1]):
        line = line.split(' ')
        key, val = line[0], (' ').join(line[1:])
        sql = f"INSERT INTO vectors(sense, vector) VALUES (?, ?);"
        data = (key, val)
        con.execute(sql, data)
    con.commit()
    # with open(output_path, 'w+') as f:
    #     json.dump(hash_map, f, indent=4)

con = sqlite3.connect('maps.sqlite3')
# for table in tables.keys():
#     table = tables[table]
#     con.execute(f"""
#         CREATE TABLE {table['table']}(
#             {table['key']} VARCHAR PRIMARY KEY,
#             {table['value']} VARCHAR
#         );
#     """)
generate('wn_sense_vectors')
# curs = con.execute("SELECT * FROM keys;")
# print(curs.fetchall())