We recommend you to use the docker image to run the codes, which can avoid the dependent environment problems.
    ```bash
    # build docker image with name "finet" via Dockerfile
    docker build -t finet .

    # run docker container from image "finet"
    docker run -it --gpus all --rm --shm-size=8g \
        -v your_code_path:/root/FINet \
        --name finet finet
    ```

    If you want to run the codes in your own environment, please refer to [docs/dependencies.md](https://github.com/zhangzhengde0225/FINet/blob/master/docs/dependencies.md).
