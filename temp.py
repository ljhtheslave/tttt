from types import BuiltinMethodType
import pyupbit
import time
import math
from pyupbit import WebSocketManager
import numpy
access_key = "r1Y4rUunVebN7XIsUde9UQBixt8jX5hAKHXmgvhh"
secret_key = "tTNgxMfAHYF2XxblizvrFGr0e5zi8SzYexeLrK0H"

middle = 241000
size = 100
stride = 1.006
unit_price = 50
unit_amount = 5010
ticker = "KRW-DOGE"
buy_delay = 0.01

upbit = pyupbit.Upbit(access_key, secret_key)


dd = upbit.get_order("KRW-XRP")
print(numpy.size(dd))
for i in range(2):
    print(dd[i])
    print(i, dd[i]['state'], dd[i]['price'])
