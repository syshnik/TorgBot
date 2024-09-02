import small
import db
import load_price
import mysql.connector
import time
import sys
from datetime import datetime 

from time import sleep
import small



    #обновляем новые цены 
    #по все биржам перерыв 6 часов ... или меньше...
while True:
    try:
        usnuli=datetime.now()
        print('Usnuli '+str(usnuli)+'     ')
        load_price.AddPricesNewOrOld(True, 'okx', 'BTC', 'USDT', None)
        load_price.AddPricesNewOrOld(True, 'okx', 'ETH', 'USDT', None)
        load_price.AddPricesNewOrOld(True, 'bybit', 'BTC', 'USDT', None)
        load_price.AddPricesNewOrOld(True, 'bybit', 'ETH', 'USDT', None)
        load_price.AddPricesNewOrOld(True, 'bybit', 'BNB', 'USDT', None)
        print('Usnuli '+str(usnuli)+'     spim 5 min            ')
        sleep(5*60)
    except:
        print("Except Run 222888")

