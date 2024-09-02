import db
#from birja import birjaclass 
import small

# def CreateTableSymb():
#     conn=db.GetConnect()
#     cursor = conn.cursor()
#     #
#     cursor.execute("drop table IF EXISTS symb")
#     z='create table symb('
#     z=small.adder(z,   ' id  BIGINT UNSIGNED not null   auto_increment primary key, ')
#     z=small.adder(z,   ' birja CHAR(44) NULL DEFAULT NULL , ')
#     z=small.adder(z,   ' iname		CHAR(44) NULL DEFAULT NULL ,	 ')
#     z=small.adder(z,   ' coin		CHAR(44) NULL DEFAULT NULL ,	 ')
#     z=small.adder(z,   ' bcoin		CHAR(44) NULL DEFAULT NULL,	 ')
#     z=small.adder(z,   ' smotrim  INT UNSIGNED null DEFAULT NULL, ')
#     z=small.adder(z,   ' stavim  INT UNSIGNED  null DEFAULT NULL, ')
#     z=small.adder(z,   ' znpz  INT UNSIGNED  null DEFAULT NULL, ')
#     z=small.adder(z,   ' fortables  INT UNSIGNED  null DEFAULT 1)')
#     cursor.execute(z)
#     #
#     conn.commit()
#     conn.close()
#     cursor.close()
#     #
def AddNotesTable(cursor, birja, coin, bcoin):
        name2=small.GetTableName(birja, coin)
        # if birja=='bybit':
        #     name2="bybit_"+coin
        # else:
        #     name2=birja+"_"+coin+"_"+bcoin
        db.CreateTableIfNotExists(cursor, name2)

def LoadCoin(cursor, birja, coin, bcoin, smotrim, stavim,znpz):
    z='insert into symb (birja, iname, coin, bcoin, smotrim, stavim, znpz) values (\''
    z=small.adder(z,  birja, '\', ')
    z=small.adder(z,  '\'', coin, bcoin, '\', ',  '\'', coin, '\', ',  '\'',  bcoin, '\', ')
    z=small.adder(z, str(smotrim), ', ', str(stavim), ', ', znpz, ') ')
    cursor.execute(z)
    AddNotesTable(cursor, birja, coin, bcoin)

def LoadTableSymb():
    conn=db.GetConnect()
    cursor = conn.cursor()
    #----------------------------------------------------------------------------
    bcoin='USDT'
    birja='bybit'
    # clear
    z="delete from symb where birja='"+birja+"' and bcoin='"+bcoin+"'"
    cursor.execute(z)
    conn.commit()
    # ADD
    LoadCoin(cursor, birja, 'BTC', bcoin, 1, 1, 6)
    LoadCoin(cursor, birja, 'ETH', bcoin, 1, 1,5)
    LoadCoin(cursor, birja, 'BNB', bcoin, 1, 1, 5)
    LoadCoin(cursor, birja, 'XRP', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'SOL', bcoin, 1, 1, 3)
    LoadCoin(cursor, birja, 'WLD', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'APT', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'OP', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'AAVE', bcoin, 1, 1, 3)
    LoadCoin(cursor, birja, 'ADA', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'ALGO', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'APE', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'ATOM', bcoin, 1, 1, 3)
    LoadCoin(cursor, birja, 'AVAX', bcoin, 1, 1, 3)
    LoadCoin(cursor, birja, 'DOGE', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'TRX', bcoin, 1, 1, 2)
    # LoadCoin(cursor, birja, 'BONK', bcoin, 1, 1, 1) # не  читает в историю
    LoadCoin(cursor, birja, 'TIA', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'INJ', bcoin, 1, 1, 2)
    #LoadCoin(cursor, birja, 'WBTC', bcoin, 0, 1, 3)
    #LoadCoin(cursor, birja, 'AVAX2L', bcoin, 0, 1, 3)
    #LoadCoin(cursor, birja, 'AVAX2S', bcoin, 0, 1, 3)
    LoadCoin(cursor, birja, 'ARB', bcoin, 1, 1, 2)
    #LoadCoin(cursor, birja, 'AXL', bcoin, 1, 1)#не  читает в историю
    #LoadCoin(cursor, birja, 'AGLD', bcoin, 1, 1, 2)#
    LoadCoin(cursor, birja, 'BCH', bcoin, 1, 1,3)
    LoadCoin(cursor, birja, 'CRV', bcoin, 1, 1, 2)
    #LoadCoin(cursor, birja, 'CTC', bcoin, 1, 1, 2)#не  читает в историю
    LoadCoin(cursor, birja, 'CYBER', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'DOT', bcoin, 1, 1, 3)
    LoadCoin(cursor, birja, 'FTM', bcoin, 1, 1, 2)
    #LoadCoin(cursor, birja, 'FON', bcoin, 1, 1)#не  читает в историю
    LoadCoin(cursor, birja, 'GALA', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'LINK', bcoin, 1, 1, 3)
    LoadCoin(cursor, birja, 'LTC', bcoin, 1, 1, 5)
    #LoadCoin(cursor, birja, 'LGX', bcoin, 1, 1)#не  читает в историю
    LoadCoin(cursor, birja, 'MNT', bcoin, 1, 1, 2)
    #LoadCoin(cursor, birja, 'SHRAP', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'SNX', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'MATIC', bcoin, 1, 1, 2)
    #LoadCoin(cursor, birja, 'NEON', bcoin, 1, 1)
    #LoadCoin(cursor, birja, 'PEPE', bcoin, 1, 1)#не  читает в историю
    #LoadCoin(cursor, birja, 'SHIB', bcoin, 1, 1)#не  читает в историю
    LoadCoin(cursor, birja, 'SUI', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'XLM', bcoin, 1, 1, 1)
    # фиксирование
    conn.commit()
    # удаление лишнего - старого
    db.DeleteTablesNeVSymb(conn, cursor, birja+'\_%')
    # close

    #----------------------------------------------------------------------------
    bcoin='BNB'
    birja='binancebnb'
    # clear
    z="delete from symb where birja='"+birja+"' and bcoin='"+bcoin+"'"
    cursor.execute(z)
    conn.commit()
#     # ADD
#     LoadCoin(cursor, birja, 'XRP', bcoin, 1, 1, 0)
#     LoadCoin(cursor, birja, 'OP', bcoin, 1, 1, 1)#?????????
#     LoadCoin(cursor, birja, 'AAVE', bcoin, 1, 1,3)
#     LoadCoin(cursor, birja, 'ADA', bcoin, 1, 1, 1)
#     #LoadCoin(cursor, birja, 'ALGO', bcoin, 1, 1, 0)
#     #LoadCoin(cursor, birja, 'APE', bcoin, 1, 1,  3)
#     LoadCoin(cursor, birja, 'ATOM', bcoin, 1, 1, 2)
#     #LoadCoin(cursor, birja, 'ARKM', bcoin, 1, 1, 0)#DELETE TOO LITL V
#     LoadCoin(cursor, birja, 'AVAX', bcoin, 1, 1, 2)
#     LoadCoin(cursor, birja, 'AXS', bcoin, 1, 1, 2)
#     #LoadCoin(cursor, birja, 'BAKE', bcoin, 1, 1, 1)#del
#     LoadCoin(cursor, birja, 'BCH', bcoin, 1, 1, 3)
#     #LoadCoin(cursor, birja, 'BEL', bcoin, 1, 1, 1)#del
#     LoadCoin(cursor, birja, 'CHZ', bcoin, 1, 1, 0)
#     LoadCoin(cursor, birja, 'CYBER', bcoin, 1, 1, 2)
#     #LoadCoin(cursor, birja, 'DAR', bcoin, 1, 1, 45)
#     LoadCoin(cursor, birja, 'DOT', bcoin, 1, 1, 2)
#     #LoadCoin(cursor, birja, 'EGLD', bcoin, 1, 1, 2)
#     #LoadCoin(cursor, birja, 'ETC', bcoin, 1, 1, 2)
#     #LoadCoin(cursor, birja, 'FTM', bcoin, 1, 1, 0)
#     LoadCoin(cursor, birja, 'FIL', bcoin, 1, 1, 2)
#     LoadCoin(cursor, birja, 'FLOW', bcoin, 1, 1, 2)
#     LoadCoin(cursor, birja, 'GALA', bcoin, 1, 1, 0)
#     LoadCoin(cursor, birja, 'GMT', bcoin, 1, 1, 1)
#     LoadCoin(cursor, birja, 'HBAR', bcoin, 1, 1, 0)
#     #LoadCoin(cursor, birja, 'ICP', bcoin, 1, 1, 2)
#     #LoadCoin(cursor, birja, 'ID', bcoin, 1, 1, 0)
# #    LoadCoin(cursor, birja, 'IMX', bcoin, 1, 1, 2)
#     LoadCoin(cursor, birja, 'INJ', bcoin, 1, 1, 1)
#     #LoadCoin(cursor, birja, 'KAVA', bcoin, 1, 0, 1)#delete
#     LoadCoin(cursor, birja, 'LINK', bcoin, 1, 1, 3)
#     LoadCoin(cursor, birja, 'LTC', bcoin, 1, 1, 3)
#     #LoadCoin(cursor, birja, 'LPT', bcoin, 1, 1, 2)
#     LoadCoin(cursor, birja, 'MATIC', bcoin, 1, 1, 1)
#     LoadCoin(cursor, birja, 'MEME', bcoin, 1, 1, 1)
#     LoadCoin(cursor, birja, 'MASK', bcoin, 1, 1, 1)
#     LoadCoin(cursor, birja, 'NEAR', bcoin, 1, 1, 1)
#     #LoadCoin(cursor, birja, 'NEO', bcoin, 1, 1, 2)
#     LoadCoin(cursor, birja, 'RUNE', bcoin, 1, 1, 1)
#     LoadCoin(cursor, birja, 'SAND', bcoin, 1, 1, 0)
#     LoadCoin(cursor, birja, 'SEI', bcoin, 1, 1, 1)
#     LoadCoin(cursor, birja, 'SOL', bcoin, 1, 1, 2)
#     LoadCoin(cursor, birja, 'SUI', bcoin, 1, 1, 1)
#     #LoadCoin(cursor, birja, 'STX', bcoin, 1, 1, 1)
#     #LoadCoin(cursor, birja, 'SNX', bcoin, 1, 1, 1)
#     LoadCoin(cursor, birja, 'UNI', bcoin, 1, 1, 2)
#     LoadCoin(cursor, birja, 'TRX', bcoin, 1, 1, 0)
#     LoadCoin(cursor, birja, 'VET', bcoin, 1, 1, 0)
#     LoadCoin(cursor, birja, 'XLM', bcoin, 1, 1, 0)
#     LoadCoin(cursor, birja, 'XVS', bcoin, 1, 1, 0)
#     LoadCoin(cursor, birja, 'XMR', bcoin, 1, 1, 3)
#     LoadCoin(cursor, birja, 'ICP', bcoin, 1, 1, 2)
#     #LoadCoin(cursor, birja, 'WIN', bcoin, 1, 1, )
    # фиксирование
    conn.commit()
    # удаление лишнего - старого
    db.DeleteTablesNeVSymb(conn, cursor, birja+'\_%')

    #----------------------------------------------------------------------------
    bcoin='USDT'
    birja='binanceusdt'
    # clear
    z="delete from symb where birja='"+birja+"' and bcoin='"+bcoin+"'"
    cursor.execute(z)
    conn.commit()
    # ADD
    LoadCoin(cursor, birja, 'BTC', bcoin, 1, 1, 5)
    LoadCoin(cursor, birja, 'ETH', bcoin, 1, 1, 4)
    LoadCoin(cursor, birja, 'BNB', bcoin, 1, 1, 3)
    LoadCoin(cursor, birja, 'XRP', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'OP', bcoin, 1, 1, 2)#?????????
    LoadCoin(cursor, birja, 'AAVE', bcoin, 1, 1,3)
    LoadCoin(cursor, birja, 'ADA', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'ALGO', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'APE', bcoin, 1, 1,  2)
    LoadCoin(cursor, birja, 'ATOM', bcoin, 1, 1, 2)
    #LoadCoin(cursor, birja, 'ARKM', bcoin, 1, 1, 0)#DELETE TOO LITL V
    LoadCoin(cursor, birja, 'AVAX', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'AXS', bcoin, 1, 1, 2)
    #LoadCoin(cursor, birja, 'BAKE', bcoin, 1, 1, 1)#del
    LoadCoin(cursor, birja, 'BCH', bcoin, 1, 1, 3)
    #LoadCoin(cursor, birja, 'BEL', bcoin, 1, 1, 1)#del
    LoadCoin(cursor, birja, 'CHZ', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'CYBER', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'DAR', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'DOT', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'EGLD', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'ETC', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'FTM', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'FIL', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'FLOW', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'GALA', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'GMT', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'HBAR', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'ID', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'IMX', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'INJ', bcoin, 1, 1, 1)
    #LoadCoin(cursor, birja, 'KAVA', bcoin, 1, 0, 1)#delete
    LoadCoin(cursor, birja, 'LINK', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'LTC', bcoin, 1, 1, 3)
    #LoadCoin(cursor, birja, 'LPT', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'MATIC', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'MEME', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'MASK', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'NEAR', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'NEO', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'RUNE', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'SAND', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'SEI', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'SOL', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'SUI', bcoin, 1, 1, 1)
    #LoadCoin(cursor, birja, 'STX', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'SNX', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'UNI', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'TRX', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'VET', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'XLM', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'XVS', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'XMR', bcoin, 1, 1, 3)
    LoadCoin(cursor, birja, 'ICP', bcoin, 1, 1, 2)
    #LoadCoin(cursor, birja, 'WIN', bcoin, 1, 1, )
    # фиксирование
    conn.commit()
    # удаление лишнего - старого
    db.DeleteTablesNeVSymb(conn, cursor, birja+'\_%')


    #----------------------------------------------------------------------------
    bcoin='USDT'
    birja='okx'
    # clear
    z="delete from symb where birja='"+birja+"' and bcoin='"+bcoin+"'"
    cursor.execute(z)
    conn.commit()
    # ADD
    LoadCoin(cursor, birja, 'WBTC', bcoin, 1, 1, 4)
    LoadCoin(cursor, birja, 'BTC', bcoin, 1, 1, 5)
    LoadCoin(cursor, birja, 'ETH', bcoin, 1, 1, 4)
    LoadCoin(cursor, birja, 'BNB', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'XRP', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'STETH', bcoin, 1, 1, 3)
    #LoadCoin(cursor, birja, 'OKB', bcoin, 1, 1, 1)#no history
    LoadCoin(cursor, birja, 'ADA', bcoin, 1, 1, 0)
    #LoadCoin(cursor, birja, 'DOGE', bcoin, 1, 1, )0.1???????????
    LoadCoin(cursor, birja, 'TON', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'SOL', bcoin, 1, 1, 2)
    #LoadCoin(cursor, birja, 'TRX', bcoin, 1, 1, )0.1?????????????
    LoadCoin(cursor, birja, 'DOT', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'MATIC', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'LTC', bcoin, 1, 1, 2)
    #LoadCoin(cursor, birja, 'SHIB', bcoin, 1, 1, )50000 /?????????
    LoadCoin(cursor, birja, 'BCH', bcoin, 1, 1, 3)
    LoadCoin(cursor, birja, 'LINK', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'UNI', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'XLM', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'AVAX', bcoin, 1, 1, 2) 
    # LoadCoin(cursor, birja, 'XMR', bcoin, 1, 1, 2)ВАБЧЕ УДАЛИЛИ
    LoadCoin(cursor, birja, 'ETC', bcoin, 1, 1, 1)
    LoadCoin(cursor, birja, 'ATOM', bcoin, 1, 1, 1)
    #LoadCoin(cursor, birja, 'HBAR', bcoin, 1, 1, )0.01 ?????????????
    LoadCoin(cursor, birja, 'FIL', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'ICP', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'APT', bcoin, 1, 1, 1)
    #LoadCoin(cursor, birja, 'ARG', bcoin, 1, 1, 3)
    #LoadCoin(cursor, birja, 'ASTR', bcoin, 1, 1, 4)
    LoadCoin(cursor, birja, 'OP', bcoin, 1, 1, 0)#?????????
    LoadCoin(cursor, birja, 'ARB', bcoin, 1, 1, 0)#?????????
    LoadCoin(cursor, birja, 'AAVE', bcoin, 1, 1, 2)
    LoadCoin(cursor, birja, 'AGLD', bcoin, 1, 1, 0)#??????
    LoadCoin(cursor, birja, 'LDO', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'STX', bcoin, 1, 1, 0)
    LoadCoin(cursor, birja, 'IMX', bcoin, 1, 1, 0)
#    LoadCoin(cursor, birja, 'EOS', bcoin, 1, 1, 1)
#    LoadCoin(cursor, birja, 'SAND', bcoin, 1, 1, 0)
#    LoadCoin(cursor, birja, 'BSV', bcoin, 1, 1, 2)
#    LoadCoin(cursor, birja, 'AXS', bcoin, 1, 1, 2)
    # фиксирование
    conn.commit()
    # удаление лишнего - старого
    db.DeleteTablesNeVSymb(conn, cursor, birja+'\_%')

    #----------------------------------------------------------------------------
    bcoin='USDT'
    birja='binance'
    # clear
    z="delete from symb where birja='"+birja+"' and bcoin='"+bcoin+"'"
    cursor.execute(z)
    conn.commit()
        # фиксирование
    conn.commit()
    # удаление лишнего - старого
    db.DeleteTablesNeVSymb(conn, cursor, birja+'\_%')
    
    #-------------------------------------------------------------------------------
    conn.commit()
    conn.close()
    cursor.close()
    #
# CreateTableSymb()
LoadTableSymb()