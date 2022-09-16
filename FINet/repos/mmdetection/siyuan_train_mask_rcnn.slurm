#!/bin/bash

#SBATCH --job-name=mask_rcnn_train
#SBATCH --partition=a100
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1            #若使用 2 块卡，就给 gres=gpu:2
#SBATCH --mail-type=end
#SBATCH --mail-user=zhangzhengde@sjtu.edu.cn
#SBATCH --output=%j.out
#SBATCH --error=%j.err

#module load gcc cuda
#
#./cudaTensorCoreGemm

#conda init bash
conda activate yolov5

python zzd_train.py -m mask_rcnn
