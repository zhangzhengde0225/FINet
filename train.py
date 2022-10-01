from hai_api import hai
import argparse
    
def run(opt):
    FINet = hai.hub.load('FINet')

    # print(FINet)
    FINet.switch_train()  # switch to train mode
    
    cfg = FINet.get_config()  # get the configs of the model in train mode

    cfg.source = opt.source  # you can modify the `source` config here or in the config file
    cfg.weights = opt.weights
    cfg.epochs = opt.epochs
    cfg.batch_size = opt.batch_size
    cfg.device = opt.device
    cfg.img_size = opt.img_size
    
    print(cfg)
    
    FINet.train()  # train the model with the modified configs


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', type=str,
						default=f'data/SFID_demo',
						help='the input source path')
    parser.add_argument('-w', '--weights', type=str, default='', help='initial weights path')
    parser.add_argument('--epochs', type=int, default=3, help='number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='total batch size for all GPUs')
    parser.add_argument('--device', default='0', help='cuda device, i.e. 0 or 0, 1, 2, 3 or cpu')
    parser.add_argument('--img-size', nargs='+', type=int, default=[640, 640], help='train,test sizes')
    opt = parser.parse_args()
    run(opt)
    






