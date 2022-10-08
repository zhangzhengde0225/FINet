#!/bin/bash

docker run -it --gpus all --rm --shm-size=8g \
    -v ~/VSProjects/FINet:/root/FINet \
    --name finet nvcr.io/nvidia/pytorch:21.08-py3
    # --name finet nvidia/cuda:11.0.3-base-ubuntu20.04
    
    # -v ~/VSProjects/hai:/root/hai \
    
