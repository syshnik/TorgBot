

from __future__ import print_function
from datetime import datetime 
import random
import small
import db
from iireshalka_606 import iireshalkaclass_0_606
from iireshalka_606 import iireshalkaclass_606
from obuchalka_606 import Obuchalka_class_606
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import matplotlib.pyplot as plt                              # построение графиков
print(torch.cuda.is_available()) # Should print True
from time import sleep
import array as arr 
import torch.optim as optim
import numpy as np
# import simpleaudio as simple_audio 
import time
import load_price

import simplejson
from iimodels import model_900_606
import  iimodels 

from iiobuchalka_606 import Obuchalka_606
# from iihshar import hshar
# from iihshar_606 import hshar_900_606
# from wold_ii_bloha_606 import bloha_606
from zapolnalka import zapolnalka_class 
import shutil
# from zapolnalkaprobelov import zapolnalka_probelov_class

Global_plusname = "_606_"


def GeneratorProcentMassive(epoch,lernsize, endtime, birja, days, plusnammassive, periodh, debug, debug2, FCreateMassiv, FObchenie):
    if np.isnan(np.inf) != False:
        print('Errorr 665555')
        small.ifnoterr(1==7)
    zc=zapolnalka_class( 10*periodh/2, 80*periodh/2)
    zc._debug, zc._debug2=debug, debug2
    rmname="D:/BS/Save/WORK/Programm/bi/ii/ShortVector"+Global_plusname+str(periodh)+"_"+birja+"_rm.pt"
    vmname="D:/BS/Save/WORK/Programm/bi/ii/ShortVector"+Global_plusname+str(periodh)+"_"+birja+"_vm.pt"
    if FCreateMassiv:
        rm, vm=zc.CreateMassiveToLernShortVector(birja, lernsize, days, endtime, plusnammassive, periodh)
        torch.save(rm, rmname)
        torch.save(vm, vmname)
    if FObchenie:
        rm=torch.load(rmname)
        vm=torch.load(vmname)
        ob=Obuchalka_class_606(epoch, "model_short_vector_900_606", plusnammassive, zc._debug)
        ob.ProytiObouchenieOneVector(rm, vm, None, birja,  periodh)

def MakeModel(birja):
    # ok 2-24
    period=24
    #if birja=='finam': period=8
    # ok  27
    epoch=27
    # ok     700
    dayslern=700
    # ok     500000
    lernsize=500000
    # ok                       False, False, False
    debug, debug2, debugtime = False, False, False
    # debug, debug2, debugtime = True, True, True
    # ok                       True, True
    FCreateMassiv, FObchenie = True, True
    # ---------------------------------------------
    if debug  or debug2 or debugtime:
        plusnammassive='test_vr_'
    else:
        plusnammassive=''
    # if debugtime:
    #     # ТЕКУЩЕЕ ВРЕМЯ С НЕБОЬШИМ ОТСТУПОМ
    #     milliseconds = int(round(time.time() * 1000)) - 24*60*60*1000
    # else:
    #     # все обновим
    #     while True:
    #         sik1, sik2=load_price.AddPricesNewOrOld(True, birja, '', '', None)
    #         if sik1 == 0 and sik2 == 0: break
    #     # ТЕКУЩЕЕ ВРЕМЯ С НЕБОЬШИМ ОТСТУПОМ
    #     milliseconds = int(round(time.time() * 1000)) - 2*5*60*1000
    # ТЕКУЩЕЕ ВРЕМЯ С НЕБОЬШИМ ОТСТУПОМ
    milliseconds = int(round(time.time() * 1000)) - 24*60*60*1000
    GeneratorProcentMassive(epoch, lernsize, milliseconds, birja, dayslern, plusnammassive, period, debug, debug2, FCreateMassiv, FObchenie)

def GetStrTime():
    dt=datetime.now()
    date_time = dt.strftime("%m.%d.%Y, %H:%M")
    return date_time

bm=['okx']
bm=['bybit',  'binanceusdt']
bm=['binanceusdt', 'okx']
bm=['bybit']
bm=['binanceusdt', 'bybit', 'okx']
next55=0
bm=['finam']
bm=['bybit']
# ------------------
while True:
    next55+=1
    dt=datetime.now()
    # время старта
    if True:        #dt.hour==1 and dt.minute > 11 and dt.minute < 22:
        # делаем модели ии
        for birja in bm:
            t1=GetStrTime()
            small.SetAlgoName('Algo_606_'+birja)
            MakeModel(birja)
            t2=GetStrTime()
            #db.PrintInfoToComments(None, small.GetAlgoName(), "Ok. PodsgotovkaDannih for sex model for "+birja+".  "+t1+" - "+t2)  
            try:
                gy=0
            except:
                gg=0
                #db.PrintInfoToComments(None, small.GetAlgoName(), "Error 433564. PodsgotovkaDannih for sex model for "+birja+".  "+GetStrTime())  
        # # дополним бракованные монеты
        # try:
        #     zpc=zapolnalka_probelov_class()
        #     str1=zpc.Run()
        #     db.PrintInfoToComments(None, small.GetAlgoName(), "Ok. PodsgotovkaDannih. Del Brak. "+str1+" "+ GetStrTime())  
        # except:
        #     db.PrintInfoToComments(None, small.GetAlgoName(), "Error 3256785. PodsgotovkaDannih. Del Brak. "+ GetStrTime())  
    else:
        print('Obnovlenie modeley otlojeno. '+str(next55))
        sleep(60)
    break
