import small
import db
import load_price
import mysql.connector
import time
import sys
from datetime import datetime 

from time import sleep
import small


# import asyncio
import time


# async 
def Obnovim(cursor, conn, birja, coin, bcoin):
    print('Обновление для '+coin+' начато')
    if small.ItInTry():
        try:
            load_price.AddPricesNewOrOldAndCursor(cursor, conn, True, birja, coin, bcoin, None)
        except:
            for i in range(0, 3):
                print(coin+"-----------------Error 55577337 obnovlenie-------------------"+coin)
    else:
        load_price.AddPricesNewOrOldAndCursor(cursor, conn, True, birja, coin, bcoin, None)
    print('Обновление для '+coin+' завершенo')


def Dogruzim(cursor, conn, birja, rows, bcoin):
    # догружаем недогруженные монеты
    z2='select 0 '
    for r1 in rows:
        z2=z2+" , '"+r1[0]+"'  "
        z2=z2+" , (select  max(id) from "+small.GetTableName( birja, r1[0])+") "
    rows2=db.GetSel77(cursor, z2)
    # последнее значение
    maxid=0
    for n1 in range (0, len(rows)):
        coin=rows2[0][1+n1*2]
        id=rows2[0][1+n1*2+1]
        if id is not None:
            if maxid < id: maxid=id
    # список на догрузку
    dogruz=[]
    for n1 in range (0, len(rows)):
        coin=rows2[0][1+n1*2]
        id=rows2[0][1+n1*2+1]
        if id is not None:
            if maxid > id: dogruz.append(coin)
    print('++++++++ Dogruzim '+str(len(dogruz))+' monet. +++++++')
    # догрузим
    for d1 in dogruz:
        Obnovim(cursor, conn, birja, d1, bcoin)
    return 0

# async 
def main(cursor, conn, birja):
    global _birja
    birja=_birja
    bcoin=small.GetBCoin(birja)
    # список монет
    limit=" limit 3 " if small.ItDebug() else ""
    rows=db.GetSel77(cursor, "select coin from symb where  stavim=1 and birja='"+birja+"' order by id"+limit)
    # # недогруженные данные
    # Dogruzim(cursor, conn, birja, rows, bcoin)
    # новые данные
    for r1 in rows:
        Obnovim(cursor, conn, birja, r1[0], bcoin)
    # недогруженные данные
    Dogruzim(cursor, conn, birja, rows, bcoin)
    # средние
    load_price.CalcSredneeAndCursor(cursor, conn, True, birja)
    # ВЫПОЛНЕНИЕ
    # if False:
    #     # создание множества корутин
    #     coros = [Obnovim(cursor, conn, birja, coin, bcoin) for coin in _cm]
    #     # выполнение задач
    #     await asyncio.gather(*coros)
    # else:
    #     _tm=[]
    #     for coin in _cm:
    #         task1 = asyncio.create_task(Obnovim(birja, coin, bcoin))
    #         _tm.append(task1)
    #     for t1 in _tm:
    #         await t1


# async def main():
#     global _birja
#     birja=_birja
#     bcoin="USDT"
#     if birja=="binance": bcoin="BNB"
#     # список монет
#     rows=db.GetSel77(None, "select coin from symb where  stavim=1 and birja='"+birja+"' order by id")
#     _cm=[]
#     for r1 in rows:
#         _cm.append(r1[0])
#     # ВЫПОЛНЕНИЕ
#     _tm=[]
#     for coin in _cm:
#         task1 = asyncio.create_task(Obnovim(birja, coin, bcoin))
#         _tm.append(task1)
#     for t1 in _tm:
#         await t1


    # await task2

# async def main2(birja):
#     bcoin="USDT"
#     if birja=="binance": bcoin="BNB"
#     # список монет
#     rows=db.GetSel77(None, "select coin from symb where  stavim=1 and birja='"+birja+"' order by id")
#     _cm=[]
#     for r1 in rows:
#         _cm.append(r1[0])
#     # ВЫПОЛНЕНИЕ
#     next=0
#     task1 = asyncio.create_task(Obnovim(birja, _cm[next], bcoin))
#     next=next+1
#     task2 = asyncio.create_task(Obnovim(birja, _cm[next], bcoin))
#     next=next+1
#     task3 = asyncio.create_task(Obnovim(birja, _cm[next], bcoin))
#     next=next+1
#     task4 = asyncio.create_task(Obnovim(birja, _cm[next], bcoin))
#     next=next+1
#     task5 = asyncio.create_task(Obnovim(birja, _cm[next], bcoin))
#     next=next+1
#     await task1
#     await task2
#     await task3
#     await task4
#     await task5


def VsehObnovim555(cursor, conn, birja):
    print(time.strftime('%X'))
    global _birja
    _birja=birja
    # asyncio.run(main(cursor, conn, birja))
    main(cursor, conn, birja)
    print(time.strftime('%X'))


def VsehObnovim(cursor, conn, birja):
    # if small.ItInTry():
    #     try:
    #         VsehObnovim555(birja)
    #     except:
    #         for i in range(0, 4):
    #             print("-----------------Error 555777 obnovlenie-------------------")
    # else:
    VsehObnovim555(cursor, conn, birja)


