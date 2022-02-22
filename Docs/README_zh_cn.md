## FINet
本项目是Foggy Insulator Network (FINet), 包含论文《基于合成雾和深度学习的绝缘子数据增强和检测方法》的数据集和复现代码。

论文连接: [暂不可用](link)

本项目为Foggy Insulator Network (FINet)，其中包含论文“基于合成雾和深度学习的绝缘体数据增强与检测方法”的数据集和源代码。

![](https://github.com/zhangzhengde0225/FINet/raw/master/Docs/results.jpg)

Fig.1  复杂环境下绝缘子及其缺陷检测效果。（a）简单背景；（b）简单背景和薄雾；（c）浓雾带缺陷；（d）天空背景；（e）不同尺度；（f）竖的绝缘子+中雾；（g）被截绝缘子；（h）模糊图像；（d）浓雾无缺陷

# 亮点

1. 基于暗通道先验的加雾算法和加雾算法优化，提供了生成的约13700张图的绝缘子数据集。
2. 改进的网络SE-YOLOv5，实现晴天、雾天场景下均具有更强的鲁棒性的绝缘子及其缺陷检测模型。
3. 数据集和代码开源。

# 安装

```
git clone https://github.com/zhangzhengde0225/FINet.git
```

# 数据集

1. 合成雾绝缘子数据集,SFID(我们的),2021.  共约13700张图片，下载地址：[百度云](https://pan.baidu.com/s/1jpqrtMOlln9xC_L2_tGu7w) 提取码：jej3
2. 统一公共绝缘体数据集,UPID,2020.  共约6800张图片             下载地址：[百度云](https://pan.baidu.com/s/1pvk0tCbyJiP5hjakrTTI4Q) 提取码：bcgw ，[github](https://github.com/heitorcfelix/public-insulator-datasets) 地址
3. 中国电力线绝缘子数据集,CPLID,2018.  共约800张图片        下载地址：[百度云](https://pan.baidu.com/s/1BQnZSCTPGQsEOKOe1Z4sXA) 提取码：ik2j，[github](https://github.com/InsulatorData/InsulatorDataSet) 地址

# 模型

您可以下载训练日志和权重来重现论文中的实验结果。

下载地址：[百度云](https://pan.baidu.com/s/129ZTtU-0Hq6fVRv2q7LkEA) 提取码：pupm

# 开始

## Docker

项目环境采用docker镜像

```
docker pull zhangbo2020/finet:v1  # 获取镜像
# 建立容器运行镜像，使用宿主机GPU，将宿主机项目代码与数据集映射到容器
docker run -i -t --gpus all -v /home/XX/FINet:/home/FINet -v /home/XX/datasets:/home/datasets zhangbo20/finet:v1 /bin/bash 

# 例如：
docker run -i -t --gpus all -v /home/XX/FINet:/home/zb/FINet -v /home/zb/datasets:/home/datasets zhangbo20/finet:v1 /bin/bash 
```

## 合成雾

加雾算法：下载完代码以后执行

```
cd /home/FINet/FINet/scripts/  #进入项目代码相应位置 
python synthetic_fog.py        #默认非优化方式加雾
```

主要可选参数：

```
--speed_up  #矩阵优化计算
--img       #输入图片路径
--out       #输出图片路径
```

## 训练

下载代码与数据集以后执行：

```
cd home/FINet/FINet/
python train.py --trainset_path /home/datasets/insulator/SFID
```

主要可选参数

```
--trainset_path #训练集路径
--batch-size    #batch 大小
--img-size      #图片大小
```

## 测试

下载数据集与模型权重后执行：

```
cd home/FINet/FINet/
#测试数据集地址设置在FINet/FINet/sources/sfid.yaml
#加雾模型测试
python test.py --weights /home/datasets/insulator/runs/m_ep99_fogged/weights/best.pt
#无雾模型测试
python test.py --weights /home/datasets/insulator/runs/m_ep99_without_fog/weights/best.pt
#改进加雾模型测试
python test.py --weights /home/datasets/insulator/runs/se_m_ep99_fogged/weights/best.pt
```

# 贡献者

FINet 的作者是 xxx，张正德。

目前由张正德（driverer@163.com）维护。

# 许可

FINet 及其数据集可免费用于非商业用途，并可在这些条件下重新分发。
对于商业用途，请发送电子邮件至driverer@163.com。 我们会将详细协议发送给您。

