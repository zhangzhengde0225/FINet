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

#### [English](https://github.com/zhangzhengde0225/FINet) | 简体中文


## FINet
本项目是Foggy Insulator Network的官方实现, 论文[FINet: An Insulator Dataset and Detection Benchmark Based on Synthetic Fog and Improved YOLOv5](https://doi.org/10.1109/TIM.2022.3194909)

![GA](https://zhangzhengde0225.github.io/images/FINet_GA.png)
Fig.1 FINet图形摘要

[//]: # (Fig.1  复杂环境下绝缘子及其缺陷检测效果。（a）简单背景；（b）简单背景和薄雾；（c）浓雾带缺陷；（d）天空背景；（e）不同尺度；（f）竖的绝缘子+中雾；（g）被截绝缘子；（h）模糊图像；（d）浓雾无缺陷)

# Highlights

1. 本项目实现和优化了基于暗通道先验的加雾算法，代码已可用。
2. 提供了用于绝缘子及其缺陷检测的包含约13700张图的数据集。
3. 改进的网络SE-YOLOv5，实现了晴天、雾天场景下均具有更强的鲁棒性的绝缘子及其缺陷检测模型。

# 开始

对于`FINet`项目，我们采用了HAI](https://code.ihep.ac.cn/zdzhang/hai) 框架来提供简便的数据集下载、模型训练、评估、推理和部署等功能。

安装`hai`, 运行:

```bash
pip install hepai
hai --version  # check the version
```


1. ## 获取FINet源码
    ```bash
    git clone https://github.com/zhangzhengde0225/FINet.git
    cd FINet
    pip install -r requirements.txt  # install dependencies
    ```

2. ## 检查数据集

    通过将标注绘制到图像上检测数据集，运行：
    ```bash
    python scripts/check_dataset.py
        [-s --source DATASET_PATH]  # [optional] Default: data/SFID_demo
    ```

3. ## 训练Train
    训练一个模型，运行：
    ```bash
    python train.py
        [-s --source DATASET_PATH]  # [optional] Default: data/SFID_demo
        [-w --weights WEIGHTS_PATH]  # [optional] Default: None
        [--epochs EPOCHS]  # [optional] Default: 3
        [--batch-size BATCH_SIZE]  # [optional] Default: 32
        [--device CPU/GPU]  # [optional] Default: GPU:0
        [--img-size IMAGE_SIZE]  # [optional] Default: 640
    ```
    通过设置`--source`参数指定训练使用的数据集，指定`--weights`参数指定预训练模型，以此类推。

    训练后，模型将会存储在`runs/exp/weights/last.pt`.

4. ## 下载数据集和训练好的权重
    通过`hai`下载数据集和训练好的模型，运行：
    ```bash
    hai download FINet
    hai download FINet --weights
    ```
    我们发布了`Synthetic Foggy Insulator Dataset (SFID)数据集`和`Trained logs & weights训练日志`, 通过如下命令下载它们：
    ```bash
    python download.py [SFID|logs]  # Choice: SFID, logs
        [--save-dor SAVE_DIR]  # [optional] Default: current directory
    ```
    `SFID`下载后，默认数据集将会存储在`data/SFID`.
    
    `logs`下载后，三项训练日志和权重将会存储在 `runs/xx`, 其中`runs/se_m_ep99_fogged/weights/best.pt`权重将默认用于后续性能评估。

    对于`SFID`的其他下载方法、前人的数据集[UPID](https://github.com/heitorcfelix/public-insulator-datasets)和[CPLID](https://github.com/InsulatorData/InsulatorDataSet)请查看[docs/dataset.md](https://github.com/zhangzhengde0225/FINet/blob/master/docs/datasets.md).


5. ## 评估Evaluate
    
    训练后或下载好权重后，可以通过如下命令评估模型性能：
    ```bash
    # evaluate the model on the testset
    python evaluate.py
        [--source DATASET_PATH]  # [optional] Default: data/SFID
        [--weights TRAINED_WEIGHTS]  # [optional] Deafult: runs/se_m_ep99_fogged/weights/best.pt
    ```

6. ## 推理Inference [TODO]
   
   `HAI`框架提供了简单的部署`FINet`到容器中并通过远程调用的`API`，可用于从图像或视频中检测绝缘子：
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

    如果想自己生成雾化图像，你可以使用`synthetic_fog.py`实现，运行：
    ```bash
    python scripts/synthetic_fog.py
        [-s --source INPUT_PATH]  # [optional] Default: data/SFID_demo/images/train/001040.jpg
        [--save-dir OUTPUT_PATH]  # [optional] Default: None, display it
        [--speed_up NEED_SPEED_UP]  # Default: False
    ```

详细的教程见[docs/tutorial.md](https://github.com/zhangzhengde0225/FINet/blob/master/docs/tutorial.md).


# 贡献者

FINet的作者是：[张正德]((https://zhangzhengde0225.github.io))，张博，兰志才，刘海春，李东瀛，裴凌和郁文贤。

目前由张正德(zdzhang@ihep.ac.cn)和张博(zhangbo20@sjtu.edu.cn)和维护。

如果您有任何问题，请发起一个新[issue](https://github.com/zhangzhengde0225/FINet/issues)或随时与我们联系。

# 引用
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

# 许可
FINet及其数据集可免费用于非商业用途，并可在这些条件下重新分发。
对于商业用途，请发送电子邮件至zdzhang@ihep.ac.cn, 我们会将详细协议发送给您。

