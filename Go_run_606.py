import sys
import db
from birja import birjaclass 
from wallet import walletclass 
# from reshalka import reshalkaclass 
from birja_binance import birja_binance_class
from birja_bybit import birja_bybit_class
from birja_okx import birja_okx_class
from birja_finam import birja_finam101_class
import small
import time
import datetime

from time import sleep
import small
import requests 
import json
import small
import db
from dbuse import dbuse
import mysql.connector
# from datetime import datetime 
from pybit.unified_trading import HTTP
from pybit.unified_trading import HTTP
import timerazn
import AddNewPricesForBirja
#_BybitTimeRazn=0_BinanceTimeRazn=0
# from orders import  ordersclass
# from datetime import datetime
from ii_bloha_up_doun_606_run import bloha_up_doun_606_run
from orders_606 import ordersclass_606

print('В параметрах - имена бирж')
blist=[]
if __name__ == "__main__":
    # ЧТЕНИЕ ПАРАМЕТРОВ ИЗ ПАРАМЕТРОВ
    for param in sys.argv:
        blist.append(param)
else:
    # ЗАПУСК ИЗ ДРУГОГО СКРИПТА
    blist.append('bybit')
    blist.append('binancebnb')
    blist.append('binanceusdt')
    blist.append('okx')
    blist.append('finam')


# забиваем биржу и алгоритм
birja100500=''
plusalgo100500=''
for b11 in blist:
    if b11 == 'bybit': birja100500=b11
    if b11 == 'binancebnb': birja100500=b11
    if b11 == 'binanceusdt': birja100500=b11
    if b11 == 'okx': birja100500=b11
    if b11 == 'finam': birja100500=b11
    if b11 == 'simulgame': plusalgo100500="_"+b11
    if b11 == 'smsgame': plusalgo100500="_"+b11
small.SetAlgoName('Algo_606_'+birja100500+plusalgo100500)


_Gl_showcoins=False
nextfortime=0
exceptsikoko=0
FinamTimeRazn=0
OKXTimeRazn=0
BybitTimeRazn=0
BinanceTimeRazn=0
SikokoSpim=0
_LastRunTime=0

print(blist)
#test names
next=0
bnamesstr=' and (1=2 '
for b1 in blist:
    next=next+1
    if next == 1: continue
    if b1 != 'bybit' and b1 != 'binancebnb'  and b1 != 'binanceusdt' and b1 != 'okx' and b1 != 'finam':
        if b1 == 'showcoins':
            _Gl_showcoins=True
        else:
            print(b1+' not right bname')
            break
    else :
        bnamesstr=small.adder(bnamesstr, ' or birja=\'' , b1, '\' ')

bnamesstr=small.adder(bnamesstr, ' ) ')
print(bnamesstr)



	


def GetBirjaClass(cursor, conn, birja):
    # возвращает класс биржы

    global nextfortime
    global exceptsikoko
    global FinamTimeRazn
    global OKXTimeRazn
    global BybitTimeRazn
    global BinanceTimeRazn
    global SikokoSpim
    global _LastRunTime

    b1=None
    if birja=='finam':
        b1=birja_okx_class(cursor, conn, 'finam', 5, 'SBER', 'RUB', 0, FinamTimeRazn)
    if birja=='okx':
        b1=birja_okx_class(cursor, conn, 'okx', 5, 'BTC', 'USDT', 0, OKXTimeRazn)
    if birja=='bybit':
        b1=birja_bybit_class(cursor, conn, 'bybit', 5, 'BTC', 'USDT', 0, BybitTimeRazn)
    if birja=='binancebnb':
        b1=birja_binance_class(cursor, conn, 'binancebnb', 5, 'AAVE', 'BNB', 0, BinanceTimeRazn)
    if birja=='binanceusdt':
        b1=birja_binance_class(cursor, conn, 'binanceusdt', 5, 'AAVE', 'USDT', 0, BinanceTimeRazn)
    return b1
    
def APora(cursor, conn, birja):
    # решает пора или не пора 

    global nextfortime
    global exceptsikoko
    global FinamTimeRazn
    global OKXTimeRazn
    global BybitTimeRazn
    global BinanceTimeRazn
    global SikokoSpim
    global _LastRunTime

    bi=GetBirjaClass(cursor, conn, birja)
    btime=bi.GetBirjaTime_From_MS_SMesh()
    #btime = int(round(time.time() * 1000))
    btime5=btime-(btime%(5*60*1000))
    pora=False
    spim=0
    if _LastRunTime==0: 
        pora=True
    else:
        if _LastRunTime < btime5:
            pora=True
        else:
            spim=1+round((_LastRunTime+5*60*1000-btime)/2000)
    if pora:
        _LastRunTime=btime5
    return pora, spim

def AddNewPrices000():

    global nextfortime
    global exceptsikoko
    global FinamTimeRazn
    global OKXTimeRazn
    global BybitTimeRazn
    global BinanceTimeRazn
    global SikokoSpim
    global _LastRunTime
    global _Gl_showcoins
    #
    d1=dbuse(None, None)
    for birja in blist:
        if birja != 'bybit' and birja != 'binancebnb'  and birja != 'binanceusdt' and birja != 'okx' and birja != 'finam':
            continue
        # small.SetAlgoName('Algo_606_'+birja)
        # Флаг что занят
        db.AddUpdate_peremenniye_AndCursor(d1.GetCursor(), d1.GetConn(), "work_in_606_"+birja, "True")
        # обновим прайсы
        AddNewPricesForBirja.VsehObnovim(d1.GetCursor(), d1.GetConn(), birja)
        # Флаг что не  занят
        db.AddUpdate_peremenniye_AndCursor(d1.GetCursor(), d1.GetConn(), "work_in_606_"+birja, "False")


def OrderOpenClose():

    global nextfortime
    global exceptsikoko
    global FinamTimeRazn
    global OKXTimeRazn
    global BybitTimeRazn
    global BinanceTimeRazn
    global SikokoSpim
    global _LastRunTime
    global _Gl_showcoins
    #
    d1=dbuse(None, None)
    for birja in blist:
        if birja != 'bybit' and birja != 'binancebnb'  and birja != 'binanceusdt' and birja != 'okx' and birja != 'finam':
            continue
        # small.SetAlgoName('Algo_606_'+birja)
        TimeRazn=0
        if birja=='bybit':
            TimeRazn=BybitTimeRazn
        elif birja=='binancebnb' or birja=='binanceusdt':
            TimeRazn=BinanceTimeRazn
        elif birja=='okx':
            TimeRazn=OKXTimeRazn
        elif birja=='finam':
            TimeRazn=FinamTimeRazn
        else:
            small.ifnoterr(1==2)
        # Флаг что занят
        db.AddUpdate_peremenniye_AndCursor(d1.GetCursor(), d1.GetConn(), "work_in_606_"+birja, "True")
        # заходим 
        bstr=' and birja=\''+birja+'\' '
        order=ordersclass_606(d1.GetCursor(), d1.GetConn(), SikokoSpim, TimeRazn, bstr)
        bloha=bloha_up_doun_606_run(d1.GetCursor(), d1.GetConn(), order, birja, False, _Gl_showcoins)
        # correct
        order.CorrectBadClosedOrders()
        # go
        if _LastRunTime == 0:
            _LastRunTime = int(round(time.time() * 1000))
        bloha.Go(_LastRunTime)
        bloha.PrintInfo(_LastRunTime)
        # Флаг что не  занят
        db.AddUpdate_peremenniye_AndCursor(d1.GetCursor(), d1.GetConn(), "work_in_606_"+birja, "False")


def Jdem5Min():

    global nextfortime
    global exceptsikoko
    global FinamTimeRazn
    global OKXTimeRazn
    global BybitTimeRazn
    global BinanceTimeRazn
    global SikokoSpim
    global _LastRunTime
    global _Gl_showcoins
    #
    d1=dbuse(None, None)
    for birja in blist:
        if birja != 'bybit' and birja != 'binancebnb'  and birja != 'binanceusdt' and birja != 'okx' and birja != 'finam':
            continue
        # small.SetAlgoName('Algo_606_'+birja)
        # ждем 5 мни
        while True:
            pora, spim=APora(d1.GetCursor(), d1.GetConn(), birja)
            if pora or small.ItJdem5Minut() == False: 
                break
            now = datetime.datetime.now() # current date and time
            print("Sleep "+str(spim)+" secund    "+str(now)+"  "+str(_LastRunTime))
            sleep(spim)
        sleep(12)  
        if birja=='okx' :
            if small.ItDebug() == False and small.ItJdem5Minut():
                print("==========Sleep plus 22 secund for okx========")
                sleep(22)  
        if birja=='finam':
            if small.ItDebug() == False and small.ItJdem5Minut():
                print("==========Sleep plus 22 secund for finam========")
                sleep(44)  


def UpdateFinamLotsSizes():

    global nextfortime
    global exceptsikoko
    global FinamTimeRazn
    global OKXTimeRazn
    global BybitTimeRazn
    global BinanceTimeRazn
    global SikokoSpim
    global _LastRunTime
    global _Gl_showcoins
    # обновление таблицы кол-ва лотов для ФИНАМ
    # работает ночью тк оч меденная
    now2=datetime.datetime.now()
    t0=now2.time()
    t1mono=datetime.time(3, 0)
    t2mono=datetime.time(4, 0)
    debugmono=False
    if debugmono==False:
        if t0 < t1mono or t0 > t2mono:
            return 0
    # mono
    for birja in blist:
        if birja != 'bybit' and birja != 'binancebnb'  and birja != 'binanceusdt' and birja != 'okx' and birja != 'finam':
            continue
        if birja=='finam':
            b1 = b1=birja_finam101_class(None, None, 'finam', 1, 'SBER',  'RUB', 1, 0)
            # зачистка NULL
            b1.MakeCommand("update  symb set lotize_changedate=NOW() WHERE birja='finam' AND lotize_changedate IS null")
            # берем наперед давно не обновленные    order BY lotize_changedate
            rows=b1.GetSell("select coin from symb where birja='finam'  order BY lotize_changedate")
            for r1 in rows:
                for n1 in range(0, 3):
                    ok=b1.UpdateLotSize(r1[0])
                    # sleep(10)
                    if ok:
                        # отметка времени обновления
                        # b1.MakeCommand("update  symb set lotize_changedate=NOW() WHERE birja='finam' \
                        #                AND coin='"+r1[0]+"' ")
                        sleep(70)
                        break
                    sleep(70)



def SmeshenieVremeni():
    #смещение для локального определения времени

    global nextfortime
    global exceptsikoko
    global FinamTimeRazn
    global OKXTimeRazn
    global BybitTimeRazn
    global BinanceTimeRazn
    global SikokoSpim
    global _LastRunTime

    if nextfortime % 100 == 0:
        FinamTimeRazn, OKXTimeRazn, BybitTimeRazn, BinanceTimeRazn = timerazn.CalcTimeRazn()
        nextfortime=0
    nextfortime=nextfortime+1
    print('exceptsikoko = '+str(exceptsikoko)+'  time '+str(time.gmtime()))



while True :
    # new lots sizes
    if small.ItInTry():
        try:
            UpdateFinamLotsSizes()
        except :
            d1=dbuse(None, None)
            db.PrintInfoToComments(d1.GetCursor(), d1.GetConn(), None, small.GetAlgoName(), "Try Except UpdateFinamLotsSizes 224567866")
            print("Try Except UpdateFinamLotsSizes 224567866")
    else:
        UpdateFinamLotsSizes()
    # обновление цен
    if small.ItInTryAddPrices():
        try:
            SmeshenieVremeni()
            AddNewPrices000()
        except :
            d1=dbuse(None, None)
            str4="Try Except 26565777. Error in SmeshenieVremeni()"
            db.PrintInfoToComments(d1.GetCursor(), d1.GetConn(), None, small.GetAlgoName(), str4)
            print(str4)
            if small.ItDebug() :            sleep(3)
            else :            sleep(11)
            exceptsikoko=exceptsikoko+1
    else:
        if True:
            SmeshenieVremeni()
            AddNewPrices000()
    #  купить продать 
    if small.ItInTry():
        try:
            OrderOpenClose()
        except :
            d1=dbuse(None, None)
            db.PrintInfoToComments(d1.GetCursor(), d1.GetConn(), None, small.GetAlgoName(), "Try Except 222777")
            print("Try Except 222777")
            if small.ItDebug() :            sleep(3)
            else :            sleep(130)
            exceptsikoko=exceptsikoko+1
    else:
        if True:
            OrderOpenClose()
    # pause -----
    if small.ItInTry():
        try:
            Jdem5Min()
        except :
            d1=dbuse(None, None)
            db.PrintInfoToComments(d1.GetCursor(), d1.GetConn(), None, small.GetAlgoName(), "Try Except 2277722")
            print("Try Except 2277722")
    else:
        Jdem5Min()
    
