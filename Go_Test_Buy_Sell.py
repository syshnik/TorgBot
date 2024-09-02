

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
from zapolnalka import zapolnalka_class 
from ii_bloha_up_doun_606 import bloha_up_doun_606
from ii_bloha_up_doun_606_run import bloha_up_doun_606_run
from orders_606 import ordersclass_606
from dbuse import dbuse
Global_plusname = "_606_"
import timerazn
from birja_bybit import birja_bybit_class
from birja_finam import birja_finam101_class
from sms_obmen_base import sms_obmen_base_class
from wallet import walletclass 

_Gl_showcoins=False
nextfortime=0
exceptsikoko=0
OKXTimeRazn=0
BybitTimeRazn=0
BinanceTimeRazn=0
SikokoSpim=0
_LastRunTime=0

def SmeshenieVremeni():
    #смещение для локального определения времени

    global nextfortime
    global exceptsikoko
    global OKXTimeRazn
    global BybitTimeRazn
    global BinanceTimeRazn
    global SikokoSpim
    global _LastRunTime

    if nextfortime % 100 == 0:
        OKXTimeRazn, BybitTimeRazn, BinanceTimeRazn = timerazn.CalcTimeRazn()
        nextfortime=0
    nextfortime=nextfortime+1
    print('exceptsikoko = '+str(exceptsikoko)+'  time '+str(time.gmtime()))


def OrderOpenClose(birja):
    global nextfortime
    global exceptsikoko
    global OKXTimeRazn
    global BybitTimeRazn
    global BinanceTimeRazn
    global SikokoSpim
    global _LastRunTime
    global _Gl_showcoins
    
    d1=dbuse(None, None)
    # Флаг что занят
    db.AddUpdate_peremenniye_AndCursor(d1.GetCursor(), d1.GetConn(), "work_in_606_"+birja, "True")
    # заходим 
    bstr=' and birja=\''+birja+'\' '
    order=ordersclass_606(d1.GetCursor(), d1.GetConn(), SikokoSpim, OKXTimeRazn, BybitTimeRazn, BinanceTimeRazn, bstr)
    bloha=bloha_up_doun_606_run(d1.GetCursor(), d1.GetConn(), order, birja, False, _Gl_showcoins)
    # correct
    order.CorrectBadClosedOrders()
    # go
    if _LastRunTime == 0:
        _LastRunTime = int(round(time.time() * 1000))
    # input
    bloha.Go(_LastRunTime)
    bloha.PrintInfo(_LastRunTime)
    # output
    bloha.Go(_LastRunTime)
    bloha.PrintInfo(_LastRunTime)
    # Флаг что не  занят
    db.AddUpdate_peremenniye_AndCursor(d1.GetCursor(), d1.GetConn(), "work_in_606_"+birja, "False")


## go go go go go go go go go go go go go go go go go go go go go go go go go go go go go go go go
if False:
    small.SetAlgoName('Algo_606_'+'bybit')
    SmeshenieVremeni()
    OrderOpenClose('binanceusdt')
if False:
    small.SetAlgoName('Algo_606_'+'bybit')
    sb = sms_obmen_base_class(None, None)
    sb.SendMess_Buy_Sell_Short_Long(60*10000, 'bybit', 'BNB',  True, False, True, False)
    b1 = b1=birja_bybit_class(None, None, 'bybit', 11, 'BNB',  'USDT', 1, 0)
    b1.BySellCoin(1, 'BNB', False, 1, False, 3, True)
if False:
    small.SetAlgoName('Algo_606_'+'finam'+'_simulgame')
    w1=walletclass('finam' , 0)
    w1.ClearForOrder(1)
    w1.UpdateCoin('RUB', 10000)
    w1.UpdateCoin('SBER', 0)
    b1 = b1=birja_finam101_class(None, None, 'finam', 1, 'SBER',  'RUB', 1, 0)
    b1.BySellCoin(1, 'SBER', False, 10000, False, 3)
    b1.BySellCoin(1, 'SBER', True, 10000, False, 3)
    gg=9

if False:
    # класс биржи. покупка продажа через смс
    small.SetAlgoName('Algo_606_'+'finam'+'_smsgame')
    b1 = b1=birja_finam101_class(None, None, 'finam', 1, 'SBER',  'RUB', 1, 0)
    sb = sms_obmen_base_class(None, None)
    sb.OrMess('finam', 'SBER', None, sb.StatusZavershen())
    okin=b1.BySellCoin(1, 'SBER', False, 10000, False, 3)
    okuot=b1.BySellCoin(1, 'SBER', True, 10000, False, 3)
    gg=9


if False:
    # покупка продажа через смс с ордерами
    small.SetAlgoName('Algo_606_'+'finam'+'_smsgame')
    d1=dbuse(None, None)
    bstr=' and birja=\'finam\' '
    order=ordersclass_606(d1.GetCursor(), d1.GetConn(), SikokoSpim, 0, bstr)
    bloha=bloha_up_doun_606_run(d1.GetCursor(), d1.GetConn(), order, 'finam', False, True)
    # correct
    order.CorrectBadClosedOrders()
    sb = sms_obmen_base_class(None, None)
    sb.OrMess('finam', 'SBER', None, sb.StatusZavershen())
    # bs
    rows=d1.GetSell("SELECT max(id) from finam_ozon ")
    # milliseconds = int(round(time.time() * 1000))
    milliseconds = int(small.GetCorrectOneFloatNoteFromRowsAsOne(rows))
    bloha.Go(milliseconds)
    gg=0

if True:
    # покупка продажа с ордерами
    small.SetAlgoName('Algo_606_'+'finam'+'_simulgame')
    d1=dbuse(None, None)
    bstr=' and birja=\'finam\' '
    order=ordersclass_606(d1.GetCursor(), d1.GetConn(), SikokoSpim, 0, bstr)
    bloha=bloha_up_doun_606_run(d1.GetCursor(), d1.GetConn(), order, 'finam', False, True)
    # correct
    order.CorrectBadClosedOrders()
    # bs
    milliseconds = int(round(time.time() * 1000)) - 2*24*60*60*1000
    bloha.Go(milliseconds)
    gg=0


