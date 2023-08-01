import pandas as pd
import pickle


def df_pre(name,file_path):
    df =  pd.read_csv(file_path)
    
    df.index = df['Date'].astype('datetime64[ns]')
    
    df = df['Price'].to_frame()
    
    df.columns = [name]
    df = df[::-1]    
    return df

def df_concat(index_list, path_list):
    kr2ty = df_pre('kr2ty',  r'C:\Users\NH\Downloads\South Korea 2-Year Bond Yield Historical Data.csv')
    kr10ty = df_pre('kr10ty', r'C:\Users\NH\Downloads\South Korea 10-Year Bond Yield Historical Data.csv')
    data = pd.concat([kr10ty,kr2ty],axis = 1)
    
    with open(r'C:\Users\NH\index_trend\dataCrawled\dataCrawled.pickle', 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


# 클래스로 만들어야 돌아갈듯;;;

kr2ty = df_pre('kr2ty',  r'C:\Users\NH\Downloads\South Korea 2-Year Bond Yield Historical Data.csv')
kr10ty = df_pre('kr10ty', r'C:\Users\NH\Downloads\South Korea 10-Year Bond Yield Historical Data.csv')
data = pd.concat([kr10ty,kr2ty],axis = 1)

with open(r'C:\Users\NH\index_trend\dataCrawled\dataCrawled.pickle', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)