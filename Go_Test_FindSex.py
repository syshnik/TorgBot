

from __future__ import print_function
from datetime import datetime 
import random
import small
import db
# from iireshalka import iireshalkaclass
from iireshalka_606 import iireshalkaclass_0_606
from iireshalka_606 import iireshalkaclass_606
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
import simpleaudio as simple_audio 
import time

import simplejson
from iimodels import model_900_606
import  iimodels 

from iiobuchalka_606 import Obuchalka_606
# from iihshar import hshar
# from iihshar_606 import hshar_900_606
# from wold_ii_bloha_606 import bloha_606
from zapolnalka import zapolnalka_class
from obuchalka_606 import Obuchalka_class_606
import GetBLSrypt
from ii_bloha_up_doun_606 import bloha_up_doun_606

Global_plusname = "_606_"
bl=None

def WriteToFileTestTorg(str1, e1):
    with open("d:\\vrem\\TestFindSex_"+str(e1)+"_.txt", 'w', encoding='UTF-8',) as outfile:
        outfile.write(str1)

# def SbrosVFile(bl, e1):
#         # all
#         # str1=str(5)+" \n"
#         str1=str(float(bl._summ))+" \n"
#         for i in bl._prm:
#             str1=str1+i+', '
#         for i in bl._ppprm:
#             str1=str1+i+', '
#         # print(str1)
#         WriteToFileTestTorg(str1, e1)
#         # prognoz procent
#         str1="Procent and Prognoz\n"
#         for i in  range(0, len(bl._cm)):
#             str1=small.adder(str1, bl._cm[i], ",", bl._cm_pohoj_proc[i], ",", bl._cm_pohoj_prog[i], "\n")
#         # print(str1)
#         WriteToFileTestTorg(str1, 1000+e1)

def TestFindSex(birja, debugf):
    # ok  1
    epoch=1
    # ok 15
    days=15
    # ok 1
    shag=1
    # ok 1000
    maxcoins=500
    # sikokodannih ok 10000000
    sikokodannih=500
    # ok False
    debug1, debug2=False, False
    #debug1, debug2=True, True
    #---------------------------------------
    # clear
    for e1 in range(0,epoch):
        WriteToFileTestTorg("No no info", e1)
    #
    small.SetAlgoName('Algo_606_'+birja)
    periodh=small.GetPeriod()
    # ---------------  ВРЕМЯ до 13.02.2024
    bigt0=1707819963913-18*24*60*60*1000
    # ---------------  # now
    bigt0=int(round(time.time() * 1000))-1*60*60*1000
    # ---------------  # now
    bigt0=int(round(time.time() * 1000))-days*24*60*60*1000
    bigt0=int(round(time.time() * 1000))-2*days*24*60*60*1000
    # ---------------  ВРЕМЯ
    # -------------------------------FOR -----------------------------------------------
    conn=db.GetConnect()
    cursor = conn.cursor()
    for e1 in range(0,epoch):
        str1=''
        # создание массива для обучения и обучение
        if False:
            zc=zapolnalka_class( 10, 80)
            zc._debug=False
            zc._debug2=False
            rm, upm, dounm=zc.CreateMassiveToLernSex(birja, 1000, days, t0, 'test55plusname')
            ob=Obuchalka_class_606(20, "model_sex_900_606", 'test55plusname', zc._debug)
            ob.ProytiObouchenie(rm, upm, dounm, True, birja,  periodh)
            ob.ProytiObouchenie(rm, upm, dounm, False, birja,  periodh)
        # заполнение массива данных и печать всех характеристик        
        if True:
            bl=bloha_up_doun_606(None, None,  birja, False, '', False)
            #bl=GetBLSrypt.GetBL(None, birja, bigt0)
            zc=None
            if periodh==2: zc=zapolnalka_class( 10, 80)
            if periodh==8: zc=zapolnalka_class( 8*60, 48*60)
            zc._debug=debug1
            zc._debug2=debug2
            df=zc.PodsgotovkaDannih(birja, sikokodannih, days, -2, 2, bigt0, True)
            #df=df.sort_index(ascending=False)
            for i, row in df.iterrows():
                print(f"Index: {i}")
                print(f"{row}\n")
                id=row['id']
                p1=bl.GetPrognoz( row['coin'], row['id'], None, False, False)
                if p1 is not None:
                    id=row['id']
                    str11=row['coin']+", "+str(round(row['proc'], 2))+"% -------,"+str(id)+","+" -------,"+str(row['date'])+",\n"
                    str2=p1.GetDebugInfo(id, id, bl._Strat_Standart, bl._Strat_BigDoun, bl._Strat_BigDoun_Size, bl._Strat_Tolko_BNB, bl._XMul, bl._XMinOut, 0)
                    str1=str1+str11+str2
                cf=0
        # print
        WriteToFileTestTorg(str1, 1000+e1)
        #play
        small.PlaySSSSSSSSSSS(True)
        bigt0=bigt0-days*24*60*60*1000
    conn.commit()
    conn.close()
    

TestFindSex('finam', False)
# TestFindSex('okx', False)
# TestFindSex('bybit', False)
# TestFindSex('binanceusdt', False)
