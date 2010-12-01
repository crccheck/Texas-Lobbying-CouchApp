from csv import DictReader
import logging
import couchdb
from urllib import urlopen, urlretrieve
from zipfile import ZipFile
import os
from calendar import timegm
from time import strptime
from CSVProcessors import CSVProcessorAwrd, CSVProcessorEnt, CSVProcessorEvnt, CSVProcessorFood, CSVProcessorGift, CSVProcessorTran


DATABASE = {
    'name': 'lobbying',
    'host': 'localhost',
    'port': '5984'
}

CONFLICT = 'ignore' #update, replace, ignore

def couch_start(dbname = None):
    if dbname is None:
        dbname = DATABASE['name']
    debug('dbname is %s' % dbname)
    dbname = dbname.lower()
    server = couchdb.client.Server()
    try:
        db = server.create(dbname)
    except couchdb.PreconditionFailed as e:
        db = server[dbname]
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

def download():
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
    data_dir = 'csvdata'
    url = 'http://www.ethics.state.tx.us/tedd/TEC_LA_CSV.zip'
    log('time check %s %s' % (remote_getmtime(), local_getmtime()))
    if abs(remote_getmtime() - local_getmtime()) > 7 * 864000:
        # local data files are more than 7 days old
        f = urlretrieve(url)    # wishlist show progress bar of file download
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
        os.system('unzip %s *.csv -d %s' % (f[0], os.path.abspath(data_dir)))
    return [data_dir + '/' + f for f in os.listdir(data_dir) if f[-3:] == 'csv']

def process(path_to_file):
    log(path_to_file)
    processors = {
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

def main():
    files = download()
    for f in files:
        process(f);

logging.basicConfig(level=logging.INFO)


main()
