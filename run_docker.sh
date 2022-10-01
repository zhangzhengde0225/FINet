#!/bin/bash

docker run -it --gpus all --rm --shm-size=8g \
    -v ~/VSProjects/FINet:/root/FINet \
    -v ~/VSProjects/hai:/root/hai \
    --name finet finet
