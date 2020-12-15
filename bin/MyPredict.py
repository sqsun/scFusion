# -*- coding: utf-8 -*-
"""
@author: Huang Wenjian
"""

from keras.models import Sequential
from keras.layers import Embedding,Dropout,Bidirectional,Flatten,Dense,LSTM,TimeDistributed, Activation
from keras.callbacks import ModelCheckpoint,CSVLogger
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D
from keras.optimizers import Adam
import numpy as np
from keras.utils import to_categorical
from Model1 import Cla_LSTM
import os
import matplotlib.pyplot as plt
import sys

# os.environ["CUDA_VISIBLE_DEVICES"] = "0"

outfile = open(sys.argv[1], 'w')
weightfile = sys.argv[2]
prefix = ''
if len(sys.argv) == 4:
    prefix = sys.argv[3]

findgang = sys.argv[1].rfind('/')
filedir = sys.argv[1][:findgang+1]
findgang = sys.argv[0].rfind('/')
codedir = sys.argv[0][:findgang+1]

Good_for_Tra = np.load(filedir + prefix + 'Reads.npy')
Good_for_Tra_rev = np.load(filedir + prefix + 'Reads_rev.npy')
Tst_x = np.squeeze(Good_for_Tra)
Tst_x_rev = np.squeeze(Good_for_Tra_rev)

model = Cla_LSTM()
model.load_weights(weightfile)

batch_size = 500 

Prob = model.predict(Tst_x,batch_size)
Prob_rev = model.predict(Tst_x_rev,batch_size)
AveProb = (Prob[:,0] + Prob_rev[:,0]) / 2

sys.stderr.write(str(np.mean(AveProb)))
sys.stderr.write('\n')

above5 = 0
above6 = 0
above7 = 0
above8 = 0
above9 = 0
above0 = 0
above1 = 0
above2 = 0
above3 = 0
above4 = 0
for i in range(len(AveProb)):
    outfile.write(str(Prob[i,0]) + '\t' + str(Prob_rev[i,0]) + '\t' + str(AveProb[i]) + '\n')
    if i >= 0:
        above0 += 1
    if i >= 0.1:
        above1 += 1
    if i >= 0.2:
        above2 += 1
    if i >= 0.3:
        above3 += 1
    if i >= 0.4:
        above4 += 1
    if i >= 0.5:
        above5 += 1
    if i >= 0.6:
        above6 += 1
    if i >= 0.7:
        above7 += 1
    if i >= 0.8:
        above8 += 1
    if i >= 0.9:
        above9 += 1
sys.stderr.write(str(above0))
sys.stderr.write('\n')
sys.stderr.write(str(above1))
sys.stderr.write('\n')
sys.stderr.write(str(above2))
sys.stderr.write('\n')
sys.stderr.write(str(above3))
sys.stderr.write('\n')
sys.stderr.write(str(above4))
sys.stderr.write('\n')
sys.stderr.write(str(above5))
sys.stderr.write('\n')
sys.stderr.write(str(above6))
sys.stderr.write('\n')
sys.stderr.write(str(above7))
sys.stderr.write('\n')
sys.stderr.write(str(above8))
sys.stderr.write('\n')
sys.stderr.write(str(above9))
outfile.close()