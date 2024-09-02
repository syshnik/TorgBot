

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
# import simpleaudio as simple_audio 
import time

import simplejson
from iimodels import model_900_606
import  iimodels 

from iiobuchalka_606 import Obuchalka_606
# from iihshar import hshar
# from iihshar_606 import hshar_900_606
#from ii_bloha_606 import bloha_606
from ii_bloha_up_doun_606 import bloha_up_doun_606
import os
import pandas as pd
#from ii_bloha_606  import bloha_stavka_606
from ii_bloha_stavka_606 import bloha_stavka_606
#import GetBLSrypt


Global_plusname = "_606_"

# def GetBL(oldbl, birja, starttime):
#     # иниц-ем 
#     # Указываем путь к директории
#     directory = "D:/BS/Save/WORK/Programm/bi/ii"
#     df=pd.DataFrame()
#     df['id']=0
#     # Получаем список файлов
#     files = os.listdir(directory)
#     for file in files:
#         s1='_test_'
#         s2='_okx_model_sex_900_606__up2.pt'
#         if file.find(s1) != -1 and file.find(s2) != -1:
#             str1=file.replace(s1, '')
#             str2=str1.replace(s2, '')
#             df.loc[len(df.index)] = [int(str2)]
#     df.sort_values(by='id', ascending=False)
#     df2=df.loc[(df['id'] < starttime)]
#     maxid=df2['id'].max()
#     #
#     plusname=small.GetPlusName223345656(maxid)
#     bl=None
#     try:
#         bl=bloha_606(birja, 2, False, plusname)
#         if oldbl is None:
#             oldbl=bl
#         else:
#             oldbl._sh=bl._sh
#             oldbl._sex_sh=bl._sex_sh
#     except:
#         print('Error 33337777')
#         gg=9/0
#     return oldbl



def TestIn(bl, sik , ret,  lostprofit, vminus, 	  regrdel, progshort , oknotok):
    sik+=1
    okprog=bl.GetInputProgWithConst(regrdel)
    if okprog < progshort and oknotok > 0:
        # правильно заходим
        ret+=1
    elif okprog > progshort and oknotok < 0:
        # не заходим и это правильно
        ret+=1
    else:
        if oknotok < 0:
            vminus+=1        # вабче не надо заходить
        else:
            lostprofit+=1
    
    
    return sik , ret,  lostprofit, vminus

def TestIn55Finam(birja,coin, starttime, momenttime, Strat_Standart, Strat_BigDoun, Strat_BigDoun_Size, Strat_Tolko_BNB, XMul, XMinOut, procenthiscorrectplus):
    small.SetAlgoName('Algo_606_'+birja)
    okinput, i6, okout=False, False, False
    #bl=GetBLSrypt.GetBL(None, birja, starttime)
    bl=bloha_up_doun_606(None, None, birja, False, '', True)
    bl.InitStratRukami(Strat_Standart, Strat_BigDoun, Strat_BigDoun_Size, Strat_Tolko_BNB, XMul, XMinOut, procenthiscorrectplus)
    sik, ret, lostprofit, vminus = 0, 0, 0, 0
    for  i in range(0, 100):
        x2=random.uniform(0.5, 1.14)
        inputprog = bl.GetInputProgWithConst(x2)
        print('for regdel ' +str(round(x2, 3))+', short is '+str(round(inputprog ,3)))
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		0.58417	 , 	0.8	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		0.61523	 , 	0.85	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		0.62982	 , 	0.8	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		0.66646	 , 	0.8	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		0.70023	 , 	0.85	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		0.91684	 , 	0.79	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		0.92854	 , 	0.78	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		0.97552	 , 	0.8	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		0.99583	 , 	0.78	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		0.9973	 , 	0.77	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		0.99841	 , 	0.77	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.01312	 , 	0.74	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.01662	 , 	0.73	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.01995	 , 	0.7	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.0218	 , 	0.75	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.02229	 , 	0.7	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.02387	 , 	0.69	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.02453	 , 	0.71	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.02505	 , 	0.69	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.02916	 , 	0.77	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.03013	 , 	0.66	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.03055	 , 	0.67	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.03139	 , 	0.68	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.03192	 , 	0.65	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.03369	 , 	0.65	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.03497	 , 	0.66	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.03553	 , 	0.65	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.03677	 , 	0.7	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.03789	 , 	0.67	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.03789	 , 	0.66	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.03791	 , 	0.65	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.04165	 , 	0.69	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.04456	 , 	0.65	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.04827	 , 	0.6	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.04912	 , 	0.61	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.04992	 , 	0.6	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.05294	 , 	0.67	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.05382	 , 	0.67	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.05412	 , 	0.61	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.06003	 , 	0.6	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.06159	 , 	0.63	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.06891	 , 	0.63	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.06946	 , 	0.75	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.0722	 , 	0.6	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.07437	 , 	0.61	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.07828	 , 	0.58	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.08643	 , 	0.6	 , 	-1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.09486	 , 	0.66	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.11104	 , 	0.69	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.11107	 , 	0.69	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.11107	 , 	0.68	 , 	1	)
    sik, ret, lostprofit, vminus = 	TestIn(	bl, sik, ret, lostprofit, vminus, 		1.1127	 , 	0.59	 , 	-1	)
    print('sik='+str(sik)+'  ret='+str(ret)+' lostprofit='+str(round(lostprofit, 3))+'  v minus='+str(round(vminus, 3)))
    return ret



def RunTest88(birja,coin, starttime, momenttime, Strat_Standart, Strat_BigDoun, Strat_BigDoun_Size, Strat_Tolko_BNB, XMul, XMinOut, procenthiscorrectplus):
    small.SetAlgoName('Algo_606_'+birja)
    okinput, i6, okout=False, False, False
    #bl=GetBLSrypt.GetBL(None, birja, starttime)
    bl=bloha_up_doun_606(None, None, birja, False, '', True)
    bl.InitStratRukami(Strat_Standart, Strat_BigDoun, Strat_BigDoun_Size, Strat_Tolko_BNB, XMul, XMinOut, procenthiscorrectplus)
    # stavka
    conn=db.GetConnect()
    cursor = conn.cursor()
    s1=bloha_stavka_606()
    # s1. Init2(cursor, birja, coin, starttime, 0,0)
    # s1=bl.GetPrognoz( coin, starttime, None, False,False)
    s1, ss1 = bl.GetPrognozLongShort(coin, starttime)
   # print(s1._ii.GetDebugInfoII())
    # buy
    if bl.ANadoVhodim(s1, starttime):
        bl.BuyCoin(s1, starttime)
        okinput=True
    else:
        bl.BuyCoin(s1, starttime)
        i6=True
    # sell
    #bl=GetBLSrypt.GetBL(bl, birja, starttime)
    #bl=bloha_up_doun_606(birja, 2, False, '')
    s1, ss1 = bl.GetPrognozLongShort(coin, momenttime)
    # s1=bl.GetPrognoz(coin,  momenttime, None, False, False)
    if bl.ANadoViiiiiiihodim( s1, False, True, momenttime, True):
        bl.SellCoin(momenttime)
        okout=True
    conn.commit()
    conn.close()
    cursor.close()
    return okinput,i6, okout
    
def RunTest8899(birja,coin, starttime, Strat_Standart, Strat_BigDoun, Strat_BigDoun_Size, Strat_Tolko_BNB, XMul, XMinOut, procenthiscorrectplus, test5=True):
    small.SetAlgoName('Algo_606_'+birja)
    okinput, i6, okout=False, False, False
    #bl=GetBLSrypt.GetBL(None, birja, starttime)
    bl=bloha_up_doun_606(None, None, birja, False, '', test5)
    bl.InitStratRukami(Strat_Standart, Strat_BigDoun, Strat_BigDoun_Size, Strat_Tolko_BNB, XMul, XMinOut, procenthiscorrectplus)
    # stavka
    conn=db.GetConnect()
    cursor = conn.cursor()
    s1=bloha_stavka_606()
    # s1. Init2(cursor, birja, coin, starttime, 0,0)
    # s1=bl.GetPrognoz(coin,  starttime, None, False, False)
    s1, ss1 = bl.GetPrognozLongShort(coin, starttime)
    # buy
    if bl.ANadoVhodim(s1, starttime):
        bl.BuyCoin(s1, starttime)
        okinput=True
    else:
        bl.BuyCoin(s1, starttime)
        i6=True
    # sell
    sum1=0
    for i in range(0, 1000):
        momenttime=starttime+i*5*60*1000
        #bl=GetBLSrypt.GetBL(bl,  birja, momenttime)
        #bl=bloha_up_doun_606(birja, 2, False, '')
        # s1=bl.GetPrognoz(coin,  momenttime, None,False, False)
        s1, ss1 = bl.GetPrognozLongShort(coin, momenttime)
        bl.CalcAndSaveProcentPlus(s1)
        price, proc, buytime=bl.GetPriceAndProcentAndBuyTime(momenttime)
        print(str(proc)+"$ID$"+str(momenttime))
        if s1 is not None:
            print(s1.GetDebugInfo(starttime, momenttime, bl._Strat_Standart, bl._Strat_BigDoun, bl._Strat_BigDoun_Size, bl._Strat_Tolko_BNB, bl._XMul, bl._XMinOut, bl._procenthiscorrectplus))
        if bl.ANadoViiiiiiihodim( s1, False, True, momenttime, True):
            bl.ANadoViiiiiiihodim( s1, False, True, momenttime, True)
            bl.SellCoin(momenttime)
            summ1=bl._summ
            break
    conn.commit()
    conn.close()
    cursor.close()
    return okinput, sum1, True

def RunTest77(order, Strat_Standart, Strat_BigDoun, Strat_BigDoun_Size, Strat_Tolko_BNB, XMul, XMinOut, procenthiscorrectplus):
    rows=db.GetSel77(None, "select kuplen,birja, coin from orders where id="+str(order))
    kuplen=rows[0][0]
    birja=rows[0][1]
    small.SetAlgoName('Algo_606_'+birja)
    coin=rows[0][2]
    kuplen1=int(kuplen.timestamp() )*1000     #  -10*60*1000
    kuplen1=int(kuplen1-(kuplen1%(5*60*1000)))
    tnow=int(round(time.time() * 1000))
    ot=kuplen1
    RunTest8899(birja,	coin,	kuplen1, Strat_Standart, Strat_BigDoun, Strat_BigDoun_Size, Strat_Tolko_BNB, XMul, XMinOut, procenthiscorrectplus, False)

def PrinrErrorOrOk(out, okinput, okout, proc):
    if okinput: 
        out+=out*proc/100
        print('ok')
    else:
        print('error')
    return out

def ControlRun():
    out=10
    okinput,i6, okout = RunTest88('finam','TRMK',1704396620029,1704442820029, True, False, 2.5, 0.0005, 0.9, 0.3428036925798655) 
    out=PrinrErrorOrOk(out, okinput, okout, 2)
    okinput,i6, okout = RunTest88('finam','SNGSP',1711697420029,1711729820029, True, False, 2.5, 0.0005, 0.9, 0.7063938224694413) 
    out=PrinrErrorOrOk(out, okinput, okout, 2)
    okinput,i6, okout = RunTest88('finam','MVID',1709822120029,1710144920029, True, False, 2.5, 0.0005, 0.9, 0.0693550980091095) 
    out=PrinrErrorOrOk(out, okinput, okout, 3)
    okinput,i6, okout = RunTest88('finam','POLY',1709144720029,1709152220029, True, False, 2.5, 0.0005, 0.9, 0) 
    out=PrinrErrorOrOk(out, okinput, okout, 2)
    okinput,i6, okout = RunTest88('finam','GLTR',1705069993527,1705070593527, True, False, 2.5, 0.0005, 0.9, 0) 
    out=PrinrErrorOrOk(out, okinput, okout, 4)
    okinput,i6, okout = RunTest88('finam','MVID',1709822293527,1709824393527, True, False, 2.5, 0.0005, 0.9, 0) 
    out=PrinrErrorOrOk(out, okinput, okout, 4)
    okinput,i6, okout = RunTest88('finam','MTLR',1703184767038,1703230967038, True, False, 2.5, 0.0005, 0.9, 0)     
    out=PrinrErrorOrOk(out, okinput, okout, 2)
    print(str(round(out, 2)))
#################################
okinput,i6, okout = RunTest8899('bybit','BNB',1710481258405, False, False, 2.5, True, 0.04, 0.4, 0.02159288227558136) 
okinput,i6, okout = RunTest88('bybit','BNB',1710481258405,1710482458405, False, False, 2.5, True, 0.04, 0.4, 0.02159288227558136) 
okinput,i6, okout = RunTest8899('bybit','BNB',1720152024001, False, False, 2.5, True, 0.04, 0.4, 0.06204789318412543) 
okinput,i6, okout = RunTest88('bybit','BNB',1720152024001,1720187724001, False, False, 2.5, True, 0.04, 0.4, 0.06204789318412543) 

okinput,i6, okout = RunTest88('bybit','BNB',1718711313782,1718784213782, False, False, 2.5, True, 0.04, 0.4, 0.0108007550239563) 
okinput,i6, okout = RunTest88('bybit','BNB',1718711313782,1718780613782, False, False, 2.5, True, 0.04, 0.4, 0.0033775269985198975) 
okinput,i6, okout = RunTest88('bybit','BNB',1718711313782,1718717313782, False, False, 2.5, True, 0.04, 0.4, 0) 
okinput,i6, okout = RunTest88('bybit','BNB',1718717313782,1718717313782, False, False, 2.5, True, 0.04, 0.4, 0) 
okinput,i6, okout = RunTest88('bybit','BNB',1718711313782,1718780613782, False, False, 2.5, True, 0.04, 0.4, 0.0033775269985198975) 
okinput,i6, okout = RunTest88('bybit','BNB',1718218713782,1718259213782, False, False, 2.5, True, 0.04, 0.4, 0) 
okinput,i6, okout = RunTest88('bybit','BNB',1718218713782,1718258013782, False, False, 2.5, True, 0.04, 0.4, 0) 
okinput,i6, okout = RunTest88('bybit','BNB',1720097555774,1720164155774, False, False, 2.5, True, 0.04, 0.4, 0) 
okinput,i6, okout = RunTest88('finam','RUAL',1713165384522,1713186084522, True, False, 2.5, False, 0.0005, 0.9, 0.04472780227661133) 
okinput,i6, okout = RunTest8899('finam','RUAL',1713165384522, True, False, 2.5, False, 0.0005, 0.9, 0.04472780227661133) 
okinput,i6, okout = RunTest88('finam','RNFT',1712581284522,1712646384522, True, False, 2.5, False, 0.0005, 0.9, 675.0769390230689) 
okinput,i6, okout = RunTest88('finam','RNFT',1712581284522,1712609184522, True, False, 2.5, False, 0.0005, 0.9, 613.6357533448856) 
okinput,i6, okout = RunTest88('finam','AFLT',1712041709022,1712128709022, True, False, 2.5, False, 0.0005, 0.9, 0.026293104887008666) 
okinput,i6, okout = RunTest8899('finam','AFLT',1712041709022, True, False, 2.5, False, 0.0005, 0.9, 0.026293104887008666) 
okinput,i6, okout = RunTest88('finam','AGRO',1699464833257,1699547033257, True, False, 2.5, False, 0.0005, 0.9, 0.009354570508003235) 
okinput,i6, okout = RunTest8899('finam','AGRO',1699464833257, True, False, 2.5, False, 0.0005, 0.9, 0.009354570508003235) 
okinput,i6, okout = RunTest88('finam','AGRO',1697543333257,1697547533257, True, False, 2.5, False, 0.0005, 0.9, 0.017735302448272705) 
okinput,i6, okout = RunTest88('finam','QIWI',1705695533257,1705695833257, True, False, 2.5, False, 0.0005, 0.9, 0) 
okinput,i6, okout = RunTest88('finam','QIWI',1709660464162,1709712064162, True, False, 2.5, False, 0.0005, 0.9, 0) 
okinput,i6, okout = RunTest88('finam','QIWI',1709031364162,1709031664162, True, False, 2.5, False, 0.0005, 0.9, 0) 
okinput,i6, okout = RunTest88('finam','QIWI',1710237964162,1710238264162, True, False, 2.5, False, 0.0005, 0.9, 0) 
okinput,i6, okout = RunTest88('finam','QIWI',1709660464162,1709660764162, True, False, 2.5, False, 0.0005, 0.9, 0) 
okinput,i6, okout = RunTest88('finam','OZON',1709639464162,1709643364162, True, False, 2.5, False, 0.0005, 0.9, 0.40188296030399967) 
okinput,i6, okout = RunTest88('finam','QIWI',1715002890895,1715015190895, True, False, 2.5, False, 0.0005, 0.9, 0.007604572176933288) 
okinput,i6, okout = RunTest8899('finam','QIWI',1716968710465, True, False, 2.5, False, 0.0005, 0.9, 0.028799933195114136) 
okinput,i6, okout = RunTest88('finam','RUAL',1712133310465,1712238910465, True, False, 2.5, False, 0.0005, 0.9, 15.235643278425536)
okinput,i6, okout = RunTest8899('finam','RUAL',1712133310465, True, False, 2.5, False, 0.0005, 0.9, 0.035859203338623045) 
okinput,i6, okout = RunTest8899('finam','AFLT',1715677210465, True, False, 2.5, False, 0.0005, 0.9, 0.01029142141342163) 
okinput,i6, okout = RunTest88('finam','AFLT',1715677210465,1715763610465, True, False, 2.5, False, 0.0005, 0.9, 0.01029142141342163) 
okinput,i6, okout = RunTest88('finam','SOFL',1712942247479,1713169047479, True, False, 2.5, False, 0.0005, 0.9, 0.015363398194313049) 
okinput,i6, okout = RunTest88('finam','ASTR',1711621947479,1711649547479, True, False, 2.5, False, 0.0005, 0.9, 0) 
# вялый много предупреждений 
okinput,i6, okout = RunTest88('finam','AFKS',1710414747479,1710854547479, True, False, 2.5, False, 0.0005, 0.9, 3.0370466294785077) 
okinput,i6, okout = RunTest8899('finam','AFKS',1710414747479, True, False, 2.5, False, 0.0005, 0.9, 3.0370466294785077) 
ff=7/0
okinput,i6, okout = RunTest88('bybit','BNB',1718875800000,1718892300000, False, False, 1, True, 0.04, 0.4, 0)
okinput,i6, okout = RunTest88('finam','QIWI',1717075313775,1717086713775, True, False, 2.5, False, 0.0005, 0.9, 0) 
RunTest77(6933, False, False, 1, True, 0.04, 0.4, 0.35943734512347303) 
ff=0
# okinput,i6, okout = RunTest88('finam','AFKS',1716543212547,1716556712547, True, False, 2.5, False, 0.0005, 0.9, 0.03110470917820931) 
# okinput,i6, okout = RunTest88('finam','AFKS',1716543212547,1716554312547, True, False, 2.5, False, 0.0005, 0.9, 0.017483655810356137) 
# okinput,i6, okout = RunTest88('bybit','BNB',1717641561212,1717685961212, False, False, 2.5, True, 0.04, 0.4, 912.680171205323) 
# okinput,i6, okout = RunTest88('bybit','BNB',1717641561212,1717663161212, False, False, 2.5, True, 0.04, 0.4, 0.35943734512347303) 
# okinput,i6, okout = RunTest88('bybit','BNB',1717425561212,1717490061212, False, False, 2.5, True, 0.04, 0.4, 2.8810180045123017)
# okinput,i6, okout = RunTest8899('bybit','BNB',1717425561212, False, False, 2.5, True, 0.04, 0.4, 0.03145313858985901) 
# okinput,i6, okout = RunTest88('bybit','BNB',1717425561212,1717482861212, False, False, 2.5, True, 0.04, 0.4, 0.03145313858985901) 
# okinput,i6, okout = RunTest88('bybit','BNB',1717162461212,1717396761212, False, False, 2.5, True, 0.04, 0.4, 0.15503917833030229) 
# okinput,i6, okout = RunTest88('bybit','BNB',1715696630790,1715779730790, False, False, 2.5, True, 0.04, 0.4, 0.013644790649414063) 
# okinput,i6, okout = RunTest88('bybit','BNB',1717783130790,1717943630790, False, False, 2.5, True, 0.04, 0.4, 0.309303735065347) 
# # okinput,i6, okout = RunTest88('bybit','BNB',1717425963559,1717485363559, False, False, 2.5, True, 0.04, 0.4, 0.45721523504551526) 
# # okinput,i6, okout = RunTest88('finam','FLOT',1703498267038,1703498867038, True, False, 2.5, 0.0005, 0.9, 0) 
# okinput,i6, okout = RunTest8899('finam','MTLR',1703184767038,True, False, 2.5, 0.0005, 0.9, 0) 
# RunTest88('finam','MTLRP',1704300793527,1704301093527, True, False, 2.5, 0.0005, 0.9, 0) 
TestIn55Finam('finam','SOFL',1712942247479,1713169047479, True, False, 2.5, False, 0.0005, 0.9, 0.015363398194313049) 
ControlRun()
print('The end.')



