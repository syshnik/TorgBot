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
import load_price
from time import sleep
import small
import requests 
import json
import small
import db
from dbuse import dbuse
import mysql.connector
from datetime import datetime 
from pybit.unified_trading import HTTP
from pybit.unified_trading import HTTP
import timerazn



class ordersclass_606(dbuse):
 

    def PostSleepSSS(self):
        sleep(self.SikokoSpim) 

    def __init__(self, cursor, conn, SikokoSpim, TimeRazn, bnamesstr):
        super().__init__(cursor, conn)
        self.SikokoSpim = SikokoSpim
        self.___id=int(0)
        self.___long=True
        #
        self.	___url_bybit	  =''
        self.	___url_binance	  =''
        self.	___url_primexbt	  =''
        self.	___birja	  =''
        self.	___coin	  =''
        self.	___bcoin	  =''
        self.	___instrument	  =''
        self.	___min_up_percent	  =''
        self.	___max_up_percent	  =''
        self.	___min_doun_percent	  =''
        self.	___max_doun_percent	  =''
        self.	___sozdan	  =''
        self.	___kuplen	  =''
        self.	___prodan	  =''
        self.	___endorder	  =''
        self.	___beginorder	  =''
        self.	___krayprice	  =''
        self.	___hesh	  =''
        self.	___kuda	  =''
        self.	___marja	  =''
        self.	___period	  =''
        self.	___proshlo	  =''
        self.	___inputprice	  =''
        self.	___outputprice	  =''
        self.   ___kraypriceproshli =''
        self._TimeRazn=TimeRazn
        # self._BybitTimeRazn=BybitTimeRazn
        # self._BinanceTimeRazn=BinanceTimeRazn
        self._bnamesstr=bnamesstr
 
    def AddComment(self,comment):
        db.MakeCommand("insert into comments(_order, _date, _comment) values ("
                       +str(self.___id)+", now(), '"+comment+"')")
    
    def MError_Fatal_TryEx(self, comment):
        self.AddComment(comment)
        print(comment)
        small.ifnoterr(1==0)

    def GetOrder(self, id):  
        #ордер info
        self.___id=int(id)
        # conn=db.GetConnect()
        # cursor = conn.cursor()
        proslo5='if( kuplen is null, (TIME_TO_SEC(TIMEDIFF(now(), beginorder ) )/60), (TIME_TO_SEC(TIMEDIFF(now(), kuplen ) )/60))'
        z1='select '
        z1=small.adder(z1, 		'url_bybit'	, ', ')
        z1=small.adder(z1, 		'url_binance'	, ', ')
        z1=small.adder(z1, 		'url_primexbt'	, ', ')
        z1=small.adder(z1, 		'birja'	, ', ')
        z1=small.adder(z1, 		'coin'	, ', ')
        z1=small.adder(z1, 		'quote'	, ', ')
        z1=small.adder(z1, 		'instrument'	, ', ')
        z1=small.adder(z1, 		'min_up_percent'	, ', ')
        z1=small.adder(z1, 		'max_up_percent'	, ', ')
        z1=small.adder(z1, 		'min_doun_percent'	, ', ')
        z1=small.adder(z1, 		'max_doun_percent'	, ', ')
        z1=small.adder(z1, 		'sozdan'	, ', ')
        z1=small.adder(z1, 		'kuplen'	, ', ')
        z1=small.adder(z1, 		'prodan'	, ', ')
        z1=small.adder(z1, 		'endorder'	, ', ')
        z1=small.adder(z1, 		'beginorder'	, ', ')
        z1=small.adder(z1, 		'krayprice'	, ', ')
        z1=small.adder(z1, 		'hesh'	, ', ')
        z1=small.adder(z1, 		'kuda'	, ', ')
        z1=small.adder(z1, 		'(TIME_TO_SEC(TIMEDIFF(endorder, beginorder ) )/60)'	, ', ')
        z1=small.adder(z1, 		proslo5	, ', ')
        z1=small.adder(z1, 		'inputprice'	, ', ')
        z1=small.adder(z1, 		'kraypriceproshli'	, ', ')
        z1=small.adder(z1, 		'dnoprobil'	, ', ')
        z1=small.adder(z1, 		'outputprice'	, ', ')
        z1=small.adder(z1, 		'marja'	, ', ')
        z1=small.adder(z1, 		'1  FROM orders where id=', str(id))
        rows=db.GetSel55(self.GetCursor(), z1)
        if len(rows) == 0:
            return False
#        for row in rows:            ret1=row[0]
        self.	___url_bybit	 =rows[0][	0	]
        self.	___url_binance	 =rows[0][	1	]
        self.	___url_primexbt	 =rows[0][	2	]
        self.	___birja	 =rows[0][	3	]
        self.	___coin	 =rows[0][	4	]
        self.	___bcoin	 =rows[0][	5	]
        self.	___instrument	 =rows[0][	6	]
        self.	___min_up_percent	 =rows[0][	7	]
        self.	___max_up_percent	 =rows[0][	8	]
        self.	___min_doun_percent	 =rows[0][	9	]
        self.	___max_doun_percent	 =rows[0][	10	]
        self.	___sozdan	 =rows[0][	11	]
        self.	___kuplen	 =rows[0][	12	]
        self.	___prodan	 =rows[0][	13	]
        self.	___endorder	 =rows[0][	14	]
        self.	___beginorder	 =rows[0][	15	]
        self.	___krayprice	 =rows[0][	16	]
        self.	___hesh	 =rows[0][	17	]
        self.	___kuda	 =rows[0][	18	]
        self.	___period	 =rows[0][	19	]
        self.	___proshlo	 =rows[0][	20	]
        self.	___inputprice	 =rows[0][	21	]
        self.   ___kraypriceproshli	 =rows[0][	22	]
        self.   ___dnoprobil	 =rows[0][	23	]
        self.	___outputprice	 =rows[0][	24	]
        self.	___marja	 =rows[0][	25	]
        #
        self.___long=(self.	___kuda=='buy')
        self.	___marja=int(self.	___marja)
        self.   ___kraypriceproshli=True if (self.___kraypriceproshli==1) else False
        self.   ___dnoprobil=True if (self.___dnoprobil==1) else False
        # #раззница времени
        # if self.___birja=='bybit':
        #     self._TimeRazn=self._BybitTimeRazn
        # elif self.___birja=='binancebnb' or self.___birja=='binanceusdt':
        #     self._TimeRazn=self._BinanceTimeRazn
        # elif self.___birja=='okx':
        #     self._TimeRazn=self._OKXTimeRazn
        # else:
        #     small.ifnoterr(1==2)
        # conn.commit()
        # conn.close()
        # cursor.close()
        return True
    
    def GetNextPosicionTo__Open__or__Close(self, oldnext,isopen):  
        #ордер для открытия ... или закрытия
        # conn=db.GetConnect()
        # cursor = conn.cursor()
        id=int(0)
        zapros=small.adder("SELECT min(id) FROM orders where coin is not null and (arhiv is null or arhiv != 1)",
                           " and  id > ", str(oldnext), self._bnamesstr)
        if(isopen):
            zapros=small.adder(zapros, " and kuplen is null ")
            # if small.ItDebug()!=True:                zapros=small.adder(zapros, "  and endorder > now() ")
        else:
            zapros=small.adder(zapros, " and kuplen is not null and prodan is null ")
        #zapros=small.adder(zapros, " and birja='bybit' ")
        rows=db.GetSel55(self.GetCursor(), zapros)
        if rows[0][0] != None:
            for row in rows:
                id=row[0]
        # conn.commit()
        # conn.close()
        # cursor.close()
        return id
    
    def Obnovim(self, id, setstr):  
        #ордер для открытия ... или закрытия
        conn=db.GetConnect()
        cursor = conn.cursor()
        cursor.execute("update orders set "+setstr+" where  id="+str(id))
        conn.commit()
        conn.close()
        cursor.close()
        return id
    


    def GetNextPosicionToOpen(self, oldnext):  
        return self.GetNextPosicionTo__Open__or__Close(oldnext,True)
    
    def GetNextPosicionToClose(self, oldnext): 
        return self.GetNextPosicionTo__Open__or__Close(oldnext,False)

    def GetBirjaClass(self, idorder):
        b1=''
        if self.___birja=='finam':
            b1=birja_finam101_class(self.GetCursor(), self.GetConn(), self.___birja, self.SikokoSpim, self.	___coin, self. ___bcoin,idorder, self._TimeRazn)
        elif self.___birja=='okx':
            b1=birja_okx_class(self.GetCursor(), self.GetConn(), self.___birja, self.SikokoSpim, self.	___coin, self. ___bcoin,idorder, self._TimeRazn)
        elif self.___birja=='bybit':
            b1=birja_bybit_class(self.GetCursor(), self.GetConn(), self.___birja, self.SikokoSpim, self.	___coin, self. ___bcoin,idorder, self._TimeRazn)
        elif self.___birja=='binancebnb' or self.___birja=='binanceusdt':
            b1=birja_binance_class(self.GetCursor(), self.GetConn(), self.___birja, self.SikokoSpim, self.	___coin, self. ___bcoin, idorder, self._TimeRazn)
        else:
            small.ifnoterr(1==2)
        return b1

    def GetUtochnenniyPrognoz(self, percentprognoz, lastprice):
        #  уточним прогноз сделанный по базе 5-ти минутной с текущей ценой
        tname=small.GetTableName(self.___birja, self.___coin)
        rows=db.GetSel77(None, 
            'select    price from '+tname+' ORDER BY id DESC  LIMIT 1')
        newprice=rows[0][0]
        ujeperc=(newprice-lastprice)*100/lastprice
        retprognoz=percentprognoz-ujeperc
        return retprognoz
    
    def UjeOtkrito(self):
        # ОПРЕДЕЛЯЕТ ЧТО ДАННАЯ МОНЕТА УЖЕ КУПЛЕНА
        rows=db.GetSel77(None, 
            "select    id from  orders WHERE   birja='"+self.___birja+"' "
            +" and coin='"+self.___coin+"' "
            +" and kuplen is not null and prodan is null")
        if len(rows) == 0:
            return False
        return True

    def Zachistka(self, birja):
        # зачистка кривых ордеров
        z1="update orders set arhiv=1 WHERE \
            ((kuplen is null and prodan is null) or (kuplen is not null and prodan is not null))\
            and    birja='"+birja+"' "
        self.MakeCommand(z1)
        return 0
    
    def AddNewOrder(self, buy, marja, birja, coin, bcoin):
        ssilka=''
        if birja=="bybit":
            ssilka = small.adder("https://www.bybit.com/ru-RU/trade/spot/", coin, "/", bcoin)
        if birja=="binancebnb" or birja=="binanceusdt":
            ssilka = small.adder("https://www.binance.com/ru/trade/", coin, "_", bcoin, "?theme=light&type=spot")
        if birja=="okx":
            ssilka = small.adder("https://www.okx.com/ru/trade-spot/", coin, "-", bcoin)
        z0=small.adder("select iname  from symb where birja='", birja
                                    , "' and  coin='" ,  coin ,  "' "
                                    ,"		and stavim=1")
        iname=db.GetSel77(None, z0)
        buystr = "buy" if buy else "sell"
        z1=small.adder("insert into orders (birja, url_bybit, coin, quote, instrument\
                       , beginorder\
                       , kuda, marja, endorder)"
                       , " values ("
                        ,  " '" ,  birja ,  "', "
                        ,  " '" ,  ssilka ,  "', "
                        ,  " '" ,  coin ,   "', "
                        ,  " '" ,  bcoin ,   "', "
                        ,  " '" ,  iname[0][0] ,   "', "
                        ,  " now(), "
                        ,  " '" ,  buystr ,  "', "
                        ,  " '" ,  marja ,  "', "
                        ,  " null )")
        db.MakeCommand(z1)


    def AddCommentBig(self, order, timepar):
        db.MakeCommand("insert into comments (_comment, _order, _date, _int) values ('Add order 606', "
                       +str(order)+", now(), "+str(timepar)+")")
                      
                      

    def CorrectBadClosedOrders(self):
        # выберем плохо закрытые ордера
        id=0
        while True:
            id=self.GetNextPosicionToClose( id)
            if id==0: break
            rows=db.GetSel77(self.GetCursor(), "select tryoutput from orders where  id="+str(id))
            tryoutput=small.GetCorrectOneNoteFromRowsAsOne(rows)
            if tryoutput != 1: continue
            # correct
            if self.GetOrder(id) != True: continue
            b1=self.GetBirjaClass(id)
            err, sikusd, sikcoin=b1.GetRealSumm(self.___coin, self.___marja)
            lp=b1.GetCorrectKrayPrice(self.___coin, self.___long==False)
            if lp is None:
                print('Error 3457889433')
                continue
            sikcoin_in_usdt=sikcoin*lp
            # решаем закрыть ордер или нет
            if b1.Stavka() == 0:
                del1=sikcoin_in_usdt/sikusd
                if del1 > 0.7:
                    continue
            else:
                del1=sikcoin_in_usdt/b1.Stavka()
                if del1 > 0.7:
                    continue
            # видимо уже все сделано (продану...)
            self.WorkCloseOrder(id, "ok Close in CorrectBadClosedOrders",  lp)
            gffgt=0


    def OpenPosicion(self):  
        #открываем оррдераа
        id=0
        id=self.GetNextPosicionToOpen( id)
        if id==0:
            #нету ордеров
            print('No orders to stavka')
            return False
        if self.GetOrder(id) == False:
            small.ifnoterr(0==1)
            return False
        buy=True if self.___long==True  else False
        #locaL CLASSES
        w1=walletclass(self.___birja, self.SikokoSpim)
        b1=self.GetBirjaClass(id)
        #пробуем войти
        ret1=''
        db.MakeCommand("update  orders set  tryinput=1 where id="+str(self.___id))
        #пытаемся войти несколько раз
        sik1=3
        if small.ItSMSBuySell() or small.ItDebugRandBuySell() or small.ItDebugBuySell(): sik1=1
        for  n1 in range(0, sik1):
            if small.ItInTry():
                try:
                    ret1=b1.BySellCoin( self.___id, self.___coin, buy, b1.Stavka(), self.___long, self.___marja)
                except :
                    ret1='except'
            else:
                ret1=b1.BySellCoin( self.___id, self.___coin, buy, b1.Stavka(), self.___long, self.___marja)
            if ret1=='ok':
                break
            sleep(10)
        #for-----------------------------------------------------
        if ret1=='ok':
            self.Obnovim(id, ' kuplen=now(), inputprice='+str(b1._for_order_Price/b1.GetLotSize()))  
            return True
        else:
            self.Obnovim(id, "  comm='except ("+str(ret1)+") when try input', arhiv=1 ")
            self.AddComment(str(ret1)+' except when try input '+self.___birja+'   '+self.___coin)
            return False
        return False



    def GetWorkCoinOrderId(self, AndToOpen=False, AndToClose=True):
        #текущая монета
        id=0
        if id==0 and AndToClose: id=self.GetNextPosicionToClose( id)
        if id==0 and AndToOpen: id=self.GetNextPosicionToOpen( id)
        if id==0:
            #нету ордеров
            print('No orders to close')
            return None
        if self.GetOrder(id) == False:
            small.ifnoterr(0==1)
            return None
        return id

    def WorkCloseOrder(self, id, comm,  price):
        w1=walletclass(self.___birja, self.SikokoSpim)
        self.Obnovim(id, '  arhiv=1 , prodan=now(), outputprice='+str(price)
                        +' , comm=\''+comm+'\'')  
        w1.ClearForOrder(id)

    def ClosePosicion(self):  
        #zaaaaaкрываем оррдераа
        id=0
        id=self.GetNextPosicionToClose( id)
        if id==0:
            #нету ордеров
            print('No orders to close')
            return False
        if self.GetOrder(id) == False:
            small.ifnoterr(0==1)
            return False
        buy=False if self.___long==True  else True
        #locaL CLASSES
        w1=walletclass(self.___birja, self.SikokoSpim)
        b1=self.GetBirjaClass(id)
        #пробуем выйти
        ret1=''
        comm1='ok'
        if small.ItSMSBuySell() == False:
            # машинка не предпологает отмены своихрешений
            # а человек может
            db.MakeCommand("update  orders set  tryoutput=1 where id="+str(self.___id))
        if small.ItInTry():
            sik1=10
            if small.ItSMSBuySell() or small.ItDebugRandBuySell() or small.ItDebugBuySell(): sik1=1
            for ntry in range (0, sik1):
                okclose=False
                try:
                    ret1=b1.BySellCoin( self.___id, self.___coin, buy, b1.Stavka(), self.___long, self.___marja)
                    okclose=True
                except :
                    self.Obnovim(id, "  comm='except close' ")
                    self.AddComment('except when try close '+self.___birja+'   '+self.___coin)
                if okclose:
                    break
                sleep(5)
        else:
            ret1=b1.BySellCoin( self.___id, self.___coin, buy, b1.Stavka(), self.___long, self.___marja)
        if ret1=='ok':
            self.WorkCloseOrder(id, comm1,  str(b1._for_order_Price/b1.GetLotSize()))
            return True
        return False

