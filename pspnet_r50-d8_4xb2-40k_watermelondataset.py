# -*- coding = utf-8 -*-
# @Time : 2023/6/18 23:09
# @Author : Happiness
# @File : pspnet_r50-d8_4xb2-40k_watermelondataset.py
# @Software : PyCharm

_base_ = [
    '../_base_/models/pspnet_r50-d8.py', '../_base_/datasets/watermelondataset_pipeline.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
crop_size = (64, 64) # 输入图像尺寸，根据自己数据集情况修改
data_preprocessor = dict(size=crop_size)
model = dict(data_preprocessor=data_preprocessor)