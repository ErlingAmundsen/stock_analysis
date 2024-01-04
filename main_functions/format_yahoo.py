import yfinance as yf
import datetime

def format_yahoo(ticker,period = None ,start = None, end = None , drop_cols = None, bug_test = True):
    """
    Currently just normal yahoo_ticker, but here so that I can easily 
    change or add columns to a stock later, before it needs to be processed
    """

    metadata_ = {'Start': None, 'End': None, 'Ticker': ticker}

    if period == None and start == None:
        print('You need to pass either period (how far back from today do you want the data?)\n'
              'Or you need to pass the start and end date manually')
        return
    
    if end != None and period != None:
        print('You only need one of these values to get the data, if you dont get all your data it is because you are missing start')


    data = yf.Ticker(ticker = ticker).history(period=period, start=start, end=end)

    if drop_cols:
        data.drop(drop_cols)

    if len(data) == 0:
        print('no data returned')
        return

    if not end:
        end = datetime.date.today()

    ## If start is before stock
    start_test = data.index[0]
    if start_test.to_pydatetime().year > start.year:
        print('WARNING: THE STOCK MIGHT NOT HAVE BEEN OUT AT THE START DATE')

    metadata_['Start'] = start_test
    metadata_['End'] = end

    return data, metadata_



if __name__ == '__main__':
    ticker = 'AAPL'
    start = datetime.datetime(year=2023, month=1, day=1)
    end = datetime.date.today()
    period = '2y'

    data, _ = format_yahoo(ticker = ticker,start=start)
    print(data.head())