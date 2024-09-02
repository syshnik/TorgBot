

from __future__ import print_function
from datetime import datetime 
import random
import small
import db
from dbuse import dbuse
import matplotlib.pyplot as plt                              # построение графиков
# pip install matplotlib
from time import sleep
import array as arr 
import numpy as np
# import simpleaudio as simple_audio 
import time
import pandas as pd
import math
from math import sqrt

# вычисление среднего значения монет

class usrednyalka_class(dbuse):
    def __init__(self, cursor, conn, birja):
        super().__init__(cursor, conn)
        self._birja=birja
        self._cmm=None

    def WorkWrightKrayNote(self, tbname, kraynote, kraytime):
        self.MakeCommand("insert IGNORE  into "+tbname+" set id="+str(kraytime)+", price="+str(kraynote)+" ")

    def GetCorrectKrayNote(self, tbname, kraytime, newprices):
        # возвращает крайнее значение
        # для пустой таблицы его создает
        rows=self.GetSell("SELECT MAX(price) FROM "+tbname+" where id="+str(kraytime))
        kraynote=small.GetCorrectOneFloatNoteFromRowsAsOne(rows)
        # нулевое значеие
        if kraynote is None:
            # попали в пробел ищем выше и ниже
            if newprices:
                rows=self.GetSell( "SELECT MAX(price) FROM "+tbname+" where id < "+str(kraytime))
                kraynote=small.GetCorrectOneFloatNoteFromRowsAsOne(rows)
            else:
                rows=self.GetSell( "SELECT MIN(price) FROM "+tbname+" where id > "+str(kraytime))
                kraynote=small.GetCorrectOneFloatNoteFromRowsAsOne(rows)
        if kraynote is None:
            # проверка что других нету
            notenull=small.GetCorrectOneFloatNoteFromRowsAsOne(self.GetSell( "SELECT MAX(price) FROM "+tbname))
            if notenull is not None:
                fgf=9/0
            kraynote=1000.0
            # для пустой таблицы его создает
            self.WorkWrightKrayNote(tbname, kraynote, kraytime)
        return kraynote

    def AddPricesNewOrOldUC(self, newprices, limit, dountime, sname):
        # догружаем данные сверху или снизу (новые или старые)
        tbname=small.GetTableName(self._birja, sname)
        # край
        nowtime=int(round(time.time() * 1000))
        nowtime=nowtime-nowtime%(5*60*1000)
        kraytime=db.get_kray_time(self.GetCursor(), newprices,  tbname)
        kraytime=kraytime-kraytime%(5*60*1000)
        # догружаем
        retsik=0
        for l1 in range(0, limit):
            kraynote=self.GetCorrectKrayNote( tbname, kraytime, newprices)
            if newprices:
                kraytime=kraytime+(5*60*1000)
                proctimepar=kraytime
                pr1=self.GetObshiyProcent( 1, proctimepar, sname)
                if pr1 is None: 
                    if self.ProverimNaSushUp(proctimepar)==False:
                        break
                    continue
                kraynote=kraynote*(100+pr1)/100
            else:
                proctimepar=kraytime
                pr1=self.GetObshiyProcent( 1, proctimepar, sname)
                kraytime=kraytime-(5*60*1000)
                if pr1 is None: 
                    continue
                kraynote=kraynote*(100-pr1)/100
            print("add sredniy "+("up"if newprices else "doun")+" "+str(round(kraynote, 5)))
            self.WorkWrightKrayNote(tbname, kraynote, kraytime)
            retsik=retsik+1
            # значений еще нет
            if kraytime > nowtime: 
                break
            # туда уже не надо
            if kraytime < dountime:
                for i in range(0, 1000): print("================================ Too old ================================")
                sleep(333)
                break
        return retsik


    def ReadFromBase(self):
        rows=self.GetSell("select coin from symb where  stavim=1 and birja='"+self._birja+"' order by id")
        self._cmm=pd.DataFrame(rows)
        #self._cmm.index=self._cmm[0]
        self._cmm.rename(columns = {0:'coin'}, inplace = True )
        self._cmm['proc']=float(0)
        self._cmm['prog']=float(0)
        self._cmm['pricenew']=float(0)
        self._cmm['priceold']=float(0)
        self._cmm['procsred']=float(0)
        self._cmm['sumpohoj']=int(0)
        self._cmm.index = range(0,len(self._cmm),1)
                # self._cm=[]
        # self._cm_pohoj_proc=[]
        # self._cm_pohoj_prog=[]
        # for r1 in rows:
        #     self._cm.append(r1[0])
        #     self._cm_pohoj_proc.append(0)
        #     self._cm_pohoj_prog.append(0)

    def DeletNepohojiyCoin(self):
        sumpohoj=self._cmm['sumpohoj'].min()
        delcoin=self._cmm.loc[self._cmm['sumpohoj'] == sumpohoj]
        i1=delcoin.index[0]
        self._cmm = self._cmm.drop (index=i1)
        self._cmm.index = range(0,len(self._cmm),1)
        return 0

    def CreateUsrednyalkaFile(self, ostavim, progonov):    
        if ostavim > 1 or ostavim < 0.2:            ggg=667/0
        self.ReadFromBase()
        sik=len(self._cmm)
        while sik*ostavim < len(self._cmm): 
            self.CalcSrednieProcentCoins(progonov)
            self.Test55()
            self.DeletNepohojiyCoin()
            self.Test55()
        self.SbrosToFile()
        self.ReadFromFile()
        print('-----------')
        print(self._cmm)

    def CalcSrednieProcentCoins(self, sikokorazsmotrim):
        # от настоящего идем назад считаем проценты
        id=int(round(time.time() * 1000))
        id=id-id%(5*60*1000)
        # conn=db.GetConnect()
        # cursor = conn.cursor()
        #
        countperiod=4
        for i in range(0, sikokorazsmotrim):
            while True:
                id=id-countperiod*5*60*1000
                pr1=self.GetObshiyProcent(countperiod,id, 'srednee')
                if pr1 is not None:
                    print(str(round(pr1, 4))+"%")
                    break
                else:
                    print("Pustoe...")
        #
        self.Commit()
        # conn.commit()
        # cursor.close()
        # conn.close()
        return 0

    def Test55(self):
        return 0
        for coin in self._cmm['coin']:
            if pd.isnull(coin):
                fr=7/0

    def ProverimNaSushUp(self, timepar):
        # проверим есть ли в будущем значения
        timepar=int(timepar-(timepar%(5*60*1000)))
        # чтение max id
        z="select 1  "
        for coin in self._cmm['coin']:
            tname=small.GetTableName(self._birja, coin)
            z=small.adder(z, ", (select max(id) from "+tname+") ")
        rows=self.GetSell(z)
        # проверка на сущ-е
        for i in range(len(self._cmm)):
            note1=rows[0][i+1]
            if note1 is not None: 
                if note1 > timepar:
                    # есть такое
                    return True
        return False


    def GetObshiyProcent(self, countperiod, timepar, sname):
        # срезка цен и общий процент
        # countperiod - сколько периодов по 5 мин отступаем
        timepar=int(timepar-(timepar%(5*60*1000)))
        # чтение цен
        z="select 1  "
        for coin in self._cmm['coin']:
            tname=small.GetTableName(self._birja, coin)
            z=small.adder(z, ", (select max(price) from "+tname
                            +" where id = "+str(timepar)+") ")
            z=small.adder(z, ", (select (price) from "+tname
                            +" where id = "+str(timepar-countperiod*5*60*1000)+") ")
        rows=self.GetSell(z)
        # проверка на пустое
        pustoe=0
        for i in range(len(self._cmm)):
            if rows[0][i] is None: pustoe+=1
        if float(pustoe) > len(self._cmm)/3:
            return None
        # заполнение массивов
        l2=int((len(rows[0])-1)/2)
        for i in range(0, l2):
            newp=rows[0][i*2+1]
            oldp=rows[0][i*2+2]
            # self._cmm['pricenew'][i] = newp
            # self._cmm['priceold'][i] = oldp
            self.Test55()
            self._cmm.at[i,  'pricenew'] = newp
            self._cmm.at[i,  'priceold'] = oldp
            self.Test55()
        # ВЫЧИСЛЕНИЕ процентов
        self._cmm['procsred'] = (self._cmm['priceold']-self._cmm['pricenew'])*100/self._cmm['priceold']
        self.Test55()
        srpr=self._cmm['procsred'].mean()    
        self.Test55()
        savesrpr=srpr
        # выбросы  0-ВЫБРОС 1-НОРМА
        otstup=0.1
        otstupplus=0.02*countperiod
        if sname == 'bigsrednee':
            otstup=5
        for i in range(0, 11):
            otstup=otstup+otstupplus
            otstupplus=otstupplus*2
            self._cmm['vibros'] = self._cmm['procsred'].apply ( lambda x: 0 if (pd.isnull(x) or x > srpr+otstup or x < srpr-otstup) else 1)
            self.Test55()
            if self._cmm['vibros'].sum() > len(self._cmm)/2:
                break
        #self._cmm['vibros'] = self._cmm['procsred'].apply ( lambda x: 0 if (pd.isnull(x)) else 1)
        #print(self._cmm)
        # обнуляем выбросы
        self._cmm['procsred'] = self._cmm['procsred']*self._cmm['vibros']
        self.Test55()
        # а для похожих увеличим число совпадений
        self._cmm['sumpohoj'] = self._cmm['sumpohoj']+self._cmm['vibros']
        self.Test55()
        # пересчитываем
        sumpr=float(self._cmm['procsred'].sum())
        sumvibros=float(self._cmm['vibros'].sum())
        if sumvibros==0: return None
        return sumpr/sumvibros
        # del5=int(sumvibros)
        # if del5 != 0:
        #     retsrpr=sumpr/del5
        # else:
        #     retsrpr=0
        # # подчистим 
        # if retsrpr is None or np.isnan(retsrpr):
        #     retsrpr=savesrpr
        # if retsrpr is None or np.isnan(retsrpr):
        #     retsrpr=0
        # return retsrpr

    def SbrosToFile(self):
        algo=small.GetAlgoName(True)
        self._cmm.to_csv('D:/BS/Save/WORK/Programm/bi/ii/'+'usrednyalka_'+algo+'.csv', encoding='utf-8')
        return 0

    def ReadFromFile(self):
        algo=small.GetAlgoName(True)
        self._cmm=pd.read_csv('D:/BS/Save/WORK/Programm/bi/ii/'+'usrednyalka_'+algo+'.csv')
        self._cmm.index = range(0,len(self._cmm),1)
        #self._cmm.set_index('col1')
        return 0    