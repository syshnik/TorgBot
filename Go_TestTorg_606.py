

from __future__ import print_function
from datetime import datetime 
import random
import small
import db
# from iireshalka import iireshalkaclass
from iireshalka_606 import iireshalkaclass_0_606
from iireshalka_606 import iireshalkaclass_606
from obuchalka_606 import Obuchalka_class_606
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import matplotlib.pyplot as plt                              # построение графиков
# # Moving to GPU
# tensor_gpu = tensor_from_list.to('cuda')
# # Moving back to CPU
# tensor_cpu = tensor_gpu.to('cpu')
print(torch.cuda.is_available()) # Should print True
from time import sleep
import array as arr 
#import torch
#import torch.nn as nn
import torch.optim as optim
import numpy as np
# https://qudata.com/ml/ru/NN_Base_Torch_NN.html
# import simpleaudio as simple_audio 
import time

import simplejson
from iimodels import model_900_606
import  iimodels 

from iiobuchalka_606 import Obuchalka_606
# from iihshar import hshar
# from iihshar_606 import hshar_900_606
#from wold_ii_bloha_606 import bloha_606
from zapolnalka import zapolnalka_class 
from ii_bloha_up_doun_606 import bloha_up_doun_606
Global_plusname = "_606_"


def WriteToFileTestTorg(str1, e1, pluskatname):
    with open("d:\\vrem\\tt_"+pluskatname+"\\TestTorg_"+str(e1)+"_.txt", 'w', encoding='UTF-8',) as outfile:
        outfile.write(str1)

def MasivToString(massivpar):
    str1=''
    for i in massivpar:
        str1=str1+i+'$ '
    return str1

def SbrosVFile(bl, e1, str_ppprm, pluskatname):
        # all
        # str1=str(5)+" \n"
        str1=str(float(bl._summ))+" \n"
        for i in bl._prm:
            str1=str1+i+', '
        # for i in bl._ppprm:
        #     str1=str1+i+', '
        str1=str(float(bl._summ))+str1+" \n"+str_ppprm
        # print(str1)
        WriteToFileTestTorg(str1, e1, pluskatname)
        # # prognoz procent
        # str1="Procent and Prognoz\n"
        # for i in  range(0, len(bl._cm)):
        #     str1=small.adder(str1, bl._cm[i], ",", bl._cm_pohoj_proc[i], ",", bl._cm_pohoj_prog[i], "\n")
        # # print(str1)
        # WriteToFileTestTorg(str1, 1000+e1)

def GeneratorProcentMassive(lernsize, endtime, birja, days, plusnammassive, periodh):
    zc=zapolnalka_class( 10, 80)
    zc._debug=False
    zc._debug2=False
    rm, upm, dounm=zc.CreateMassiveToLernSex(birja, lernsize, days, endtime, plusnammassive)
    ob=Obuchalka_class_606(20, "model_sex_900_606", plusnammassive, zc._debug)
    ob.ProytiObouchenie(rm, upm, dounm, True, birja,  periodh)
    ob.ProytiObouchenie(rm, upm, dounm, False, birja,  periodh)

def TestTorg(birja, debugf, Test5):
    if birja=='finam':
        # ok  5
        epoch=8
        # ok 5-30
        days=30
        # ok 1
        shag=1
        # ok 1000
        maxcoins=1000
        # ok True
        obnovlaemPM=True
        # _IndexNastroeniya ok 1
        IndexNastroeniya=1
        # strat
        Strat_BigDoun=False
        Strat_BigDoun_Size=2.5
        Strat_Tolko_BNB = False
        Strat_Standart = True
        XMul=0.0005
        XMinOut=0.9
    else:       # CRYPTA
        # ok  5
        epoch=8
        # ok 5-30
        days=30
        # ok 1
        shag=1
        # ok 1000
        maxcoins=1000
        # ok True
        obnovlaemPM=True
        # _IndexNastroeniya ok 1
        IndexNastroeniya=1
        # strat
        Strat_Tolko_BNB=True
        Strat_Standart=False
        Strat_BigDoun=False
        Strat_BigDoun_Size=2.5
        XMul=0.04
        XMinOut=0.4
    procenthiscorrectplus=0
    if Test5: print("Играем по програмным настройкам!")
    else: print("Играем по РЕАЛЬНЫМ настройкам!")
    sleep(5)
    # clear
    for e1 in range(0,epoch):
        WriteToFileTestTorg("No no info", e1, birja)
    #
    plusnammassive='test55plusname'
    #
    small.SetAlgoName('Algo_606_'+birja)

    # ---------------  ВРЕМЯ до 13.02.2024
    bigt0=1707819963913-18*24*60*60*1000
    # ---------------  # now
    bigt0=int(round(time.time() * 1000))-days*24*60*60*1000
    # bigt0=int(round(time.time() * 1000))-days*24*60*60*1000-days*24*60*60*1000
    # ---------------  ВРЕМЯ
    bigt0=int(round(time.time() * 1000))
    # -------------------------------FOR -----------------------------------------------
    for e1 in range(0,epoch):
        str_ppprm = ''
        t0=bigt0
        ot=t0-days*24*60*60*1000
        bigt0=ot-2*60*60*1000
        #bl=bloha_606(birja, periodh, debugf, plusnammassive)
        bl=bloha_up_doun_606(None,  None, birja, debugf, '', Test5)
        bl.SetStopLoss(0)
        bl.InitStratRukami(Strat_Standart, Strat_BigDoun, Strat_BigDoun_Size, Strat_Tolko_BNB, XMul, XMinOut, procenthiscorrectplus)
        # bl._Strat_Standart=Strat_Standart
        # bl._Strat_BigDoun=Strat_BigDoun
        # bl._Strat_BigDoun_Size=Strat_BigDoun_Size
        while len(bl._cm) > maxcoins:
            bl._cm.pop()
        ostalos=0
        nextforsave=0
        oldot=0
        next55=0
        while True:
            # comments sbros to buffer
            nextforsave+=1
            porasbrosit = True if nextforsave%(max(1, int(30/shag)))==0 else False
            # пропускаем уже отработанные периоды (-1 с начала)
            if e1 > -1:
                if porasbrosit:
                    str_ppprm=str_ppprm+MasivToString(bl._ppprm)
                    bl._ppprm=[]        # освободим массив чтоб меньше тормозил
                    SbrosVFile(bl, e1, str_ppprm, birja)
                if ot==1705907763913:
                    dcdr=0
                bl._IndexNastroeniya=IndexNastroeniya
                bl.PrintInfo(ot)
                print("Ostalos "+str(ostalos)+" h. Epoch "+str(epoch-e1-1))
                bl.Go(ot)
                
            ot=ot+shag*5*60*1000
            ostalos=round((t0-ot)/(1*60*60*1000))
            if ostalos <= 0:
                break
        # продажа остатков
        if bl._coin != None:
            bl.DebComm("\nProdaja ostatkov")
            bl.SellCoin(ot)
        # print
        str_ppprm=str_ppprm+MasivToString(bl._ppprm)
        SbrosVFile(bl, e1, str_ppprm, birja)
        #play
        small.PlaySSSSSSSSSSS(True)
    

TestTorg('bybit', False, False)
# TestTorg('binanceusdt', False)
# TestTorg('okx', False)
# TestTorg('finam', False)
