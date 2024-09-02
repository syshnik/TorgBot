  
import sys
import db
from birja import birjaclass 
from wallet import walletclass 
# from reshalka import reshalkaclass 
from birja_binance import birja_binance_class
from birja_bybit import birja_bybit_class
import small
import time

from time import sleep
import small
import requests 
import json
import small
import db
from dbuse  import dbuse
import mysql.connector
from datetime import datetime 
from pybit.unified_trading import HTTP
from pybit.unified_trading import HTTP


def GetTimeWithTomeRazn(timerazn):
    t1=timerazn+int(round(time.time() * 1000))
    return t1


def CalcTimeRazn():
    FinamTimeRazn, OKXTimeRazn, BybitTimeRazn, BinanceTimeRazn=0,0,0, 0
    d1=dbuse(None, None)
    try:
        #Finam
        b1=birja_bybit_class(d1.GetCursor(), d1.GetConn(), 'finam', 1, 'SBER', 'RUB', 0, 0)
        milliseconds = int(round(time.time() * 1000))
        #print(milliseconds)
        t1=b1.GetBirjaTime()
        small.ifnoterr(t1 > 1693293263915 and t1 < 1693293263915+100*365*24*60*60*1000 )
        FinamTimeRazn=t1-milliseconds
        small.ifnoterr(abs(t1-GetTimeWithTomeRazn(FinamTimeRazn)) < 60*60*1000)
    except :
        print('Get time error 222333')
        if small.ItDebug()==False:            sleep(3)
    try:
        #OKX
        b1=birja_bybit_class(d1.GetCursor(), d1.GetConn(), 'okx', 1, 'BTC', 'USDT', 0, 0)
        milliseconds = int(round(time.time() * 1000))
        #print(milliseconds)
        t1=b1.GetBirjaTime()
        small.ifnoterr(t1 > 1693293263915 and t1 < 1693293263915+100*365*24*60*60*1000 )
        OKXTimeRazn=t1-milliseconds
        small.ifnoterr(abs(t1-GetTimeWithTomeRazn(OKXTimeRazn)) < 60*60*1000)
    except :
        print('Get time error 222333')
        if small.ItDebug()==False:            sleep(3)
    try:
        #bybit
        b1=birja_bybit_class(d1.GetCursor(), d1.GetConn(), 'bybit', 1, 'BTC', 'USDT', 0, 0)
        milliseconds = int(round(time.time() * 1000))
        #print(milliseconds)
        t1=b1.GetBirjaTime()
        small.ifnoterr(t1 > 1693293263915 and t1 < 1693293263915+100*365*24*60*60*1000 )
        BybitTimeRazn=t1-milliseconds
        small.ifnoterr(abs(t1-GetTimeWithTomeRazn(BybitTimeRazn)) < 60*60*1000)
    except :
        print('Get time error 222333')
        if small.ItDebug()==False:            sleep(3)
    try:
        #binance
        b1=birja_binance_class(d1.GetCursor(), d1.GetConn(), 'binanceusdt', 1, 'AAVE', 'USDT', 0, 0)
        t1=b1.GetBirjaTime()
        small.ifnoterr(t1 > 1693293263915 and t1 < 1693293263915+100*365*24*60*60*1000 )
        BinanceTimeRazn=t1-milliseconds
        small.ifnoterr(abs(t1-GetTimeWithTomeRazn(BinanceTimeRazn)) < 60*60*1000)
    except :
        print('Get time error 222333')
        if small.ItDebug()==False:            sleep(3)
    return FinamTimeRazn, OKXTimeRazn, BybitTimeRazn, BinanceTimeRazn

