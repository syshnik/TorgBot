

from __future__ import print_function
from datetime import datetime 
import random
import small
import db
# from iireshalka import iireshalkaclass
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
print(torch.cuda.is_available()) # Should print True
from time import sleep
import array as arr 
#import torch
#import torch.nn as nn
import torch.optim as optim
import numpy as np
# https://qudata.com/ml/ru/NN_Base_Torch_NN.html
# import simpleaudio as simple_audio 
import time

import simplejson
from iimodels import model_900_606
import  iimodels 

from iiobuchalka_606 import Obuchalka_606
# from iihshar import hshar
# from iihshar_606 import hshar_900_606
# from wold_ii_bloha_606 import bloha_606
import os
import pandas as pd
# from wold_ii_bloha_606  import bloha_stavka_606

Global_plusname = "_606_"

def GetBL(oldbl, birja, starttime):
    # иниц-ем 
    # Указываем путь к директории
    directory = "D:/BS/Save/WORK/Programm/bi/ii"
    df=pd.DataFrame()
    df['id']=0
    # Получаем список файлов
    files = os.listdir(directory)
    for file in files:
        s1='_test_'
        s2='_okx_model_sex_900_606__up2.pt'
        if file.find(s1) != -1 and file.find(s2) != -1:
            str1=file.replace(s1, '')
            str2=str1.replace(s2, '')
            df.loc[len(df.index)] = [int(str2)]
    df.sort_values(by='id', ascending=False)
    df2=df.loc[(df['id'] < starttime)]
    maxid=df2['id'].max()
    #
    plusname=small.GetPlusName223345656(maxid)
    bl=None
    try:
        bl=bloha_606(birja, 2, False, plusname)
        if oldbl is None:
            oldbl=bl
        else:
            oldbl._sh=bl._sh
            oldbl._sex_sh=bl._sex_sh
    except:
        print('Error 33337777')
        gg=9/0
    return oldbl
