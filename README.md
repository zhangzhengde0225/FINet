[![Stars](https://img.shields.io/github/stars/zhangzhengde0225/FINet)](
https://github.com/zhangzhengde0225/FINet)
[![Open issue](https://img.shields.io/github/issues/zhangzhengde0225/FINet)](
https://github.com/zhangzhengde0225/FINet/issues)
[![Datasets](https://img.shields.io/static/v1?label=Download&message=datasets&color=green)](
https://github.com/zhangzhengde0225/FINet/blob/master/docs/datasets.md)
[![Source Code](https://img.shields.io/static/v1?label=Download&message=source_code&color=orange)](
https://github.com/zhangzhengde0225/FINet/archive/refs/heads/master.zip)

#### English | [简体中文](https://github.com/zhangzhengde0225/FINet/blob/master/docs/README_zh_cn.md)

Please star this project if its helpful to you.

## FINet

This project is Foggy Insulator Network (FINet), which contains the datasets and reproduction code for the paper 
"FINet: An Insulator Dataset and Detection Benchmark Based on Synthetic Fog and Improved YOLOv5"

Paper link：[Unavailable now](https://zhangzhengde0225.github.io)

![GA](https://zhangzhengde0225.github.io/images/FINet_GA.png)

Fig.1 Graphical Abstract of FINet.

[//]: # (Insulator and its defect detection effect in complex environment.&#40;a&#41; Simple background, &#40;b&#41; Simple background and mist, &#40;c&#41; Defect in dense fog, &#40;d&#41; Sky background, &#40;e&#41; Different scales, &#40;f&#41; Vertical insulator + medium fog, &#40;g&#41; Truncated insulator, &#40;h&#41; Blurred image, &#40;d&#41; No defect in dense fog)
 

# Highlights
1. This project realizes and optimizes the fogging algorithm based on the dark channel prior, and the codes are availalbe now.

2. We provides an datasets for Insulator Detection with about 13,700 images.

3. The improved network SE-YOLOv5 realizes a more robust model in both sunny and foggy scenarios.


# Datasets
To download the datasets of insulators and defects, please refer to [docs/dataset.md](
https://github.com/zhangzhengde0225/FINet/blob/master/docs/datasets.md)

# Trained Weights

You can download training logs and weights to reproduce the experimental results in the paper.

Download **weights** from [BaiduYun](https://pan.baidu.com/s/129ZTtU-0Hq6fVRv2q7LkEA). Code: pupm

# Install
```
git clone https://github.com/zhangzhengde0225/FINet.git
```
# Quick start
## Docker

```
cd FINet
docker build -t finet .  # build docker image

# run docker container
docker run -it --gpus all --shm-size=8g \
    -v your_code_path:/root/FINet \
    -v your_data_path:/root/datasets \
    --name finet finet
```

## Synthetic fogging
After you get the FINet code, type:

```
cd /home/FINet/FINet/scripts/  
python synthetic_fog.py        # default 
```
The main optional arguments:
```
--speed_up  #matrix optimization caculation
--img       #input image path
--out       #output image path
```

## Training
Once you get the FINet code, configure the environment and download the dataset, just type:

```
cd home/FINet/FINet/
python train.py --trainset_path /home/datasets/insulator/SFID
```
The main optional arguments:
```
--trainset_path #trainset path
--batch-size    #batch size
--img-size      #image size
```

## Inference


```
cd home/FINet/FINet/

#testset_path set: FINet/FINet/sources/sfid.yaml
#foggy model inference

python test.py --weights /home/datasets/insulator/runs/m_ep99_fogged/weights/best.pt

#model without fog inference

python test.py --weights /home/datasets/insulator/runs/m_ep99_without_fog/weights/best.pt

#foggy model with SE module inference

python test.py --weights /home/datasets/insulator/runs/se_m_ep99_fogged/weights/best.pt
```

# Contributors
FINet is authored by Zheng-De Zhang\*, Bo Zhang,*, Zhi-Cai Lan, Hai-Chun Liu, Dong-Ying Li, Ling Pei and Wen-Xian Yu.

Currently, it is maintained by Zheng-De Zhang (zdzhang@ihep.ac.cn) and Bo Zhang (zhangbo20@sjtu.edu.cn) 
 
Please feel free to contact us if you have any question.

Personal page of Zheng-De Zhang: [zhangzhengde0225.github.io](https://zhangzhengde0225.github.io)

# Citation
```
@article{FINet,
author={Zheng-De Zhang, Bo Zhang, Zhi-Cai Lan, Hai-Chun Liu, Dong-Ying Li, Ling Pei and Wen-Xian Yu},
title={FINet: An Insulator Dataset and Detection Benchmark Based on Synthetic Fog and Improved YOLOv5},
year={2022},
}
```

# License
FINet and it's datasets is freely available for non-commercial use, and may be redistributed under these conditions. 
For commercial queries, please drop an e-mail at drivener@163.com. We will send the detail agreement to you.
