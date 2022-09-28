#!/bin/bash

# Download the SFID dataset
hai datasets download SFID:latest  # DATASET_NAME:VERSION

wget -c -O SFID.zip https://ihepbox.ihep.ac.cn/ihepbox/index.php/s/adTHe1UPu0Vc7vI/download
unzip SFID.zip
rm SFID.zip

# Download the FINet trainning logs and weights
wget -c -O runs.zip https://ihepbox.ihep.ac.cn/ihepbox/index.php/s/0tZtSS5sp0tnqAN/download
unzip runs.zip
rm runs.zip

# Config run_docker.sh

