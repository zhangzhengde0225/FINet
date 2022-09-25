"""
转换训练集，YOLOv5 format to COCO format
"""
import os, sys
from pathlib import Path
pydir = Path(os.path.abspath(__file__)).parent
try:
    import damei as dm
except:
    sys.path.append(f'{pydir.parent.parent.parent}/damei')
    import damei as dm

sp = f'{Path.home()}/datasets/insulator/SFID'
tp = f"{Path.home()}/datasets/insulator/SFID_coco_format"
dm.tools.yolo2coco(sp=sp, tp=tp)

