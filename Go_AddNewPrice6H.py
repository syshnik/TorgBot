import small
import db
import load_price
import mysql.connector
import time
import sys
from datetime import datetime 

from time import sleep
import small


def Add3567856():
    usnuli=datetime.now()
    print('Usnuli '+str(usnuli)+'     ')
    small.SetAlgoName('Algo_606_'+'finam')
    load_price.AddPricesNewOrOld(True, 'finam', '', '', None)
    small.SetAlgoName('Algo_606_'+'okx')
    load_price.AddPricesNewOrOld(True, 'okx', '', '', None)
    small.SetAlgoName('Algo_606_'+'bybit')
    load_price.AddPricesNewOrOld(True, 'bybit', '', '', None)
    small.SetAlgoName('Algo_606_'+'binanceusdt')
    load_price.AddPricesNewOrOld(True, 'binanceusdt', '', '', None)
    print('Usnuli '+str(usnuli)+'     spim 10 мин')
    sleep(10*60*2)

    #обновляем новые цены 
    #по все биржам перерыв 6 часов ... или меньше...
while True:
    if small.ItInTry():
        try:
            Add3567856()
        except:
            print("Except Run 222888")
    else:
        Add3567856()


