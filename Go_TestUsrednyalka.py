from  napravlalka import NapravlalkaClass
import  db
from usrednyalka import usrednyalka_class
import small
import time
# @shtefanntzAWS предоставляет стандартный сервер в /etc/chrony.conf
# архив значений усредненного массива монет
if True:
    dountime=int(round(time.time() * 1000))-2*365*24*60*60*1000
    limit=2000
    for i in range(0, 11111111):
        if True:
            birjamassiv=['finam', 'bybit', 'okx', 'binanceusdt']
            for  birja in birjamassiv:
                u1 = usrednyalka_class(None, None, birja)
                small.SetAlgoName('Algo_606_'+birja)
                u1.ReadFromFile()
                u1.AddPricesNewOrOldUC(False, limit, dountime, 'bigsrednee')
        try:
            gg=0
        except:
            print("except---------------")
# создание усредненного массива монет
if False:
    ostavim=0.78
    progonov=800
    birjamassiv=['bybit',  'binanceusdt','okx']
    for  birja in birjamassiv:
        small.SetAlgoName('Algo_606_'+birja)
        u1 = usrednyalka_class(None, None, birja)
        u1.CreateUsrednyalkaFile(ostavim, progonov)
        gvf=0
