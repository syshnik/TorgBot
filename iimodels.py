

from __future__ import print_function
import random
import small
import db
# from iireshalka import iireshalkaclass
# from iireshalka_2 import iireshalkaclass_2
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import matplotlib.pyplot as plt                              # построение графиков
# # Moving to GPU
# tensor_gpu = tensor_from_list.to('cuda')
# # Moving back to CPU
# tensor_cpu = tensor_gpu.to('cpu')
#print(torch.cuda.is_available()) # Should print True
from time import sleep
import array as arr 
#import torch
#import torch.nn as nn
import torch.optim as optim
import numpy as np
# https://qudata.com/ml/ru/NN_Base_Torch_NN.html
import moonphase

from datetime import datetime 


class class55:

    def GetOneMul(self, maxnote, note):
         maxnote=float(maxnote)
         note=float(note)
         maxnote=maxnote*2
         if note > maxnote: note=maxnote
         if note < 0: note=float(0)
         return note/maxnote

    def GetOne(self, maxnote, note):
         maxnote=float(maxnote)
         note=float(note)
         if note > maxnote: note=maxnote
         if note < 0: note=float(0)
         return note/maxnote
    
    def GetOne_M_do_05_P_posle_05(self, maxnote, note):
         # формат: -10 >>> 0.4           10 >>> 0.6
         maxnote=float(maxnote)
         note=float(note)
         if note > maxnote: note=maxnote
         if note < -maxnote: note=-maxnote
         # >> 0.5
         note=note/2
         note=note/maxnote
         ret = 0.5+note
         return ret
    
    def RetIf_M(self,par):
            if par < 0:
                    return -float(par)
            return float(0)
    
    def RetIf_P(self,par):
            if par > 0:
                    return float(par)
            return float(0)
    def RetIf_M(self,par):
            if par < 0:
                    return -float(par)
            return float(0)
    
    def RetIf_P(self,par):
            if par > 0:
                    return float(par)
            return float(0)

class class55plus(class55):
    def __init__(self):
        super(class55, self).__init__()
        self._Nastroy_WeekDay=0
        self._Nastroy_MoonPhase=0
        self._Nastroy_TimeMin=0
        self._Nastroy_TimeHour=0
        self._timeid=0


    def InitNastroyTime_NoCursor(self, cursor):
        # conn=db.GetConnect()
        # cursor = conn.cursor()
        self.InitNastroyTime(cursor)
        # conn.commit()
        # conn.close()
        # cursor.close()
         
    def InitNastroyTime(self, cursor):
        # дата текущего положения
        rows=db.GetSel55(cursor, "SELECT max(perznachenie) FROM peremenniye WHERE  pername='bybit_time_as_ms'")
        if len(rows) != 1: return False
        secund1=int((int(self._timeid)-int(rows[0][0]))/1000)
        rows=db.GetSel55(cursor, "SELECT ((perznachenie)) FROM peremenniye WHERE  pername='bybit_time_as_date'")
        if len(rows) != 1: return False
        date1=rows[0][0]
        rows=db.GetSel55(cursor, "SELECT DATE_ADD('"+date1+"', INTERVAL "+str(secund1)+" SECOND)")
        if len(rows) != 1: return False
        date2=rows[0][0]
        #деньнедели, луный календарь...
        # Создание объекта datetime
        date = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

        # Вывод дня недели
        self._Nastroy_WeekDay=date.weekday()
        #время
       # t1 = dt.now().time()
        #l1 = str(t1).split(":")
        self._Nastroy_TimeHour=date.hour
        self._Nastroy_TimeMin=date.minute
        #фазы луны
        #self._Nastroy_MoonPhase=moonphase.GetMoonPhasePar()
        self._Nastroy_MoonPhase=moonphase.GetMoonPhasePar(date)
        return True


class model100(nn.Module):
    def __init__(self):        
#        lsizes = arr.array('i',[2,5,1])
        lsizes = arr.array('i',[61,300,300,150,50,20,8,1]) #7 laers
        super(model100, self).__init__()     # конструктор предка с этим именем
        #for  n1 in range(1, len(lsizes)):
        nls=1
        self.fc1 = nn.Linear(lsizes[nls-1], lsizes[nls])             # создаём параметры модели
        nls=2
        self.fc2 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=3
        self.fc3 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=4
        self.fc4 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=5
        self.fc5 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=6
        self.fc6 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=7
        self.fc7 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
          
    def forward(self, x):                        # задаётся прямой проход
        x = self.fc1(x)                          # выход первого слоя
        x = nn.Sigmoid()(x)                      # пропускаем через Sigmoid
        x = self.fc2(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc3(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc4(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc5(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc6(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc7(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        return x
 
class model200(nn.Module):
    def __init__(self):        
#        lsizes = arr.array('i',[2,5,1])
        lsizes = arr.array('i',[61,60,60,50,40,20,8,1]) #7 laers
        super(model200, self).__init__()     # конструктор предка с этим именем
        #for  n1 in range(1, len(lsizes)):
        nls=1
        self.fc1 = nn.Linear(lsizes[nls-1], lsizes[nls])             # создаём параметры модели
        nls=2
        self.fc2 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=3
        self.fc3 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=4
        self.fc4 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=5
        self.fc5 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=6
        self.fc6 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=7
        self.fc7 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
          
    def forward(self, x):                        # задаётся прямой проход
        x = self.fc1(x)                          # выход первого слоя
        x = nn.Sigmoid()(x)                      # пропускаем через Sigmoid
        x = self.fc2(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc3(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc4(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc5(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc6(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc7(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        return x


class model400(nn.Module):
    def __init__(self):        
#        lsizes = arr.array('i',[2,5,1])
        lsizes = arr.array('i',[61,200,1000,1000,1000,200,100,50,20,1]) #7 laers
        super(model400, self).__init__()     # конструктор предка с этим именем
        #for  n1 in range(1, len(lsizes)):
        nls=1
        self.fc1 = nn.Linear(lsizes[nls-1], lsizes[nls])             # создаём параметры модели
        nls=2
        self.fc2 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=3
        self.fc3 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=4
        self.fc4 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=5
        self.fc5 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=6
        self.fc6 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=7
        self.fc7 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=8
        self.fc7 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
        nls=9
        self.fc7 = nn.Linear(lsizes[nls-1], lsizes[nls])             # в полносвязных слоях
          
    def forward(self, x):                        # задаётся прямой проход
        x = self.fc1(x)                          # выход первого слоя
        x = nn.Sigmoid()(x)                      # пропускаем через Sigmoid
        x = self.fc2(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc3(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc4(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc5(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc6(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc7(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc8(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        x = self.fc9(x)                          # выход второго слоя
        x = nn.Sigmoid()(x)                      # пропускаем через сигмоид 
        return x
 

class model500(nn.Module):
    def __init__(self):
        super(model500, self).__init__()
        #self.layer1 = nn.Linear(2, 6)
        self.layer1 = nn.Linear(61, 61) 
        self.layer2 = nn.Linear(61, 40) 
        self.layer3 = nn.Linear(40, 20) 
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(20, 1)
        self.sigmoid = nn.Sigmoid()
    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.sigmoid(x)
        return x
    
class model600(nn.Module):
   def __init__(self):
       super(model600, self).__init__()
       self.layer = torch.nn.Linear(61, 1)

   def forward(self, x):
       x = self.layer(x)      
       return x

    
class model700(nn.Module):
   def __init__(self):
        super(model700, self).__init__()
        self.layer1 = nn.Linear(61, 305) 
        self.layer3 = nn.Linear(305, 125) 
        self.layer4 = nn.Linear(125, 62) 
        self.layer100 = nn.Linear(62, 1)
        self.relu20 = nn.ReLU()

   def forward(self, x):
        x = self.relu20( self.layer1(x) ) 
        x = self.relu20( self.layer3(x) ) 
        x = self.relu20( self.layer4(x) ) 
        x = self.layer100(x)
        return x

   
class model800(nn.Module):
   def __init__(self):
        super(model800, self).__init__()
        self.layer1 = nn.Linear(61, 305) 
        self.layer3 = nn.Linear(305, 125) 
        self.layer4 = nn.Linear(125, 62) 
        self.layer100 = nn.Linear(62, 1)
        self.relu20 = nn.ReLU()

   def forward(self, x):
        x = self.relu20( self.layer1(x) ) 
        x = self.relu20( self.layer3(x) ) 
        x = self.relu20( self.layer4(x) ) 
        x = self.layer100(x)
        return x

class model900(nn.Module):
   def __init__(self):
        super(model900, self).__init__()
        self.layer1 = nn.Linear(72, 345) 
        self.layer3 = nn.Linear(345, 145) 
        self.layer4 = nn.Linear(145, 62) 
        self.layer100 = nn.Linear(62, 1)
        self.relu20 = nn.ReLU()

   def forward(self, x):
        x = self.relu20( self.layer1(x) ) 
        x = self.relu20( self.layer3(x) ) 
        x = self.relu20( self.layer4(x) ) 
        x = self.layer100(x)
        return x

class model_900_606(nn.Module):
   def __init__(self):
        super(model_900_606, self).__init__()
        self.layer1 = nn.Linear(209, 209) 
        self.layer2 = nn.Linear(209, 160) 
        self.layer3 = nn.Linear(160, 110) 
        self.layer4 = nn.Linear(110, 62) 
        self.layer5 = nn.Linear(62, 30)
        self.layer6 = nn.Linear(30, 15)
        self.layer100 = nn.Linear(15, 1)
        self.relu20 = nn.ReLU()

   def forward(self, x):
        x = self.relu20( self.layer1(x) ) 
        x = self.relu20( self.layer2(x) ) 
        x = self.relu20( self.layer3(x) ) 
        x = self.relu20( self.layer4(x) ) 
        x = self.relu20( self.layer5(x) ) 
        x = self.relu20( self.layer6(x) ) 
        x = self.layer100(x)
        return x


class model_sex_900_606(nn.Module):
   def __init__(self):
        super(model_sex_900_606, self).__init__()
        self.layer1 = nn.Linear(476, 500) 
        self.layer2 = nn.Linear(500, 300) 
        self.layer3 = nn.Linear(300, 200) 
        self.layer4 = nn.Linear(200, 100) 
        self.layer5 = nn.Linear(100, 30)
        self.layer6 = nn.Linear(30, 15)
        self.layer100 = nn.Linear(15, 1)
        self.relu20 = nn.ReLU()

   def forward(self, x):
        x = self.relu20( self.layer1(x) ) 
        x = self.relu20( self.layer2(x) ) 
        x = self.relu20( self.layer3(x) ) 
        x = self.relu20( self.layer4(x) ) 
        x = self.relu20( self.layer5(x) ) 
        x = self.relu20( self.layer6(x) ) 
        x = self.layer100(x)
        return x

class model_inputdoun_outup_900_606(nn.Module):
   def __init__(self):
        super(model_inputdoun_outup_900_606, self).__init__()
        self.layer1 = nn.Linear(397, 397) 
        self.layer2 = nn.Linear(397, 300) 
        self.layer3 = nn.Linear(300, 220) 
        self.layer4 = nn.Linear(220, 150) 
        self.layer5 = nn.Linear(150, 80) 
        self.layer6 = nn.Linear(80, 30)
        self.layer7 = nn.Linear(30, 15)
        self.layer100 = nn.Linear(15, 1)
        self.relu20 = nn.ReLU()

   def forward(self, x):
        x = self.relu20( self.layer1(x) ) 
        x = self.relu20( self.layer2(x) ) 
        x = self.relu20( self.layer3(x) ) 
        x = self.relu20( self.layer4(x) ) 
        x = self.relu20( self.layer5(x) ) 
        x = self.relu20( self.layer6(x) ) 
        x = self.relu20( self.layer7(x) ) 
        x = self.layer100(x)
        return x

class model_short_vector_900_606(nn.Module):
   def __init__(self):
        super(model_short_vector_900_606, self).__init__()
        self.layer1 = nn.Linear(340, 340) 
        self.layer2 = nn.Linear(340, 300) 
        self.layer3 = nn.Linear(300, 220) 
        self.layer4 = nn.Linear(220, 150) 
        self.layer5 = nn.Linear(150, 80) 
        self.layer6 = nn.Linear(80, 30)
        self.layer7 = nn.Linear(30, 15)
        self.layer100 = nn.Linear(15, 1)
        self.relu20 = nn.ReLU()

   def forward(self, x):
        x = self.relu20( self.layer1(x) ) 
        x = self.relu20( self.layer2(x) ) 
        x = self.relu20( self.layer3(x) ) 
        x = self.relu20( self.layer4(x) ) 
        x = self.relu20( self.layer5(x) ) 
        x = self.relu20( self.layer6(x) ) 
        x = self.relu20( self.layer7(x) ) 
        x = self.layer100(x)
        return x

# file:///d:/BS/Infa/Intelekt/Rosch%20M.%20PyTorch%20Cookbook.%20100+%20Solutions...2023.pdf
# p 152
class LSTMModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, batch_size, output_dim=1, num_layers=2):
        super(LSTMModel, self).__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.batch_size = batch_size
        self.num_layers = num_layers
        # Define the LSTM layer
        self.lstm = nn.LSTM(self.input_dim, self.hidden_dim, self.num_layers)
        # Define the output layer
        self.linear = nn.Linear(self.hidden_dim, output_dim)
    def init_hidden(self):
        # Initialize hidden and cell states
        return (torch.zeros(self.num_layers, self.batch_size, self.hidden_dim), torch.zeros(self.num_layers, self.batch_size, self.hidden_dim))
    def forward(self, input):
        # Forward pass through LSTM layer
        lstm_out, self.hidden = self.lstm(input.view(len(input), self.batch_size, -1), self.hidden)
        # Only take the output from the final timestep
        y_pred = self.linear(lstm_out[-1].view(self.batch_size, -1))
        return y_pred.view(-1)
    
class MultiLayerRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers):
        super(MultiLayerRNN, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    def forward(self, x):
        h_0 = torch.zeros(num_layers, x.size(0), hidden_size) 
        # Initial hidden state
        c_0 = torch.zeros(num_layers, x.size(0), hidden_size) 
        # Initial cell state
        out, _ = self.lstm(x, (h_0, c_0))
        out = self.fc(out[:, -1, :])
        return out

# class CustomLayer(nn.Module):
# def __init__(self, in_features, out_features):
# super(CustomLayer, self).__init__()
# self.linear = nn.Linear(in_features, out_features)
# self.selu = nn.SELU()
# def forward(self, x):
# x = self.linear(x)
# x = self.selu(x)
# return x

def GetActModelFileName(upf,  debugf, nameplus, classname, birja, periodh):
    # if birja=='okx':
    #      birja='bybit'
    # if birja=='binanceusdt':
    #      birja='bybit'
#    birja="bybitbinanceokxusdt"
    ret="D:/BS/Save/WORK/Programm/bi/ii/"+nameplus+birja+"_"+classname+"_"
    if upf==None:
         updoun=""
    else:
        updoun="_up" if upf else "_doun"
    if debugf: updoun=updoun+"_debug"
    updoun=updoun+str(periodh)
    ret=ret+updoun+".pt"
    # if upf:
    #      ret="d:/BS/Save/WORK/Programm/bi/ii/_606_bybitbinanceusdt_model_900_606__up2.pt"
    # else:
    #      ret="d:/BS/Save/WORK/Programm/bi/ii/_606_bybitbinanceusdt_model_900_606__doun2.pt"
    return ret
    # classname="model700"
#----------------------------

def GetActIIClassObj(classname):
    if classname == "model800":
        return  model800()                    # экземпляр сети
    if classname == "model900":
        return  model900()                    # экземпляр сети
    if classname == "model_900_606":
        return  model_900_606()                    # экземпляр сети
    if classname == "model_sex_900_606":
        return  model_sex_900_606()                    # экземпляр сети
    if classname == "model_inputdoun_outup_900_606":
        return  model_inputdoun_outup_900_606()                    # экземпляр сети
    if classname == "model_short_vector_900_606":
        return  model_short_vector_900_606()                    # экземпляр сети
    # not class find 
    small.ifnoterr(1==0)
    return None


