#!/bin/bash

#SBATCH --job-name=sem_200_train
#SBATCH --partition=a100
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:2            #若使用 2 块卡，就给 gres=gpu:2
#SBATCH -x gpu11
#SBATCH --mail-type=end
#SBATCH --mail-user=zhangzhengde@sjtu.edu.cn
#SBATCH --output=%j.out
#SBATCH --error=%j.err

#module load gcc cuda
#
#./cudaTensorCoreGemm

#conda init bash
conda activate yolov5

python train.py -p p3 --batch-size 128
