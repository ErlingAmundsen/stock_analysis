import sys
from dataclasses import dataclass

sys.path.append("./")
from main_functions import format_yahoo as fy


def testing(vals):
    list_test = vals.copy()

    for i in range(len(list_test)):
        list_test[i] = min(0, list_test[i])
    return list_test


@dataclass
class test_class:
    _name: str

    def __post_init__(self):
        self._name = self._name.upper()

    @property
    def name_t(self):
        return self._name

    @name_t.setter
    def name_t(self, val):
        self._name = val.upper()


if __name__ == "__main__":
    data, meta = fy.format_yahoo("BTC-USD", period="1y")

    vals = "hello"
    cls = test_class(vals)
    print(cls._name)
    print(cls.name_t)
    cls.name_t = "not_hello"
    print(cls.name_t)
    cls.name_t = "Nnonon"
