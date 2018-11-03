'''
实现最简单的faster RCNN
'''

import os 
import sys 
import numpy as np 
import keras
import random 
import pprint 
from keras import backend as K 
from keras.optimizers import Adam 
from keras.layers import Input 
from keras.models import Model 
from keras_applications import resnet50



