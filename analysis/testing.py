import os

os.sys.path.append("./")
import main_functions.format_yahoo as fy
import main_functions.plotting_standard as ps


def testing(data, list_time_indexes, axis="Close", days_lookback=None):
    for date in list_time_indexes:
        data_points = data[axis][data.index <= date]


if __name__ == "__main__":
    data, meta = fy("BTC-USD", period="1y")
