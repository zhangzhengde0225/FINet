
+ This is the tutorial for reproducing the results in the paper, including the training and testing process.
+ We recommend you to use the docker image to run the codes, which can avoid the environment problems.

#### Docker
Please ensure that you have installed the [docker](docker.com) via the following command:
```bash
docker --version 
```

```bash
hai datasets info  # View all datasets available
hai datasets download SFID  # download SFID. You can specify version by DATASET_NAME:VERSION, e.g. SFID:latest
unzip SFID.zip
rm SFID.zip
```
The dataset is unzipped to the `SFID` folder, and the training logs in the `runs` folder.