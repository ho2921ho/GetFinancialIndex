import os
import pandas as pd
import pickle
os.chdir(r'C:/Users/NH/index_trend')

from getDataYF import getDataYF
# from getDataIC import getDataIC

today = '2023-6-5' # 매주 금요일 9시 이후 뽑는걸 가정.

data_sub_1 = getDataYF(today)
data_sub_1[['000001.SS', 'ALI=F', 'BUS=F', 'BZ=F', 'CL=F', 'CNY=X', 'DX=F','EURUSD=X', 'GBPUSD=X', 'GC=F', 'HG=F', 'JPY=X', 'KC=F', 'KE=F','KRW=X', 'NG=F', 'SI=F', 'ZC=F']] = data_sub_1.shift(-1)[['000001.SS', 'ALI=F', 'BUS=F', 'BZ=F', 'CL=F', 'CNY=X', 'DX=F','EURUSD=X', 'GBPUSD=X', 'GC=F', 'HG=F', 'JPY=X', 'KC=F', 'KE=F','KRW=X', 'NG=F', 'SI=F', 'ZC=F']]
# 야후 파이낸스 api 문제, 하루 늦게 15분 지연된 데이터를 적재함.
# getDataIC(today)
# getDataIC.download_csv()
# getDataIC.df_concat()

with open(r'C:\Users\NH\index_trend\dataCrawled\dataCrawled.pickle', 'rb') as f:
    data_sub_2 = pickle.load(f)
    
    
with open(r'C:\Users\NH\index_trend\dataDaum\krAAmty.pickle', 'rb') as f:
    data_sub_3 = pickle.load(f)
    

data = pd.concat([data_sub_1,data_sub_2,data_sub_3], axis = 1)

data = data.fillna(method='ffill')
data = data.dropna()

with open(r'C:\Users\NH\index_trend\Database\Database.pickle', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
# pickle 저장 -> editData로 넘어가기

sample = data_sub_1.iloc[-6:,:]
