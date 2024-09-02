

# from __future__ import print_function
# from datetime import datetime 
# import random
# import small
# import db
# from iireshalka_606 import iireshalkaclass_0_606
# from iireshalka_606 import iireshalkaclass_606
# from obuchalka_606 import Obuchalka_class_606
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# from torch.autograd import Variable
# import matplotlib.pyplot as plt                              # построение графиков
# print(torch.cuda.is_available()) # Should print True
# from time import sleep
# import array as arr 
# import torch.optim as optim
# import numpy as np
# import simpleaudio as simple_audio 
# import time
# import load_price

# import simplejson
# from iimodels import model_900_606
# import  iimodels 

# from iiobuchalka_606 import Obuchalka_606
# # from iihshar import hshar
# # from iihshar_606 import hshar_900_606
# # from wold_ii_bloha_606 import bloha_606
# from zapolnalka import zapolnalka_class 
# import shutil
# from zapolnalkaprobelov import zapolnalka_probelov_class

# Global_plusname = "_606_"


# def GeneratorProcentMassive(epoch,lernsize, endtime, birja, days, plusnammassive, periodh, debug, debug2):
#     zc=zapolnalka_class( 10, 80)
#     zc._debug, zc._debug2=debug, debug2
#     rupm, upm, rdounm, dounm=zc.CreateMassiveToLernOutInputUpDoun(birja, lernsize, days, endtime, plusnammassive)
#     ob=Obuchalka_class_606(epoch, "model_inputdoun_outup_900_606", plusnammassive, zc._debug)
#     ob.ProytiObouchenieOneVector(rupm, upm, True, birja,  periodh)
#     ob.ProytiObouchenieOneVector(rdounm, dounm, False, birja,  periodh)

# def MakeModel(birja):
#     # ok 2
#     period=2
#     # ok 25
#     epoch=25
#     # ok 700
#     dayslern=3
#     # ok 1000
#     maxcoins=1000
#     # ok 1500000 использует только "up or doun" и реальный размер будет сильно меньше 
#     lernsize=150
#     # ok False
#     debug, debug2, debugtime = False, False, False
#     debug, debug2, debugtime = True, True, True
#     # ---------------------------------------------
#     if debug  or debug2 or debugtime:
#         plusnammassive='test_vr_'
#     else:
#         plusnammassive=''
#     # if debugtime:
#     #     # ТЕКУЩЕЕ ВРЕМЯ С НЕБОЬШИМ ОТСТУПОМ
#     #     milliseconds = int(round(time.time() * 1000)) - 24*60*60*1000
#     # else:
#     #     # все обновим
#     #     while True:
#     #         sik1, sik2=load_price.AddPricesNewOrOld(True, birja, '', '', None)
#     #         if sik1 == 0 and sik2 == 0: break
#     #     # ТЕКУЩЕЕ ВРЕМЯ С НЕБОЬШИМ ОТСТУПОМ
#     #     milliseconds = int(round(time.time() * 1000)) - 2*5*60*1000
#     # ТЕКУЩЕЕ ВРЕМЯ С НЕБОЬШИМ ОТСТУПОМ
#     milliseconds = int(round(time.time() * 1000)) - 24*60*60*1000
#     GeneratorProcentMassive(epoch, lernsize, milliseconds, birja, dayslern, plusnammassive, period, debug, debug2)

# def GetStrTime():
#     dt=datetime.now()
#     date_time = dt.strftime("%m.%d.%Y, %H:%M")
#     return date_time

# bm=['okx']
# bm=['bybit',  'binanceusdt']
# bm=['binanceusdt']
# bm=['bybit']
# #bm=['finam']
# next55=0
# # ------------------
# while True:
#     next55+=1
#     dt=datetime.now()
#     # время старта
#     if True:        #dt.hour==1 and dt.minute > 11 and dt.minute < 22:
#         # делаем модели ии
#         for birja in bm:
#             t1=GetStrTime()
#             small.SetAlgoName('Algo_606_'+birja)
#             MakeModel(birja)
#             t2=GetStrTime()
#             db.PrintInfoToComments(None, small.GetAlgoName(), "Ok. PodsgotovkaDannih for sex model for "+birja+".  "+t1+" - "+t2)  
#             try:
#                 gy=0
#             except:
#                 db.PrintInfoToComments(None, small.GetAlgoName(), "Error 433564. PodsgotovkaDannih for sex model for "+birja+".  "+GetStrTime())  
#         # # дополним бракованные монеты
#         # try:
#         #     zpc=zapolnalka_probelov_class()
#         #     str1=zpc.Run()
#         #     db.PrintInfoToComments(None, small.GetAlgoName(), "Ok. PodsgotovkaDannih. Del Brak. "+str1+" "+ GetStrTime())  
#         # except:
#         #     db.PrintInfoToComments(None, small.GetAlgoName(), "Error 3256785. PodsgotovkaDannih. Del Brak. "+ GetStrTime())  
#     else:
#         print('Obnovlenie modeley otlojeno. '+str(next55))
#         sleep(60)
#     break
