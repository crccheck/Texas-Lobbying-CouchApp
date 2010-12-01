import re
import couchdb
from csv import DictReader
import simplejson as json
import sys

f = open('../.couchapprc','r')
data = json.load(f)
f.close()
DATABASE = data['env']['default']['db'].rsplit('/', 1)
DATABASE = {'server': DATABASE[0], 'db': DATABASE[1]}


def add_client(doc, client):
    if 'client' in doc:
        for existing_client in doc['client']:
            if existing_client['name'] == client['name']:
                return doc
        doc['client'].append(client)
    else:
        # initial client
        doc['client'] = [client]
    return doc


couch = couchdb.Server(DATABASE['server'])
try:
    db = couch[DATABASE['db']]
except couchdb.ResourceNotFound:
    db = couch.create(DATABASE['db'])
f = open('csvdata/LobCon10.csv','r')
reader = DictReader(f)
for i, row in enumerate(reader):
    id = "lobbyist-%d_%d" % (int(row['FILER_ID']), int(row['YEAR_APPL']))
    year = int(row['YEAR_APPL'])
    lobbyist = {
        'name': row['LOBBYNAME'],
        'id': int(row['FILER_ID']),
        'occupation': row['NORM_BUS'],
        'phone': row['LOBPHON'],
        'address': row['ADDRESS1'] + (' ' + row['ADDRESS2'] if row['ADDRESS2'] else ''),
        'city': row['CITY'],
        'state': row['STATE'],
        'zip': row['ZIPCODE'],
        'employer': row['FIRM_NAML'],
        'interest': row['I4E_NAML'],
    }
    client = {
                'name': row['CONCERNAME'],
                'compensation': {'low': row['NLOW'],
                                 'high': row['NHIGH'],
                                 'type': row['TYPECOPM']},
                'address': row['EC_ADR1'] + ' ' + row['EC_ADR2'],
                'state': row['EC_STCD'],
                'city': row['EC_CITY'],
                'zip': row['EC_ZIP4'],
             }
    report = {
                'date': row['RPT_DATE'],
                'number': int(row['REPNO'])
             }
    doc = db.get(id)
    if not doc:
        doc = {
            '_id': id,
            'year': year,
            'lobbyist': lobbyist,
            'report': report,
            'type': 'lobbyist',
        }
    db[id] = add_client(doc, client)
    if not (i % 100):
        print i
