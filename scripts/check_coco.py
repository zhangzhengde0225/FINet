"""
检查coco数据集
"""
import os, sys
import argparse

sys.path.append(f'/home/zzd/PycharmProject/damei')
import damei as dm
from pathlib import Path

# parser = argparse.ArgumentParser()
# parser.add_argument('--json_path', )


# dp = f"{Path.home()}/datasets/crosswalk/fogged_train_data_coco_format"
dp = f'{Path.home()}/datasets/insulator/SFID_coco_format'
jp = f'{dp}/annotations/instances_train2017.json'
# jp = "/home/zzd/datasets/mscoco/annotations/instances_train2017.json"
dm.tools.check_COCO(json_path=jp)









