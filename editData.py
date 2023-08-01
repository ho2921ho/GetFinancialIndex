import pickle
from datetime import datetime
from datetime import timedelta
import numpy as np

with open(r'C:\Users\NH\index_trend\Database\Database.pickle', 'rb') as f:
    database = pickle.load(f)
    
target_date = "2023-1-30"

mainF(target_date ,database)


def mainF(today,database):
    today = datetime.strptime(today, "%Y-%m-%d")
    
    d1 = today - timedelta(days=1)
    d7 = today - timedelta(days=7)
    dm = today - timedelta(days=30)
    dq = today - timedelta(days=90)
    dy = today - timedelta(days=365)
    
    ''' database['Spreed_kr'] = database['kr10ty'] - database['kr2ty']
    database['Spreed_us'] = database['us10ty'] - database['us2ty'] '''
    
    ytH = database[dy:today].max()
    ytL = database[dy:today].min()

    result_table = database[today:today].T
    result_table['D-1'] = get_rate_of_change(database, today, d1)
    result_table['D-7'] = get_rate_of_change(database, today, d7)
    result_table['MTD'] = get_rate_of_change(database, today, dm)
    result_table['QTD'] = get_rate_of_change(database, today, dq)
    result_table['YTD'] = get_rate_of_change(database, today, dy)
    result_table['Yr High'] = ytH
    result_table['Yr Low'] = ytL

    amount_table = database[today:today].T
    amount_table['D-1'] = get_amount_of_change(database, today, d1)
    amount_table['D-7'] = get_amount_of_change(database, today, d7)
    amount_table['MTD'] = get_amount_of_change(database, today, dm)
    amount_table['QTD'] = get_amount_of_change(database, today, dq)
    amount_table['YTD'] = get_amount_of_change(database, today, dy)
    amount_table['Yr High'] = ytH
    amount_table['Yr Low'] = ytL
    
    
    result_table = result_table.T

    result_table[ ['kr10ty','kr2ty','krAAmty'] ] = amount_table.T[ ['kr10ty','kr2ty','krAAmty'] ]

    result_table = result_table.T

    result_table.index = ['중국(상해)', '알루미늄', '철광석', 'Brent', 'WTI', 'CNY', 'Dollar Index',
           'EUR', 'GBP', '금', '구리', 'JPY', '커피', '밀',
           'USD/KRW', '천연가스', '은', '옥수수', 'DOW', 'S&P', '홍콩(H)', 'NASSDAQ',
           'KOSDAQ', 'KOSPI', '일본(Nikkei225)', '유럽(Euro Stoxx 50)', '국채 10Y', '국채 2Y', '회사채AA-']

    result_table = result_table.T

    result_table = result_table[['KOSPI','KOSDAQ','DOW','S&P','NASSDAQ','일본(Nikkei225)','유럽(Euro Stoxx 50)','중국(상해)','홍콩(H)',
                                 '국채 10Y', '국채 2Y', '회사채AA-', 
                                 'Dollar Index','USD/KRW','EUR', 'GBP','JPY','CNY',
                                 'WTI','Brent','금','은','철광석','구리','옥수수','밀','커피','천연가스','알루미늄']]

    result_table = result_table.T
    
    result_table.to_csv(r'C:\Users\NH\index_trend\ResultTables\ResultTable_{}.csv'.format(str(today)[:10]),encoding="utf-8-sig")



    
def get_rate_of_change(database,today,norm):
    values = np.round((database[today:today].values - database[norm:norm].values)*100 / database[today:today].values,2)
    values = values.reshape(-1,1)
    return values





def get_amount_of_change(database,today,norm):
    values = np.round((database[today:today].values - database[norm:norm].values)*100,2)
    values = values.reshape(-1,1)
    return values





