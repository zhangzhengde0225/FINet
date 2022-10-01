[![Stars](https://img.shields.io/github/stars/zhangzhengde0225/FINet)](
https://github.com/zhangzhengde0225/FINet)
[![Open issue](https://img.shields.io/github/issues/zhangzhengde0225/FINet)](
https://github.com/zhangzhengde0225/FINet/issues)
[![Datasets](https://img.shields.io/static/v1?label=Download&message=datasets&color=green)](
https://github.com/zhangzhengde0225/FINet/blob/master/docs/datasets.md)
[![Source Code](https://img.shields.io/static/v1?label=Download&message=source_code&color=orange)](
https://github.com/zhangzhengde0225/FINet/archive/refs/heads/master.zip)
<<<<<<< HEAD

#### English | [简体中文](https://github.com/zhangzhengde0225/FINet/blob/master/docs/README_zh_cn.md)

Please star this project if its helpful to you.

## FINet

This project is Foggy Insulator Network (FINet), which contains the datasets and reproduction code for the paper 
"FINet: An Insulator Dataset and Detection Benchmark Based on Synthetic Fog and Improved YOLOv5"

Paper link：[Unavailable now](https://zhangzhengde0225.github.io)

=======
[![Paper](https://img.shields.io/static/v1?label=Read&message=paper&color=pink)](
https://doi.org/10.1109/TIM.2022.3194909)

# FINet

#### English | [简体中文](https://github.com/zhangzhengde0225/FINet/blob/master/docs/README_zh_cn.md)

This is the official implemtentation of Foggy Insulator Network in the paper [FINet: An Insulator Dataset and Detection Benchmark Based on Synthetic Fog and Improved YOLOv5](https://doi.org/10.1109/TIM.2022.3194909)
 
>>>>>>> main
![GA](https://zhangzhengde0225.github.io/images/FINet_GA.png)

Fig.1 Graphical Abstract of FINet.

[//]: # (Insulator and its defect detection effect in complex environment.&#40;a&#41; Simple background, &#40;b&#41; Simple background and mist, &#40;c&#41; Defect in dense fog, &#40;d&#41; Sky background, &#40;e&#41; Different scales, &#40;f&#41; Vertical insulator + medium fog, &#40;g&#41; Truncated insulator, &#40;h&#41; Blurred image, &#40;d&#41; No defect in dense fog)
 

# Highlights
<<<<<<< HEAD
1. This project realizes the fogging algorithm and the optimization of fogging algorithm based on the dark channel prior, and provides an insulator data set of about 13,700 images generated.

2. The improved network SE-YOLOv5 realizes a more robust insulator and defect detection model in both sunny and foggy scenarios.

3. The dataset and codes are public.


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
docker pull zhangbo2020/finet:v1  # get the docker image

# Establish a container running image, use the host GPU to map the host project code and data set to the container

docker run -i -t --gpus all -v /home/XX/FINet:/home/FINet -v /home/XX/datasets:/home/datasets zhangbo20/finet:v1 /bin/bash 

# example
docker run -i -t --gpus all -v /home/zb/FINet:/home/zb/FINet -v /home/zb/datasets:/home/datasets zhangbo20/finet:v1 /bin/bash 
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
Once you get the FINet code, configure the environment and download the dataset, juse type:

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

Currently, it is maintained by Bo Zhang (zhangbo20@sjtu.edu.cn) and Zheng-De Zhang (drivener@163.com).
 
Please feel free to contact us if you have any question.

Personal page of Zheng-De Zhang: [zhangzhengde0225.github.io](https://zhangzhengde0225.github.io)
=======
1. This project realizes and optimizes the fogging algorithm based on the dark channel prior, and the codes are availalbe now.

2. We provides an datasets for Insulator Detection with about 13,700 images.

3. The improved network SE-YOLOv5 realizes a more robust model in both sunny and foggy scenarios.


# Getting Started

For `FINet`, the [HAI](https://code.ihep.ac.cn/zdzhang/hai) framework is used to provide simple dataset download, training, evaluation, inference and deployment functions. To install `hai`, run:

```bash
pip install hepai
hai --version  # check the version
```


1. ## Get Source Codes
    ```bash
    git clone https://github.com/zhangzhengde0225/FINet.git
    cd FINet
    pip install -r requirements.txt  # install dependencies
    ```

2. ## Check dataset

    To check the dataset by drawing labels into images, run:
    ```bash
    python scripts/check_dataset.py
        [-s --source DATASET_PATH]  # [optional] Default: data/SFID_demo
    ```

3. ## Train model

    To train a model, run:
    ```bash
    python train.py
        [-s --source DATASET_PATH]  # [optional] Default: data/SFID_demo
        [-w --weights WEIGHTS_PATH]  # [optional] Default: None
        [--epochs EPOCHS]  # [optional] Default: 3
        [--batch-size BATCH_SIZE]  # [optional] Default: 32
        [--device CPU/GPU]  # [optional] Default: GPU:0
        [--img-size IMAGE_SIZE]  # [optional] Default: 640
    ```
    After training, the model will be saved in `runs/exp/weights/last.pt`.
    You can train the model with your own dataset by modifying the `--source` parameter.

4. ## Get Datasets and Trained Weights

    
   We released the `Synthetic Foggy Insulator Dataset (SFID)` and `Trained logs & weights`,  download them by following command:
    ```bash
    python download.py [SFID|logs]  # Choice: SFID, logs
        [--save-dor SAVE_DIR]  # [optional] Default: current directory
    ```

    For other download ways and the previous [UPID](https://github.com/heitorcfelix/public-insulator-datasets) and [CPLID](https://github.com/InsulatorData/InsulatorDataSet) datasets, please refer to [docs/dataset.md](https://github.com/zhangzhengde0225/FINet/blob/master/docs/datasets.md).


5. ## Evaluate
    After training or download trained weights, you can evaluate the model by running:
    ```bash
    # evaluate the model on the test set
    python evaluate.py
        [--source DATASET_PATH]  # [optional] Default: data/SFID
        [--weights TRAINED_WEIGHTS]  # [optional] Deafult: runs/se_m_ep99_fogged/weights/best.pt
    ```

6. ## Inference [TODO]
   The `HAI` provides simple way to deploy the `FINet` via docker and provides remote inference `API`, which can be used to detect insulators in images or videos.
    ```bash
    # Deploy the FINet in docker
    hai deploy --name FINet --image zhangzhengde0225/finet:latest

    python inference.py 
        [--source IMAGE_PATH]  # [optional] Default: data/SFID_demo/images/test/00400.jpg
        [--weights TRAINED_WEIGHTS]  # [optional] Deafult: runs/se_m_ep99_fogged/weights/best.pt
        [--device CPU/GPU]  # [optional] Default: GPU:0
        [--img-size IMAGE_SIZE]  # [optional] Default: 640
    ```

7. ## Synthetic fog

    You can use the `synthetic_fog.py` to generate foggy images. The fogging algorithm is based on the dark channel prior described in our paper, and the codes are availalbe now.

    ```bash
    python scripts/synthetic_fog.py
        [-s --source INPUT_PATH]  # [optional] Default: data/SFID_demo/images/train/001040.jpg
        [--save-dir OUTPUT_PATH]  # [optional] Default: None, display it
        [--speed_up NEED_SPEED_UP]  # Default: False
    ```

Detailed tutorials are available in [docs/tutorial.md](https://github.com/zhangzhengde0225/FINet/blob/master/docs/tutorial.md).
 
# Contributors
The FINet is authored by [Zheng-De Zhang](https://zhangzhengde0225.github.io)\*, Bo Zhang,*, Zhi-Cai Lan, Hai-Chun Liu, Dong-Ying Li, Ling Pei and Wen-Xian Yu.

Currently, it is maintained by Zheng-De Zhang (zdzhang@ihep.ac.cn) and Bo Zhang (zhangbo20@sjtu.edu.cn) 

If you have any questions, please new an [issue](https://github.com/zhangzhengde0225/FINet/issues) or feel free contact us by email, thank you for your attention!

Please **Star** this project and **Cite** this paper if its helpful to you.
>>>>>>> main

# Citation
```
@article{FINet,
<<<<<<< HEAD
author={Zheng-De Zhang, Bo Zhang, Zhi-Cai Lan, Hai-Chun Liu, Dong-Ying Li, Ling Pei and Wen-Xian Yu},
title={FINet: An Insulator Dataset and Detection Benchmark Based on Synthetic Fog and Improved YOLOv5},
year={2022},
=======
Title={FINet: An Insulator Dataset and Detection Benchmark Based on Synthetic Fog and Improved YOLOv5},
Author={Zheng-De Zhang, Bo Zhang, Zhi-Cai Lan, Hai-Chun Liu, Dong-Ying Li, Ling Pei and Wen-Xian Yu},
Journal={IEEE T INSTRUM MEAS},
DOI={10.1109/TIM.2022.3194909},
Year={2022},
>>>>>>> main
}
```

# License
<<<<<<< HEAD
FINet and it's datasets is freely available for non-commercial use, and may be redistributed under these conditions. 
For commercial queries, please drop an e-mail at drivener@163.com. We will send the detail agreement to you.
=======
THe FINet and it's datasets is freely available for non-commercial use, and may be redistributed under these conditions. 
For commercial queries, please drop an e-mail to zdzhang@ihep.a.cn, we will send the detail agreement to you.
>>>>>>> main
