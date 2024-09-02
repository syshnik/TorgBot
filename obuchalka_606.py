

from __future__ import print_function
from datetime import datetime 
import random
import small
import db
#from iireshalka import iireshalkaclass
from iireshalka_606 import iireshalkaclass_0_606
from iireshalka_606 import iireshalkaclass_606
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import matplotlib.pyplot as plt                              # построение графиков
# # Moving to GPU
# tensor_gpu = tensor_from_list.to('cuda')
# # Moving back to CPU
# tensor_cpu = tensor_gpu.to('cpu')
from time import sleep
import array as arr 
#import torch
#import torch.nn as nn
import torch.optim as optim
import numpy as np
# https://qudata.com/ml/ru/NN_Base_Torch_NN.html
# import simpleaudio as simple_audio 
from usrednyalka import usrednyalka_class
import pandas as pd
import math

# from iimodels import model100
# from iimodels import model200
# from iimodels import model400
# from iimodels import model500
# from iimodels import model600
# from iimodels import model700
import  iimodels 
from iimodels import model_900_606
from iimodels import model_sex_900_606
from iimodels import model_inputdoun_outup_900_606          
from iimodels import model_short_vector_900_606          
class Obuchalka_class_606:
    def __init__(self, epochspar, classname, plusname, debugf):   
        self._epochs = epochspar
        self._model = 0     #model100()                    # экземпляр сети
        self._debug=debugf
        self._loss=0
        self._optimizer=0
        self._classname, self._plusname = classname, plusname
    
    def MonoUchitcya(self):
        return True
    
    def fit(self, model, X,Y, batch_size=50, train=True):    
        # batch_size ЭТО ПРИМЕРНО КОЛ-ВО СЕКУНД НА ЦИКЛ
        vr1=len(X)
        if self._debug: batch_size=int(batch_size/10)
        if batch_size > len(X): batch_size = len(X)
        model.train(train)                                 # важно для Dropout, BatchNorm
        sumL, sumA, numB = 0, 0, int( len(X)/batch_size )  # ошибка, точность, батчей

        for i in range(0, numB*batch_size, batch_size):          
            xb = X[i: i+batch_size]                          # текущий батч,
            yb = Y[i: i+batch_size]                          # X,Y - torch тензоры
                            
            y = model(xb)                                    # прямое распространение
            # # корректировка
            # n44=y[:, 1]
            # if y[0] > yb[0]:
            #     y[0] = yb[0]
            # if y[1] < yb[1]:
            #     y[1] = yb[1]
            L = self._loss(y, yb)                                  # вычисляем ошибку

            if train:                                        # в режиме обучения
                self._optimizer.zero_grad()                        # обнуляем градиенты        
                L.backward()                                 # вычисляем градиенты            
                self._optimizer.step()                             # подправляем параметры
                                            
            sumL += L.item()                                 # суммарная ошибка (item из графа)
            # sumA += (y.round() == yb).float().mean()         # точность определения класса
            sumA += (abs(y - yb)).float().mean()         # точность определения класса
                
        return sumL/numB,  sumA/numB                         # средняя ошибка и точность

                                                            # режим оценки модели:
    def KursObucheniya(self, rm, pm):
        # работал для bybit
        # self._loss      = nn.MSELoss()
        #self._optimizer = torch.optim.SGD(self._model.parameters(), lr=0.005, momentum=0.4)
        # NEW
        self._loss      = nn.MSELoss()
        #self._loss      = nn.CrossEntropyLoss()
        #self._optimizer = torch.optim.Adam(self._model.parameters(), lr=0.05)
        self._optimizer = torch.optim.SGD(self._model.parameters(), lr=0.05, momentum=0.7)
# работал для bybit                                    lr=0.005, momentum=0.4)        # параметры оптимизатора
#                                    lr=0.5, momentum=0.8)        # параметры оптимизатора
#lr=0.005,momentum=0.9,weight_decay=0.0005
#{'lr': 0.005, 'momentum': 0.4, 'dampening': 0, 'weight_decay': 0, 'nesterov': False, 'maximize': False, 'foreach': None, 'differentiable': False}
# приеры из книг
# imizer = torch.optim.SGD(net.parameters(), lr=0.2)
# loss_function = nn.BCELoss()
# optimizer = torch.optim.SGD(net.parameters(),Lr=2,momentum=0.75)
# Наша сеть на самом деле представляет собой нелинейную регрессию, и поэтому нам нужен 
#среднеквадратический показатель. функция потери ошибок для соответствия параметров сети нашему набору данных
# loss_function = nn.MSELoss()
# Как и раньше, мы будем использовать стохастический оптимизатор градиентного спуска, 
# но на этот раз добавим импульс. Momentum ускоряет обучение и помогает объединить сложные сети.
# optimizer = torch.optim.SGD(net.parameters(),lr=0.001, momentum=0.7)
# optimizer = optim.SGD(net.parameters(), lr=0.001,momentum=0.5)
# optimizer = optim.Adam(net.parameters(), lr=0.005)
# optimizer = optim.Adam(net.parameters(), lr=0.005)
# optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
# criterion = nn.CrossEntropyLoss()
# optimizer = optim.Adam(model.parameters(),lr=0.001)
        #lr=0.001,momentum=0.5 пример из книжки
        epochs1 = 20                                            # число эпох
        epochs2 = self._epochs                                            # число эпох
        if self._debug: epochs1=int(epochs1/10)
        if self._debug: epochs2=int(epochs2/10)
        navihod=False   # for debug
        for epoch1 in range(epochs1):                              # эпоха - проход по всем примерам
            for epoch2 in range(epochs2):                              # эпоха - проход по всем примерам
                while self.MonoUchitcya() == False:                     # пауза если занят другими
                    sleep(6)
                    print("Prostaivaem.")
                L,A = self.fit(self._model, rm, pm)                               # одна эпоха
                if int(epoch2%10) == 0:                 
                    comm2=f'epoch: {epoch1:5d} loss: {L:.4f} accuracy: {A:.4f}'
                    print(comm2 )   
                    # db.PrintInfoToComments(None, small.GetAlgoName(), comm2)
                if self._debug:
                    sleep(1)
                if navihod: break
            if navihod: break

    # def PerevodMassivVTensor(self, om0,notevmassiv):
    #     # переводит простые массивы в массивы torch.FloatTensor
    #     if notevmassiv:
    #         om000=[]
    #         for o111 in om0:
    #             o=[]
    #             o.append(o111)
    #             om000.append(o)
    #         om1 = np.array(om000)
    #     else:
    #         om000=[]
    #         for o111 in om0:
    #             om000.append(o111)
    #         om1 = np.array(om000)
    #     om2=torch.FloatTensor(om1)
    #     return om2
    

    # def PerevodMassivov(self, birja, rm, upm, dounm):
    #     # переводит простые массивы в массивы torch.FloatTensor
    #     rm2=self.PerevodMassivVTensor(rm, False)
    #     upm2=self.PerevodMassivVTensor(upm, True)
    #     dounm2=self.PerevodMassivVTensor(dounm, True)
    #     # и сохраняет на диске
    #     pname=self._plusname
    #     if self._debug: pname=pname+'_debug_'
    #     torch.save(rm2, "D:/BS/Save/WORK/Programm/bi/ii/"+pname+birja+"_"+str(self._posle_period_h)+"_rm.pt")
    #     torch.save(upm2, "D:/BS/Save/WORK/Programm/bi/ii/"+pname+birja+"_"+str(self._posle_period_h)+"_upm.pt")
    #     torch.save(dounm2, "D:/BS/Save/WORK/Programm/bi/ii/"+pname+birja+"_"+str(self._posle_period_h)+"_dounm.pt")
    #     db.PrintInfoToComments(None, small.GetAlgoName(), "Write "+str(len(rm))+" notes for lerning. "+pname)

    
    def ProytiObouchenie(self, rm, upm, dounm,  upf, birja, posle_period_h):
        #подготовка данных
        # upm1=df['up'].to_numpy()
        # upm=self.PerevodMassivVTensor(upm1,True)
        # dounm1=df['doun'].to_numpy()
        # dounm=self.PerevodMassivVTensor(dounm1,True)
        # onem1=df['onem'].to_numpy()
        # onem=self.PerevodMassivVTensor(onem1,False)
        #обучение
        if self._classname=="model_sex_900_606":
            self._model=model_sex_900_606()
        elif self._classname=="model_900_606":
            self._model=model_900_606()
        else:
            tf=9/0
        if upf:            self.KursObucheniya(rm, upm)
        else:            self.KursObucheniya(rm, dounm)
        #сохранение
        fn=iimodels.GetActModelFileName(upf, self._debug, self._plusname, self._classname, birja, posle_period_h)
        while True:
            try:
                torch.save(self._model.state_dict(), fn)
                break
            except:
                print ('error 333333')
                sleep(11)

    def ProytiObouchenieOneVector(self, rm, vm,  upf, birja, posle_period_h):
        #подготовка данных
        #обучение
        self._model=iimodels.GetActIIClassObj(self._classname)
        # if self._classname=="model_sex_900_606":
        #     self._model=model_sex_900_606()
        # elif self._classname=="model_900_606":
        #     self._model=model_900_606()
        # elif self._classname=="model_inputdoun_outup_900_606":
        #     self._model=model_inputdoun_outup_900_606()
        # else:
        #     tf=9/0
        self.KursObucheniya(rm, vm)
        #сохранение
        fn=iimodels.GetActModelFileName(upf, self._debug, self._plusname, self._classname, birja, posle_period_h)
        while True:
            try:
                torch.save(self._model.state_dict(), fn)
                break
            except:
                print ('error 333333')
                sleep(11)


