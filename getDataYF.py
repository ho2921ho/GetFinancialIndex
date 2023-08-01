# get historical market data (by yf)
import yfinance as yf


def getDataYF(end = '2023-1-6'):
   
    Ticker_list = ['^KS11','^KQ11','^DJI','^GSPC','^STOXX50E','^HSI','^N225',
                   'DX=F','KRW=X','EURUSD=X','CNY=X','JPY=X']

    
    tickers = yf.Tickers(' '.join(Ticker_list))
    start = '2021-01-01'
    data = tickers.download(start=start, end=end)
    data = data.xs('Close', axis = 1)
    data.index = data.index.astype('datetime64[ns]')
    return data


# get historical market data (by crawler)


