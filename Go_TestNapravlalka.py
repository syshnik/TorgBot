from  napravlalka import NapravlalkaClass
import  db
c1='op'
rows=db.GetSel77(None, "select max(id)   from bybit_"+c1)
id=int(rows[0][0])
#id=1708506000000
for i in range(0, 111):
    id=id-4*60*60*1000
    # размер день  по 15 мин и запас
    nc1=NapravlalkaClass(id , 'bybit', c1, True, True, 0.2, 0.1, 80, 14, 2,12, True, True, True, 3, None)
    ret=nc1.CalcNapravlalka(None)
    ncdrdrdr=0
for i in range(0, 111):
    id=id-4*60*60*1000
    # размер 1-2 недели  по 15 мин и запас
    nc1=NapravlalkaClass(id , 'bybit', c1, True, True, 0.2, 0.1, 80, 2*12, 2,12,  True, True, True, 3, None)
    nc1.CalcNapravlalka(None)
    ncdrdrdr=0

    # ShowGrafici, ShowRealFuture, RealProcFutureUp, RealProcFutureDoun