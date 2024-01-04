import yfinance as yf

def stop_loss(stock, ):





if __name__ == '__main__':
    ticker = 'APPL'
    stock = yf.Ticker(ticker).history('1yr')
    stop_loss(stock)