import small
import db
import load_price
import mysql.connector
from datetime import datetime 
from time import sleep


#обновляем новые цены для всех монет

print("Input command: 'new5min', 'new', 'old', 'oldoldold', 'testprices','oldoldold_binance'")



kudakuda=input()
def Add(kuda1, birja):
    if kuda1 == 'new':
        load_price.AddPricesNewOrOld(True, birja, '', '', None)
    elif kuda1 == 'old':
        load_price.AddPricesNewOrOld(False, birja, '', '', None)
    elif kuda1 == 'testprices':
        load_price.TestPriceOrder_ForAll_bybit()
    else:
        print('incorrect parametrs')
        small.ifnoterr(1==7)

def Run():
    if kudakuda == 'new55min':
        #для таймера
        old=None
        while True:
            print(datetime.now())
            old=small.SleepSecund(55, old)
            Add('new', 'okx')
            old=small.SleepSecund(55, old)
            Add('new', 'bybit')
            old=small.SleepSecund(55, old)
            Add('new', 'binancebnb')
            old=small.SleepSecund(55, old)
            Add('new', 'binanceusdt')
    if kudakuda == 'new5min':
        #для таймера
        old=None
        while True:
            print(datetime.now())
            old=small.SleepSecund(15, old)
            Add('new', 'okx')
            old=small.SleepSecund(15, old)
            Add('new', 'bybit')
            old=small.SleepSecund(15, old)
            Add('new', 'binancebnb')
            old=small.SleepSecund(15, old)
            Add('new', 'binanceusdt')
    if kudakuda == 'new':
            Add('new', 'okx')
            Add('new', 'bybit')
            Add('new', 'binancebnb')
            Add('new', 'binanceusdt')
    elif kudakuda == 'old':
            Add('old', 'okx')
            Add('old', 'binancebnb')
            Add('old', 'binanceusdt')
            Add('old', 'bybit')
    elif kudakuda == 'oldoldold':
        old=None
        while True:
            old=small.SleepSecund(15, old)
            Add('old', 'okx')
            Add('old', 'bybit')
            Add('old', 'binancebnb')
            Add('old', 'binanceusdt')
    elif kudakuda == 'oldoldold_binance':
        old=None
        while True:
            old=small.SleepSecund(15, old)
            Add('old', 'binancebnb')
            old=small.SleepSecund(15, old)
            Add('old', 'binanceusdt')
    elif kudakuda == 'testprices':
            Add('testprices', 'okx')
            Add('testprices', 'bybit')
            Add('testprices', 'binancebnb')
            Add('testprices', 'binanceusdt')
    else:
        print('incorrect parametrs')
        small.ifnoterr(1==7)


if small.ItDebug() :
     Run()
else :
     while True:
        try:
            Run()
        except:
            print("Except Run 8888888")
            sleep(30)





    # if kuda1 == 'new5min':
    #     #список список с именами таблиц и крайними временами
    #     savelist='musor'
    #     #период обновления списка таблиц
    #     next12=0
    #     #для таймера
    #     old=None
    #     while True:
    #         old=small.SleepSecund(5, old)
    #         print(datetime.now())
    #         if next12 % (12*12) == 0:
    #             savelist=None
    #         nextnew12=next12+1
    #         savelist=AddPricesNewOrOld(True, '', savelist)
    # if kuda1 == 'new':
    #     AddPricesNewOrOld(True, '', None)
    # elif kuda1 == 'old':
    #     AddPricesNewOrOld(False, '', None)
    # elif kuda1 == 'oldoldold':
    #     while True:
    #         AddPricesNewOrOld(False, '', None)
    # elif kuda1 == 'testprices':
    #     load_price.TestPriceOrder_ForAll_bybit()
    # else:
    #     print('incorrect parametrs')
    #     small.ifnoterr(1==7)
