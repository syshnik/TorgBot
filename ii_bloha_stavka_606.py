

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
# https://qudata.com/ml/ru/NN_Base_Torch_NN.html
# import simpleaudio as simple_audio 
import time
from iimodels import model_900_606
import  iimodels 
from iiobuchalka_606 import Obuchalka_606
# from iihshar_606 import hshar_900_606
from iimodels  import class55plus
from napravlalka import NapravlalkaClass
from napravlalka import NapravlalkaInfa
# Global_plusname = "_606_"
# classname="model_900_606"
# sikokoskokov=0
# modelshablon=model_900_606()

class bloha_stavka_606:
    def __init__(self):
        self._birja=''
        self._coin=''
        self._fup, self._fdoun, self._vshort=0,0,0
        self._long_or_buy=True
        self._marja=False
        self._maxperc=0
        self._minperc=0
        self._maxpercsex=0
        self._minpercsex=0
        self._razn=0
        self._razn_abs=0
        self._razn_sex_abs=0
        self._sredniy_max=0
        self._sredniy_min=0
        self._ii=iireshalkaclass_0_606()
        self._RealMaxProc=0
        self._RealMinProc=0
        self._dopusk_kray_time=0
        self._dopusk_kray_procent=0
        self._risk=1
        self._riskc=1
        self._k_n_shortshortdel=None #self._ii._ni_coin_shortshort.GetRegressProporcii()
        self._k_n_shortdel=None #self._ii._ni_coin_short.GetRegressProporcii()
        self._k_n_longdel=None #self._ii._ni_coin_long.GetRegressProporcii()
        self._k_s_shortshortdel=None #self._ii._ni_sredniy_shortshort.GetRegressProporcii()
        self._k_s_shortdel=None #self._ii._ni_sredniy_short.GetRegressProporcii()
        self._k_s_longdel=None #self._ii._ni_sredniy_long.GetRegressProporcii()
        self._k_s_v3=None #self._ii._ni_coin_short._ii_v[l1-1]
        self._k_s_v2=None #self._ii._ni_coin_short._ii_v[l1-2]
        self._k_s_v1=None #self._ii._ni_coin_short._ii_v[l1-3]
        self._k_l_v3=None #=self._ii._ni_coin_long._ii_v[l1-1]
        self._k_l_v2=None #=self._ii._ni_coin_long._ii_v[l1-2]
        self._k_l_v1=None #=self._ii._ni_coin_long._ii_v[l1-3]

    # def InitRisk222(self,up, doun, prop, stepen):
    #     if prop > 1:
    #         up=up*pow(2-prop, stepen)
    #     if prop < 1:
    #         doun=doun*pow(2-prop, stepen)
    #     return up, doun
    
    # def InitRisk333(self,up, doun, prop, stepen):
    #     if prop > 0:
    #         up=up*pow(1-prop, stepen)
    #     if prop < 0:
    #         doun=doun*pow(1-prop, stepen)
    #     return up, doun
    def ReversToShortToLong(self):
        # self._fup, self._fdoun, self._vshort=0,0,0
        self._long_or_buy=True if self._long_or_buy==False else False
        self._k_l_v1=-self._k_l_v1
        self._k_l_v2=-self._k_l_v2
        self._k_l_v3=-self._k_l_v3
        self._k_n_longdel=2-self._k_n_longdel
        self._k_n_shortdel=2-self._k_n_shortdel
        self._k_n_shortshortdel=2-self._k_n_shortshortdel
        self._k_s_longdel=2-self._k_s_longdel
        self._k_s_shortdel=2-self._k_s_shortdel
        self._k_s_shortshortdel=2-self._k_s_shortshortdel
        self._k_s_v1=-self._k_s_v1
        self._k_s_v2=-self._k_s_v2
        self._k_s_v3=-self._k_s_v3
        self._k_ss_v1=-self._k_ss_v1
        self._k_ss_v2=-self._k_ss_v2
        self._k_ss_v3=-self._k_ss_v3
        self._vshort=1-self._vshort
        # self._maxperc=0
        # self._minperc=0
        # self._maxpercsex=0
        # self._minpercsex=0
        # self._razn=0
        # self._razn_abs=0
        # self._razn_sex_abs=0
        # self._sredniy_max=0
        # self._sredniy_min=0
        # self._ii=iireshalkaclass_0_606()
        # self._RealMaxProc=0
        # self._RealMinProc=0
        # self._dopusk_kray_time=0
        # self._dopusk_kray_procent=0
        # self._risk=1
        # self._riskc=1
        # self._k_n_shortshortdel=None #self._ii._ni_coin_shortshort.GetRegressProporcii()
        # self._k_n_shortdel=None #self._ii._ni_coin_short.GetRegressProporcii()
        # self._k_n_longdel=None #self._ii._ni_coin_long.GetRegressProporcii()
        # self._k_s_shortshortdel=None #self._ii._ni_sredniy_shortshort.GetRegressProporcii()
        # self._k_s_shortdel=None #self._ii._ni_sredniy_short.GetRegressProporcii()
        # self._k_s_longdel=None #self._ii._ni_sredniy_long.GetRegressProporcii()
        # self._k_s_v3=None #self._ii._ni_coin_short._ii_v[l1-1]
        # self._k_s_v2=None #self._ii._ni_coin_short._ii_v[l1-2]
        # self._k_s_v1=None #self._ii._ni_coin_short._ii_v[l1-3]
        # self._k_l_v3=None #=self._ii._ni_coin_long._ii_v[l1-1]
        # self._k_l_v2=None #=self._ii._ni_coin_long._ii_v[l1-2]
        # self._k_l_v1=None #=self._ii._ni_coin_long._ii_v[l1-3]

    def InitRisk(self):
        longdel=self._ii._ni_coin_long.GetRegressProporcii()
        shortdel=self._ii._ni_coin_short.GetRegressProporcii()
        shortshortdel=self._ii._ni_coin_shortshort.GetRegressProporcii()
        sredniy_shortshortdel=self._ii._ni_sredniy_shortshort.GetRegressProporcii()
        sredniy_shortdel=self._ii._ni_sredniy_short.GetRegressProporcii()
        sredniy_longdel=self._ii._ni_sredniy_long.GetRegressProporcii()
        risk = 1 / (pow(sredniy_shortshortdel,5)*pow(sredniy_shortdel, 9)*pow(sredniy_longdel,11))
        self._risk = risk
        risk = 1 / (pow(shortshortdel,5)*pow(shortdel, 9)*pow(longdel,11))
        self._riskc = risk
        # # up, doun=1, 1
        # # up, doun = self.InitRisk222(up, doun, longdel, 15)
        # # up, doun = self.InitRisk222(up, doun, shortdel, 12)
        # # up, doun = self.InitRisk222(up, doun, shortshortdel, 9)
        # # up, doun = self.InitRisk222(up, doun, sredniy_shortshortdel, 17)
        # # up, doun = self.InitRisk222(up, doun, sredniy_shortdel, 15)
        # # up, doun = self.InitRisk222(up, doun, sredniy_longdel, 11)
        # # # v ector
        # # # v1=self._ii._ni_coin_shortshort._ii_v[len(self._ii._ni_coin_shortshort._ii_v)-1]
        # # # up, doun = self.InitRisk333(up, doun, v1, 0.14)
        # # # v1=self._ii._ni_coin_short._ii_v[len(self._ii._ni_coin_short._ii_v)-1]
        # # # up, doun = self.InitRisk333(up, doun, v1, 0.11)
        # # # v1=self._ii._ni_coin_long._ii_v[len(self._ii._ni_coin_long._ii_v)-1]
        # # # up, doun = self.InitRisk333(up, doun, v1, 0.06)

        # # risk=(up+doun)/2
        # self._risk=risk

    def Init2(self, cursor, birja, coin, timepar, maxperc, minperc, maxpercsex, minpercsex,fup, fdoun, vshort):
        self._coin=coin
        self._birja=birja
        self._maxperc=maxperc
        self._minperc=minperc
        self._maxpercsex=maxpercsex
        self._minpercsex=minpercsex
        if self._maxperc is not None and self._minperc is not None:
            self._razn=self._maxperc-self._minperc
            self._razn_abs=abs(self._razn)
            max1=max(self._maxperc, self._minperc)
            min1=min(self._maxperc, self._minperc)
            self._sredniy_max=(max1+max1+min1)/3
            self._sredniy_min=(max1+min1+min1)/3
        self._RealMaxProc, self._RealMinProc=self.GetRealProcent(cursor, birja, coin, timepar)
        self._fup=fup
        self._fdoun=fdoun
        self._vshort=vshort
        self.InitRisk()

        self._k_n_shortshortdel=self._ii._ni_coin_shortshort.GetRegressProporcii()
        self._k_n_shortdel=self._ii._ni_coin_short.GetRegressProporcii()
        self._k_n_longdel=self._ii._ni_coin_long.GetRegressProporcii()
        self._k_s_shortshortdel=self._ii._ni_sredniy_shortshort.GetRegressProporcii()
        self._k_s_shortdel=self._ii._ni_sredniy_short.GetRegressProporcii()
        self._k_s_longdel=self._ii._ni_sredniy_long.GetRegressProporcii()
        # self._k_bs_shortshortdel=self._ii._ni_bigsredniy_shortshort.GetRegressProporcii()
        # self._k_bs_shortdel=self._ii._ni_bigsredniy_short.GetRegressProporcii()
        # self._k_bs_longdel=self._ii._ni_bigsredniy_long.GetRegressProporcii()
        # l1=len(self._ii._ni_coin_shortshort._ii_v)
        # self._k_ss_v3=self._ii._ni_coin_shortshort._ii_v[l1-1]
        # self._k_ss_v2=self._ii._ni_coin_shortshort._ii_v[l1-2]
        # self._k_ss_v1=self._ii._ni_coin_shortshort._ii_v[l1-3]
        self._k_ss_v1, self._k_ss_v2, self._k_ss_v3 = self._ii._ni_coin_shortshort.GetLast_3_From__v_l_lv_s_m('v')
        # l1=len(self._ii._ni_coin_short._ii_v)
        # self._k_s_v3=self._ii._ni_coin_short._ii_v[l1-1]
        # self._k_s_v2=self._ii._ni_coin_short._ii_v[l1-2]
        # self._k_s_v1=self._ii._ni_coin_short._ii_v[l1-3]
        self._k_s_v1, self._k_s_v2, self._k_s_v3 = self._ii._ni_coin_short.GetLast_3_From__v_l_lv_s_m('v')
        # l1=len(self._ii._ni_coin_long._ii_v)
        # self._k_l_v3=self._ii._ni_coin_long._ii_v[l1-1]
        # self._k_l_v2=self._ii._ni_coin_long._ii_v[l1-2]
        # self._k_l_v1=self._ii._ni_coin_long._ii_v[l1-3]
        self._k_l_v1, self._k_l_v2, self._k_l_v3 = self._ii._ni_coin_long.GetLast_3_From__v_l_lv_s_m('v')

    def GetDebugInfo(self, bytime, timepar, Strat_Standart, Strat_BigDoun, Strat_BigDoun_Size, Strat_Tolko_BNB, XMul, XMinOut, procenthiscorrectplus):
        ret=self.GetDebugInfoObshiy(bytime, timepar, Strat_Standart, Strat_BigDoun, Strat_BigDoun_Size, Strat_Tolko_BNB, XMul, XMinOut, procenthiscorrectplus)
        ret=ret+self._ii.GetDebugInfoII()
        return ret

    def GetDebugInfoObshiy(self, bytime, timepar, Strat_Standart, Strat_BigDoun, Strat_BigDoun_Size, Strat_Tolko_BNB, XMul, XMinOut, procenthiscorrectplus):
        def str5(strpar):
            return small.str5(strpar)
        ret0=''
        ret0=small.adder(ret0, "real max...min$"+str5(self._RealMaxProc)+"..."+str5(self._RealMinProc))
        if self._long_or_buy: str2="long_buy"
        else: str2="short_sell"
        ret0=small.adder(ret0, "$"+str2)
        ret0=small.adder(ret0, "$vect up...doun$"+str5(self._fup)+"..."+str5(self._fdoun))
        ret0=small.adder(ret0, "$vshort$"+str5(self._vshort))
        ret0=small.adder(ret0, "$risk$"+str5(self._risk))
        ret0=small.adder(ret0, "$riskc$"+str5(self._riskc))
        #ret0=small.adder(ret0, ",Up ", self._ii._ni_coin_short._Up[len(self._ii._ni_coin_short._Up)-1])
        #ret0=small.adder(ret0, ",Doun ", self._ii._ni_coin_short._Doun[len(self._ii._ni_coin_short._Doun)-1])
        #ret0=small.adder(",up...doun,"+str5(self._fup)+"..."+str5(doun))
        if self._maxpercsex is not None and self._minpercsex is not None:
            ret0=small.adder(ret0, "$sex max...min$"+str5(self._maxpercsex)+"..."+str5(self._minpercsex))
        if self._maxperc is not None and self._minperc is not  None:
            ret0=small.adder(ret0, "$max...min$"+str5(self._maxperc)+"..."+str5(self._minperc))
            ret0=small.adder(ret0, "$sr max...min$"+str5(self._sredniy_max)+"..."+str5(self._sredniy_min))
            ret0=small.adder(ret0, "$razn,"+str5(self._razn_abs))
        ret0=small.adder(ret0, "$okinput,i6, okout = RunTest88('"+self._birja+"','"+self._coin+"',"+str(bytime)+","+str(timepar)+"")
        ret0=small.adder(ret0, ", ", str(Strat_Standart), ", ", str(Strat_BigDoun), ", ", str(Strat_BigDoun_Size))
        ret0=small.adder(ret0, ", ", str(Strat_Tolko_BNB))
        ret0=small.adder(ret0, ", ", str(XMul), ", ", str(XMinOut), ", ", procenthiscorrectplus, ") ")

        
        return ret0


    def GetRealProcent(self, cursor, birja, coin, timepar):
        # прогноз по реальным данным через период
        periodh=small.GetPeriod()
        timepar=int(round(timepar/(5*60*1000))*5*60*1000)
        tn=small.GetTableName(birja, coin)
        rows=db.GetSel77(cursor, "select price  from "+tn
                         +" where id = "+str(timepar))
        p1=small.GetCorrectOneFloatNoteFromRowsAsOne(rows)
        pmax, pmin=None, None
        for periodfind in periodh, periodh*2,periodh*4:
            rows=db.GetSel77(cursor, "select max(price)  from "+tn
                            +" where id >= "+str(timepar+(int(periodfind*2/3))*60*60*1000)
                            +" and id <= "+str(timepar+(int(periodfind*4/3))*60*60*1000))
            pmax=small.GetCorrectOneFloatNoteFromRowsAsOne(rows)
            rows=db.GetSel77(cursor, "select min(price)  from "+tn
                            +" where id >= "+str(timepar+(int(periodfind*2/3))*60*60*1000)
                            +" and id <= "+str(timepar+(int(periodfind*4/3))*60*60*1000))
            pmin=small.GetCorrectOneFloatNoteFromRowsAsOne(rows)
            if pmax is not None and pmin is not  None:
                break
        if p1 == None or pmax==None or pmin==None: return 222, 222
        return (pmax-p1)*100/p1,  (pmin-p1)*100/p1
    
    def GetKlines555(self, cursor, birja, coin, timepar, shag):
        # последние данные свечи
        tn=small.GetTableName(birja, coin)
        # select ROUND((id/(15*60*1000))) AS id5 ,avg(price) from binanceusdt_aave_usdt
        # where id >= 1707828600000-10*15*60*1000  and id <= 1707828600000  GROUP BY id5 order by id5 desc;
        rows=db.GetSel77(cursor, "select ROUND((id/("+str(shag)+"*60*1000))) AS id5 ,avg(price)  from "+tn
                         +" where id >= "+str(timepar)+"-"+str(10*shag*60*1000)
                         +" and id <= "+str(timepar)
                         +" GROUP BY id5 order by id5 desc")
        klm=[]
        if rows is None: return klm
        for r1 in rows:
            klm.append(float(r1[1]))
        return klm

    def PodnimaetcyaOpuskaetcya555(self, klines, mul3):
        #определяет поднимается или опускается курс
        PodnimaetcyaPlus=float(0)
        OpuskaetcyaPlus=float(0)
        #СЧИТАЕМ СРЕДНИЙ ПРОЦЕНТ БИЕНИЯ
        dlitel=0
        per=0
        for next in range(1, len(klines) ):
            dlitel=dlitel+1
            oldp=float(klines[next])
            newp=float(klines[next-1])
            nextpercent=abs(oldp-newp)*100/oldp
            per=per+nextpercent
        r1=per/dlitel
        if dlitel > 0:
            per=(per/dlitel)/10
        #======сколько поднимается и опускается======================
        dounpodryad=0
        uppodryad=0
        delm=[0.4, 0.8, 1.6, 3.2, 6.4, 12, 24, 50, 100, 200, 400, 500]
        for next in range(1, len(klines) ):
            del5=delm[next-1]
            oldp=float(klines[next])
            newp=float(klines[next-1])
            np=abs(oldp-newp)*100/oldp
            del77=per*del5*mul3
            if oldp < newp and np > del77:
                PodnimaetcyaPlus = PodnimaetcyaPlus+np/del77
                uppodryad=uppodryad+1
                dounpodryad=0
            if oldp > newp and np > del77:
                OpuskaetcyaPlus = OpuskaetcyaPlus+np/del77
                dounpodryad=dounpodryad+1
                uppodryad=0
            del5=del5*del5
        return PodnimaetcyaPlus, OpuskaetcyaPlus, r1

