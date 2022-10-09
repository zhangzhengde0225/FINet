[![Stars](https://img.shields.io/github/stars/zhangzhengde0225/FINet)](
https://github.com/zhangzhengde0225/FINet)
[![Open issue](https://img.shields.io/github/issues/zhangzhengde0225/FINet)](
https://github.com/zhangzhengde0225/FINet/issues)
[![Datasets](https://img.shields.io/static/v1?label=Download&message=datasets&color=green)](
https://github.com/zhangzhengde0225/FINet/blob/master/docs/datasets.md)
[![Source Code](https://img.shields.io/static/v1?label=Download&message=source_code&color=orange)](
https://github.com/zhangzhengde0225/FINet/archive/refs/heads/master.zip)
[![Paper](https://img.shields.io/static/v1?label=Read&message=paper&color=pink)](
https://doi.org/10.1109/TIM.2022.3194909)

# FINet

#### English | [简体中文](https://github.com/zhangzhengde0225/FINet/blob/master/docs/README_zh_cn.md)

This is the official implemtentation of Foggy Insulator Network in the paper [FINet: An Insulator Dataset and Detection Benchmark Based on Synthetic Fog and Improved YOLOv5](https://doi.org/10.1109/TIM.2022.3194909)
 
![GA](https://zhangzhengde0225.github.io/images/FINet_GA.png)

Fig.1 Graphical Abstract of FINet.

[//]: # (Insulator and its defect detection effect in complex environment.&#40;a&#41; Simple background, &#40;b&#41; Simple background and mist, &#40;c&#41; Defect in dense fog, &#40;d&#41; Sky background, &#40;e&#41; Different scales, &#40;f&#41; Vertical insulator + medium fog, &#40;g&#41; Truncated insulator, &#40;h&#41; Blurred image, &#40;d&#41; No defect in dense fog)
 

# Highlights
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

4. ## Download Datasets and Trained Weights

    
   We released the `Synthetic Foggy Insulator Dataset (SFID)` and `Trained logs & weights`,  download them by following command:
    ```bash
    python download.py [SFID|logs]  # Choice: SFID, logs
        [--save-dor SAVE_DIR]  # [optional] Default: current directory
    ```

    After `SFID` downloading, the dataset will be saved in `data/SFID`.
    
    After `logs` downloading, three trained logs and weights will be saved in `runs/xx`, and the `runs/se_m_ep99_fogged/weights/best.pt` will be used for evaluation by default.


    For other download ways and the previous [UPID](https://github.com/heitorcfelix/public-insulator-datasets) and [CPLID](https://github.com/InsulatorData/InsulatorDataSet) datasets, please refer to [docs/dataset.md](https://github.com/zhangzhengde0225/FINet/blob/master/docs/datasets.md).


5. ## Evaluate
    After training or download trained weights, you can evaluate the model by running:
    ```bash
    # evaluate the model on the testset
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

Please **Star** this project and **Cite** this paper if its helpful to you .

# Citation
```
@article{FINet,
Title={FINet: An Insulator Dataset and Detection Benchmark Based on Synthetic Fog and Improved YOLOv5},
Author={Zheng-De Zhang, Bo Zhang, Zhi-Cai Lan, Hai-Chun Liu, Dong-Ying Li, Ling Pei and Wen-Xian Yu},
Journal={IEEE T INSTRUM MEAS},
DOI={10.1109/TIM.2022.3194909},
Year={2022},
Pages={1-8},
ISSN={0018-9456},
Online_ISSN={1557-9662},
}
```

# License
THe FINet and it's datasets is freely available for non-commercial use, and may be redistributed under these conditions. 
For commercial queries, please drop an e-mail to zdzhang@ihep.a.cn, we will send the detail agreement to you.

# TODO
+ Function: Inference
+ Fixbug: download: no hai/configs/urls.json [Fixed]
+ Fixbug: invalid cv2.imshow in docker
+ Fixbug: Synthetic fog invalid in docker

