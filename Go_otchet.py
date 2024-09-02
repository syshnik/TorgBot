#from typing import List
import db
from dbuse import dbuse
#from birja import birjaclass 
import small
#import os
import pandas as pd
from datetime import datetime 
from time import sleep
#d1=dbuse(None, None)
class otchet(dbuse):
    def __init__(self, birjapar):
        super().__init__(None, None)

        self._birja=birjapar
        self._cmm=[]
        # self._conn=db.GetConnect()
        # self._cursor = self._conn.cursor()
        self._maxid=0
        self._maxidsrednee=0
        self._sikokomaxid=0
        # coins
        rows=self.GetSell( "select coin from symb where  stavim=1 and birja='"+self._birja+"' order by id")
        self._cmm=pd.DataFrame(rows)
        self._cmm.rename(columns = {0:'coin'}, inplace = True )
        z="select 1  "
        for coin in self._cmm['coin']:
            tname=small.GetTableName(self._birja, coin)
            z=small.adder(z, ", (select max(id) from "+tname+") ")
        rows=self.GetSell( z)
        # ids
        for i in range(len(self._cmm)):
            note1=rows[0][i+1]
            if note1 is not None: 
                self._maxid = max(note1, self._maxid)
        for i in range(len(self._cmm)):
            note1=rows[0][i+1]
            if note1 is not None: 
                if (note1 == self._maxid):
                    self._sikokomaxid+=1
        # srednee
        rows=self.GetSell(  "select max(id) from "+small.GetTableName(self._birja, "srednee")+"")
        self._maxidsrednee=small.GetCorrectOneNoteFromRowsAsOne(rows)                    

    # def __del__(self):
    #     self._conn.commit()
    #     self._cursor.close()
    #     self._conn.close()

    def IdToStr(self, idpar):
        date222 = datetime.utcfromtimestamp(idpar / 1e3+1)
        str2=date222.strftime("%Y-%m-%d %H:%M:%S")
        return str2

    def Print(self):
        print("Отчет для "+self._birja)
        print("Дата обновления"+self.IdToStr(self._maxid)+" количество "+str(self._sikokomaxid)+" среднее "+self.IdToStr(self._maxidsrednee))
        return 0

    def CreateCommentsTextFile(self):
        # отладочная инфа в виде текстового файла
        # зачистка
        self.MakeCommand("delete from comments where _date  < DATE_SUB(now(), INTERVAL 3 DAY) ")
        self.MakeCommand("delete from commentstext where date1  < DATE_SUB(now(), INTERVAL 3 DAY) ")
        # текст
        str1=''
        
        rows=self.GetSell( "select comm1, date1, order1 from commentstext where  algo1='"+small.GetAlgoName()+"' order by id desc")
        for r1 in rows:
            str1=small.adder(str1, r1[1], ", ", r1[2], "\n")
            str1=small.adder(str1, r1[0], "\n")
        # сброс в файл
        with open("d:\\vrem\\TestDebug_"+small.GetAlgoName()+"_.txt", 'w', encoding='UTF-8',) as outfile:
            outfile.write(str1)


while True:
    bm=['okx','bybit',  'binanceusdt','finam']
    for birja in bm:
        small.SetAlgoName('Algo_606_'+birja)
        if small.ItInTry():
            try:
                o1=otchet(birja)
                o1.Print()
                o1.CreateCommentsTextFile()
            except:
                print('Error 22234454322')
        else:
            if True:
                o1=otchet(birja)
                o1.Print()
                o1.CreateCommentsTextFile()
    print("-------------sleep-----------")
    sleep(20*60)