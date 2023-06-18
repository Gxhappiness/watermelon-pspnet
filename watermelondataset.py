# -*- coding = utf-8 -*-
# @Time : 2023/6/18 22:49
# @Author : Happiness
# @File : watermelondataset.py
# @Software : PyCharm


from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class watermelondataset(BaseSegDataset):
    # 类别和对应的可视化配色
    METAINFO = {
        'classes': ['red', 'green', 'white', 'seed-black', 'seed-white', 'Unlabeled'],
        'palette': [[1,], [2,], [3,], [4,], [5,], [0,]]
    }

    # 指定图像扩展名、标注扩展名
    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 reduce_zero_label=False,  # 类别ID为0的类别是否需要除去
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            reduce_zero_label=reduce_zero_label,
            **kwargs)