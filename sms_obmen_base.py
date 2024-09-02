# import sys
# import db
# import small
import time
# import load_price
from time import sleep
import small
# import requests 
import db
from dbuse import dbuse
# import mysql.connector
# from datetime import datetime 

import re

class sms_message:
    def __init__(self):
        self._id=0
        self._otpravil=''
        self._mess=''
        self._kogda=''
        self._status=0
        self._birja=''
        self._coin=''
        self._jdem=0



class sms_obmen_base_class(dbuse):
    def __init__(self,  cursor, conn):
        super().__init__(cursor, conn)

    def StatusOtpravlen(self): return 1
    def StatusViponnen(self): return 2
    def StatusOtmenen(self): return 4
    def StatusPause(self): return 8
    def StatusZavershen(self): return 16

    def OrMess(self, birja, coin, id, orstatus):
        # отметка о выполнении отмене...закрытии сообщения
        z1="update sms set messstatus = messstatus | "+str(orstatus)+" where 1=1 "
        if birja is not None: z1=z1+" and birja='"+birja+"'  "
        if coin is not None: z1=z1+" and coin='"+coin+"' "
        if id is not None:
            if id != 0:
                z1=z1+" and id="+str(id)
        self.MakeCommand(z1)


    def SendMess_Buy_Sell_Short_Long(self, jdem, birja, coin, Buy, Sell, Short, Long):
        if small.SikokoTrue(Buy, Sell, Short, Long) != 2:
            print('Error 445643232')
            return 0
        # зачистка старья   
        # if (Buy and Long) or (Sell and Short):
        # self.OrMess(birja, coin, None, self.StatusZavershen())
        str1=''
        if Buy: str1=str1+'buy'
        if Sell: str1=str1+'sell'
        if Short: str1=str1+'short'
        if Long: str1=str1+'long'
        return self.SendMess('comp', str1, jdem, birja, coin)

    def DoInput(self, sm:sms_message, message:str):
        # ручной вход в сделку 
        if message.find('buylong') == -1 and message.find('sellshort') == -1 : return 0
        lst = message.split()
        if len(lst) !=  2: return 0
        if lst[0] != 'buylong' and lst[0] != 'sellshort': return 0
        coin=lst[1]
        id=self.MakeCommand("insert into sms (otpravil, message, kogda, birja, coin,jdem) \
                            values ('user', '"+lst[0]+"', NOW(), '"+small.GetBirjaNameFromAlgo()+"', '"+coin+"', 11)", True, True)
        return id
    
    def DoOutput(self, sm:sms_message, message:str):
        # ручной вход в сделку 
        if message.find('selllong') == -1 and message.find('buyshort') == -1 : return 0
        lst = message.split()
        if len(lst) !=  2: return 0
        if lst[0] != 'selllong' and lst[0] != 'buyshort': return 0
        coin=lst[1]
        id=self.MakeCommand("insert into sms (otpravil, message, kogda, birja, coin,jdem) \
                            values ('user', '"+lst[0]+"', NOW(), '"+small.GetBirjaNameFromAlgo()+"', '"+coin+"', 11)", True, True)
        return id
    
    def DoSetIndexNastroeniya(self, sm:sms_message, message:str):
        # переписываем индекс настроения
        if message.find('IndexNastroeniya') == -1: return None
        lst=re.split(r'\=', message)
        if len(lst) != 2: return None
        bn=small.GetBirjaNameFromAlgo()
        ind1=lst[0]
        sik1=float(lst[1])
        if bn=='finam':
            if ind1 != 'IndexNastroeniyaFinam': return None
        else:
            if ind1 != 'IndexNastroeniyaCrypta': return None
        if sik1 < 0.2 or sik1 > 1.8: return None
        # пишем
        du = dbuse(None, None)
        db.SetPerToPremennie(du.GetCursor(), du.GetConn(), ind1, str(sik1))
        return True
    
    def ReadMess(self, sm:sms_message, message:str):
        # выполняет команду 
        # возвращает сообщение с измененным состоянием 

        if message.find('IndexNastroeniya') != -1:
            self.DoSetIndexNastroeniya( sm, message)
            return None
        if message=='allclear':
            self.MakeCommand("delete from sms where birja='"+small.GetBirjaNameFromAlgo()+"'")
            self.MakeCommand("delete from orders where birja='"+small.GetBirjaNameFromAlgo()+"'")
            return None
        id456=self.DoInput(sm, message)
        if id456 != 0:
            return self.GetMessageFromId(id456)
        id456=self.DoOutput(sm, message)
        if id456 != 0:
            return self.GetMessageFromId(id456)
        if message=='pause':
            self.OrMess(sm._birja, sm._coin, sm._id, self.StatusPause())
            return self.GetMessageFromId(sm._id)
        if message=='cancel':
            self.OrMess(sm._birja, sm._coin, sm._id, self.StatusOtmenen() | self.StatusZavershen())
            return self.GetMessageFromId(sm._id)
        if message=='input' or message=='output':
            self.OrMess(sm._birja, sm._coin, sm._id, self.StatusViponnen() | self.StatusZavershen())
            return self.GetMessageFromId(sm._id)
        return sm
    
    def SendMess(self, otpravil, message, jdem, birja, coin):
        # записываем в базу  сообщение для отправки
        plusjdem=jdem*5
        id=self.MakeCommand("insert into sms (otpravil, message, kogda, birja, coin,jdem) \
                            values ('"+otpravil+"', '"+message+"', NOW(), '"+birja+"', '"+coin+"', "+str(jdem)+")", True, True)
        while True:
            # read
            rows=self.GetSell("select messstatus from sms where id="+str(id))
            self.Commit()       # и после SELECT надо делать!!!
            messstatus=small.GetCorrectOneNoteFromRowsAsOne(rows)
            messstatus=int(messstatus)
            if (messstatus & self.StatusViponnen()) != 0 or (messstatus & self.StatusOtmenen()) != 0:
                # выход
                break
            # elif (messstatus & self.StatusPause()) != 0:
            # ---------  pause ------------
            jdem-=10
            ostalos=jdem
            if ((messstatus & self.StatusPause()) != 0): ostalos=jdem+plusjdem
            if ostalos <= 0: 
                # время вышло
                self.OrMess(birja, coin, None, self.StatusZavershen())
                break
            print('Jdu otveta  '+str(ostalos)+" s   "+message+"  "+birja+"  "+coin)
            # self.CloseConnect()
            sleep(10)
            # self.ConnectToBase()
            gg=0
        # return 
        rows=self.GetSell("select messstatus from sms where id="+str(id))
        messstatus=small.GetCorrectOneNoteFromRowsAsOne(rows)
        ret = int(messstatus)
        return ret

    def GetMessage(self, birja) -> sms_message:
        # возвращает заполненное сообщение
        rows=self.GetSell("select max(id) from sms where (messstatus & "+str(self.StatusZavershen())+")=0 \
                          and birja='"+birja+"' ")
        id=small.GetCorrectOneNoteFromRowsAsOne(rows)
        if id is None: return None
        return self.GetMessageFromId(id)

                          
    def GetMessageFromId(self, id) -> sms_message:
        # возвращает заполненное сообщение
        sm=sms_message ()
        rows=self.GetSell("select id, otpravil, message, kogda, messstatus, birja, coin, jdem  from sms where id = "+str(id))
        # return ---------------
        for row in rows:
            sm._id=row[0]
            sm._otpravil=row[1]
            sm._mess=row[2]
            sm._kogda=row[3]
            sm._status=row[4]
            sm._birja=row[5]
            sm._coin=row[6]
            sm._jdem=row[7]
            return sm
        return None
                          
