import sys
import pandas as pd
import datetime

sys.path.append("./")
from main_functions import format_yahoo as mf
import main_functions.plotting_standard as ps


def testing(data, list_time_indexes, axis="Close", days_lookback=None):
    for date in list_time_indexes:
        if days_lookback:
            lookback = date - datetime.timedelta(days=days_lookback)
        else:
            lookback = data.index[0]
        # convert lookback to datime64
        lookback = pd.to_datetime(lookback)
        temp_data = data[data.index >= lookback]


if __name__ == "__main__":
    data, meta = mf.format_yahoo("BTC-USD", period="1y")
    # get 21 June 2023
    date_time = datetime.datetime(year=2023, month=6, day=21)
    list_time_indexes = [date_time]
    seen_dates = testing(data, list_time_indexes, axis="Close", days_lookback=30)
