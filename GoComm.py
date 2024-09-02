import os
import simplejson
import db
import small
import asyncio
import tabulate
import pandas as pd
import matplotlib.pyplot as plt

def PrintHelp(strpar):
    if strpar!='-h': return False
    print('Help')
    print('-h Help')
    print('-p 0.0003 0.5 okx ...up porabola')
    print('      0.04--: in test, 0.0087--: 6 h, 0.0047--: 12 h, 0.0022: 1 day, 0.0012: 2 days, ')
    print('      0.0005: 5 days, 0.0003: 10 days, 0.00014: 20 days, 0.00008: 30 days ')
    print('-pv okx ...show pordabola as text')
    print('-pvg okx ...show pordabola as grafic')
    print('-ic 0.9 ...index nastroeniya crypta')
    print('-iv')
    print('-sk on okx ... -sk off bybit ... StopKran For Buy Coins')
    print('-skv all')
    print('-strbd on 3.2 okx, -strbd off bybit')
    print('-strbdv all')

    return True

def GetBM(birja):
    ret=[]
    if birja=='okx': ret.append('okx')
    if birja=='bybit': ret.append('bybit')
    if birja=='binanceusdt': ret.append('binanceusdt')
    if birja=='finam': ret.append('finam')
    if birja=='all': 
        ret.append('okx')
        ret.append('bybit')
        ret.append('binanceusdt')
        ret.append('finam')
    return ret


def Set_Index_Nastroeniya(strpar:str):
    sm=strpar.split()
    if len(sm) !=  2: return False
    if sm[0] != '-ic': return False
    ina=small.GetFloatFromAll(sm[1])
    if ina < 0.7 or ina > 1.3:
        print('Error 2345. Index nastroeniya is from 0.7 to 1.3')
        return False
    db.MakeCommand("update  peremenniye set perznachenie="+str(ina)+"  where pername='IndexNastroeniyaCrypta'")
    Show_Index_Nastroeniya('-iv')
    return True

def Set_Start_Stop(strpar:str):
    bm=GetBM('all')
    sm=strpar.split()
    if len(sm) !=  3: return False
    if sm[0] != '-sk': return False
    kuda=sm[1]
    if kuda !='on' and kuda != 'off':
        print('Format: -sk on okx, -sk off bybit')
        return False
    bm=GetBM(sm[2])
    if len(bm)==0: 
        print('Format: -sk on okx, -sk off bybit')
        return False
    for b1 in bm:
        an='StopKran_'+'Algo_606_'+b1
        per='True' if kuda=='on'  else 'False'
        db.AddUpdate_peremenniye(an, str(per))
        #show 
        Show__Start_Stop('-skv '+b1)
    return True


def Set_Strat_BigDoun_On(strpar:str):
    sm=strpar.split()
    if len(sm) != 4: return False
    bm=GetBM(sm[3])
    if sm[0] != '-strbd' or sm[1] !='on' or small.is_number(sm[2]) != True or len(bm)==0:
        if sm[0] == '-strbd' and sm[1] =='on': print('Format: -strbd on 3.2 okx, -strbd off bybit')
        return False
    for b1 in bm:
        an='Strat_BigDoun_'+'Algo_606_'+b1
        db.AddUpdate_peremenniye(an, 'True')
        an='Strat_BigDoun_Size_'+'Algo_606_'+b1
        db.AddUpdate_peremenniye(an, str(sm[2]))
        #show 
        Show_Strat_BigDoun('-strbdv '+b1)
    return True

def Set_Strat_BigDoun_Off(strpar:str):
    sm=strpar.split()
    if len(sm) != 3: return False
    bm=GetBM(sm[2])
    if sm[0] != '-strbd' or sm[1] !='off' or  len(bm)==0:
        if sm[0] == '-strbd' and sm[1] =='off': print('Format: -strbd on 3.2 okx, -strbd off bybit')
        return False
    bm=GetBM(sm[2])
    for b1 in bm:
        an='Strat_BigDoun_'+'Algo_606_'+b1
        db.AddUpdate_peremenniye(an, 'False')
        #show 
        Show_Strat_BigDoun('-strbdv '+b1)
    return True

def Show_Strat_BigDoun(strpar:str):
    bm=GetBM('all')
    if strpar != '-strbdv':
        sm=strpar.split()
        if len(sm) !=  2: return False
        if sm[0] != '-strbdv': return False
        bm=GetBM(sm[1])
        if len(bm)==0: return False
    # show
    for b1 in bm:
        an='Strat_BigDoun_'+'Algo_606_'+b1
        f1=db.GetPerFromPremennie(None, an, 'bool', None, None, None)
        an='Strat_BigDoun_Size_'+'Algo_606_'+b1
        n1=db.GetPerFromPremennie(None, an, 'float', None, None, None)
        #show 
        print('-strbdv '+b1+' '+str(f1)+' '+str(n1))
    return True


def Show_Index_Nastroeniya(strpar:str):
    if strpar != '-iv':  return False
    rows=db.GetSel77(None, "select  perznachenie from peremenniye where pername='IndexNastroeniyaCrypta'")
    note1=small.GetCorrectOneNoteFromRowsAsOne(rows)
    if note1 is None:
        print('Error 3467834')
        return False
    ina=float(note1)
    print('Index nastroeniya crypta: '+str(ina))

def Show_XMul_XMinOut_birja(strpar:str):
    bm=GetBM('all')
    if strpar != '-pv':
        sm=strpar.split()
        if len(sm) !=  2: return False
        if sm[0] != '-pv': return False
        bm=GetBM(sm[1])
        if len(bm)==0: return False
    # show
    df=WriteDF_For_XMul_XMinOut(bm, 0)
    if df is None: return False
    print(df)
    return True


def WriteDF_For_XMul_XMinOut(bm,algopar=55):
    # заполнение точками по времени минимального процента
    # show
    df=pd.DataFrame()
    df['time']=''
    sm=[]
    for b1 in bm:
        timepar, buytime, XMul, XMinOut =  1, 1, 1, 1
        an='XMul_'+'Algo_606_'+b1
        rows=db.GetSel77(None, "select  perznachenie from peremenniye where pername='"+an+"'")
        note1=small.GetCorrectOneNoteFromRowsAsOne(rows)
        if note1 is None:
            print('Error 34678')
            return None
        XMul=float(note1)
        an='XMinOut_'+'Algo_606_'+b1
        rows=db.GetSel77(None, "select  perznachenie from peremenniye where pername='"+an+"'")
        note1=small.GetCorrectOneNoteFromRowsAsOne(rows)
        if note1 is None:
            print('Error 34678')
            return None
        XMinOut=float(note1)
        m2=[b1, timepar, buytime, XMul, XMinOut]
        sm.append(m2)
        df[b1]=''
    plus2=5*60*1000
    while True:
        plus2=int(plus2*1.2)
        time1=int(plus2/(60*60*1000))
        pm=[time1]
        for s1 in sm:
            small.SetAlgoName('Algo_606_'+s1[0])
            period=small.GetPeriod()
            # CalcProcent55(buytime, timepar, XMul, XMinOut):
            # CalcProcent88(buytime, timepar, period, XMinOut):
            if algopar==55: p1=small.CalcProcent55(0,plus2, s1[3], s1[4])
            elif algopar==88: p1=small.CalcProcent88(0,plus2, period, s1[4])
            else: p1=small.CalcProcentMinOut(0,plus2, period, s1[3], s1[4])
            if p1 < -10: p1=222
            pm.append(p1)
        df.loc[ len(df.index )] = pm
        if plus2 > 33*24*60*60*1000: 
            break
    # столбик с флагами - пусто
    df['empty']=1
    for b1 in bm:
        df.loc[(df['empty']==1) & (df[b1]==222), 'empty'] = 0
    # print(df)
    df = df.loc[df['empty'] != 0]
    # print(df)
    df['hour']=df['time']
    df['hour'] = df['hour'].astype('string')
    df['hour'] = df['hour'].apply(lambda x: x+' h')
    df['day']=df['time'].apply(lambda x: round(x/24,0))
    df['day'] = df['day'].astype('string')
    df['day'] = df['day'].apply(lambda x: x+' day')
    return df

def Show_XMul_XMinOut_Grafic_birja(strpar:str):
    bm=GetBM('all')
    if strpar != '-pvg':
        sm=strpar.split()
        if len(sm) !=  2: return False
        if sm[0] != '-pvg': return False
        bm=GetBM(sm[1])
        if len(bm)==0: return False
    # show
    df00=WriteDF_For_XMul_XMinOut(bm, 0)
    if df00 is None: return False
    df55=WriteDF_For_XMul_XMinOut(bm, 55)
    if df55 is None: return False
    df88=WriteDF_For_XMul_XMinOut(bm, 88)
    if df88 is None: return False
    # 
    x00 = df00.index.values.tolist ()
    x55 = df55.index.values.tolist ()
    x88 = df88.index.values.tolist ()
    for b1 in bm:
        y00=df00[b1]. tolist ()
        plt.plot(x00, y00, 'r-', linewidth=5)
        y55=df55[b1]. tolist ()
        plt.plot(x55, y55, 'b-')
        y88=df88[b1]. tolist ()
        plt.plot(x88, y88, 'g-')
        for x1 in x55:
            if x1 == 0: continue
            if df55.at [x1-1, 'time'] != df55.at [x1, 'time']:
                plt.axvline (x=x1, linestyle=':', marker='*', color='y')
        plt.axhline (y=0, linestyle=':', color='y')
        plt.xlabel('Дни') #Подпись для оси х
        plt.ylabel('Старт  '+str(round(df55.at [0, b1], 2))+'%') #Подпись для оси y
        plt.title(b1) #Название
        plt.show()
        gygy=0
    return True

def Show__Start_Stop(strpar:str):
    bm=GetBM('all')
    if strpar != '-skv':
        sm=strpar.split()
        if len(sm) !=  2: return False
        if sm[0] != '-skv': return False
        bm=GetBM(sm[1])
        if len(bm)==0: return False
    # show
    for b1 in bm:
        an='StopKran_'+'Algo_606_'+b1
        note1=db.GetPerFromPremennie(None, an, 'bool', True, False, True)
        print('StopKran '+b1+' '+str(note1))
    return True


def Set_XMul_XMinOut_birja(strpar:str):
    sm=strpar.split()
    if len(sm) !=  4: return False
    if sm[0] != '-p': return False
    XMul, XMinOut, birja = sm[1], sm[2], sm[3]
    try:
        XMul=float(XMul)
        XMinOut=float(XMinOut)
        if birja!='okx' and birja!='bybit' and birja!='binanceusdt' and birja!='finam' and birja!='all': small.ifnoterr(4==9)
    except:
        print('Error parametrs')
        return False
    # write
    bm=GetBM(birja)
    for b1 in bm:
        an='XMul_'+'Algo_606_'+b1
        db.AddUpdate_peremenniye(an, str(XMul))
        an='XMinOut_'+'Algo_606_'+b1
        db.AddUpdate_peremenniye(an, str(XMinOut))
    #show 
    Show_XMul_XMinOut_birja('-pv '+birja)
    return True


def main():
    print('Main')
    # Set_XMul_XMinOut_birja('-p 0.0003 0.5 finam')
    # Show_XMul_XMinOut_Grafic_birja('-pvg finam')
    # Show_XMul_XMinOut_birja('-pv finam')
    #Set_Start_Stop('-sk off bybit')
    #Show_Strat_BigDoun('-strbdv all')
    # Set_Strat_BigDoun_Off('-strbd  off  okx')
    # Set_Strat_BigDoun_On('-strbd  on 2.4  okx')
    Set_XMul_XMinOut_birja('-p 0.0005 0.6 finam')
    Show_XMul_XMinOut_birja('-pv finam')
    Show_XMul_XMinOut_Grafic_birja('-pvg finam')
    while True:
        c1 = input("Command: ")
        PrintHelp(c1)
        Set_XMul_XMinOut_birja(c1)
        Show_XMul_XMinOut_birja(c1)
        Set_Index_Nastroeniya(c1)
        Show_Index_Nastroeniya(c1)
        Show_XMul_XMinOut_Grafic_birja(c1)
        Set_Start_Stop(c1)
        Show__Start_Stop(c1)
        Set_Strat_BigDoun_Off(c1)
        Set_Strat_BigDoun_On(c1)
        Show_Strat_BigDoun(c1)


if __name__ == '__main__':
    main()