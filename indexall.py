import os
import copy
import json


from elasticsearch import Elasticsearch

import dave_python_util as dutil


#utility functions



MONSTER_PATH = "../open5e-api/data/WOTC_5e_SRD_v5.1/monsters.json"


index_name = "open5e-monsters"
es_url = os.getenv('ES_URL', 'https://localhost:9200')
es_user = os.getenv('ES_USER', 'USER')
es_password = os.getenv('ES_PASS', 'CHANGEME')
# Define the Elasticsearch client
es = Elasticsearch(
    [es_url],
    basic_auth=(es_user, es_password),
    verify_certs=True
)

if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

with open(MONSTER_PATH, 'r') as file:
    data = json.load(file)

for obj in data:
    # print(dutil.pretty_print_json(obj,2))
    es.index(index=index_name, document=obj)

# print(dutil.pretty_print_json(data,2))