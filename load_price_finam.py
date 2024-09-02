# import small
# from birja import birjaclass 
# from wallet import walletclass 
# # from reshalka import reshalkaclass 
# from birja_finam import birja_finam101_class
# import db


# def GetTimeShag():
#     if small.ItDebugAddPrice():
#         return 1
#     else:
#         return 5

# def GetAdd777_TimeShag():
#     if small.ItDebugAddPrice():
#         return (2*60*1000)
#     else:
#         return (10*24*60*60*1000)
    
# def GetAdd888_TimeShag():
#     if small.ItDebugAddPrice():
#         return (3*60*1000)
#     else:
#         return(12*60*60*1000)

# def GetBirjaClassFromName(birja, coin, bcoin):
#     b1=birja_finam101_class(birja, 1, coin, bcoin, 0, 0)
#     return b1

# def addprice77_save_list(conn, cursor, listpar, newprices, tb_name):
#     for l1 in listpar:
#         cursor.execute("insert IGNORE  into "+tb_name+" set id="+str(l1[0])+", price="+str(l1[1])+" ")
#         #cursor.execute("insert into "+tb_name+"(id, price) values ("+l1[0]+","+l1[4]+" ) ")
#     conn.commit()

# def ExistNotesInCoin(cursor, tb_name):
#     rows = db.GetSel77(cursor, "select count(*) from "+tb_name)
#     if rows is None: return False
#     if len(rows) == 0: return False
#     if rows[0][0] == 0: return False
#     if rows[0][0] != 0: return True
#     return False



# def addprice77(conn,cursor, newprices, bybit_name, tb_name, kraytime, birja, coin, bcoin):
#     #--ХОДИМ ПО ДНЯМ И ПО ЧАСАМ И ДОБАВЛЯЕМ ДАННЫЕ
#     if newprices:
#         ottime=kraytime
#         do1=int(ottime)+GetAdd888_TimeShag()
#         #his1=small.GetHist(bybit_name, 222, ottime,do1, GetTimeShag())
#         b1=GetBirjaClassFromName(birja, coin, bcoin)
#         his1=b1.GetHist(bybit_name, 222, ottime,do1, GetTimeShag())
#         if his1 is None:
#             return 0
#         if len(his1) == 0:
#             if ExistNotesInCoin(cursor, tb_name) == False:
#                 # при отсутствии значений добавим как старые значения
#                 return addprice77(conn,cursor, False, bybit_name, tb_name, kraytime, birja, coin, bcoin)
#         if his1 is None or len(his1) == 0:
#             return 0
#         addprice77_save_list(conn, cursor, his1, newprices, tb_name)
#         return len(his1)
#     else :
#         dotime=kraytime
#         ot1=int(dotime)-GetAdd888_TimeShag()
#         #his1=small.GetHist(bybit_name, 222, ot1, dotime, GetTimeShag())
#         b1=GetBirjaClassFromName(birja, coin, bcoin)
#         his1=b1.GetHist(bybit_name, 222, ot1, dotime, GetTimeShag())
#         if his1 is None or len(his1) == 0:
#             return 0
#         addprice77_save_list(conn, cursor, his1, newprices, tb_name)
#         return len(his1)



# #def addprices44(cursor, newprices, krytime,newprices):
# def get_kray_time(cursor, newprices, name2):
#         #время крайнего значения
#         time1=0
#         if(newprices) :
#             time1=db.GetSel55(cursor, "SELECT MAX(id) FROM "+name2)
#         else :
#             time1=db.GetSel55(cursor, "SELECT MIN(id) FROM "+name2)
#         time2=time1[0][0]
#         if time2 == None :
#             time2=small.GetTimeS()
#         return time2

# def AddWorkTimeNewOrOld(conn,cursor, newprices, birja, coin, bcoin):
#     b1=GetBirjaClassFromName(birja, coin, bcoin)
#     t1=b1.GetBirjaTime()
#     kr=get_kray_time(cursor, newprices, 'work_time_f_i_n_a_m')
#     ot1, do1 = 0, 0

# def AddPricesNewOrOld(newprices, birja, coin, bcoin, list2):
#     #добаввляем цены сверху и снизу
#     conn=db.GetConnect()
#     cursor = conn.cursor()
#     ot1, do1=AddWorkTimeNewOrOld(conn,cursor, newprices, birja, coin, bcoin)
#     #--------подготовим список с именами таблиц и крайними временами----------------
#     #rows5=db.GetSel55(cursor, "SELECT bybit_base_currency, CONCAT('bybit_', bybit_base_currency), 'kraytime' FROM symbols where bybit_quote_currency='USDT' and bybit_status='Trading'")
#     sik1=0
#     if list2 == None:
#         tbname=small.GetTableName(birja, coin)
#         zapros="SELECT iname, "+tbname+", birja, coin, bcoin FROM symb where birja='"+birja+"'  "
#         if bcoin!='':
#             zapros=small.adder(zapros, " and bcoin='" , bcoin, "'  ")
#         zapros=small.adder(zapros, "  and (smotrim=1 or stavim=1)")
#         if coin!='':
#             zapros=small.adder(zapros, " and coin='", coin, "'")
#         rows=db.GetSel55(cursor, zapros)
#         #копия списка (тот не редактируетс)
#         list2= [[0] * 6 for i in range(len(rows))]
#         print("Load kray times.")
#         size2=0
#         for row in rows:
#             list2[size2][0]=row[0]
#             list2[size2][1]=row[1]
#             list2[size2][2]=get_kray_time(cursor, newprices, row[1])
#             list2[size2][3]=row[2]
#             list2[size2][4]=row[3]
#             list2[size2][5]=row[4]
#             size2=size2+1
#         conn.commit()
#     #--------------поиск первого или последнего времени от цены---------------
#     for l2 in list2:
#         sik1=addprice77(conn, cursor, newprices, l2[0], l2[1], l2[2], l2[3], l2[4], l2[5])
#         print("added new-old ", sik1, " nones for ", l2[0])
#     conn.close()
#     cursor.close()
#     return sik1

# def TestPriceOrder(coinname):
#     #проверим порядок цен
#     conn=db.GetConnect()
#     cursor = conn.cursor()
#     #--------подготовим список с именами таблиц и  временами----------------
#     tname='bybit_'+coinname
#     rows=db.GetSel55(cursor, "SELECT id, price "
#                                   +"FROM "+tname+""  )
#     size2=0
#     msave=0
#     next1=0
#     for row in rows:
#         m1=row[0]/(1000*60)
#         if size2 > 0:
#             if msave < m1-6 or msave > m1-4:
#                 print(tname, ' - ', row[0])
#                 small.ifnoterr(1==0)

#         if next1 % 1000 == 0:
#             print(tname, ' - ', m1)
#         size2=size2+1
#         msave=m1
#         next1=next1+1
#     conn.commit()
#     conn.close()
#     cursor.close()



# def TestPriceOrder_ForAll_bybit():
#     #проверим порядок значений для всех инструментов байбит
#     conn=db.GetConnect()
#     cursor = conn.cursor()
#     #--------подготовим список с именами монет ---------------
#     rows=db.GetSel55(cursor, "SELECT bybit_base_currency  FROM symbols where bybit_quote_currency='USDT' and bybit_status='Trading'")
#     for row in rows:
#         TestPriceOrder(row[0])
#     conn.commit()
#     conn.close()
#     cursor.close()

# def TestPriceOrder(coinname):
#     #проверим порядок цен
#     conn=db.GetConnect()
#     cursor = conn.cursor()
#     #--------подготовим список с именами таблиц и  временами----------------
#     tname='bybit_'+coinname
#     rows=db.GetSel55(cursor, "SELECT id, price "
#                                   +"FROM "+tname+""  )
#     size2=0
#     msave=0
#     next1=0
#     for row in rows:
#         m1=row[0]/(1000*60)
#         if size2 > 0:
#             if msave < m1-6 or msave > m1-4:
#                 print(tname, ' - ', row[0])
#                 small.ifnoterr(1==0)

#         if next1 % 1000 == 0:
#             print(tname, ' - ', m1)
#         size2=size2+1
#         msave=m1
#         next1=next1+1
#     conn.commit()
#     conn.close()
#     cursor.close()



