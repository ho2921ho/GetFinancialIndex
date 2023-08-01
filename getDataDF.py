import pickle
import pandas as pd
import requests
import json

custom_header = {
    'referer' : 'http://http://finance.daum.net/quotes/A048410#home',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'  }


def get_data(url) :
    result = []
    page = 1 
    req = requests.get(url, headers = custom_header)
    
    if req.status_code == requests.codes.ok:    
        print("접속 성공")
        # API에 접속에 성공하였을 때의 logic을 작성
        # JSON 데이터의 원하는 부분만 불러와 result에 저장
        stock_data = json.loads(req.text)
        
        for d in stock_data["data"]:
            result.append([d['date'], d['tradePrice']])
        
    else:
        print("접속 실패")
    
    return result



df_list = []
for i in range(1,30):
    page = i
    url = "https://finance.daum.net/api/domestic/exchanges/BOND-/KRGUCORP=KQ/days?symbolCode=BOND-/KRGUCORP=KQ&page={}&perPage=30&fieldName=changeRate&order=desc&pagination=true".format(page)
    df = get_data(url)
    df = pd.DataFrame(df) 
    df_list.append(df)



df = pd.concat(df_list)
df.columns = ['Date','krAAmty']
df['Date'] = df['Date'].astype('datetime64[ns]')
df = df.set_index('Date')
df = df[::-1]

with open(r'C:\Users\NH\index_trend\dataDaum\krAAmty.pickle', 'wb') as f:
    pickle.dump(df, f, pickle.HIGHEST_PROTOCOL)