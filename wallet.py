import db
#from birja import birjaclass 
import small


class walletclass:
 
    def __init__(self, birjanamepar, SikokoSpim):
        self.birjaname = birjanamepar
        self.SikokoSpim = SikokoSpim
 
    def UpdateCoin(self, coin, sik):
        #обновление балланса монеты
        conn=db.GetConnect()
        cursor = conn.cursor()
        id=int(0)
        #проверка на сущ-е
        zapros=small.adder("SELECT id FROM wallet where  coin='", coin,  "' "
            , " and birja='" , self.birjaname , "' "
            , " and idorder is null")
        rows=db.GetSel55(cursor, zapros)
        for row in rows:
            id=int(row[0])
        #обавим запись
        if id==0:
            cursor.execute("insert into wallet(coin, birja, sikoko, sozdan, idorder) values ("
                        +" '"+str(coin)+"', "
                        +" '"+str(self.birjaname)+"', "
                        +     str(sik)+   ", "
                        + "NULL, NULL)")
        #изменим запись
        else:
            cursor.execute("update wallet set sikoko="+str(sik)+   " where id= " + str(id))
                       
        conn.commit()
        cursor.close()
        conn.close()



    def ClearWallet(self):
        #clear балланса монеты
        conn=db.GetConnect()
        cursor = conn.cursor()
        cursor.execute("delete from  wallet where birja="+" '"+str(self.birjaname)+"' ")
        conn.commit()
        cursor.close()
        conn.close()



    def ClearForOrder(self, order):
        #clear балланса монеты
        conn=db.GetConnect()
        cursor = conn.cursor()
        cursor.execute("delete from  wallet where   idorder="+str(order))

        conn.commit()
        cursor.close()
        conn.close()



    # def InitBallance(self):
    #     self.ClearWallet()
    #     if self.birjaname=='bybit':
    #         self.UpdateCoin('USDT', '5.2')
    #     else:
    #         small.ifnoterr(1==2)

    def GetFreeSumm(self, coin):
        #ballance coin
        conn=db.GetConnect()
        cursor = conn.cursor()
        zapros=small.adder("SELECT sikoko FROM wallet where birja='"+self.birjaname+"' and  coin='", coin,  "' "
            , " and idorder is null")
        rows=db.GetSel55(cursor, zapros)
        ret=float(0)
        for row in rows:
            ret+=float(row[0])
        conn.commit()
        cursor.close()
        conn.close()
        return ret
    
    def GetCoinsFromOrder(self, coinname, OrderId):
        #ballance coin
        conn=db.GetConnect()
        cursor = conn.cursor()
        zapros=small.adder("SELECT sikoko FROM wallet where  coin='", coinname,  "' "
            , " and idorder = ", str(OrderId))
        rows=db.GetSel55(cursor, zapros)
        ret=float(0)
        for row in rows:
            ret+=float(row[0])
        conn.commit()
        cursor.close()
        conn.close()
        return ret

    def AddOder(self, IdOrder, sellcoin, buycoin,  sellsik, buysik):
        #добавляем в кошелек инфу об текущих ордерах
        conn=db.GetConnect()
        cursor = conn.cursor()
        #
        cursor.execute("insert into wallet(coin, birja, sikoko, sozdan, idorder) values ("
                       +" '"+str(sellcoin)+"', "
                       +" '"+str(self.birjaname)+"', "
                       +" -"+str(sellsik)+   ", "
                       + "now(), "
                       +str(IdOrder)+")")
        cursor.execute("insert into wallet(coin, birja, sikoko, sozdan, idorder) values ("
                       +" '"+str(buycoin)+"', "
                       +" '"+str(self.birjaname)+"', "
                       +" "+str(buysik)+   ", "
                       + "now(), "
                       +str(IdOrder)+")")
        #
        conn.commit()
        cursor.close()
        conn.close()
        # #
        # old_sellsik=self.GetFreeSumm(sellcoin)
        # old_buysik=self.GetFreeSumm(buycoin)
        # self.UpdateCoin( sellcoin, old_sellsik-sellsik)
        # self.UpdateCoin( buycoin, old_buysik+buysik)

  