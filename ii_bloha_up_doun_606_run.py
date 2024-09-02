

from __future__ import print_function
from datetime import datetime 
import random
import small
import db
from iireshalka_606 import iireshalkaclass_0_606
from iireshalka_606 import iireshalkaclass_606
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import matplotlib.pyplot as plt                              # построение графиков
from time import sleep
import array as arr 
import torch.optim as optim
import numpy as np
# import simpleaudio as simple_audio 
import time
from iimodels import model_900_606
import  iimodels 
from iiobuchalka_606 import Obuchalka_606
# from iihshar_606 import hshar_900_606
from iimodels  import class55plus
from ii_bloha_stavka_606  import bloha_stavka_606
from ii_bloha_up_doun_606  import bloha_up_doun_606
from orders_606 import ordersclass_606

Global_plusname = "_606_"
classname="model_900_606"


class bloha_up_doun_606_run(bloha_up_doun_606):
    def __init__(self, cursor, conn,order: ordersclass_606, birja, debugf, showcoins=True):
        super().__init__(cursor, conn, birja, debugf, '', False)
        self._order: ordersclass_606 = order
        self._debugf=debugf
        self._birja=birja
        self._showcoins=showcoins
        self._procent_max_ro_show_77=0  
        self._procent_min_ro_show_77=0
        #self._For_Show55=None
    
    def Get_Long_or_Buy(self):
        return self._order._ordersclass_606___long
        # return self._order.___long

    def SetForSwow(self, minperc,maxperc):
        self._procent_max_ro_show_77=maxperc
        self._procent_min_ro_show_77=minperc

    def GetFlagShowcoins(self):
        return self._showcoins

    # def PrintBudushee(self, cursor, coin, timepar):
    #     return 0
    def DebCommProcent(self, timepar):
        return 0
    def PrognozAdd(self, pp:bloha_stavka_606, i):
        return 0
    def GetWorkCoin(self):
        id = self._order.GetWorkCoinOrderId()
        if id is None: return None
        if id == 0: return None
        rows=self.GetSell("select coin from orders where id="+str(id))
        if rows is None: return None
        if len(rows) == 0: return None
        return rows[0][0]


    def AddPrintInfoToComments(self, comm1):
        self.DebComm(comm1)
        db.PrintInfoToComments(self.GetCursor(), self.GetConn(), None, small.GetAlgoName(), comm1)

    # 
    def Zachistka(self):
        self._order.Zachistka(self._birja)
        return 0

    def GetMorjesize(self, newp: bloha_stavka_606):
        if newp._marja==False:
            return 0
        return "3"
    

    def BuyCoin(self, newp: bloha_stavka_606, timepar):
        # buy
        marja=self.GetMorjesize(newp)
        self._order.AddNewOrder(newp._long_or_buy, marja, self._birja, newp._coin, small.GetBCoin(self._birja))
        ret = self._order.OpenPosicion()
        if ret:
            self._order.AddCommentBig(self._order._ordersclass_606___id, timepar)
            # self._order.AddCommentBig(self._order.___id, timepar)
        return ret
    
    # def BuyCoin222(self, newp: bloha_stavka_606, timepar):
    #     # buy
    #     if True:
    #         self._order.AddCommentBig(self._order._ordersclass_606___id, timepar)
    #         # self._order.AddCommentBig(self._order.___id, timepar)
    
    def GetPriceAndProcentAndBuyTime(self, timepar):
        # ТЕКУЩАЯ Цена и процент от покупки
        coin, price, proc, buytime=self.Get_Coin_Price_Procent(timepar)
        return price, proc, buytime

    def Get_Coin_Price_Procent(self, timepar):
        # ТЕКУЩАЯ Цена и процент от покупки
        id = self._order.GetWorkCoinOrderId()
        if id is None: return None, None, None, None
        if id == 0: return None, None, None, None
        rows=self.GetSell("select coin , inputprice, kuplen from orders where id="+str(id))
        if rows is None: return None, None, None, None
        if len(rows) == 0: return None, None, None, None
        #
        coin, price, proc, buytime=None, None, None, None
        bt1=rows[0][2]
        buytime=small.GetIntTimeFromDateTime(bt1)
        coin=rows[0][0]
        price=self.GetPriceCoin(coin, timepar)
        inputprice=rows[0][1]
        if price is None:
            return None, None, None, None
        proc=(price-inputprice)*100/inputprice
        return coin, price, proc, buytime
        # coin=self.GetWorkCoin()
        # price=self.GetPriceCoin(coin, timepar)
        # buyprice=db.GetSel77(None, "select inputprice from orders ")
        # if price is None:
        #     return None
        # proc=(price-buyprice)*100/buyprice
        # return price, proc


    # def GetPriceCoin(self, coin, timepar):
    #     # текущая цена монеты
    #     if coin is None:
    #         return None
    #     tname=small.GetTableName(self._birja, coin)
    #     rows=db.GetSel77(None, "select max(id) from "+tname
    #                      +" where id <= "+str(timepar))
    #     if len(rows) != 1: return None
    #     id=int(rows[0][0])
    #     rows=db.GetSel77(None, "select max(price) from "+tname
    #                      +" where id = "+str(id))
    #     if len(rows) != 1: return None
    #     # sell
    #     price=rows[0][0]
    #     return price
    
    def IsklBuyOldCCoin(self, i1: bloha_stavka_606, timepar):
        return False

    def SellCoin(self, timepar):
        # sell
        return self._order.ClosePosicion()

    def GetStopLossName(self):
        return str("SL_deb_"+self._birja)

    def DebComm(self,comm):
        comm2=db.GetCorrectStrToBase(comm)
        order=small.GetIntFromAll(self._order._ordersclass_606___id)

        z1="insert into commentstext (comm1, date1, order1, algo1) values ("+comm2+", now(), "+str(order)+", '"+small.GetAlgoName()+"')"
        try:
            self.MakeCommand(z1)
        except:
            self.MakeCommand("insert into commentstext (comm1, date1, order1, algo1) values ('Error 346434567', now(), 0, '"+small.GetAlgoName()+"')")

    def DebugPrintBudushee(self, coin, timepar):
        gg=0

    def GetBuyTime(self):
        bo=self._order._ordersclass_606___beginorder
        bt=small.GetIntTimeFromDateTime(bo)
        return bt

    def StopKran(self):
        StopKran=db.GetPerFromPremennie(self.GetCursor(), 'StopKran_'+small.GetAlgoName(), 'bool', True, False, False)
        return StopKran

    def GetHisCoorrectProcentPlus(self):
        id = self._order.GetWorkCoinOrderId()
        if id is None: return 0
        if id == 0: return 0
        rows=self.GetSell("select pp from orders where id="+str(id))
        pp=small.GetCorrectOneFloatNoteFromRowsAsOne(rows)
        if pp is None: return 0
        return pp
    
    def SetProcentPlus(self, pp):
        id = self._order.GetWorkCoinOrderId()
        if id is not None:
            self.MakeCommand("update  orders set pp="+str(pp)+" where id="+str(id))

    def PrintInfo(self, timepar):
        # self.GetPriceCoin()
        coin, price, proc, buytime=self.Get_Coin_Price_Procent(timepar)
        for i in range(0, 3):
            print("-------------"+self._birja+"--------------------------------------------------------")
        self.PrintSikokoCoinsObnovleno(timepar)
        if self.GetFlagShowcoins():
            coin = self.GetWorkCoin()
            if coin is None or price is None:
                print("------------"+self._birja+"----------no coins--------------------------")
            else:
                price=str(round(price, 6))
                proc=str(round(proc, 2))
                h1=str(round((timepar-buytime)/(60*60*1000), 1))
                str1="Coin is "+coin+" h="+h1+" procent="+proc
                print(str1)
                an1=small.GetAlgoName()
                db.PrintInfoToComments(self.GetCursor(), self.GetConn(), None, an1, str1)
