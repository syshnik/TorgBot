import requests 
import json
import small
import mysql.connector
from mysql.connector import connect, Error
import time
def GetConnect():
    conn = mysql.connector.connect(host='localhost',
                                database='treyd',
                                user='root',
                                password='823945')
    if conn.is_connected():
        YYY=0
        #print('Connected to MySQL database')
    else :
        small.ifnoterr(1==2)
    return conn



    
def GetSel55(cur, query):
    cur.execute(query)
    ret=[]
    for row in cur:
        ret.append(row)
    return ret

def CreateTableIfNotExists(cur, tname):
    rows=GetSel55(cur, "SHOW TABLES  LIKE '" + tname + "'")
    if len(rows) == 0:
        c1="create table IF NOT EXISTS " + tname + " "
        c1=small.adder(c1, " ( ", "	id	BIGINT UNSIGNED not null    primary key,", " price FLOAT NULL DEFAULT NULL)  ")
        cur.execute(c1)


def connect55():
    conn=GetConnect()
    cursor = conn.cursor()
    #-------------read names-----------------
    rows=GetSel55(cursor, "SELECT coin FROM symbols where bcoin='USDT' and bybit_status='Trading'")
    #--------------create tables---------------
    for row in rows:
        name1=row[0]
        name2="bybit_"+name1
        CreateTableIfNotExists(cursor, name2)
    conn.commit()
    cursor.close()
    conn.close()

def CreateSymbolsTables():
    connect55()

def GetListFromBase(zapros):
    #выдает список из запроса
    conn=GetConnect()
    cursor = conn.cursor()
    rows=GetSel55(cursor, zapros)
    conn.commit()
    cursor.close()
    conn.close()
    return rows

def MakeCommand(zapros):
    #выдает список из запроса
    conn=GetConnect()
    cursor = conn.cursor()
    cursor.execute(zapros)
    cursor.close()
    conn.commit()
    conn.close()
   
def MakeCommandCursorConn(zapros, cursor, conn):
    #выдает список из запроса
    cursor.execute(zapros)
    conn.commit()
   
   
def GetSel77(cur, query):
    if cur != None:
        return GetSel55(cur, query)
    else:
        return GetListFromBase(query)

def get_kray_time(cursor, newprices, name2):
    #время крайнего значения
    time2=None
    if(newprices) :
        time1=GetSel55(cursor, "SELECT MAX(id) FROM "+name2)
    else :
        time1=GetSel55(cursor, "SELECT MIN(id) FROM "+name2)
    time2=small.GetCorrectOneNoteFromRowsAsOne(time1)
    if time2 == None :
        #time222=small.GetTimeS()
        milliseconds = int(round(time.time() * 1000))
        time2=milliseconds
    return time2


def AddUpdate_peremenniye(pername, pernewnote):
    #--------save----------------------------------------
    conn=GetConnect()
    cursor = conn.cursor()
    #cursor.execute("delete  from peremenniye where pername='"+pername+"'   ")
    #conn.commit()
    rows=GetSel55(cursor, "select id from peremenniye where pername='"+pername+"' ")
    find1=False
    if rows != None:
        if len(rows) != 0:
            find1=True
    if find1:
        cursor.execute("update peremenniye set perznachenie='"+pernewnote+"' where "
                       +" pername = '"+pername+"' ")
    else:
        cursor.execute("insert into peremenniye(pername, perznachenie) values ('"+pername+"', '"+pernewnote+"' ) ")
    conn.commit()
    cursor.close()
    conn.close()


def AddUpdate_peremenniye_AndCursor(cursor, conn, pername, pernewnote):
    #--------save----------------------------------------
    # conn=GetConnect()
    # cursor = conn.cursor()
    #cursor.execute("delete  from peremenniye where pername='"+pername+"'   ")
    #conn.commit()
    rows=GetSel55(cursor, "select id from peremenniye where pername='"+pername+"' ")
    find1=False
    if rows != None:
        if len(rows) != 0:
            find1=True
    if find1:
        cursor.execute("update peremenniye set perznachenie='"+pernewnote+"' where "
                       +" pername = '"+pername+"' ")
    else:
        cursor.execute("insert into peremenniye(pername, perznachenie) values ('"+pername+"', '"+pernewnote+"' ) ")
    conn.commit()
    # conn.commit()
    # cursor.close()
    # conn.close()


def GetCorrectStrToBase(strpar: str, maxsize=250):
    strpar=str(strpar)
    ret = strpar.replace('\'', '\\\'')
    ret='\''+ret[:maxsize-2]+'\''
    return ret

def PrintInfoToComments(cursor, conn, order, pisaka, comm, intpar=None, floatpar=None, comm0=None, comm1=None, comm2=None):
    if order is None:   order='null'
    else: order=str(int(order))
    if intpar is None:   intpar='null'
    else: intpar=str(small.GetIntFromAll(intpar))
    if floatpar is None:   floatpar='null'
    else: floatpar=str(small.GetFloatFromAll(floatpar))
    if pisaka is None: pisaka = 'null'
    else: pisaka =  GetCorrectStrToBase(pisaka)
    if comm is None: comm = 'null'
    else: comm =  GetCorrectStrToBase(comm)
    if comm0 is None: comm0 = 'null'
    else: comm0 =  GetCorrectStrToBase(comm0)
    if comm1 is None: comm1 = 'null'
    else: comm1 =  GetCorrectStrToBase(comm1)
    if comm2 is None: comm2 = 'null'
    else: comm2 =  GetCorrectStrToBase(comm2)
    z1='insert into comments(_order, _pisaka, _comment, _int, _float, _comm0, _comm1, _comm2, _date) values (' +order+', '+pisaka+', '+comm+', '+intpar+', '+floatpar+', '+comm0+', '+comm1+', '+comm2+', now())'
    try:
        # MakeCommand('insert into comments(_order, _pisaka, _comment, _int, _float, _comm0, _comm1, _comm2, _date) values ('
        #                 +order+', '+pisaka+', '+comm+', '+intpar+', '+floatpar+', '+comm0+', '+comm1+', '+comm2+', now())')
        cursor.execute(z1)
        conn.commit()
    except:
        print('Error78754222')
        gg=False
        if gg:
            # MakeCommand('insert into comments(_order, _pisaka, _comment, _int, _float, _comm0, _comm1, _comm2, _date) values ('
            #     +order+', '+pisaka+', '+comm+', '+intpar+', '+floatpar+', '+comm0+', '+comm1+', '+comm2+', now())')
            cursor.execute(z1)
            conn.commit()



def SrezkaCen(birja):
    njn=0

def DeleteTablesNeVSymb(conn, cursor, likepar):
     # удаление таблиц вне списка symb
    l1=GetSel77(cursor, "SHOW TABLES like '"+likepar+"'")
    l2=GetSel77(cursor, "select birja, coin, bcoin from symb")
    # ходим по списку сущ-х таблиц
    for r1 in l1:
        bn1=str(r1[0])
        bn1=bn1.lower()
        # и ищем эту таблицу в списк symb
        findtable=False
        for r2 in l2:
            bn2=str(small.GetTableName(r2[0], r2[1]))
            bn2=bn2.lower()
            if bn1 == bn2:
                 findtable=True
                 break
        if findtable: continue
        # удаление таблицы не из списка
        print("Delete table "+bn1)
        cursor.execute("DROP TABLE "+bn1)
        conn.commit()
        # db.MakeCommand("DROP TABLE "+bn1)
    
def SetPerToPremennie(cursor, conn, pername, pernote):
    # запись переменной в массив пер-х
    # установка значений по умолчанию
    an=pername
    # удаление дубликатов
    rows=GetSel77(cursor, "select  count(*) from peremenniye where pername='"+an+"'")
    note1=small.GetCorrectOneNoteFromRowsAsOne(rows)
    if note1 > 1:
        MakeCommandCursorConn("delete from peremenniye where pername='"+an+"'", cursor, conn)
    # перезапись
    rows=GetSel77(cursor, "select  id from peremenniye where pername='"+an+"'")
    id=small.GetCorrectOneNoteFromRowsAsOne(rows)
    if id is None:
        MakeCommandCursorConn("insert into peremenniye (perznachenie, pername) values ('"+str(pernote)+"', '"+an+"')", cursor, conn)
    else:
        MakeCommandCursorConn("update peremenniye set perznachenie='"+str(pernote)+"' where id = "+str(int(id)), cursor, conn)


def GetPerFromPremennie(cursor, pername, pertype, perot, perdo, perifnotexist):
    # чтение переменной из массива пер-х
    # установка значений по умолчанию
    an=pername
    # удаление дубликатов
    rows=GetSel77(cursor, "select  count(*) from peremenniye where pername='"+an+"'")
    note1=small.GetCorrectOneNoteFromRowsAsOne(rows)
    if note1 > 1:
        MakeCommand("delete from peremenniye where pername='"+an+"'")
    # чтение из базы
    rows=GetSel77(cursor, "select  perznachenie from peremenniye where pername='"+an+"'")
    note1=small.GetCorrectOneNoteFromRowsAsOne(rows)
    # создание переменнойесли её нет
    if note1 is None:
        note1=perifnotexist
        MakeCommand("insert into peremenniye (perznachenie, pername) values ('"+str(note1)+"', '"+an+"')")
    note2=0
    if pertype=='float':
        try:
            note2=float(note1)
        except:
            note2=perifnotexist
    elif pertype=='int':
        try:
            note2=int(note1)
        except:
            note2=perifnotexist
    elif pertype=='str':
        try:
            note2=str(note1)
        except:
            note2=perifnotexist
    elif pertype=='bool':
        try:
            if note1=='True': note2=True
            elif note1=='False': note2=False
            elif note1=='1': note2=True
            elif note1=='0': note2=False
            else :
                ddd=5/0
        except:
            note2=perifnotexist
    else:
        print('Error 3356753223')
        small.ifnoterr(5==0)
    # проверка допуска
    if pertype=='str':
        hh=0
    elif pertype=='bool':
        if perot is not None and perdo is not None:
            if note2 != False and note2 != True:
                note2=perifnotexist
    else:
        if perot is not None and perdo is not None:
            if note2 < perot or note2 > perdo:
                note2=perifnotexist
    return note2

