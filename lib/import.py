from csv import DictReader
import logging
import simplejson as json
import couchdb
from urllib import urlopen, urlretrieve
import os
import sys
from calendar import timegm
from time import strptime
from CSVProcessors import CSVProcessorAwrd, CSVProcessorCVR, CSVProcessorEnt, CSVProcessorEvnt, CSVProcessorFood, CSVProcessorGift, CSVProcessorTran


f = open('../.couchapprc','r')
data = json.load(f)
f.close()
DATABASE = data['env']['default']['db'].rsplit('/', 1)
DATABASE = {'server': DATABASE[0], 'db': DATABASE[1]}

CONFLICT = 'replace' #update, replace, ignore
data_dir = 'csvdata'


def couch_start(dbname = None):
    if dbname is None:
        dbname = DATABASE['db']
    debug('dbname is %s' % dbname)
    dbname = dbname.lower()
    server = couchdb.client.Server(DATABASE['server'])
    try:
        db = server[dbname]
    except couchdb.ResourceNotFound as e:
        db = server.create(dbname)
    return db

def debug(s):
    logging.debug(s)
def log(s):
    logging.info(s)
def warn(s):
    logging.warn(s)
def err(s):
    logging.error(s)
def derp(s):
    logging.critical(s)

def download(force = False):
    ''' download the ZIP file to a temporary directory, and extract to the dataapp directory
        returns a list of CSV files '''
    def remote_getmtime():
        data = urlopen(url)
        date = data.info()['last-modified']
        return timegm(strptime(date, '%a, %d %b %Y %H:%M:%S %Z'))
    def local_getmtime():
        try:
            return int(os.path.getmtime(data_dir + '/' + os.listdir(data_dir)[0]))
        except:
            return 0
    url = 'http://www.ethics.state.tx.us/tedd/TEC_LA_CSV.zip'
    log('time check %s %s' % (remote_getmtime(), local_getmtime()))
    if force or abs(remote_getmtime() - local_getmtime()) > 7 * 864000:
        log('.FAIL pulling new files')
        # local data files are more than 7 days old
        f = urlretrieve(url)    # wishlist show progress bar of file download
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
        os.system('unzip %s -d %s' % (f[0], os.path.abspath(data_dir)))
    return [data_dir + '/' + f for f in os.listdir(data_dir) if f[-3:] == 'csv']

def process(path_to_file):
    log(path_to_file)
    if (path_to_file.find('LobCon')):
        get_lobbyists(path)
        return
    processors = {
        'LaCVR.csv'  : CSVProcessorCVR,
        'LaAwrd.csv' : CSVProcessorAwrd,
        'LaEnt.csv'  : CSVProcessorEnt,
        'LaEvnt.csv' : CSVProcessorEvnt,
        'LaFood.csv' : CSVProcessorFood,
        'LaGift.csv' : CSVProcessorGift,
        'LaTran.csv' : CSVProcessorTran,
    }
    try:
        processor = processors[os.path.basename(path_to_file)]()
    except KeyError:
        return;
    db = couch_start()
    f = open(path_to_file,'r')
    reader = DictReader(f)
    updates = 0
    for i, row in enumerate(reader):
        row_id, row_data = processor.process(row)
        debug("%d : %s %s" % (i, row_id, row_data))
        doc = db.get(row_id)
        if doc:
            if CONFLICT == 'update':
                doc.update(row_data)
                db[doc.id] = doc
                updates += 1
            elif CONFLICT == 'replace':
                doc.update(row_data)
                row_data['_rev'] = doc['_rev']
                db[doc.id] = row_data
                updates += 1
        else:
            db[row_id] = row_data
        if not (i % 100):
            log("%d: Updates(%s)" % (i, updates))
    log("%d: Finished! Updates(%s)" % (i, updates))
    f.close()

def get_lobbyists(path='csvdata/LobCon10.csv'):
    '''import list of lobbyist from csv file. to get the csv file, you have to
    download it from http://www.ethics.state.tx.us/dfs/loblists.htm '''
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

    db = couch_start()
    f = open(path, 'r')
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


def main():
    log('Importing CSVs')
    log('Conflict Resolution Method: %s' % CONFLICT)
    log('Database: {server}/{db}'.format(*DATABASE))
    download()
    files = [data_dir + '/' + f for f in os.listdir(data_dir) if f[-3:] == 'csv']
    for f in files:
        process(f);

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    main()
