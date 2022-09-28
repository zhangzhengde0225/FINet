docker run -it --gpus all --rm --shm-size=8g \
    -v ~/VSProjects/FINet:/root/FINet \
    -v ~/datasets/hai_datasets/SFID:/root/SFID \
    -v ~/VSProjects/hai:/root/hai \
    --name finet finet
