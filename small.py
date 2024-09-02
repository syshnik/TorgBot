from pybit.unified_trading import HTTP
#pip install pybit

from datetime import datetime 
from time import sleep
import time
import requests 
import json
import math
import os
# -------------------------------sound------------------------------------
# import simpleaudio as simple_audio 
# from playsound import playsound
# from pydub import AudioSegment 
# from pydub.playback import play
import winsound 
# -------------------------------sound------------------------------------
 

from scipy. special import expit


# глобальная переменная для отладки - поиска множителя сигмоида
vector_for_podschet=0
def AddVector(vector):
    global vector_for_podschet
    vector_for_podschet=vector
def GetVector():
    global vector_for_podschet
    return vector_for_podschet

def PopravkaNaVextor():
    return 0.13

# -------------------------------------------------------------
def is_number(strpar):
    try:
        f1=float(strpar)
        str1=str(f1)
        if strpar == str1: return True
        return False
    except ValueError:
        return False

def is_birja(bname):
    bm=['okx','bybit',  'binanceusdt','finam']
    for birja in bm:
        if birja==bname: return True
    return False

def Sigmoid(x, maxx, andminus):
    # Значение сигмовидной функции для x = 2,5 равно 0,924
    x=x*2.3/maxx
    x=expit(x)
    if andminus:
        x=x*2-1
    return  x

def SikokoTrue(*args):
    ret=0
    for i in args:
        if i: ret+=1
    return ret

    
# def GetByBitTime() :
#     #время сервера 
#     r = requests.get('https://api.bybit.com/v5/market/time')
#     code1=r.status_code
#     ifnoterr(code1 == 200)
#     t2=r.text
#     j3=json.loads(t2)
#     j4=j3["retMsg"]
     #ifnoterr(j4 == 'OK')
#     rettime=j3["time"]
#     return rettime
# ---------------------------------------------- debug flags -----------------------------------
def ItDebug():
    # ok is False
    return False

def ItDebugCorrectSigmoid():
    # ok is False
    return False

def ItInTry():
    #ok is True
    algo=GetAlgoName()
    if algo == 'Algo_606_finam_simulgame': return True
    if algo == 'Algo_606_finam_smsgame': return True
    if algo == 'Algo_606_finam': return False
    if algo == 'Algo_606_okx': return True
    if algo == 'Algo_606_okx_simulgame': return True
    if algo == 'Algo_606_bybit_smsgame': return True
    if algo == 'Algo_606_bybit': return True
    if algo == 'Algo_606_binanceusdt': return True
    if algo == 'Algo_606_binanceusdt_simulgame': return True
    if algo == 'Algo_606_binanceusdt_smsgame': return False
    return True

def ItInTryAddPrices():
    #ok is True
    algo=GetAlgoName()
    if algo == 'Algo_606_finam_simulgame': return True
    if algo == 'Algo_606_finam_smsgame': return True
    if algo == 'Algo_606_finam': return True
    if algo == 'Algo_606_okx': return True
    if algo == 'Algo_606_okx_simulgame': return True
    if algo == 'Algo_606_bybit_smsgame': return True
    if algo == 'Algo_606_bybit': return True
    if algo == 'Algo_606_binanceusdt': return True
    if algo == 'Algo_606_binanceusdt_simulgame': return True
    if algo == 'Algo_606_binanceusdt_smsgame': return True
    print ('Error 44445555')
    ff=7/0
    return True

def ItDebugNotTestWallet():
    # ok is False
    return False

def ItDebugBuySell(long_or_buy=None):
    #ok is False
    # подряд покупает и продает
    ret=None
    algo=GetAlgoName()
    if algo == 'Algo_606_finam_simulgame': ret=False
    if algo == 'Algo_606_finam_smsgame': ret=False
    if algo == 'Algo_606_finam': ret=False
    if algo == 'Algo_606_okx': ret=False
    if algo == 'Algo_606_okx_simulgame': ret=False
    if algo == 'Algo_606_bybit_smsgame': ret=False
    if algo == 'Algo_606_bybit': ret=False
    if algo == 'Algo_606_binanceusdt': ret=False
    if algo == 'Algo_606_binanceusdt_simulgame': ret=False
    if algo == 'Algo_606_binanceusdt_smsgame': ret=False
    if ret is None:
        print ('Error 4444555523')
        ff=7/0
    if long_or_buy is None:
        if ItDebugBuySell(True) or ItDebugBuySell(False): return True
    elif  long_or_buy==True:
        #ok is False
        return ret
    elif  long_or_buy==False:
        #ok is False
        return ret
    else:
        gg=7/0        

def ItDebugRandBuySell():
    #ok is False
    # в случайном порядке покупает и продает
    algo=GetAlgoName()
    if algo == 'Algo_606_finam_simulgame': return False
    if algo == 'Algo_606_finam_smsgame': return False
    if algo == 'Algo_606_finam': return False
    if algo == 'Algo_606_okx': return False
    if algo == 'Algo_606_okx_simulgame': return False
    if algo == 'Algo_606_bybit_smsgame': return False
    if algo == 'Algo_606_bybit': return False
    if algo == 'Algo_606_binanceusdt': return False
    if algo == 'Algo_606_binanceusdt_simulgame': return False
    if algo == 'Algo_606_binanceusdt_smsgame': return False
    print ('Error 44445555')
    ff=7/0
    return False

def ItJdem5Minut():
    #ok is True
    algo=GetAlgoName()
    if algo == 'Algo_606_finam_simulgame': return True
    if algo == 'Algo_606_finam_smsgame': return True
    if algo == 'Algo_606_finam': return True
    if algo == 'Algo_606_okx': return True
    if algo == 'Algo_606_okx_simulgame': return True
    if algo == 'Algo_606_bybit_smsgame': return True
    if algo == 'Algo_606_bybit': return True
    if algo == 'Algo_606_binanceusdt': return True
    if algo == 'Algo_606_binanceusdt_simulgame': return True
    if algo == 'Algo_606_binanceusdt_smsgame': return False
    print ('Error 44445555')
    ff=7/0
    return False

def ItSimulatorBuySell():
    #ok is False
    algo=GetAlgoName()
    if algo == 'Algo_606_finam_simulgame': return True
    if algo == 'Algo_606_finam_smsgame': return True
    if algo == 'Algo_606_finam': return True
    if algo == 'Algo_606_okx': return False
    if algo == 'Algo_606_okx_simulgame': return True
    if algo == 'Algo_606_bybit_smsgame': return True
    if algo == 'Algo_606_bybit': return False
    if algo == 'Algo_606_binanceusdt': return False
    if algo == 'Algo_606_binanceusdt_simulgame': return True
    if algo == 'Algo_606_binanceusdt_smsgame': return True
    print ('Error 44445555')
    ff=7/0
    return False

def ItSMSBuySell():
    #ok is SMS
    algo=GetAlgoName()
    # if algo == 'Algo_606_finam_simulgame': return True
    if algo == 'Algo_606_finam_smsgame': return True
    # if algo == 'Algo_606_finam': return True
    # if algo == 'Algo_606_okx': return False
    if algo == 'Algo_606_bybit_smsgame': return True
    if algo == 'Algo_606_binanceusdt_smsgame': return True
    # if algo == 'Algo_606_bybit': return False
    # if algo == 'Algo_606_binanceusdt': return False
    # print ('Error 44445555')
    # ff=7/0
    return False

def ItSimulatorPrice():
    #ok is False
    algo=GetAlgoName()
    if algo == 'Algo_606_finam_simulgame': return False
    if algo == 'Algo_606_finam_smsgame': return False
    if algo == 'Algo_606_finam': return False
    if algo == 'Algo_606_okx': return False
    if algo == 'Algo_606_okx_simulgame': return False
    if algo == 'Algo_606_bybit_smsgame':  return False
    if algo == 'Algo_606_bybit': return False
    if algo == 'Algo_606_binanceusdt': return False
    if algo == 'Algo_606_binanceusdt_simulgame': return False
    if algo == 'Algo_606_binanceusdt_smsgame': return False
    print ('Error 44445555')
    ff=7/0
    return False

def ItSimulatorBallance():
    #ok is False
    algo=GetAlgoName()
    if algo == 'Algo_606_finam_simulgame': return True
    if algo == 'Algo_606_finam_smsgame': return True
    if algo == 'Algo_606_finam': return True
    if algo == 'Algo_606_okx': return False
    if algo == 'Algo_606_okx_simulgame': return True
    if algo == 'Algo_606_bybit_smsgame':  return True
    if algo == 'Algo_606_bybit': return False
    if algo == 'Algo_606_binanceusdt': return False
    if algo == 'Algo_606_binanceusdt_simulgame': return True
    if algo == 'Algo_606_binanceusdt_smsgame': return True
    print ('Error 44445555')
    ff=7/0
    return False

def ItDebugAddPrice():
    #ok is False
    return False

def ItTestGo():
    # ok is False
    return False
# ---------------------------------------------- debug flags -----------------------------------


def GetFloatFromAll(str):
    try:
        ret=float(str)
        return ret
    except ValueError:
        return float(0)
    
def GetIntFromAll(str):
    try:
        ret=int(str)
        return ret
    except ValueError:
        return int(0)
    
def ifnoterr(par):
    try:
        if (par != True):
            raise Exception("Error Connect")
    except ValueError:
        print("Error Connect 2")

def GetBCoin(birja):
    bcoin="USDT"
    if birja=="binancebnb": bcoin="BNB"
    if birja=="finam": bcoin="RUB"
    return bcoin

def GetTimeS():
    #Запрос спецификации инструмента онлайн-торговых пар.
    #try:
    from pybit.unified_trading import HTTP
    session = HTTP(testnet=True)
    #print("------------get_instruments_info---------------")
    ret55=session.get_instruments_info(
        category="linear",
        symbol="BTCUSDT",
    )
    return ret55["time"]
    # except :
    #     print("Error. def GetTimes):")
    #     return None

def GetIntTimeFromDateTime(bt1):
    now2 = datetime.now()
    time_diff = now2 - bt1
    tsecs =int( time_diff.total_seconds() )*1000
    milliseconds = int(round(time.time() * 1000))
    return milliseconds-tsecs

def GetMaxCountZnakPosleZ(number1, number2, number3):
    #Надо  определить MAX кол-во знаков после запятой в этом числе.
    s1 = str(number1)
    cout1=abs(s1.find('.') - len(s1)) - 1
    s2 = str(number2)
    cout2=abs(s2.find('.') - len(s2)) - 1
    s3 = str(number3)
    cout3=abs(s3.find('.') - len(s3)) - 1
    coutret=cout1
    if coutret < cout2:
        coutret=cout2
    if coutret < cout3:
        coutret=cout3
    return coutret


# def GetInstrument(simbolpar):
#     #Запрос спецификации инструмента онлайн-торговых пар.
#     try:
#         from pybit.unified_trading import HTTP
#         session = HTTP(testnet=True)
#         #print("------------get_instruments_info---------------")
#         ret55=session.get_instruments_info(
#             category="linear",
#             symbol=simbolpar,
#         )
#         return ret55
#     except :
#         print("Error. def GetTimes):")
#         return None


#вычисление последних свечей
def GetLastKline(simbolpar, categorypar):
    #try:
    session = HTTP(testnet=True)
    #Запрос исторических клинов (также известных как свечи/подсвечники). Диаграммы возвращаются группами
    #  в зависимости от запрошенного интервала.
    r3=session.get_kline(
        category=categorypar,
        symbol=simbolpar,
        interval=1,
        start=GetTimeS()-60*1000,
        end=GetTimeS(),
    )
    return r3
    # except :
    #     print("Error. def Get 3566442")
    #     return None


#вычисление среднего процента свечей
def GetSredniyPercentKline(simbolpar):
    #try:
    session = HTTP(testnet=True)
    #Запрос исторических клинов (также известных как свечи/подсвечники). Диаграммы возвращаются группами
    #  в зависимости от запрошенного интервала.
    r3=session.get_kline(
        category="inverse",
        symbol=simbolpar,
        interval=15,
        start=GetTimeS()-24*60*60*1000,
        end=GetTimeS(),
    )
    r6=r3['retMsg']
    ifnoterr(r6 == 'OK')
    list1=r3['result']['list']
    sik1=0
    retper=float(0)
    for i in list1:
        #print(i[0], " ", i[1], " ", i[2], " ", i[3], " ", i[4], " ", i[5], " ", i[6])
        min1=min(i[1], i[2], i[3], i[4])
        max1=max(i[1], i[2], i[3], i[4])
        per1=(float(max1)-float(min1))*100/float(min1)
        #print(min1, " ", max1, ", ", per1)
        retper=retper+per1
        sik1=sik1+1
    if sik1 != 0:
        retper=retper/sik1
    return retper
        #print(sik1, 'percent ', retper) 
    # except :
    #     print("Error. def Get 3566442")
    #     return None


# def GetHist(simbolpar, limit1, start1, end1, shag1):
#     ifnoterr(start1 < end1)
#     if start1+shag1*60*1000 > end1:
#         return None
#     #try:
#     session = HTTP(testnet=True)
#     #Запрос исторических ценовых линий марки. Диаграммы возвращаются группами в зависимости от запрошенного интервала.
#     r3=session.get_mark_price_kline(
#         category="inverse",
#         symbol=simbolpar,
#         interval=str(shag1),
#         start=start1,
#         end=end1,
#         limit=limit1,
#     )
#     r6=r3['retMsg']
#     ifnoterr(r6 == 'OK')
#     list1=r3['result']['list']
#     return list1
    # except :
    #     print("Error. def GetHist(simbolpar, limit1, start1, end1):")
    #     return None



def SleepSecund(sikoko, oldtime):
    #ждем определенное количество времени
    now1 = datetime.now()
    if oldtime == None:
        tsecs=0
    else:
        time_diff = now1 - oldtime
        tsecs = time_diff.total_seconds()
    #уже переждали
    if tsecs >= sikoko:
        return now1
    #надо еще подождать
    sleep(sikoko - tsecs)
    return now1



def adder(*nums):
    ret=''
    for n in nums:
        ret += '' + str(n)
    return ret

def RoundToMin(par111, sikokoznakov111):
    par=float(par111)
    sikokoznakov=int(sikokoznakov111)
    for i in range(1, sikokoznakov + 1):
        par=par*10
    par = math.floor(par)
    for i in range(1, sikokoznakov + 1):
        par=par/10
    par=round(par, sikokoznakov)
    return par


def GetTableName(birjapar, coinpar):
    tname=None
    if coinpar == 'srednee' or coinpar == 'bigsrednee':
        if birjapar=='bybit': tname='bybi_t_'+coinpar
        if birjapar=='finam': tname='fina_m_'+coinpar
        if birjapar=='binancebnb': tname='binanc_ebnb_'+coinpar
        if birjapar=='binanceusdt': tname='binanc_eusdt_'+coinpar
        if birjapar=='okx': tname='ok_x_'+coinpar+'_usdt'
        yggy=0
    else:
        if birjapar=='bybit': tname='bybit_'+coinpar
        if birjapar=='finam': tname='finam_'+coinpar
        if birjapar=='binancebnb': tname='binancebnb_'+coinpar+'_bnb'
        if birjapar=='binanceusdt': tname='binanceusdt_'+coinpar+'_usdt'
        if birjapar=='okx': tname='okx_'+coinpar+'_usdt'
    return tname

def CalcProcentMinOut(buytime, timepar, period, XMul, XMinOut):
    r55=CalcProcent55(buytime, timepar, XMul, XMinOut)
    r88=CalcProcent88(buytime, timepar, period, XMinOut)
    if r88 < 0 : r88=0
    return r55+r88

def CalcProcent55(buytime, timepar, XMul, XMinOut):
    x=(buytime-timepar)/(5*60*1000)
    x=x*XMul # чем меньше тем длиннее
    # plus1 = XMinOut-0.9*x*x + 1.7*x 
    plus1 = XMinOut-0.9*x*x 
    return plus1

def CalcProcent88(buytime, timepar, period, XMinOut):
    global cryptoflag555555
    h1=(timepar-buytime)/(60*60*1000)
    ret=0
    plus1=0
    if timepar != buytime: plus1=-CalcProcent88(0, 0, period, XMinOut)
    if period == 2:
        ret=plus1-0.04*period*(h1-period)*(h1-period)
    elif period==4:
        ret=plus1-0.008*period*(h1-period)*(h1-period)
    elif period==8:
        ret=plus1-0.002*period*(h1/2-period)*(h1/2-period)
    elif period==24:
        if cryptoflag555555:
            # crypto
            ret=plus1-0.00012*period*(h1/3-period)*(h1/3-period)
        else:
            # finam
            ret=plus1-0.00010*period*(h1/5-period)*(h1/5-period)
    else:
        gg=6/0

    return ret


algo555555555=''
cryptoflag555555=None

def SetAlgoName(newname:str):
    global algo555555555
    global cryptoflag555555
    algo555555555=newname
    if newname.find("finam") == -1:
        cryptoflag555555=True
    else:
        cryptoflag555555=False

def GetAlgoName(tolkoalgo=False):
    global algo555555555
    if tolkoalgo:
        ret=str(algo555555555)
        # if b11 == 'simulgame': plusalgo100500="_"+b11
        # if b11 == 'smsgame': plusalgo100500="_"+b11
        ret=ret.replace('_simulgame', '')
        ret=ret.replace('_smsgame', '')
        return ret
    return algo555555555

def GetBirjaNameFromAlgo():
    global algo555555555
    if algo555555555.find("bybit") != -1: return 'bybit'
    if algo555555555.find("okx") != -1: return 'okx'
    if algo555555555.find("binanceusdt") != -1: return 'binanceusdt'
    if algo555555555.find("finam") != -1: return 'finam'
    print('Erroer 23255232456')
    gg=7/0
    return ''

def GetPeriod():
    an=GetAlgoName(True)
    if an=='Algo_606_finam': return 24
    return 24

def DeleteFileWhile(path):
    # path = "d:/BS/Save/WORK/Programm/bi/pyexe/dist/Go_run_606.exe"
    del5=False
    while del5==False:
        try:
            os.remove(path)
            del5=True
        except OSError:
            v1=OSError
            print("Не могу удалить файл "+path+"!")
            sleep(11)
            pass
    print(path+" удален.")

def PlaySSSSSSSSSSS(PlaySownd):
    if PlaySownd:
        gg=0
        # wave_object = simple_audio.WaveObject.from_wave_file( "d:\\BS\\Save\\WORK\\Programm\\Sounds\\av3.wav"  ) 
        # play_object = wave_object.play( ) 
        # play_object.wait_done( )   
        # playsound("av3.wav" )
        # playsound("d:\\BS\\Save\\WORK\\Programm\\Sounds\\av3.wav" )
        # sound_audio = AudioSegment.from_wav("d:\\BS\\Save\\WORK\\Programm\\Sounds\\av3.wav") 
        # play( sound_audio ) 
        winsound.PlaySound( "d:\\BS\\Save\\WORK\\Programm\\Sounds\\av3.wav", winsound.SND_FILENAME ) 

def PlaySSSSSSSSSSSWAV(filewav):
    gg=0
    # wave_object = simple_audio.WaveObject.from_wave_file( "d:\\BS\\Save\\WORK\\Programm\\Sounds\\av3.wav"  ) 
    # play_object = wave_object.play( ) 
    # play_object.wait_done( )   
    # playsound("av3.wav" )
    # playsound("d:\\BS\\Save\\WORK\\Programm\\Sounds\\av3.wav" )
    # sound_audio = AudioSegment.from_wav("d:\\BS\\Save\\WORK\\Programm\\Sounds\\av3.wav") 
    # play( sound_audio ) 
    winsound.PlaySound( "d:\\BS\\Save\\WORK\\Programm\\Sounds\\"+filewav, winsound.SND_FILENAME ) 


def GetCorrectOneNoteFromRowsAsOne(rows):
    ret=None
    try:
        ret=rows[0][0]
    except:
        ret=None
    return ret
def GetCorrectOneFloatNoteFromRowsAsOne(rows):
    ret=None
    try:
        ret=float(rows[0][0])
    except:
        ret=None
    return ret

def GetPlusName223345656(oldot):
    oldot=oldot-oldot%(5*60*1000)
    plusnammassive='_test_'+str(oldot)+'_'
    return plusnammassive

def str5(strpar):
    if strpar is None: return 'no'
    return str(round(strpar, 2))
