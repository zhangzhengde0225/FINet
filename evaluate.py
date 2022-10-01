from yaml import parse
from hai_api import hai
import argparse

def run(opt):
    FINet = hai.hub.load('FINet')

    # print(FINet)
    FINet.switch_eval()  # switch to train mode
    
    cfg = FINet.get_config()  # get the configs of the model in train mode

    cfg.source = opt.source  # you can modify the `source` config here or in the config file
    cfg.weights = opt.weights
    # cfg.source = 'data/SFID'  # Path to dataset
    # cfg.batch_size = 32
    print(cfg)
    
    FINet.evaluate()  # train the model with the modified configs



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='data/SFID', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--weights', type=str, default='runs/se_m_ep99_fogged/weights/best.pt', help='weights path')
    opt = parser.parse_args()
    run(opt)




