

from __future__ import print_function
from datetime import datetime 
import random
import small
import db
from dbuse import dbuse
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
# from iihshar_606 import hshar_sex_900_606
from iimodels  import class55plus
from ii_bloha_stavka_606 import bloha_stavka_606
from zapolnalka import zapolnalka_class
Global_plusname = "_606_"
# GlobalClassname="model_inputdoun_outup_900_606"
GlobalClassnameV="model_short_vector_900_606"
sikokoskokov=0
#modelshablon=model_900_606()
from sms_obmen_base import sms_message
from sms_obmen_base import sms_obmen_base_class

import math
    

class bloha_up_doun_606(dbuse):
    def __init__(self, cursor, conn, birja, debugf, plusname, test5):
        super().__init__(cursor, conn)
        # global GlobalClassname
        global GlobalClassnameV
        self._debugf=debugf
        self._periodh=small.GetPeriod()
        self._short_periodh=0
        self._birja=birja
        self._Test5=test5
        self._FlagAndShortModel=False
        # mjdels
        self._v_model=iimodels.GetActIIClassObj(GlobalClassnameV)
        fn = iimodels.GetActModelFileName(None, self._debugf, plusname, GlobalClassnameV, self._birja, self._periodh)
        self._v_model.load_state_dict(torch.load(fn))
        self._v_model.eval()      # включение режима оценки
        self._vs_model=None
        if self._FlagAndShortModel:
            if self._birja=='finam': self._short_periodh=4
            else: self._short_periodh=4
            self._vs_model=iimodels.GetActIIClassObj(GlobalClassnameV)
            fn = iimodels.GetActModelFileName(None, self._debugf, plusname, GlobalClassnameV, self._birja, self._short_periodh)
            self._vs_model.load_state_dict(torch.load(fn))
            self._vs_model.eval()      # включение режима оценки
        # --------------------
        self._summ=10
        self._coin=None
        self._oldcoin=None
        self._startprice=None
        self._sellprice=None
        self._long_or_buy=None
        self._bytime=0
        self._procenthiscorrectplus=0
        #self._rp=None
        #self._srpr, self._srprsik=0,0
        self._prm=[]
        self._ppprm=[]
        #self._klm=[]
        self._Strat_Tolko_BNB=False
        self._Strat_Standart=True
        self._Strat_BigDoun=False
        self._Strat_BigDoun_Size=2.5
        self._XMul=0.04
        self._XMinOut=0.4
        self._Flag_VhodMinimum=False
        #self._Flag_VhodPoUpDoun=True
        self._Flag_NunoSellPriceSr_Plus=False
        self._Flag_NotVhodNaTuJeMonetu=False
        self._FlagStopLoss=True
        self._FlagStopLossPlavaet=False
        self._Flag_RuchnoyVihod=False
        self._Flag_VihodNaPodieme=False
        self._FlagSmotrimNstroy=False
        #self._FlagStopLossNaObshemPadenii=False
        self._FlagOptimist=True
        self._FlagMinProcentOut=True
        self._FlagMinProcentOut_ByRegress=True
        self._Flag_IsklOut_AllDoun_Razvorot_ByRegress=True
        self._FlagAndBuyAndShort=False
        # if birja=='finam':
        #     self._FlagMinProcentOut=False
        self._FlagShortOut=True
        self._IndexNastroeniya=1
        # флаг разумный... не убирать ... или убирать (по деньгам-то)
        #self._Flag_NotInputNaPademnii=False
        self._FlagMonoPereskakivat=False
        # good flag !
        #self._Flag_IsklVhodPoUpDoun=True
        # self._Flag_NotInputRaznicaPrognoz=False
        # self._FlagPocentSootvetstviya=True
        self._PocentSootvetstviya=8
        #
        limit=" limit 3 " if small.ItDebug() else ""
        lot1=" and lotsize<>0  " if birja=='finam' else ""
        # if self._Strat_Tolko_BNB:
        #     rows=self.GetSell( "select coin from symb where  coin='BNB' and birja='"+birja+"' order by id"+limit)
        # else:
        rows=self.GetSell( "select coin from symb where  stavim=1 and birja='"+birja+"' "+lot1+"order by id"+limit)
        self._cm=[]
        self._cm_pohoj_proc=[]
        self._cm_pohoj_prog=[]
        for r1 in rows:
            self._cm.append(r1[0])
            self._cm_pohoj_proc.append(0)
            self._cm_pohoj_prog.append(0)
        self._GlSikUp=1
        self._GlSikDoun=1
        self._GlSikMax=1
        # sms --------------------
        self._sms_command = None
        self._sms_coin = None
        self._sms_sb = None
        self._sms_sm=None
        if small.ItSMSBuySell():
            self._sms_sb = sms_obmen_base_class(None, None)
            self._sms_sm=self._sms_sb.GetMessage(birja)
            if self._sms_sm is not None:
                # input or output
                input=True if (self._sms_sm._mess=='buylong' or self._sms_sm._mess == 'sellshort') else False
                output=True if (self._sms_sm._mess=='selllong' or self._sms_sm._mess == 'buyshort') else False
                if (input or output): 
                    if self._cm.count(self._sms_sm._coin):
                        self._sms_command = self._sms_sm._mess
                        self._sms_coin = self._sms_sm._coin
                    # delete sms
                    self._sms_sb.OrMess(birja, self._sms_sm._coin, self._sms_sm._id, self._sms_sb.StatusZavershen())



    def CorrectBuyForNastroy(self, perc):
        if self._FlagOptimist: perc = perc*self._IndexNastroeniya
        return perc

    def CorrectSellForNastroy(self, perc):
        if self._FlagOptimist:
            del1=self._IndexNastroeniya
            return ((perc)/(del1))
        return perc


    def SetStopLoss(self, timepar):
        db.AddUpdate_peremenniye_AndCursor(self.GetCursor(), self.GetConn(), self.GetStopLossName(), str(timepar))

    def GetStopLossName(self):
        return str("SL_deb_"+self._birja)
    
    # def Viiiiiiihod_PoUp(self, i1: bloha_stavka_606, timepar,bigbig, proc):
    #     # выход по флагам Doun
    #     if self._birja=='finam': return False
    #     if i1._fup:
    #         if bigbig == 'nol':
    #             if self._FlagShortOut:
    #                 if self._birja=='okx':
    #                     if proc > 2.0:
    #                         if self.Viiiiiiihod_PoUp(i1, timepar,'ras', proc):
    #                             return True
    #                     if proc > 2.5:
    #                         if self.Viiiiiiihod_PoUp(i1, timepar,'dva', proc):
    #                             return True
    #                     if proc > 3.0:
    #                         if self.Viiiiiiihod_PoUp(i1, timepar,'tri', proc):
    #                             return True
    #                 elif self._birja=='binanceusdt':
    #                     if proc > 2.0:
    #                         if self.Viiiiiiihod_PoUp(i1, timepar,'ras', proc):
    #                             return True
    #                     if proc > 2.5:
    #                         if self.Viiiiiiihod_PoUp(i1, timepar,'dva', proc):
    #                             return True
    #                     if proc > 3.0:
    #                         if self.Viiiiiiihod_PoUp(i1, timepar,'tri', proc):
    #                             return True
    #                 elif self._birja=='bybit':
    #                     if proc > 2.0:
    #                         if self.Viiiiiiihod_PoUp(i1, timepar,'ras', proc):
    #                             return True
    #                     if proc > 2.5:
    #                         if self.Viiiiiiihod_PoUp(i1, timepar,'dva', proc):
    #                             return True
    #                     if proc > 3.0:
    #                         if self.Viiiiiiihod_PoUp(i1, timepar,'tri', proc):
    #                             return True
    #                 elif self._birja=='finam':
    #                     # return False
    #                     if proc > 0.69:
    #                         if self.Viiiiiiihod_PoUp(i1, timepar,'ras', proc):
    #                             return True
    #                     if proc > 1.2:
    #                         if self.Viiiiiiihod_PoUp(i1, timepar,'dva', proc):
    #                             return True
    #                     if proc > 2.0:
    #                         if self.Viiiiiiihod_PoUp(i1, timepar,'tri', proc):
    #                             return True
    #                 else:
    #                     small.ifnoterr(5==89)
    #         elif bigbig == 'ras':
    #             if self._birja=='finam':
    #                 if i1._vshort < 0.42: return True
    #             else:
    #                 if i1._vshort < 0.30: return True
    #         elif bigbig == 'dva':
    #             if self._birja=='finam':
    #                 if i1._vshort < 0.48: return True
    #             else:
    #                 if i1._vshort < 0.40: return True
    #         elif bigbig == 'tri':
    #             if self._birja=='finam':
    #                 if i1._vshort < 0.53: return True
    #             else:
    #                 if i1._vshort < 0.50: return True
    #     return False
    
    def GetPlusByRegress(self, i1: bloha_stavka_606, raznregress):
        return 0        #4589
        # ret=0.2-self.GetInputProg(1.02, 1.03, 1.06, 0.01, 0.19)
        # ret=0.2-self.GetInputProg(1.03, 1.03, 1.06, 0.01, 0.19)
        # ret=0.2-self.GetInputProg(1.05, 1.03, 1.06, 0.01, 0.19)
        # ret=0.2-self.GetInputProg(1.06, 1.03, 1.06, 0.01, 0.19)
        # ret=0.2-self.GetInputProg(1.07, 1.03, 1.06, 0.01, 0.19)
        ret=0.2-self.GetInputProg(i1._k_n_shortshortdel, 1.025, 1.06, 0.01, 0.19)
        del1=1
        if raznregress < -0.001:
            # del1=self.GetInputProg(0.0005, 0.001, 0.01, 1, 5)
            # del1=self.GetInputProg(0.001, 0.001, 0.01, 1, 5)
            # del1=self.GetInputProg(0.002, 0.001, 0.01, 1, 5)
            # del1=self.GetInputProg(0.008, 0.001, 0.01, 1, 5)
            # del1=self.GetInputProg(0.01, 0.001, 0.01, 1, 5)
            # del1=self.GetInputProg(0.02, 0.001, 0.01, 1, 5)
            del1=11-self.GetInputProg(-raznregress, 0.001, 0.01, 1, 10)
        return -ret/del1
    
    def Viiiiiiihod_PoShort(self, i1: bloha_stavka_606, timepar,bigbig,proc, raznregress):
        # выход по флагам Doun
        upplus=self.GetUpDounPlus(i1, False)
        regplus=self.GetPlusByRegress(i1, raznregress)
        if bigbig == 'nol':
            if  self._FlagShortOut:
                if self._birja=='finam':
                    # # return False
                    # short_s=np.mean(i1._ii._ni_coin_short._ii_s)
                    # pras, pdva, ptri = 1.2, 1.6, 2.0
                    # if short_s > 0.0008: pras, pdva, ptri = 1.4, 1.9, 2.4
                    # if proc > 3:
                    #     if self.Viiiiiiihod_PoShort(i1, timepar,'ras', proc):
                    #         return True
                    # if proc > 3.5:
                    #     if self.Viiiiiiihod_PoShort(i1, timepar,'dva', proc):
                    #         return True
                    # if proc > 4:
                    #     if self.Viiiiiiihod_PoShort(i1, timepar,'tri', proc):
                    #         return True
                    hh=0
                else:
                    if self._periodh <= 8:
                        if proc > 2.5:
                            if self.Viiiiiiihod_PoShort(i1, timepar,'ras', proc):
                                return True
                        if proc > 3.0:
                            if self.Viiiiiiihod_PoShort(i1, timepar,'dva', proc):
                                return True
                        if proc > 3.5:
                            if self.Viiiiiiihod_PoShort(i1, timepar,'tri', proc):
                                return True
        elif bigbig == 'ras':
            if self._birja=='finam':
                if i1._vshort < 0.48 and i1._vshort < 0.38+regplus: return True
                #if i1._vshort < 0.48 and i1._vshort < 0.38+upplus: return True
            else:
                if i1._vshort < 0.38+upplus: return True
            # if i1._vshort < 0.25: return True
        elif bigbig == 'dva':
            if self._birja=='finam':
                if i1._vshort < 0.50 and i1._vshort < 0.43+regplus: return True
                #if i1._vshort < 0.50 and i1._vshort < 0.43+upplus: return True
            else:
                if i1._vshort < 0.415+upplus: return True
            # if i1._vshort < 0.31: return True
        elif bigbig == 'tri':
            if self._birja=='finam':
                if i1._vshort < 0.52 and i1._vshort < 0.48+regplus: 
                # if i1._vshort < 0.52 and i1._vshort < 0.48+upplus: 
                    return True
            else:
                if i1._vshort < 0.45+upplus: return True
            # if i1._vshort < 0.48: return True
        else:
            small.ifnoterr(5==8)
        return False
    
    def ObshiyDoun(self, i1: bloha_stavka_606, timepar):
        if i1._k_s_shortshortdel < 1 and i1._k_s_shortdel < 1:
            return True
        if i1._k_s_shortshortdel < 0.997:
            return True
        return False

    
    def ItIsBiiiigDoun_PoUpDoun(self, i1: bloha_stavka_606):
        # большой короткий  падение 
        sum1=i1._k_ss_v1+i1._k_ss_v2+i1._k_ss_v3
        if sum1 < -0.013 and i1._k_s_v3 < -0.018 and i1._k_ss_v3 < -0.005 and i1._k_ss_v2 < -0.001:
            return True
        if sum1 < -0.019 and i1._k_s_v3 < -0.025 and i1._k_ss_v3 < 0 and i1._k_ss_v2 < 0:
            return True
        if sum1 < -0.03 and i1._k_s_v3 < -0.025:
            return True
        if sum1 < -0.025 and i1._k_s_v3 < -0.03:
            return True
        if i1._k_n_shortshortdel > 1.015 and i1._k_ss_v3 < -0.02:
            return True
        if i1._k_n_shortshortdel > 1.008 and i1._k_ss_v3 < -0.08 and i1._k_ss_v2 < -0.08:
            return True
        if i1._k_s_v3 < 0 and i1._k_s_v2 < 0 and (i1._k_s_v3+i1._k_s_v2) < -0.05:
            if i1._k_ss_v3 < -0.0 and i1._k_ss_v2 < 0:
                return True
        return False

    def GetUpDounPlus(self, i1: bloha_stavka_606, vhodim):
        upplus=0
        upplus=upplus+i1._ii._ni_coin_long._Up[2]
        upplus=upplus+i1._ii._ni_coin_short._Up[2]
        upplus=upplus+i1._ii._ni_coin_shortshort._Up[2]
        upplus=upplus+i1._ii._ni_coin_long._Doun[2]
        upplus=upplus+i1._ii._ni_coin_short._Doun[2]
        upplus=upplus+i1._ii._ni_coin_shortshort._Doun[2]
        ret=small.Sigmoid(upplus, 1.1, True)
        ret=ret/8
        if self._Strat_Tolko_BNB:
            ret=ret/7
        elif self._birja=='finam':
            ret=ret/12
        return ret
    
    def GetInputProgWithConst(self, regress):
        inputprog=111
        if self._birja=='finam':
            inputprog = self.GetInputProg(regress, 0.99, 1.05 , 0.625, 0.846)
        else:
            ddd=7/0
        
        return inputprog
    
    def GetInputProg(self, regress, minregress, maxregress, minprog, maxprog):
        # regress
        sredregress = (minregress+maxregress)/2
        raznregress = (regress-sredregress)
        sredraznregress = abs(maxregress-sredregress)
        # sigmoid
        sig = small.Sigmoid((raznregress), sredraznregress, True)
        # if raznregress < 0: sig=-sig
        # prognoz
        sredprog = (minprog+maxprog)/2
        raznprog = abs(sredprog-minprog)
        # retrazn/raznprog == raznregress/sredraznregress
        retrazn = sig * raznprog
        retprog = sredprog-retrazn
        return retprog

    def ANadoVhodim_PoUpDoun_Tolko_BNB(self, i1: bloha_stavka_606, timepar):
        if self._Strat_Tolko_BNB != True: return False
        bigup=False
        if i1._k_n_shortdel > 1.01  and i1._k_n_longdel  > 1.01: bigup=True
        if i1._k_s_shortdel > 1.011  and i1._k_s_longdel  > 1.011: bigup=True
        s2 = (i1._k_s_shortshortdel + i1._k_n_shortshortdel*2)/3
        if bigup:
            inputprog = self.GetInputProg(s2, 1.01, 1.03, 0.60, 0.72)
        else:
            inputprog = self.GetInputProg(s2, 0.98, 1.01, 0.65, 0.81)
        while False:
            x2=random.uniform(1.7, 2.2)
            inputprog = self.GetInputProg(x2, 2.00, 2.06, 0.54, 0.72)
        if i1._vshort > self.CorrectBuyForNastroy(inputprog): 
            return True
        return False


    def ANadoVhodim_PoUpDoun(self, i1: bloha_stavka_606, timepar):
        # по историческим дынным входим
        if self._birja=='finam':
                inputprog = self.GetInputProgWithConst(i1._k_n_shortshortdel)
                if i1._k_n_shortdel < 0.97 or i1._k_n_longdel < 0.97:
                    inputprog = self.GetInputProgWithConst(i1._k_n_shortdel * i1._k_n_longdel)
                if i1._vshort > self.CorrectBuyForNastroy(inputprog): 
                    return True
        else:
            upplus=self.GetUpDounPlus(i1, True)
            if i1._fdoun:
                if self._birja=='okx':
                    if i1._vshort > self.CorrectBuyForNastroy(0.75): 
                        return True
                elif self._birja=='binanceusdt':
                    if i1._vshort > self.CorrectBuyForNastroy(0.75): 
                        return True
                elif self._birja=='bybit':
                    if i1._vshort > self.CorrectBuyForNastroy(0.72): 
                        return True
                elif self._birja=='finam':
                    if i1._vshort > self.CorrectBuyForNastroy(0.60+upplus): 
                        return True
                else:
                    small.ifnoterr(3==7)
            elif i1._fup:
                d1=False
                if i1._k_s_shortshortdel < 0.999 or i1._k_s_shortdel < 0.9999 or i1._k_s_longdel < 0.999: d1=True
                if i1._k_s_shortshortdel < 1 and i1._k_s_shortdel < 1: d1=True
                if i1._k_s_shortshortdel < 1 and i1._k_s_longdel < 1: d1=True
                if i1._k_s_shortdel < 1 and i1._k_s_longdel < 1: d1=True
                if self._birja=='okx':
                    if i1._vshort > self.CorrectBuyForNastroy(0.85): 
                        return True
                elif self._birja=='binanceusdt':
                    if i1._vshort > self.CorrectBuyForNastroy(0.85): 
                        return True
                elif self._birja=='bybit':
                    if i1._vshort > self.CorrectBuyForNastroy(0.82): 
                        return True
                elif self._birja=='finam':
                    if i1._vshort > self.CorrectBuyForNastroy(0.81+upplus): 
                        return True
                else:
                    small.ifnoterr(3==7)
            else:
                if self._birja=='okx':
                    if i1._vshort > self.CorrectBuyForNastroy(0.8): 
                        return True
                elif self._birja=='binanceusdt':
                    if i1._vshort > self.CorrectBuyForNastroy(0.8): 
                        return True
                elif self._birja=='bybit':
                    if i1._vshort > self.CorrectBuyForNastroy(0.77): 
                        return True
                elif self._birja=='finam':
                    if i1._vshort > self.CorrectBuyForNastroy(0.71+upplus): 
                        return True
                else:
                    small.ifnoterr(3==7)
        # # еще раз без up doun
        # if i1._fup or i1._fdoun:
        #     i1._fup, i1._fdoun = False, False
        #     return self.ANadoVhodim_PoUpDoun(i1, timepar)

        return  False

    def ANadoVhodim_PoBigDoun(self, i1: bloha_stavka_606, timepar):
        # заходим при большом падении
        # имеет смысл если уверен, что курс восстановится (поднимется после падения)
        if i1._fdoun != True: return False
        # test
        if self._Strat_BigDoun_Size < 1 or self._Strat_BigDoun_Size > 15:
            e1='Error 4566755454 '
            print(e1)
            self.AddPrintInfoToComments(e1)
            return False
        ssdoun = i1._ii._ni_coin_shortshort._Doun[len(i1._ii._ni_coin_shortshort._Doun)-1]
        sdoun = i1._ii._ni_coin_short._Doun[len(i1._ii._ni_coin_short._Doun)-1]
        ldoun = i1._ii._ni_coin_long._Doun[len(i1._ii._ni_coin_long._Doun)-1]
        #
        if ssdoun > -self._Strat_BigDoun_Size/20 or sdoun > -self._Strat_BigDoun_Size/20 or ldoun > -self._Strat_BigDoun_Size/20:
            return False
        if ssdoun+sdoun+ldoun > -self._Strat_BigDoun_Size:
            return False
        if self._birja=='okx':
            if i1._vshort > self.CorrectBuyForNastroy(0.65): 
                return True
        elif self._birja=='binanceusdt':
            if i1._vshort > self.CorrectBuyForNastroy(0.65): 
                return True
        elif self._birja=='bybit':
            if i1._vshort > self.CorrectBuyForNastroy(0.65): 
                return True
        elif self._birja=='finam':
            if i1._vshort > self.CorrectBuyForNastroy(0.55): 
                return True
        else:
            small.ifnoterr(3==7)
        return  False

    def ANadoVhodim(self, i1: bloha_stavka_606, timepar):
        # надо ли входить
        if small.ItDebugBuySell(i1._long_or_buy): return True
        if small.ItDebugRandBuySell() and random.randint(0, 5) == 2  : return True
        if self.IsklOut_AllDoun_ByRegress(i1, timepar):
            return False
        raznregress = self.GetRaznRegress(i1)
        # input for big doun
        if self._Strat_BigDoun:
            if self.ANadoVhodim_PoBigDoun(i1, timepar):
                return True
        # INPUT standart
        if self._Strat_Standart:
            # ререссии вниз с ускорением
            if self.ItIsRegressDounAndRazvorot(i1, raznregress):
                return False
            # big doun
            if self.ItIsBiiiigDoun( i1): 
                return False
            # ItIsSmallS
            if self.ItIsSmallS( i1): 
                return False
            
            # regress out
            if self.ItIsRO( i1): 
                return False
            # вход по истории
            if self.ANadoVhodim_PoUpDoun(i1, timepar):
                return True
        if self._Strat_Tolko_BNB:
            # вход по истории
            if self.ANadoVhodim_PoUpDoun_Tolko_BNB(i1, timepar):
                return True
        return False
    
    def ItIsBiiiigUp(self, i1: bloha_stavka_606, bigbig, raznregress):
        if self._birja=='finam': 
            if  self._periodh == 8:
                return self.ItIsBiiiigUpFinam(i1, bigbig, 1.0)
            elif  self._periodh == 4:
                return self.ItIsBiiiigUpFinam(i1, bigbig, 2)
            elif  self._periodh == 24:
                return self.ItIsBiiiigUpFinam24(i1, bigbig, 2)
            else:
                small.ifnoterr(5==8)
        else:
            if  self._periodh == 24:
                return self.ItIsBiiiigUpCrypta_24h(i1, bigbig, raznregress)
            elif  self._periodh == 2:
                return self.ItIsBiiiigUpCrypta_2h(i1, bigbig)
            else:
                small.ifnoterr(5==8)
        return False
    
    def ItIsBiiiigUpCrypta_24h(self, i1: bloha_stavka_606, bigbig, raznregress):
        # большой короткий подъем
        # hv1, hv2,  hv3 = self._ii._ni_coin_shortshort.GetLast_3_From__v_l_lv_s_m('v')
        sum1=i1._k_ss_v1+i1._k_ss_v2+i1._k_ss_v3
        sum1s=i1._k_s_v1+i1._k_s_v2+i1._k_s_v3
        sum1l=i1._k_l_v1+i1._k_l_v2+i1._k_l_v3
        sum2ss=(i1._k_ss_v3 + i1._k_ss_v2)
        sum2s=(i1._k_s_v3 + i1._k_s_v2)
        sum2l=(i1._k_l_v3 + i1._k_l_v2)
        if bigbig=='nol': 
            if raznregress > -0.0002  and i1._k_n_shortshortdel > 0.995:
                if sum1 > 9 and i1._k_ss_v3 > 1: return True
                if sum1 > 11: return True
                if sum2ss > 12: return True
        if bigbig=='ras': 
            if raznregress > -0.0  and i1._k_ss_v3 > 4:
                return True
            if raznregress > -0.0002  and i1._k_n_shortshortdel > 0.995:
                if sum1 > 6 and i1._k_ss_v3 > 1: return True
                if sum1 > 8: return True
                if sum2ss > 10: return True
        if bigbig=='dva': 
            if raznregress > -0.0001  and i1._k_n_shortshortdel > 0.999:
                if sum1 > 4 and i1._k_ss_v3 > 1: return True
                if sum1 > 6: return True
                if sum2ss > 8: return True
        if bigbig=='tri': 
            if raznregress > -0.0001  and i1._k_n_shortshortdel > 1.01:
                if sum1 > 4: return True
                if sum1 > 2 and i1._k_ss_v3 > 2: return True
                if sum2ss > 6: return True
        return False
    
    def ItIsBiiiigUpCrypta_2h(self, i1: bloha_stavka_606, bigbig):
        # большой короткий подъем
        sum1=i1._k_ss_v1+i1._k_ss_v2+i1._k_ss_v3
        if bigbig=='nol':
            if sum1 > 0.06 and i1._k_ss_v1 >0.002 and i1._k_ss_v2 > 0.002 and i1._k_ss_v3 > 0.002: return True
            if sum1 > 0.05 and i1._k_ss_v1 >0.02 and i1._k_ss_v3 > 0.02: return True
            if i1._k_ss_v2+i1._k_ss_v3 > 0.05:
                if i1._k_ss_v3 >= 0: return True
                elif abs(i1._k_ss_v3)*6 < i1._k_ss_v2: return True

        elif bigbig=='ras':
            if i1._k_ss_v2 > 0.003 and i1._k_ss_v3 > 0.003 and (i1._k_ss_v2+i1._k_ss_v3) > 0.012: return True
            if sum1 > 0.02 and i1._k_ss_v3 > 0.01: return True
            if i1._k_s_v3 > 0.015 and i1._k_ss_v3 > 0.01: return True
            if i1._k_l_v3 > 0.02 and i1._k_ss_v3 > 0.015: return True
        elif bigbig=='dva':
            if i1._k_n_shortshortdel > 1.03 and i1._k_ss_v1 > 0.01 and i1._k_ss_v2 > -0.008 and i1._k_ss_v3 > 0.01: return True
            if sum1 > 0.028 and i1._k_ss_v3 > 0: return True
            if sum1 > 0.011 and i1._k_ss_v1 > 0.0003 and i1._k_ss_v2 > 0.0003 and i1._k_ss_v3 > 0.005: return True
            if i1._k_ss_v2 > 0.012 and i1._k_ss_v3 > 0.004: return True
            if i1._k_ss_v2 > 0.03 and i1._k_ss_v3 > -0.004: return True
            if i1._k_ss_v3 > 0.008 and i1._ii._ni_coin_shortshort._ii_l[len(i1._ii._ni_coin_shortshort._ii_l)-1] < 0.21: return True
        elif bigbig=='tri':
            if i1._k_ss_v2 > 0.01 and i1._k_ss_v3 > -0.0025 and i1._k_s_v3 > 0.005: return True
            if sum1 > 0.02 and i1._k_ss_v2 > 0.008 and i1._k_ss_v3 > -0.006: return True
            if i1._k_n_shortshortdel > 1.03 and i1._k_ss_v1 > 0.02 and i1._k_ss_v2 > 0.005 and i1._k_ss_v3 > -0.01: return True
            if i1._k_s_v3 > 0.01 and i1._k_s_v2 > 0.01 and i1._k_s_v3+i1._k_s_v2 > 0.03: return True
            if i1._k_s_v3 > 0.015 and i1._k_s_v3 > 0.015: return True
            if i1._k_s_v3 > 0.015 and i1._k_s_v1 > 0 and i1._k_s_v2 > 0 and i1._k_s_v3 > 0: return True
            if i1._k_s_v3 > 0.01 and i1._k_ss_v3 > 0.002: return True
        else: small.ifnoterr(5==8)
        return False


    def ItIsBiiiigUpFinam(self, i1: bloha_stavka_606, bigbig, m1):
        # большой короткий подъем
        sum1=i1._k_ss_v1+i1._k_ss_v2+i1._k_ss_v3
        sum1s=i1._k_s_v1+i1._k_s_v2+i1._k_s_v3
        sum1l=i1._k_l_v1+i1._k_l_v2+i1._k_l_v3
        sum2ss=(i1._k_ss_v3 + i1._k_ss_v2)
        sum2s=(i1._k_s_v3 + i1._k_s_v2)
        sum2l=(i1._k_l_v3 + i1._k_l_v2)
        k_n_shortdel_k_n_longdel=i1._k_n_shortdel+i1._k_n_longdel
        return False
        if bigbig=='nol':
            if sum1 > 0.06/m1 and i1._k_ss_v1 >0.002/m1 and i1._k_ss_v2 > 0.002/m1 and i1._k_ss_v3 > 0.002/m1: return True
            if sum1 > 0.05/m1 and i1._k_ss_v1 >0.02/m1 and i1._k_ss_v3 > 0.02/m1: return True
            if i1._k_ss_v2+i1._k_ss_v3 > 0.05/m1:
                if i1._k_ss_v3 >= 0: return True
                elif abs(i1._k_ss_v3)*6 < i1._k_ss_v2: return True
            if sum2ss > 0.015: return True
            if i1._k_ss_v3 > 0.008: return True
            up5=False
            if i1._k_l_v3 > 0.003 and i1._k_s_v3 > 0.003 and  i1._k_ss_v3 > 0.003: up5=True
            if i1._k_l_v3 > 0.0045 and i1._k_s_v3 > 0.0065 and  i1._k_ss_v3 > 0.0: up5=True
            if up5:
                # разворот вверх по оч короткому
                if sum1 > 0.007 and i1._k_ss_v1 < i1._k_ss_v2 and i1._k_ss_v2 < i1._k_ss_v3:
                    return True
                # разворот вверх по среднему
                if sum1 > 0.007 and i1._k_s_v1 < i1._k_s_v2 and i1._k_s_v2 < i1._k_s_v3:
                    return True
            # по регрессиям
            if i1._k_n_shortshortdel > 1.02 and i1._k_n_shortdel > 1.0004:
                return True
            if i1._k_n_shortshortdel > 1.025 and i1._k_n_shortdel > 1.0:
                return True
            if i1._k_n_shortshortdel > 0.98 and i1._k_n_shortdel > 1.0017 and i1._k_n_longdel > 1.004:
                return True
            if i1._k_n_shortshortdel > 0.98 and i1._k_n_shortdel > 1.008 and i1._k_n_longdel > 1.0008:
                return True
            if i1._k_n_shortshortdel > 0.98 and k_n_shortdel_k_n_longdel > 2.008:
                return True

        elif bigbig=='ras':
            # if i1._k_ss_v2 > 0.003/m1 and i1._k_ss_v3 > 0.003/m1 and (i1._k_ss_v2+i1._k_ss_v3) > 0.012/m1: return True
            # if sum1 > 0.02/m1 and i1._k_ss_v3 > 0.01/m1: return True
            if i1._k_s_v3 > 0.015: return True
            # if i1._k_l_v3 > 0.02/m1 and i1._k_ss_v3 > 0.015/m1: return True
            if i1._k_s_v3 > 0.0015 and i1._k_ss_v3 > 0.001: return True
            # по регрессиям
            if i1._k_n_shortshortdel > 1.01 and i1._k_n_shortdel > 1.004:
                return True
            if i1._k_n_shortshortdel > 1.009 and i1._k_n_shortdel > 1.003 and i1._k_n_longdel > 1.006:
                return True
            if i1._k_n_shortshortdel > 0.99 and i1._k_n_shortdel > 1.0016 and i1._k_n_longdel > 1.0035:
                return True
            if i1._k_n_shortshortdel > 0.98 and k_n_shortdel_k_n_longdel > 2.006:
                return True
            if i1._k_n_shortshortdel > 0.99 and k_n_shortdel_k_n_longdel > 2.005:
                return True
        elif bigbig=='dva':
            if i1._k_n_shortshortdel > 1.009 and i1._k_ss_v3 > 0.0005: return True
            if i1._k_n_shortshortdel > 1.004 and i1._k_ss_v3 > 0.002: return True
            if i1._k_ss_v3 > 0.002 and i1._k_s_v3 > 0.001: return True
            # if sum1 > 0.028/m1 and i1._k_ss_v3 > 0: return True
            # if sum1 > 0.011/m1 and i1._k_ss_v1 > 0.0003/m1 and i1._k_ss_v2 > 0.0003/m1 and i1._k_ss_v3 > 0.005/m1: return True
            # if i1._k_ss_v2 > 0.012/m1 and i1._k_ss_v3 > 0.004/m1: return True
            # if i1._k_ss_v2 > 0.03/m1 and i1._k_ss_v3 > -0.004/m1: return True
            # if i1._k_ss_v3 > 0.008/m1 and i1._ii._ni_coin_shortshort._ii_l[len(i1._ii._ni_coin_shortshort._ii_l)-1] < 0.21/m1: return True
        elif bigbig=='tri':
            if i1._k_ss_v2 > 0.01/m1 and i1._k_ss_v3 > -0.0025/m1 and i1._k_s_v3 > 0.005/m1: return True
            if sum1 > 0.02/m1 and i1._k_ss_v2 > 0.008/m1 and i1._k_ss_v3 > -0.006/m1: return True
            if i1._k_n_shortshortdel > 1.03/m1 and i1._k_ss_v1 > 0.02/m1 and i1._k_ss_v2 > 0.005/m1 and i1._k_ss_v3 > -0.01/m1: return True
            if i1._k_s_v3 > 0.01/m1 and i1._k_s_v2 > 0.01/m1 and i1._k_s_v3+i1._k_s_v2 > 0.03/m1: return True
            if i1._k_s_v3 > 0.015/m1 and i1._k_s_v3 > 0.015/m1: return True
            if i1._k_s_v3 > 0.015/m1 and i1._k_s_v1 > 0 and i1._k_s_v2 > 0 and i1._k_s_v3 > 0: return True
            if i1._k_s_v3 > 0.01/m1 and i1._k_ss_v3 > 0.002/m1: return True
            if i1._k_s_v3 > 0.005/m1 and i1._k_ss_v3 > 0.005/m1: return True
        else: small.ifnoterr(5==8)
        return False

    
    def ItIsBiiiigUpFinam24(self, i1: bloha_stavka_606, bigbig, m1):
        # большой короткий подъем
        sum1=i1._k_ss_v1+i1._k_ss_v2+i1._k_ss_v3
        sum1s=i1._k_s_v1+i1._k_s_v2+i1._k_s_v3
        sum1l=i1._k_l_v1+i1._k_l_v2+i1._k_l_v3
        sum2ss=(i1._k_ss_v3 + i1._k_ss_v2)
        sum2s=(i1._k_s_v3 + i1._k_s_v2)
        sum2l=(i1._k_l_v3 + i1._k_l_v2)
        k_n_shortdel_k_n_longdel=i1._k_n_shortdel+i1._k_n_longdel
        if bigbig=='nol':
            return False
        elif bigbig=='ras':
            if i1._k_ss_v1 > 2 and i1._k_ss_v2 > 2 and i1._k_ss_v3 > 1.9: return True
            return False
        elif bigbig=='dva':
            return False
        elif bigbig=='tri':
            return False
        else:
            small.ifnoterr(5==8)
        return False

    
    def ItIsRO(self, i1: bloha_stavka_606):
        return False
        if self._birja=='finam': return False
        if i1._riskc > 1.18:  return True
        if i1._riskc < 0.66:  return True
        if i1._risk < 1.08 and i1._riskc < 0.70:  return True
        if i1._risk < 1.04 and i1._riskc < 0.735:  return True
        if i1._risk < 1.00 and i1._riskc < 0.77:  return True
        if i1._risk < 0.985 and i1._riskc < 0.78:  return True
        if i1._risk < 0.97 and i1._riskc < 0.79:  return True
        if i1._risk < 0.925 and i1._riskc < 0.845:  return True
        if i1._risk < 0.88 and i1._riskc < 0.88:  return True
        if i1._risk < 0.89 and i1._riskc < 0.87:  return True
        if i1._risk < 0.87 and i1._riskc < 0.89:  return True
        return False
    
    def ItIsBiiiigDoun(self, i1: bloha_stavka_606):
        if self._birja=='finam': return self.ItIsBiiiigDounFinam(i1)
        return self.ItIsBiiiigDounCrypta(i1)
    

    def ItIsBiiiigDounFinam(self, i1: bloha_stavka_606):
        # большой короткий  падение 
        sum1=i1._k_ss_v1+i1._k_ss_v2+i1._k_ss_v3
        sum1s=i1._k_s_v1+i1._k_s_v2+i1._k_s_v3
        sum1l=i1._k_l_v1+i1._k_l_v2+i1._k_l_v3
        sum2ss=(i1._k_ss_v3 + i1._k_ss_v2)
        sum2s=(i1._k_s_v3 + i1._k_s_v2)
        sum2l=(i1._k_l_v3 + i1._k_l_v2)
        sikdoun=0
        if i1._k_n_shortshortdel < 1.006: sikdoun=sikdoun+1
        if i1._k_n_shortdel < 1.002: sikdoun=sikdoun+1
        if i1._k_n_longdel < 1: sikdoun=sikdoun+1
        if i1._k_s_shortshortdel < 1: sikdoun=sikdoun+1
        if i1._k_s_shortdel < 1: sikdoun=sikdoun+1
        if i1._k_s_longdel < 1: sikdoun=sikdoun+1
        #
        if i1._k_ss_v1 < 0 and i1._k_ss_v2  < 0 and i1._k_ss_v3 < 0:
            if i1._k_n_longdel < 1 or i1._k_n_shortdel < 1 or i1._k_n_shortshortdel < 1:
                return True
        return False


    def ItIsSmallS(self, i1: bloha_stavka_606):
        # незначительные изменения курса
        # не на чем играть
        return False
        if self._birja!='finam': return False
        shortshort_s=np.mean(i1._ii._ni_coin_shortshort._ii_s)
        short_s=np.mean(i1._ii._ni_coin_short._ii_s)
        long_s=np.mean(i1._ii._ni_coin_long._ii_s)
        if shortshort_s < 0.00025 and short_s < 0.00035:
            return True
        if shortshort_s < 0.00035 and short_s < 0.00045 and long_s < 0.00045:
            return True
        if shortshort_s < 0.00115 and short_s < 0.0008 and long_s < 0.00095:
            return True
        if shortshort_s + short_s + long_s < 0.0018:
            return True
        if shortshort_s < 0.00045 and short_s < 0.00045:
            return True
        return False
    


    def ItIsBiiiigDounCrypta(self, i1: bloha_stavka_606):
        # большой короткий  падение 
        sum1=i1._k_ss_v1+i1._k_ss_v2+i1._k_ss_v3
        sikdoun=0
        if i1._k_n_shortshortdel < 1.006: sikdoun=sikdoun+1
        if i1._k_n_shortdel < 1.002: sikdoun=sikdoun+1
        if i1._k_n_longdel < 1: sikdoun=sikdoun+1
        if i1._k_s_shortshortdel < 1: sikdoun=sikdoun+1
        if i1._k_s_shortdel < 1: sikdoun=sikdoun+1
        if i1._k_s_longdel < 1: sikdoun=sikdoun+1
        #----------
        if i1._k_n_shortshortdel > 1.08: return True # TOO BIG UP
        # if i1._k_ss_v3 < -0.01 and i1._ii._ni_coin_shortshort._ii_l[len(i1._ii._ni_coin_shortshort._ii_l)-1] < 0.21: return True
        # if i1._k_ss_v1 < -0.001 and  i1._k_ss_v2 < -0.001 and i1._k_ss_v3 < -0.001: return True
        # if i1._k_s_v1 < -0.001 and i1._k_s_v2 < -0.001 and i1._k_s_v3 < -0.001: return True
        # if i1._k_s_v3 < -0.01 and  i1._k_ss_v2 < -0.001 and i1._k_ss_v3 < -0.003: return True
        if i1._k_ss_v2 < -0.001 and i1._k_ss_v3 < -0.003: return True
        if i1._k_s_v3 < -0.002 and  i1._k_ss_v3 < -0.003: return True
        if i1._k_s_v3 < -0.003 and  i1._k_ss_v2 < -0.003 and  i1._k_ss_v3 < -0.0003: return True
        if i1._k_ss_v3 < -0.008: return True
        if i1._k_l_v3 < -0.03 and i1._k_s_v3 < -0.01 and i1._k_ss_v3 < 0.01: return True
        if i1._k_l_v3 < -0.03 and i1._k_s_v3 < -0.01 and i1._k_s_v2 < -0.001 and i1._k_s_v1 < -0.001: return True
        if i1._k_l_v3 < -0.06: return True
        if i1._k_l_v3 < -0.02 and i1._k_s_v3 < -0.01: return True
        if i1._k_l_v3 < -0.01 and i1._k_s_v3 < -0.008 and i1._k_ss_v3 < -0.001: return True
        if i1._k_l_v3 < -0.006 and i1._k_s_v3 < -0.002 and i1._k_ss_v3 < -0.0015: return True
        if sum1 < 0 and i1._k_l_v3 < -0.001  and i1._k_s_v3 < -0.0001 and i1._k_ss_v3 < -0.001:  return True
        if sum1 < 0.001 and i1._k_l_v3 < -0.015  and i1._k_s_v3 < -0.009:  return True
        if i1._k_l_v3 < -0.02 and i1._k_s_v3 < -0.001 and i1._k_ss_v3 < -0.0001: 
            if i1._k_l_v2 < -0.02 and i1._k_s_v2 < -0.001 and i1._k_ss_v2 < -0.0001: return True
        if (i1._k_ss_v3+i1._k_ss_v2) < -0.002:
            if (i1._k_s_v3+i1._k_s_v2) < -0.015:
                if  i1._k_l_v3 < -0.01:
                    return True
        # -------------
        if i1._k_n_shortshortdel < 0.93:                    return True
        if i1._k_n_shortshortdel < 0.98:
            if i1._k_n_shortdel  < 0.999 or i1._k_n_longdel < 0.999 or i1._k_s_shortshortdel < 0.999 or i1._k_s_shortdel < 0.999 or i1._k_s_longdel < 0.999:
                return True
        if i1._k_s_shortshortdel < 0.997 and sikdoun > 2 :
            return True
        if i1._k_s_shortshortdel < 0.98:
            if i1._k_n_shortdel  < 0.999 or i1._k_n_longdel < 0.999 or i1._k_n_shortshortdel < 0.999 :
                return True
        if i1._k_n_shortshortdel < 0.999 and i1._k_n_shortdel  < 0.999 and i1._k_n_longdel < 0.999 :
                return True
        if i1._k_n_shortshortdel < 1 and i1._k_n_shortdel  < 1 and i1._k_n_longdel < 1:
            if i1._k_n_shortshortdel+i1._k_n_shortdel+i1._k_n_longdel < 2.985:
                return True
        if i1._k_s_longdel < 0.9989:
            return True
        if i1._k_s_shortdel < 0.995:
            return True
        if i1._k_s_shortshortdel < 0.99 and i1._k_s_shortdel < 0.997:
            return True
        if i1._k_s_shortshortdel < 0.967:
            return True
        # if i1._k_bs_longdel < 0.9989:
        #     return True
        # if i1._k_bs_shortdel < 0.995:
        #     return True
        # if i1._k_bs_shortshortdel < 0.99 and i1._k_bs_shortdel < 0.997:
        #     return True
        # if i1._k_bs_shortshortdel < 0.967:
        #     return True
        if sikdoun > 3: return True
        return False
    

    def PeriodForDopusk(self):
        return self._periodh*60*60*1000
    

    def ItIsRegressDounAndRazvorot(self, i1: bloha_stavka_606, raznregress):
        # регрессии вниз с ускорением вниз
        return False
        if i1._k_n_shortshortdel < 0.999 and raznregress < -0.0004: return True
        if i1._k_n_longdel < 0.998 and i1._k_n_shortdel < 1.01 and i1._k_n_shortshortdel <1.01:
            if raznregress < -0.001: 
                return True
        return False
    
    
    def ItIsRazvorot(self, i1: bloha_stavka_606, raznregress):
        if self._periodh <= 4:
            if raznregress > (0.946-0.94) and i1._k_ss_v3 > 0.009:
                return True
            if raznregress > (1.014-1.007) and i1._k_ss_v3 > 0.004:
                return True
        return False
    
    def ItIsLongUpByVector(self, i1):
        # длинный подъем по вектору
        # l1=i1._ii._ni_coin_shortshort._ii_l[len(i1._ii._ni_coin_shortshort._ii_l)-1]
        # v1=i1._ii._ni_coin_shortshort._ii_v[len(i1._ii._ni_coin_shortshort._ii_v)-1]
        # if v1 > 0.004 and l1 > 0.35:
        #     return True
        return False
    
    def GetRaznRegress(self, i1):
        # последняя регрессия
        l1=len(i1._ii._ni_coin_shortshort._regm)-1
        del1=i1._ii._ni_coin_shortshort._regm[l1]._y_2h[0][0] / i1._ii._ni_coin_shortshort._regm[l1]._y_now[0][0]
        # предпоследняя регессия
        l2=len(i1._ii._ni_coin_shortshort._regm)-2
        del2=i1._ii._ni_coin_shortshort._regm[l2]._y_2h[0][0] / i1._ii._ni_coin_shortshort._regm[l2]._y_now[0][0]
        # разница
        raznregress=del1-del2
        return raznregress
    
    def ItIsLongUpByRegress(self, i1, bigbig, raznregress):
        # длинный подъем
        if self._periodh == 24:
            РР=0
            # if bigbig=='dva':
            #     if i1._k_n_shortshortdel > 1.02 and raznregress > -0.0001: return True
            # if bigbig=='tri':
            #     if i1._k_n_shortshortdel > 1.015 and raznregress > -0.0001: return True
        elif self._periodh <= 4:
            if bigbig=='tri':
                if i1._k_n_shortshortdel > 0.91 and i1._k_n_shortdel > 1.02 and i1._k_n_longdel > 1.002:
                    return True
                if i1._k_n_shortshortdel > 0.94 and i1._k_n_shortdel > 1.016 and i1._k_n_longdel > 1.002:
                    return True
                if i1._k_n_shortshortdel > 1.001 and i1._k_n_shortdel > 1.001 and i1._k_n_longdel > 1.0015:
                    return True
                if i1._k_n_shortshortdel > 1.001 and i1._k_n_shortdel > 1.001 and i1._k_n_longdel > 1.0015:
                    return True
                if i1._k_n_shortshortdel > 1.03 and i1._k_n_shortdel > 0.99 and i1._k_n_longdel > 1.0015:
                    return True
                if i1._k_n_shortshortdel > 0.99 and i1._k_n_shortdel > 1.0018 and i1._k_n_longdel > 1.002:
                    return True
                if i1._k_n_shortshortdel > 0.99 and i1._k_n_shortdel > 0.99 and i1._k_n_longdel > 1.01:
                    return True
                if i1._k_n_shortshortdel > 0.99 and i1._k_n_shortdel > 0.99 and i1._k_n_longdel > 0.99:
                    if i1._k_s_shortshortdel > 0.99 and i1._k_s_shortdel > 1.012 and i1._k_s_longdel > 0.99:
                        return True
                if i1._k_n_shortshortdel > 0.985 and i1._k_n_shortdel > 0.99 and i1._k_n_longdel > 0.999:
                    if i1._k_s_shortshortdel > 1.015 and i1._k_s_shortdel > 0.999 and i1._k_s_longdel > 0.999:
                        return True
                if i1._k_n_shortshortdel > 0.999 and i1._k_n_shortdel > 0.99 and i1._k_n_longdel > 0.999:
                    if i1._k_s_shortshortdel > 1.013 and i1._k_s_shortdel > 0.999 and i1._k_s_longdel > 0.999:
                        return True
                if i1._k_n_shortshortdel > 1.01 and i1._k_n_shortdel > 0.99 and i1._k_n_longdel > 0.999:
                    if i1._k_s_shortshortdel > 1.012 and i1._k_s_shortdel > 0.999 and i1._k_s_longdel > 0.999:
                        return True
        return False
                              

    def VnizKonkretnoIdet(self,  i1: bloha_stavka_606):
        # конкретно падает 
        if self._birja != 'finam': return  False
        if i1._k_s_shortshortdel < 0.999 and i1._k_n_shortdel < 0.999:
            if i1._k_ss_v3 < -0.001 and i1._k_s_v3 < -0.0012 and i1._k_l_v3 < -0.01:
                return True
        # if i1._k_bs_shortshortdel < 0.9999 or i1._k_s_shortshortdel < 0.9999:
        #     if i1._k_n_longdel < 0.999 and i1._k_n_shortdel < 0.999 and i1._k_n_shortshortdel < 0.99:
        #         return True
        return False
    
    def ANadoViiiiiiihodim(self,  i1: bloha_stavka_606, mono, nuno, timepar, addcomm):
        price, proc, buytime=self.GetPriceAndProcentAndBuyTime(timepar)
        risk=i1._risk
        # решает надо ли выходить из сделки
        if small.ItDebugBuySell():  return True
        if small.ItDebugRandBuySell() and random.randint(0, 5) == 2  :
            return True
        if self._sms_command is not None and (self._sms_command=='selllong' or self._sms_command=='buyshort'):
            # заполняем по смс команде
            if self._sms_coin == i1._coin: return True
        #-------
        raznregress = self.GetRaznRegress(i1)
        # искл-я
        iskl, iskl5, iskl_stoploss, iskl_stoploss_big=False, False, False, False
        if self.IsklOut_AllDoun_ByRegress(i1, timepar): iskl = True
        if self.VnizKonkretnoIdet(i1): iskl = True
        if self.IsklOut_StopLoss(proc, i1, timepar): iskl, iskl_stoploss = True, True
        if self.IsklOut_StopLoss_Big(proc, i1, raznregress, timepar): iskl, iskl_stoploss , iskl_stoploss_big = True, True, True
        # минимальный процент
        flagmin=False
        if self._FlagMinProcentOut: flagmin=True
        if self._FlagMinProcentOut_ByRegress:            
            if i1._k_n_shortshortdel > 1.025 and i1._k_n_shortdel > 1.015 and i1._k_n_longdel > 1.005:
                flagmin=True
        if flagmin:
            minproc = self.GetMinProcentOut( i1, timepar, proc)
            if proc < minproc and iskl==False:
                # пробуем уменьшить процент при общем развороте
                if minproc > 0 and proc > 0:
                    if self.IsklOut_AllDoun_Razvorot_ByRegress(i1, timepar): 
                        if minproc > 0 and proc < minproc/2 and iskl==False:
                            return False
                        else:
                            iskl5=True
                    else: 
                        return False
                else:
                    return False
        else:
            if iskl_stoploss: 
                iskl5=True
        # big up
        if self.ItIsBiiiigUp(i1, 'nol', raznregress)  and iskl5 == False:
            return False
        # выход
        # if self.Viiiiiiihod_PoUp(i1, timepar,'nol', proc):
        #     return True
        if self.Viiiiiiihod_PoShort(i1, timepar,'nol',proc, raznregress):
            return True
        # big up
        if self.ItIsBiiiigUp(i1, 'ras', raznregress) and iskl5 == False:
            return False
        # if self.Viiiiiiihod_PoUp(i1, timepar,'ras', proc):
        #     return True
        if self.Viiiiiiihod_PoShort(i1, timepar,'ras',proc, raznregress):
            return True
        # big up
        if self.ItIsBiiiigUp(i1, 'dva', raznregress):
            return False
        if self.ItIsLongUpByRegress(i1, 'dva', raznregress):
            return False
        # выход 
        # if self.Viiiiiiihod_PoUp(i1, timepar,'dva', proc):
        #     return True
        if self.Viiiiiiihod_PoShort(i1, timepar,'dva',proc, raznregress):
            return True
        # big up
        if self.ItIsBiiiigUp(i1, 'tri', raznregress):  
            return False
        if self.ItIsLongUpByVector(i1):
            return False
        if self.ItIsLongUpByRegress(i1, 'tri', raznregress):
            return False
        if self.ItIsRazvorot(i1, raznregress):
            return False
        # выход 
        # if self.Viiiiiiihod_PoUp(i1, timepar,'tri', proc):
        #     return True
        if self.Viiiiiiihod_PoShort(i1, timepar,'tri',proc, raznregress):
            return True
        # big stoploss
        if iskl_stoploss_big:
            return True
        return False
            
    
    def ANadoSkakat(self, i1: bloha_stavka_606, newp: bloha_stavka_606):
        # решает надо ли перескакивать нпа другую монету 
        # f1, f2, f3, f4=False, False, False, False
        # #if i1._maxperc < self._MonoSkokSellPrice: f1=True             (f1==True or f2==True) and 
        # #if i1._maxperc-i1._minperc > self._MonoSkokSellRazn: f2=True
        # if newp._maxperc >= self._MonoSkokBuyPrice and newp._minperc >= self._MonoSkokBuyPrice: f3=True
        # if newp._razn_abs <= self._MonoSkokBuyRazn: f4=True
        # if f3==True and f4==True:
        #     return True
        return False
    
    def KolduyProcent(self, ii, upf, debugsave=False):
        # предположим какой процент на выходе будет
        # перевод в читаемую для ии форму
        iir2=iireshalkaclass_606()
        iir2.InitFrom_iireshalkaclass_0_606(ii)
        rm1=iir2.GenerateOneMassive()
        # debugsave
        if debugsave:
            jj=0
            # import json
            # with open("d:\\vrem\\TestDebug_rm1_.txt", 'w') as fw:
            #     json.dump(rm1, fw)            
        # ---------------------------------------rm1=self._iir2max.AsMaxGenerateOneMassive(iir2)
        rm2=[]
        rm2.append(rm1)
        rm3 = np.array(rm2)
        rm4=torch.FloatTensor(rm3)
        # гадаем
        vector=self._v_model(rm4)
        if vector is None:
            print('Error 77788824')
            return None
        vector=float(vector)
        return vector



    def GetPrognoz(self,  coin, timepar, oldii:iireshalkaclass_0_606, upf, dounf, prognozh):
        if coin==None: return None
        bs=bloha_stavka_606()
        shortshort1, short1, long1=None, None, None
        # bigshortshort1, bigshort1, biglong1=None, None, None
        if oldii is not None:
            shortshort1, short1, long1=oldii._ni_sredniy_shortshort, oldii._ni_sredniy_short, oldii._ni_sredniy_long
            # bigshortshort1, bigshort1, biglong1=oldii._ni_bigsredniy_shortshort, oldii._ni_bigsredniy_short, oldii._ni_bigsredniy_long
        prognozup, prognozdoun, vector = None,None,None
        bs._ii.InitUpDounFlages(True, upf, dounf, prognozh)
        if bs._ii.Init(self.GetCursor(), self._birja, coin, timepar, False, False, 0, 0, short1, long1, shortshort1) == False:
            return None
        debugsave=False
        #if coin=='CHMF' and  timepar==1705907163913: debugsave=True
        vector=self.KolduyProcent(bs._ii, None, debugsave)
        #инит ставка
        bs.Init2(self.GetCursor(), self._birja, coin, timepar,None, None,None, None, bs._ii.ItIsFullUp(), bs._ii.ItIsFullDoun(), vector)
        # marja
        bs._marja=self._FlagAndBuyAndShort
        return bs
    
    def DebComm(self,comm):
        self._ppprm.append(comm)


    def GetBuyTime(self):
        return self._bytime

    def GetHisCoorrectProcentPlus(self):
        return self._procenthiscorrectplus
    
    def SetProcentPlus(self, pp):
        self._procenthiscorrectplus=pp
    
    def CalcAndSaveProcentPlus(self, i1: bloha_stavka_606):
        p1=self.GetHisCoorrectProcentPlus()
        if i1._vshort > 0.5: p1=0
        else :
            p1=p1*1.1
            p1=p1+(-i1._vshort+0.5)*0.3
        self.SetProcentPlus(p1)

    def GetMinProcentOut(self,  i1: bloha_stavka_606, timepar, proc):
        # --correct---------
        XMul=self._XMul
        if self._birja=='finam':
            if proc < -1.0: XMul=self._XMul*2
            elif proc < -0.5: XMul=self._XMul*1.5
            if proc > 0.6: XMul=self._XMul/4
            elif proc > 0.4: XMul=self._XMul/3
            elif proc > 0.2: XMul=self._XMul/2
        # -----------
        buytime=self.GetBuyTime()
        # x=(timepar-buytime)/(5*60*1000)
        # x=x*self._XMul # чем меньше тем длиннее
        # plus1 = self._XMinOut-0.9*x*x + 1.7*x 
        plus1=small.CalcProcentMinOut(buytime, timepar, self._periodh, XMul, self._XMinOut)
        f22=False
        if f22:
            for t1 in range(buytime, timepar, 5*60*1000):
                p22=small.CalcProcentMinOut(buytime, timepar, self._periodh, XMul, self._XMinOut)
                print(str(round(p22, 3)))
                
        # add
        if self._XMul > 0.0047-0.001:
            p2=self.GetHisCoorrectProcentPlus()
            plus1=plus1-p2
        return plus1


    def BuyCoin(self, newp: bloha_stavka_606, timepar):
        # buy
        self._startprice=self.GetPriceCoin(newp._coin, timepar)
        if self._startprice is None: return False
        self._coin=newp._coin
        self._oldcoin=newp._coin
        self._summ=self._summ-(self._summ*0.15)/100
        self._bytime=timepar
        self._procenthiscorrectplus=0
        self._long_or_buy=newp._long_or_buy
        # comm
        self._prm.append(newp._coin+" ")
        self._prm.append(str(timepar)+" ")
        
        # self._prm.append(self.GetGlStr()+" ")
        self._prm.append("max "+small.str5(newp._maxperc)+" ")
        self._prm.append("min "+small.str5(newp._minperc)+" ")
        self._prm.append("sred max "+small.str5(newp._sredniy_max)+" ")
        self._prm.append("sred min "+small.str5(newp._sredniy_min)+" ")
        self._prm.append("razn "+small.str5(newp._razn_abs)+" ")
        #--------
        return True
    
        
    def GetPriceAndProcentAndBuyTime(self, timepar):
        # ТЕКУЩАЯ Цена и процент от покупки
        price=self.GetPriceCoin(self.GetWorkCoin(), timepar)
        if price is None:
            return None, None, None
        proc=(price-self._startprice)*100/self._startprice
        return price, proc, self._bytime

    def PrintInfo(self, timepar):
        # conn=db.GetConnect()
        # cursor = conn.cursor()
        self.PrintInfo555( timepar)
        # conn.close()
        # cursor.close()
    
    def PrintInfo555(self,  timepar):
        for i in range(0, 3):
            print("----------------------------------------------------------------------")
        str3="Kapital "+str(round(self._summ, 2))
        if self._FlagSmotrimNstroy: 
            str3=small.adder(str3, " nastroy up, doun "+str(self._GlSikUp)+", "+str(self._GlSikDoun)+";")
        print(str3)
        str1=''
        for i in self._prm:
            str1=str1+i+', '
        print(str1)
        if self._coin is None:
            print("No coin")
        else:
            price, proc, buytime=self.GetPriceAndProcentAndBuyTime(timepar)
            print(self._coin
                  +"  buy="+str(round(self._startprice, 8))
                  +"  now="+str(round(price, 8))
                  +"  procent="+str(round(proc, 8)))
        # comm
        if self._coin is not None:
            self.DebComm(self._coin+"  procent="+str(round(proc, 2)))
        cp = class55plus()
        cp._timeid=timepar
        cp.InitNastroyTime_NoCursor(self.GetCursor())
        # p44=self._procent_max_ro_show        p55=self._procent_min_ro_show
        ##p11, p22=self.Get__procent_max_ro_show_procent_min_ro_show()
        # p1=self.GetPrognoz( self.GetWorkCoin(), timepar, None, False, False)
        # if p1 != None:
        #     print("moon "+str(round(cp._Nastroy_MoonPhase, 2))
        #         +" dn "+str(cp._Nastroy_WeekDay)
        #         +" h "+str(cp._Nastroy_TimeHour)
        #         +" min "+str(cp._Nastroy_TimeMin)
        #         +" maxprog " +small.str5(p1._maxperc)
        #         +" minprog " +small.str5(p1._minperc)
        #         )
        # else:
        #     print("No Coin")
        self.PrintSikokoCoinsObnovleno( timepar)

    def GetPriceCoin(self, coin, timepar):
        # текущая цена монеты
        if coin is None:
            return None
        tname=small.GetTableName(self._birja, coin)
        rows=self.GetSell( "select max(id) from "+tname
                         +" where id <= "+str(timepar))
        if len(rows) != 1: return None
        id=int(rows[0][0])
        rows=self.GetSell( "select max(price) from "+tname
                         +" where id = "+str(id))
        if len(rows) != 1: return None
        # sell
        price=rows[0][0]
        return price
    
    def InitIndexNastroeniyaCrypta(self):
        # индекс настроения
        if self._Test5==False:
            if self._birja=='finam':
                self._IndexNastroeniya=db.GetPerFromPremennie( self.GetCursor(), 'IndexNastroeniyaFinam', 'float', 0.6, 1.33, 1)
            else:
                self._IndexNastroeniya=db.GetPerFromPremennie( self.GetCursor(), 'IndexNastroeniyaCrypta', 'float', 0.6, 1.33, 1)

    def Get_Long_or_Buy(self):
        return self._long_or_buy
    
    def SellCoin(self, timepar):
        # sell
        price, proc, buytime=self.GetPriceAndProcentAndBuyTime(timepar)
        self._sellprice=price
        small.ifnoterr(self._sellprice != None)
        if self.Get_Long_or_Buy()==False: 
            proc=-proc
        str1=str(round(proc, 3))
        self._prm.append(str1+"%\n")
        self._summ=self._summ-(self._summ*0.15)/100+(proc*self._summ)/100
        #
        self._coin=None
        self._startprice=None
        self._long_or_buy=None
        #self._sellprice=None
        if self._FlagSmotrimNstroy: 
            self._prm.append(" nastroy up, doun "+str(self._GlSikUp)+", "+str(self._GlSikDoun)+";"+" ")
        return True

    def SortByMax(self, i1: bloha_stavka_606):
        # if self._birja=='finam':
        #     return (i1._k_n_shortdel+i1._k_n_shortshortdel)
        return i1._k_n_shortdel
    
    def SortByRand(self, i1: bloha_stavka_606):
        return random.random()


    
    def GetWorkCoin(self):
        return self._coin
    
    def Zachistka(self):
        return 0
    
    def PrintSikokoCoinsObnovleno(self,  timepar):
        # ПИШЕМ  сколько монет обновлено 
        sikok=0
        str1=''
        for c1 in self._cm:
            t1=small.GetTableName(self._birja, c1)
            if t1 is None: continue
            rows=self.GetSell("select max(id) from "+t1+" where id <= "+str(timepar))
            if rows is None or len(rows)==0:
                str1=str1+", "+c1
                continue
            id1=rows[0][0]
            if id1 == None:
                str1=str1+", "+c1
                continue
            razn=int(timepar)-int(id1)
            if razn < 5*60*1000:
                sikok=sikok+1
            else :
                str1=str1+", "+c1
        # print  -------------------
        str2="Obnovleno "+str(sikok)+" monet is "+str(len(self._cm))+". "
        if len (str1) > 0:
            str2=str2+"  Bad: "+str1
        print(str2)
        an1=small.GetAlgoName()
        db.PrintInfoToComments(self.GetCursor(), self.GetConn(), None, an1, str2)
        
    def IsklBuyOldCCoin(self, i1: bloha_stavka_606, timepar):
        #  1 не заходить подряд на одну и ту жже монеьтцу 2 раза подряд по более дорогой цене что продал ранее
        if self._Flag_NotVhodNaTuJeMonetu:
            if i1._coin == self._oldcoin: 
                price=self.GetPriceCoin(i1._coin, timepar)
                if price != None and self._sellprice != None:
                    if price > self._sellprice:
                        return True
        return False
    
    
    def IsklOut_AllDoun_Razvorot_ByRegress(self, i1: bloha_stavka_606, timepar):
        # разворот вниз по всем регрессиям
        if self._Flag_IsklOut_AllDoun_Razvorot_ByRegress != True: return False
        if self._birja!='finam': return False
        # 
        p5=0
        for i in range(0, 3):
            rpnew=i1._ii._ni_sredniy_shortshort.GetRegressProporcii(4-i-1)
            rpold=i1._ii._ni_sredniy_shortshort.GetRegressProporcii(4-i-2)
            p55=rpold-rpnew
            p5=p5+p55
            if p55 < 0.0002:
                return False
        return True
    
    def IsklOut_AllDoun_ByRegress(self, i1: bloha_stavka_606, timepar):
        # падение по всем регрессиям
        if self._birja=='finam': 
            if i1._k_n_longdel < 0.905: return True     # такое было
            if i1._k_n_shortdel < 0.95: return True     # такое было
            return False
        elif self._Strat_Tolko_BNB:
            return False
        else:
            if i1._k_n_shortshortdel < 1 and i1._k_n_shortdel < 1 and i1._k_n_longdel < 1:
                if i1._k_s_shortshortdel < 1 and i1._k_s_shortdel < 1:
                    if i1._vshort < 0.6:
                        return True
            if (i1._k_n_shortshortdel < 1 or i1._k_n_shortdel < 1 or i1._k_n_longdel < 1) and i1._k_s_shortshortdel < 0.942:
                return True
        return False
  
    def IsklOut_StopLoss(self, proc, i1: bloha_stavka_606, timepar):
        # стоп лосс
        if self._FlagStopLoss != True: return False
        if proc < -0.7:
            return True
        return False

    def IsklOut_StopLoss_Big(self, proc, i1: bloha_stavka_606, raznregress, timepar):
        # стоп лосс
        if self._FlagStopLoss != True: return False
        if self._birja=='finam':
            if i1._vshort < 0.611 and proc < -0.7*2 and raznregress < -0.002 and i1._k_n_shortshortdel < 1.017: 
                return True
            if i1._vshort < 0.731 and proc < -0.7*2 and i1._k_n_shortdel < 0.95: 
                return True
        else:
            # crypta
            if i1._vshort < 0.611 and proc < -0.7*2 and raznregress < -0.001: 
                return True

        return False




    
    def IsklInput(self, i1: bloha_stavka_606, timepar):
        #  1 не заходить подряд на одну и ту жже монеьтцу 2 раза подряд по более дорогой цене что продал ранее
        # 4563
        #if self.ItIsBiiiigDoun( i1, True): return True
        #if self.IsklBuy_NotInputRaznicaPrognoz(i1, timepar): return True
        #if self.IsklNotVhodPoUpDoun(i1, timepar): return True
        #if self.IsklInput_AllDoun_ByRegress(i1, timepar): return True
        if self.IsklBuyOldCCoin(i1, timepar): return True
        #if self.IsklBuy_NotInputNaPademnii(i1, timepar): return True
        #if self.IsklBuyNaObshemPadenii(i1, timepar): return True
        return False


    def DebugPrintBudushee(self,  coin, timepar):
        self.DebComm("\n----------Gradushee----------"+coin+"-----------------\n")
        self.DebComm("\n----------Gradushee----------"+coin+"-----------------\n")
        self.DebComm("\n----------Gradushee----------"+coin+"-----------------\n")
        for i in range(0, 20):
            timepar=timepar+5*60*1000
            price, proc, buytime=self.GetPriceAndProcentAndBuyTime( timepar)
            self.DebComm(coin+" "+str(round(proc, 4))+"% "+str(round(price,4))+"$")
            # pp=self.GetPrognoz( coin, timepar, None, False, False)
            # if pp is not  None:
            #     self.DebComm(coin+" "+str(round(proc, 4))+"% "+str(round(price,4))+"$, "+pp.GetDebugInfo(0, 0, self._Strat_Standart, self._Strat_BigDoun, self._Strat_BigDoun_Size, self._Strat_Tolko_BNB, self._XMul, self._XMinOut, self._procenthiscorrectplus)+"")
            # else:
            #     self.DebComm(coin+" Prognos = None -----------------------------------\n")


    def Go(self, timepar):
        # conn=db.GetConnect()
        # cursor = conn.cursor()
        ret=self.Go555( timepar)
        # conn.close()
        # cursor.close()
        return ret
    
    def InitStratRukami(self, Strat_Standart, Strat_BigDoun, Strat_BigDoun_Size, Strat_Tolko_BNB, XMul, XMinOut, procenthiscorrectplus):
        self._Strat_Tolko_BNB=False
        self._Strat_Standart=True
        self._Strat_BigDoun=False
        self._Strat_BigDoun_Size=2.5
        self._XMul=0.04
        self._XMinOut=0.4
        self._procenthiscorrectplus=0
        if Strat_Tolko_BNB is not None: self._Strat_Tolko_BNB=Strat_Tolko_BNB
        if Strat_Standart is not None: self._Strat_Standart=Strat_Standart
        if Strat_BigDoun is not None: self._Strat_BigDoun=Strat_BigDoun
        if Strat_BigDoun_Size is not None: self._Strat_BigDoun_Size=Strat_BigDoun_Size
        if XMul is not None: self._XMul=XMul
        if XMinOut is not None: self._XMinOut=XMinOut
        if procenthiscorrectplus is not None: self._procenthiscorrectplus=procenthiscorrectplus
        self.CorrectStrat()


    def CorrectStrat(self):
        if self._Strat_Tolko_BNB: 
            self._FlagMinProcentOut=False
            self._FlagMinProcentOut_ByRegress=False
            if self._Test5: self._FlagAndBuyAndShort=True
        else: 
            self._FlagMinProcentOut=True
            self._FlagMinProcentOut_ByRegress=True
        if self._Strat_Tolko_BNB and self._Strat_Standart: small.ifnoterr(5==9)
        if self._Strat_Tolko_BNB and self._Strat_BigDoun: small.ifnoterr(5==9)

    
    def InitStrat(self):
        if self._Test5==False:
            
            self._Strat_Tolko_BNB=db.GetPerFromPremennie(self.GetCursor(), 'Strat_Tolko_BNB_'+small.GetAlgoName(True), 'bool', False, True, True)
            self._Strat_Standart=db.GetPerFromPremennie(self.GetCursor(), 'Strat_Standart_'+small.GetAlgoName(True), 'bool', False, True, True)
            self._Strat_BigDoun=db.GetPerFromPremennie(self.GetCursor(), 'Strat_BigDoun_'+small.GetAlgoName(True), 'bool', False, True, False)
            self._Strat_BigDoun_Size=db.GetPerFromPremennie(self.GetCursor(), 'Strat_BigDoun_Size_'+small.GetAlgoName(True), 'float', 1.4, 15, 2.5)
            self._FlagAndBuyAndShort=db.GetPerFromPremennie(self.GetCursor(), 'FlagAndBuyAndShort_'+small.GetAlgoName(True), 'bool', False, True, False)
        if self._Test5 == False:
            # --------------
            self._XMul=db.GetPerFromPremennie(self.GetCursor(), 'XMul_'+small.GetAlgoName(True), 'float', 0.01, 0.000008, 0.0012)
            self._XMinOut=db.GetPerFromPremennie(self.GetCursor(), 'XMinOut_'+small.GetAlgoName(True), 'float', 0.2, 5, 0.4)
        self.CorrectStrat()

    def DebCommProcent(self, timepar):
        price, proc, buytime=self.GetPriceAndProcentAndBuyTime(timepar)
        self.DebComm(self.GetWorkCoin()+" "+str(round(proc, 2))+"%,")


    def GetProcentPrognozFromProcentMonet(self, ProcentPrognoz, ProcentMonet):
        x=100
        max1  = (((x)/(4))*((x)/(28)))
        if ProcentMonet > 100: ProcentMonet=100
        if ProcentMonet < 0: ProcentMonet=0
        x=100-ProcentMonet
        g1  = (((x)/(4))*((x)/(28)))
        ret=0.1+ProcentPrognoz*g1/max1
        return ret

    def GetUpMassive(self, p1, pm, timepar):
        # СИНЖАЯ входной процент увеличиваем охват монет выдаем массив монет для покупки
        retupm=None
        # # СРЕДНЯЯ СТАВКА
        # ПОИСК МОНЕТКИ
        if len(pm) == 0:
            return None
        if  True:
            upm=[]
            for i in pm:
                i1: bloha_stavka_606 = i
                # повтор уже купленной
                if p1  != None :
                    if p1._coin == i1._coin:
                        continue
                if self._sms_command is not None and (self._sms_command=='buylong' or self._sms_command=='sellshort'):
                    # заполняем по смс команде
                    if self._sms_coin == i1._coin:
                        if self._sms_command=='sellshort': i1.ReversToShortToLong()
                        #добавим
                        upm.append(i1)
                        continue
                else:
                    # прогноз up
                    if self.ANadoVhodim(i1, timepar)==True:
                        #добавим
                        upm.append(i1)
                        continue
                    # прогноз doun
                    if self._FlagAndBuyAndShort!=True: continue
                    i1.ReversToShortToLong()
                    if self.ANadoVhodim(i1, timepar)==True:
                        #добавим
                        upm.append(i1)
                        continue
            if len(upm) > 0:
                # сортируем
                if small.ItDebugBuySell() or small.ItDebugRandBuySell():
                    upm.sort(key=self.SortByRand, reverse=True)
                else:
                    upm.sort(key=self.SortByMax, reverse=True)
                self.DebComm("\nSelected coins\n")
                for u1 in upm:
                    self.DebComm(u1.GetDebugInfo(0, 0, self._Strat_Standart, self._Strat_BigDoun, self._Strat_BigDoun_Size, self._Strat_Tolko_BNB, self._XMul, self._XMinOut, 0))
                self.DebComm("\n\n")
                retupm=upm
            # break
        return retupm
    
    def AddPrintInfoToComments(self, comm1):
        self.DebComm(comm1)

    def EstNotes(self,  timepar):
        # проверка нна сущ-е значений для работы
        if self._birja=='finam':
            tb=small.GetTableName(self._birja, 'srednee')
            rows=self.GetSell('select max(id) from '+tb+' where id >= '+str(timepar-5*60*1000)+' and id <= '+str(timepar))
            id=small.GetCorrectOneNoteFromRowsAsOne(rows)
            if id is None:
                print('-------------------- No notes ------------------')
                return False
        return True

    def StopKran(self):
        # an=small.GetAlgoName()
        return False

    def GetPrognozLongShort(self, wcoin, timepar):
        # делает длинный и короткий прогноз
        p1, sp1=None, None
        if wcoin is not None:
            p1=self.GetPrognoz( wcoin, timepar, None, False, False, self._periodh)
            if self._FlagAndShortModel:
                if p1 is not None:
                    sp1=self.GetPrognoz( wcoin, timepar, None, False, False, self._short_periodh)
                    if sp1 is None : p1=None
        return p1, sp1

    def Go555(self,  timepar):
        # зачистка кривых ордеров
        self.Zachistka()
        # НАСТРОЕНИЕ РЫНКА
        self.InitIndexNastroeniyaCrypta( )
        self.InitStrat()
        self.DebComm(' \n ')
        # проверка нна сущ-е значений для работы
        if self.EstNotes( timepar) == False and small.ItDebugBuySell() == False: 
            comm1='--+++ No new notes inprices tables +++-- '
            print(comm1)
            self.DebComm(comm1+'\n ')
            return False
        

        # текущая ставка
        p1, sp1=self.GetPrognozLongShort(self.GetWorkCoin(), timepar)
        if p1 is not None :
            # procent plus
            self.CalcAndSaveProcentPlus(p1)
            # # comm
            self.DebCommProcent(timepar)
            self.DebComm(p1.GetDebugInfo(self._bytime, timepar, self._Strat_Standart, self._Strat_BigDoun, self._Strat_BigDoun_Size, self._Strat_Tolko_BNB, self._XMul, self._XMinOut, self.GetHisCoorrectProcentPlus()))
            self.DebComm(",pp,"+str(round(self.GetHisCoorrectProcentPlus(), 2))+",")
            str5=p1._coin+' ~ '+str(round(p1._vshort, 2))
            db.SetPerToPremennie(self.GetCursor(), self.GetConn(), 'ShortProg_'+small.GetAlgoName(True), str5)
            # прогнозы для показа
            p3=p1
            if self.Get_Long_or_Buy()==False:
                p3.ReversToShortToLong()
                                                        # НЕ ВЫХОДИМ по любому
                                                        #     if self.ANadoViiiiiiihodim( p3, True, False, timepar, False) == False:             
                                                        #         return False
                                                        # # out
                                                        # if p1  != None :
            # выходим по любому
            if self.ANadoViiiiiiihodim( p3, False, True, timepar, True):
                self.DebugPrintBudushee( p1._coin, timepar)
                self.AddPrintInfoToComments("Sell "+p1._coin)
                oksell=self.SellCoin(timepar)
                if oksell != True: return False
                p1=None
        # запрещаем перескакивать с монеты на монету
        if self._FlagMonoPereskakivat==False and p1  != None : return False
        # ручной стоп кран
        if self.StopKran() :
            print(" +++++++++++++++++++ StopKran is on +++++++++++++++++++")
            return False
        # варианты текущие
        self.DebComm("(sex max|sex min|prognoz max|prognoz min|real max|real min):,")
        pm=[]
        spm=[]
        oldii, shortoldii=None, None
        str5=''
        for i in range(0, len(self._cm)):
            coin=self._cm[i]
            if self._Strat_Tolko_BNB:
                if coin  != 'BNB':
                    continue
            # длинный прогноз
            pp:bloha_stavka_606=self.GetPrognoz( coin, timepar, oldii, False,False, self._periodh)
            if pp is None: 
                self.DebComm(coin+" Err 3344\n")
                continue
            if oldii is None:
                oldii=pp._ii
            # короткий прогноз
            if self._FlagAndShortModel:
                spp:bloha_stavka_606=self.GetPrognoz( coin, timepar, shortoldii, False,False, self._short_periodh)
                if spp is None: 
                    self.DebComm(coin+" Err 334114\n")
                    continue
                if shortoldii is None:
                    shortoldii=spp._ii
                spm.append(spp)
                self.DebComm(spp._coin+"("+small.str5(spp._vshort)+"|"+small.str5(spp._RealMaxProc)+"|"+small.str5(spp._RealMinProc)+")")
            # ADD
            pm.append(pp)
            self.DebComm(pp._coin+"("+small.str5(pp._vshort)+"|"+small.str5(pp._RealMaxProc)+"|"+small.str5(pp._RealMinProc)+")")
            str5=pp._coin+' ~ '+str(round(pp._vshort, 2))+',   '
        db.SetPerToPremennie(self.GetCursor(), self.GetConn(), 'ShortProg_'+small.GetAlgoName(True), str5)
        self.DebComm("\n")
        # show
        maxv, minv=0, 1
        str1=''
        for pp in pm:
            maxv=max(maxv, pp._vshort)
            minv=min(minv, pp._vshort)
            str1=small.adder(str1, pp._coin, '::', str(round(pp._vshort, 2)), '  ')
        print('Sel maxv='+str(round(maxv, 2))+' minv='+str(round(minv, 2))+'  '+str1)
        # input
        upm=self.GetUpMassive( p1, pm, timepar)
        if upm == None: return False
        p3: bloha_stavka_606=upm[0]
        if p1  == None :
            self.DebComm(p3.GetDebugInfo(0, 0, self._Strat_Standart, self._Strat_BigDoun, self._Strat_BigDoun_Size, self._Strat_Tolko_BNB, self._XMul, self._XMinOut, 0))
            self.AddPrintInfoToComments(("Buy " if p3._long_or_buy == True else "Sell")+p3._coin)
            # покупаем когда нет монет уже купленных
            self.BuyCoin(p3, timepar)
        else:
            # покупаем когда уже есть купленные монеты
            if self.ANadoSkakat(p1, p3) or small.ItDebugBuySell():
                global sikokoskokov
                sikokoskokov=sikokoskokov+1
                db.PrintInfoToComments(self.GetCursor(), self.GetConn(), None, small.GetAlgoName(), "sikokoskokov is "+str(sikokoskokov))
                self.AddPrintInfoToComments("Sell to skok "+p1._coin)
                if self.SellCoin(timepar) == True:
                    self.AddPrintInfoToComments("Buy from skok  "+p3._coin)
                    self.BuyCoin(p3, timepar)
                else:
                    hh=0
                
        return False

    