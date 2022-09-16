import os
import subprocess
import argparse


def train(opt):
    model = opt.model.lower()
    if model == 'mask_rcnn':
        cfg = "./configs/mask_rcnn/zzd_mask_rcnn_r50_fpn_1x_insulator.py"
    elif model == 'faster_rcnn':
        cfg = "./configs/faster_rcnn/zzd_faster_rcnn_r50_fpn_1x_insulator.py"
    elif model == 'centernet':
        cfg = "./configs/centernet/zzd_centernet_resnet18_dcnv2_140e_insulator.py"
    elif model == 'swin-transformer':
        cfg = './configs/swin/zzd_mask_rcnn_swin-t-p4-w7_fpn_1x_insulator.py'
    elif model == 'yolox':
        cfg = './configs/yolox/zzd_yolox_m_8x8_300e_insulator.py'
    else:
        raise ValueError(f'{opt.model} is not supported!')
    code = f'python tools/train.py {cfg}'
    # subprocess.call(code)
    os.system(code)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model', type=str, default='yolox', help='model name')
    opt = parser.parse_args()
    print(f'opt: {opt}')

    train(opt)


