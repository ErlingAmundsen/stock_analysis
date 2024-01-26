import sys
import pandas as pd
import datetime
import pytz

sys.path.append("./")
from main_functions import format_yahoo as mf
import main_functions.plotting_standard as ps


def line_of_vision(data, check_point_date):
    """Checks Line of Vision for a given piece of data between two points


    Args:
        data Pandas Dataframe: Data Window
        check_point_date DataTime: Date of second point (first point is always the last date in the data window)
    """


def testing(data, meta, list_time_indexes, axis="Close", days_lookback=None):
    for date in list_time_indexes:
        if days_lookback:
            lookback = date - datetime.timedelta(days=days_lookback)
        else:
            lookback = data.index[0]

        temp_data = data[data.index >= lookback]
        temp_data = temp_data[temp_data.index <= date]


if __name__ == "__main__":
    data, meta = mf.format_yahoo("BTC-USD", period="1y")
    # get 21 June 2023
    date_time = datetime.datetime(
        year=2023, month=6, day=17, tzinfo=pytz.timezone("US/Eastern")
    )
    list_time_indexes = [date_time]
    seen_dates = testing(data, meta, list_time_indexes, axis="Close", days_lookback=30)
