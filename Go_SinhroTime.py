import requests 
import json
import small
import db
import load_price

from datetime import datetime 
from pybit.unified_trading import HTTP



def SinhroTime(birja):
    #синхронизирует милисекунды байбит и местное время
    if birja == 'bybit':
        coin='AAVE'
        bcoin='USDT'
    if birja == 'binancebnb':
        coin='AAVE'
        bcoin='BNB'
    if birja == 'binanceusdt':
        coin='AAVE'
        bcoin='USDT'
    if birja == 'okx':
        coin='BTC'
        bcoin='USDT'
    b1=load_price.GetBirjaClassFromName(birja, coin, bcoin)
    ms_name=''
    date_name=''
    if birja=='bybit':
        ms_name='bybit_time_as_ms'
        date_name='bybit_time_as_date'
    if birja=='binancebnb' or birja=='binanceusdt':
        ms_name='binance_time_as_ms'
        date_name='binance_time_as_date'
    if birja=='okx':
        ms_name='okx_time_as_ms'
        date_name='okx_time_as_date'
    #-------times-----------------------------------------
    now1 = datetime.now()
    formatted_date = now1.strftime('%Y-%m-%d %H:%M:%S')
    time1=b1.GetBirjaTime()
    if time1 == None :
        print('Error for Get Time 345780')
        return
    now2 = datetime.now()
    time_diff = now2 - now1
    tsecs = time_diff.total_seconds()
    if tsecs > 10:
        print('Tooo long...346754')
        return
    #--------save----------------------------------------
    conn=db.GetConnect()
    cursor = conn.cursor()
    time1str="{}".format(time1)
    cursor.execute("delete  from peremenniye where pername='"+date_name+"'   ")
    cursor.execute("delete  from peremenniye where pername='"+ms_name+"'   ")
    conn.commit()
    cursor.execute("insert into peremenniye(pername, perznachenie) values ('"+date_name+"', '"+formatted_date+"' ) ")
    cursor.execute("insert into peremenniye(pername, perznachenie) values ('"+ms_name+"', '"+time1str+"' ) ")
    conn.commit()
    conn.close()
    cursor.close()


small.PlaySSSSSSSSSSS(True)

print("ok load times")

SinhroTime("bybit")
SinhroTime("binancebnb")
SinhroTime("binanceusdt")
SinhroTime("okx")
