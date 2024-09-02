import small
import db
import load_price
import mysql.connector

import sys

coin1='nocoinn'
bcoin1='noc'
birja1='nob'
if __name__ == "__main__":
    next=0
    for param in sys.argv:
        print ('argument for bybit_go_AddNewPriceForCoin'+param)
        if next==1:
            birja1=param
        if next==2:
            coin1=param
        if next==3:
            bcoin1=param
        next+=1


print("Added notes: birja="+birja1+" coin="+coin1+" bcoin="+bcoin1)


    #обновляем новые цены для конкретной монеты
while True:
    ret=load_price.AddPricesNewOrOld(True, birja1, coin1, bcoin1, None)
    print('Added '+str(ret))
    if ret<10:
        break

