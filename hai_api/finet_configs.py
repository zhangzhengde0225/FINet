"""
use the 
"""

from . import hai

from FINet.train import hyp



def mapping():
    """define the mapping between the unified HAI configs and the original FINet configs"""
    mapping = {
        'source': 'trainset_path',
    }
    return mapping


def get_train_config():
    parser = hai.argparse.ArgumentParser()
    parser.add_argument('-s', '--source', type=str,
						default=f'data/SFID',
						help='the input source path')
    parser.add_argument('-w', '--weights', type=str, default='', help='initial weights path')
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--batch-size', type=int, default=32, help='total batch size for all GPUs')
    parser.add_argument('--device', default='0, 1', help='cuda device, i.e. 0 or 0, 1, 2, 3 or cpu')
    
    parser.add_argument('--img-size', nargs='+', type=int, default=[640, 640], help='train,test sizes')
    parser.add_argument('--hyp', type=dict, default=hyp, help='hyperparameters')

    parser.add_argument('--cfg', type=str, default='models/yolov5m.yaml', help='model.yaml path')
    # parser.add_argument('--data', type=str, default='sources/sfid.yaml', help='data.yaml path')
    parser.add_argument('--not-use-SE', action='store_true', help='whether to YOLOv5 embedded in SE module')
    parser.add_argument('--rect', action='store_true', help='rectangular training')
    parser.add_argument('--resume', nargs='?', const='get_last', default='',
						help='resume from given path/last.pt, or most recent run if blank')
    parser.add_argument('--nosave', action='store_true', help='only save final checkpoint')
    parser.add_argument('--notest', action='store_true', help='only test final epoch')
    parser.add_argument('--noautoanchor', action='store_true', help='disable autoanchor check')
    parser.add_argument('--evolve', action='store_true', help='evolve hyperparameters')
    parser.add_argument('--bucket', type=str, default='', help='gsutil bucket')
    parser.add_argument('--cache-images', action='store_true', help='cache images for faster training')
    parser.add_argument('--name', default='', help='renames results.txt to results_name.txt if supplied')
    parser.add_argument('--multi-scale', action='store_true', help='vary img-size +/- 50%%')
    parser.add_argument('--single-cls', action='store_true', help='train as single-class dataset')
    parser.add_argument('--adam', action='store_true', help='use torch.optim.Adam() optimizer')
    parser.add_argument('--sync-bn', action='store_true', help='use SyncBatchNorm, only available in DDP mode')
    parser.add_argument('--local_rank', type=int, default=-1, help='DDP parameter, do not modify')
    parser.add_argument('--save-interval', type=int, default=None, help='save interval of epoch for checkpoint')
    parser.add_argument('--classes', type='+', default=['insulator', 'broken_piece'], help='the classes of the dataset')
    opt = parser.parse_args()
    return opt


def get_evaluate_config():
    parser = hai.argparse.ArgumentParser(prog='test.py')
    parser.add_argument('-s', '--source', type=str, default='data/SFID', help='input source path')
    parser.add_argument('--weights', nargs='+', type=str,
						default='runs/m_ep99_fogged/weights/best.pt',
						help='model.pt path(s)')
    parser.add_argument('--batch-size', type=int, default=8, help='size of each image batch')
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--device', default='0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
	
    parser.add_argument('--conf-thres', type=float, default=0.001, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.65, help='IOU threshold for NMS')
    parser.add_argument('--save-json', action='store_true', help='save a cocoapi-compatible JSON results file')
    parser.add_argument('--task', default='val', help="'val', 'test', 'study'")
    parser.add_argument('--single-cls', action='store_true', help='treat as single-class dataset')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--merge', action='store_true', help='use Merge NMS')
    parser.add_argument('--verbose', action='store_true', help='report mAP by class')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument(f'--show-each-cls', action='store_true', help='show evaluation of each class')
    parser.add_argument('--classes', type='+', default=['insulator', 'broken_piece'], help='the classes of the dataset')
    opt = parser.parse_args()
    return opt

def get_inference_config():
    parser = hai.argparse.ArgumentParser(prog='test.py')
    parser.add_argument('-s', '--source', type=str, default='SFID', help='input source path')
    parser.add_argument('--weights', nargs='+', type=str,
						default='runs/m_ep99_fogged/weights/best.pt',
						help='model.pt path(s)')
    parser.add_argument('--batch-size', type=int, default=8, help='size of each image batch')
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--device', default='0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
	
    parser.add_argument('--conf-thres', type=float, default=0.001, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.65, help='IOU threshold for NMS')
    parser.add_argument('--save-json', action='store_true', help='save a cocoapi-compatible JSON results file')
    parser.add_argument('--task', default='val', help="'val', 'test', 'study'")
    parser.add_argument('--single-cls', action='store_true', help='treat as single-class dataset')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--merge', action='store_true', help='use Merge NMS')
    parser.add_argument('--verbose', action='store_true', help='report mAP by class')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument(f'--show-each-cls', action='store_true', help='show evaluation of each class')
    parser.add_argument('--classes', type='+', default=['insulator', 'broken_piece'], help='the classes of the dataset')
    opt = parser.parse_args()
    return opt


