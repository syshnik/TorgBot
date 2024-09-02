from time import sleep
import small
import db
from dbuse import dbuse
import time
from wallet import walletclass 
from sms_obmen_base import sms_obmen_base_class
import math
from datetime import datetime 
from pybit.unified_trading import HTTP
from pybit.unified_trading import HTTP



def MError_NoMoney():
    print('No coins')
    return 1
def MError_KrayProshli():
    print('Kray proshli')
    return 2
def MError_Napravlenie():
    print('Ne то напрвление')
    return 3
def MError_Fatal():
    print('Fatal Error 4444')
    return 4

def MErrorServer(strpar):
    print(strpar)
    return 5

#Alt-d   Alt-s bookmarks
class birjaclass(dbuse):
 
    def __init__(self, cursor, conn, name, SikokoSpim, coin, bcoin,order, BybitTimeRazn):
        super().__init__(cursor, conn)
        self._BybitTimeRazn = BybitTimeRazn
        self.name = name    # имя 
        self.SikokoSpim=SikokoSpim
        self._for_order_AskPrice=float(0)
        self._for_order_BidPrice=float(0)
        self._for_order_Price=float(0)
        self._znakov=555
        self._coin=coin
        self._bcoin=bcoin
        self._znakov=-1
        self.InitZnakovPZ()
        self._order=order
        if self._bcoin == 'USDT':
            self._zanakov_bcoin=1
        elif self._bcoin == 'BNB':
            self._zanakov_bcoin=4
        elif self._bcoin == 'RUB':
            self._zanakov_bcoin=2
        else:
            small.ifnoterr(1==2)
        self._marja=0
        self._long=True


    def GetLotSize(self):
        return 1

    def GetBirjaTime_From_MS_SMesh(self):
        t1=self._BybitTimeRazn+int(round(time.time() * 1000))
        return t1

    def PostSleepSSS(self):
        sleep(self.SikokoSpim) 

    def InitZnakovPZ(self):  
        #считает сколько заков после зпт в монете
        # conn=db.GetConnect()
        # cursor = conn.cursor()
        rows=self.GetSell("select max(znpz) from symb where birja='"
                                  +self.name+"' and coin='"
                                  +self._coin+"' and bcoin='"
                                  +self.GetSCoin()+"'  ")
        small.ifnoterr( rows[0][0] != None )
        for row in rows:
            self._znakov=row[0]
        # conn.commit()
        # cursor.close()
        # conn.close()

    def GetSCoin(self):
        return self._bcoin
    
    # def Stavka(self):
    #     if self.name=='bybit':
    #         return float(4.8)
    #     return float(0)
    

    # def GetBallance(self, coinname):
    #     self.PostSleepSSS()
    #     if self.name=='bybit':
    #         gs = HTTP(testnet=True)
    #         ps=small.GetSessionKS()
    #         w1=ps.get_wallet_balance(
    #             accountType="UNIFIED", 
    #             coin=coinname,
    #         )
    #         ret=float(w1['result']['list'][0]['coin'][0]['availableToWithdraw'])
    #         return ret
    #     return float(-1)

        
    def GetCorrectBCoin(self, sikest111, siknado111, byflag):
        #корректировка сумы в долларах для покупки
        ret=float(0)
        sikest=float(sikest111)
        siknado=float(siknado111)
        if byflag:
            if siknado==0:
                # торгуем на все
                ret = sikest
            elif sikest > siknado*3/2:
                ret = siknado
            elif sikest > siknado/2:
                ret=sikest*98/100
            else:
                ret=0
        else:
            ret=sikest
        ret=small.RoundToMin(ret, self._zanakov_bcoin)
        return ret

    def GetCorrectCoin(self, OrderId, sikest111, siknado111, byflag):
        #корректировка сумы в монетах для покупки
        ret=float(0)
        sikest=float(sikest111)
        siknado=float(siknado111)
        if sikest<=0:
            return 0
        #
        if byflag:
            ret=sikest
        else:
            ret=sikest
            # w1=walletclass(self.name , self.SikokoSpim)
            # s1=float(w1.GetCoinsFromOrder(self._coin, OrderId))
            # prop=s1/sikest
            # if prop == 0:   #ошибка в кошельке
            #     if sikest > siknado*3/2:
            #         ret = siknado
            #     else:
            #         ret=sikest
            # elif prop > 0.7 and prop < 1.4: #одна ставка в монете
            #     ret=sikest
            # else:
            #     if sikest > siknado*3/2:
            #         ret = siknado
            #     else:
            #         ret=sikest
        ret=small.RoundToMin(ret, self._znakov)
        return ret
    
    def GetCorrectSummBuySell(self, correctusd, correctcoin, lp, byflag):
        #
        retusdt=correctusd
        retcoin=correctcoin
        if byflag:
            retcoin=float(retusdt)/float(lp)
            retcoin=small.RoundToMin(retcoin, self._znakov)
        else:
            retusdt=float(retcoin)*float(lp)
            retusdt=small.RoundToMin(retusdt, self._zanakov_bcoin)
        return retusdt, retcoin

    def GetInterval(self, period, short, long, longlong):
        #выдает  период массив свечей
        #короткий длинный оч. длинный
        interval=1
        if period <= 60:
            if short:
                interval=1
            elif long:
                interval=5
            elif longlong:
                interval=30
            else:
                small.ifnoterr(1==0)
        elif period <= 120:
            if short:
                interval=3
            elif long:
                interval=15
            elif longlong:
                interval=60
            else:
                small.ifnoterr(1==0)
        elif period <= 240:
            if short:
                interval=5
            elif long:
                interval=30
            elif longlong:
                interval=120
            else:
                small.ifnoterr(1==0)
        else:
            if short:
                interval=15
            elif long:
                interval=60
            elif longlong:
                interval=240
            else:
                small.ifnoterr(1==0)
        return interval

    def WorkGetShagMul(self, interval, uinterval):
        shag=math.floor(float(interval)/float(uinterval))
        mul=shag*10+interval
        return shag,mul

    def MonoAddEmptyOrder_Po_Finansam(self):
        #смотрит по финансам есть ли деньги на ставку
        w1=walletclass(self.name , self.SikokoSpim)
        s1=w1.GetFreeSumm(self._bcoin)
        s2=self.MinStavka()
        if s1 >= s2:
            note=True
        else:
            note=False
        return note
        #    
    def MonoAddEmptyOrder(self):
        #добавляет если надо пустой ордер ля нового поиска
        note='False'
        if self.MonoAddEmptyOrder_Po_Nastroenie(True) and self.MonoAddEmptyOrder_Po_Finansam():
            note='True'
        # conn=db.GetConnect()
        # cursor = conn.cursor()
        self.MakeCommand("update peremenniye set perznachenie='"+note+"' where "
                       +" pername = 'find_for_"+self.name+"'")
        # conn.commit()
        # cursor.close()
        # conn.close()

    def AddOrderToWallet(self, byflag, order, bcoin, coin,  sum_bcoin, sum_coin, for_order_Price):
            w1=walletclass(self.name , self.SikokoSpim)
            if byflag:
                sum1=sum_bcoin/for_order_Price
                sum1-=(sum1*0.1/100)
                w1.AddOder(order, bcoin, coin,  sum_bcoin, sum1)
            else:
                sum1=sum_coin*for_order_Price
                sum1-=(sum1*0.1/100)
                w1.AddOder(order, coin, bcoin,  sum_coin, sum1)

    def SMSBySellCoin(self, OrderId, coinpar, buyflag, usdlimit, longflag=True, marja=0):
        sb = sms_obmen_base_class(None, None)
        st1=sb.SendMess_Buy_Sell_Short_Long(60*10, self.name, self._coin,  buyflag==True, buyflag==False, longflag==False, longflag==True)
        if st1 is None: return False
        if st1 & sb.StatusOtmenen(): return False
        if st1 & sb.StatusViponnen(): return True
        return False