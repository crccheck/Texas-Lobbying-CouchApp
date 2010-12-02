
class CSVProcessor(object):
    def __init__(self):
        self.type = ''
    def get_amount(self, row):
        def fix_amount(row):
            if not row['EXPAMOUNT'] or row['EXPAMOUNT'] == '0':
                if row['nLow'] != row['nHigh']:
                    print "!!!", row
                print "exp amount sucks, use:", row['nLow'], row['nHigh'], row['EXPAMOUNT']
                return row['nLow']
            else:
                return row['EXPAMOUNT']
            return 0;
        if 'EXP_OTHER' in row and row['EXP_OTHER_']:
            return fix_amount(row)
        if 'AMT_OTHER' in row and row['AMT_OTHER_']:
            return fix_amount(row)
        for amount in range(100,501,50):
            if row['AMT_%s_CB' % amount]:
                return amount
        return fix_amount(row)
    def lobbyist_info(self, row):
        data = {'name': row['LOB_NAME'], 'id': int(row['FILER_ID'])}
        if row['LOB_SORT'] != row['LOB_NAME']:
            data['sort'] = row['LOB_SORT']
        return data
    def recipient_info(self, row):
        data = {'name': u"%s %s" % (unicode(row['REC_NAMF'], errors='replace'), row['REC_NAML'])}
        if ('REC_SHORT' in row) and row['REC_SHORT']:
            data['nickname'] = row['REC_SHORT']
        if row['REC_NAMT']:
            data['title'] = row['REC_NAMT']
        if row['REC_NAMS']:
            data['suffix'] = row['REC_NAMS']
        return data
    def beneficiary_info(self, row):
        data = {'name': u"%s %s" % (unicode(row['BEN_NAMF'], errors='replace'), row['BEN_NAML'])}
        if row['BEN_SHORT']:
            data['nickname'] = row['BEN_SHORT']
        if row['BEN_NAMT']:
            data['title'] = row['BEN_NAMT']
        if row['BEN_NAMS']:
            data['suffix'] = row['BEN_NAMS']
        return data
    def process(self, row):
        row_id = "%s-%s" % (self.type, row['IDNO'])
        row_data = {
            'report': int(row['REPNO']),
            'type': self.type,
            'lobbyist': self.lobbyist_info(row),
            'recipient': self.recipient_info(row),
            #'source': row,
        }
        return (row_id, row_data)

class CSVProcessorCVR(CSVProcessor):
    ''' Cover Sheet '''
    def __init__(self):
        self.type = 'cover'
    def process(self, row):
        def num(s):
            if s == "0" or s == "":
                return 0
            return s
        row_id = "%s-%s" % (self.type, row['REPNO'])
        row_data = {
            'report': {
                            'id': int(row['REPNO']),
                            'date': row['DUE_DATE'],
                            'start': row['RPT_BEG_DT'],
                            'end': row['RPT_END_DT'],
                            'year': row['YEAR_APPL'],
                      },
            'type': self.type,
            'lobbyist': self.lobbyist_info(row),
            'expenses': {
                            'transportation': num(row['EXTYP_TRAN']),
                            'food':  num(row['EXTYP_FOOD']),
                            'ent':   num(row['EXTYP_ENT']),
                            'gift':  num(row['EXTYP_GIFT']),
                            'award': num(row['EXTYP_AWDS']),
                            'event': num(row['EXTYP_EVNT']),
                            'media': num(row['EXTYP_MEDA']),
                        },
            'benefited': {
                            'sen': num(row['EXBEN_SEN']),
                            'rep': num(row['EXBEN_REP']),
                            'other': num(row['EXBEN_OTH']),
                            'leg_emp': num(row['EXBEN_LEG']),
                            'exec_emp': num(row['EXBEN_EXEC']),
                            'family': num(row['EXBEN_FAM']),
                            'event': num(row['EXBEN_EVNT']),
                            'guest': num(row['EXBEN_GUES']),
                         }
             }
        return (row_id, row_data)


class CSVProcessorAwrd(CSVProcessor):
    ''' Schedule F - Awards & Mementos '''
    def __init__(self):
        self.type = 'award'
    def process(self, row):
        row_id, row_data = super(CSVProcessorAwrd, self).process(row)
        row_data.update({
            'amount': self.get_amount(row),
            'award': row['AWARD_DSCR'],
            'date': row['RPT_DATE'],
        })
        return (row_id, row_data)

class CSVProcessorEnt(CSVProcessor):
    ''' Schedule D - Entertainment '''
    def __init__(self):
        self.type = 'entertainment'
    def process(self, row):
        row_id, row_data = super(CSVProcessorEnt, self).process(row)
        row_data.update({
            'amount': self.get_amount(row),
            'place': {'name': row['ENT_NAME'], 'city': row['ENT_CITY']},
            'date': row['ENT_DATE'],
        })
        if row['ENT_STCD']:
            row_data['place']['state'] = row['ENT_STCD']
        if row['ENT_ZIP4']:
            row_data['place']['zip'] = row['ENT_ZIP4']
        return (row_id, row_data)

class CSVProcessorEvnt(CSVProcessor):
    ''' Schedule G - Pol. Fundraisers & Charity Events '''
    def __init__(self):
        self.type = 'event'
    def process(self, row):
        row_id, row_data = super(CSVProcessorEvnt, self).process(row)
        row_data['event'] = { 'name': row['EVENT_NAME'] }
        row_data['date'] = row['EVENT_DATE']
        if row['CHARITY_CB']:
            row_data['event']['type'] = 'charity'
        elif row['FUND_CB']:
            row_data['event']['type'] = 'fundraiser'
        row_data['beneficiary'] = self.beneficiary_info(row)
        return (row_id, row_data)

class CSVProcessorFood(CSVProcessor):
    ''' Schedule C - Food & Beverages '''
    def __init__(self):
        self.type = 'food'
    def process(self, row):
        row_id, row_data = super(CSVProcessorFood, self).process(row)
        row_data.update({
            'amount': self.get_amount(row),
            'place': {'name': row['EXP_PLACE'], 'city': row['EXP_CITY']},
            'date': row['EXP_DATE'],
        })
        if row['EXP_STCD']:
            row_data['place']['state'] = row['EXP_STCD']
        if row['EXP_ZIP4']:
            row_data['place']['zip'] = row['EXP_ZIP4']
        return (row_id, row_data)

class CSVProcessorGift(CSVProcessor):
    ''' Schedule E - Gifts '''
    def __init__(self):
        self.type = 'gift'
    def process(self, row):
        row_id, row_data = super(CSVProcessorGift, self).process(row)
        row_data.update({
            'amount': self.get_amount(row),
            'gift': row['GIFT_DSCR'],
            'date': row['RPT_DATE'],
        })
        return (row_id, row_data)

class CSVProcessorTran(CSVProcessor):
    ''' Schedule B - Transportation '''
    def __init__(self):
        self.type = 'transportation'
    def lodging_info(self, row):
        data = { 'name': row['LODGE_NAME'], 'city': row['LODGE_CITY'], 'zip': row['LODGE_ZIP'], 'state': row['LODGE_STCD'] }
        return data
    def process(self, row):
        row_id, row_data = super(CSVProcessorTran, self).process(row)
        row_data.update({
            'transportation': row['TRANSTYPE'],
            'purpose': row['PURPOSE'],
            'place' : self.lodging_info(row),
        })
        row_data['departure'] = { 'city': row['DPT_CITY'], 'date': row['DPT_DATE'] }
        row_data['arrival'] = { 'city': row['ARV_CITY'], 'date': row['ARV_DATE'] }
        return (row_id, row_data)


