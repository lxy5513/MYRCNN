'''
一些模型必须且基础的配置 
可以被继承
'''
import numpy as np 
import math 

class Config(object):
    def __init__(self):
        
        self.verbore = True #?

        # 通过旋转 切片来增加训练数据
        self.use_horizontal_flip = False 
        self.use_verhical_flip = False 
        self.roi_90 = False 

        # 对于每一个cell anchor放大的大小
        self.anchor_box_scales = [128, 256, 512]
        # 将每一个anchor按横竖比变形
        self.anchor_box_ratios = [[1,1], [1,2], [2,1]]

        # 图片最小的一边的大小 
        self.im_size = 600

        
