import os
import argparse
import cv2
from tqdm import tqdm
from pathlib import Path
import numpy as np
from glob import glob
from pycocotools.coco import COCO


def parse_args():
    parser = argparse.ArgumentParser(description='Data Label check')
    parser.add_argument('--data_root', default='', help='data file path')
    parser.add_argument('--json_file_path', default='', help='json file path')
    args = parser.parse_args()

    args.data_root = f'{os.environ["HOME"]}/datasets/insulator/UPID/augmented_images'
    args.json_file_path = f'{os.environ["HOME"]}/datasets/insulator/UPID/labels/augmented_train.json'
    # args.json_file_path = './Tomaszewski_CPLID_train.json'
    return args


def main():
    args = parse_args()

    coco_file = COCO(args.json_file_path)

    for index in tqdm(range(len(coco_file.imgToAnns.keys()))):
        # if index < 5800:
        #     continue
        img_id = list(coco_file.imgToAnns.keys())[index]
        img_name = Path(coco_file.imgs[img_id]['file_name']).name
        img_path = f'{args.data_root}/{img_name}'
        img = cv2.imread(img_path)
        print(f'indix: {index} img_name: {img_name} img:id{img_id}')
        for label in coco_file.imgToAnns[img_id]:
            if label['category_id'] == 0:
                color = (255, 0 , 0)
            elif label['category_id'] == 1:
                color = (0, 0, 255)
            elif label['category_id'] == 2:
                color = (0, 255, 0)
            bbox = label['bbox']  # x1y1xcyc
            bbox[2] += bbox[0]
            bbox[3] += bbox[1]
            bbox = np.array(bbox, dtype=np.int32)
            # img = cv2.rectangle(img, (label['bbox'][0], label['bbox'][1]), (label['bbox'][0]+label['bbox'][2], label['bbox'][1]+label['bbox'][3]), color, 2)
            img = cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
            cls = label["category_id"]
            print(f'category: {cls} bbox: {bbox}')
        # if cls != 0:
        if img_name == '049_2.jpg':
        # if index > 5850:
            cv2.imshow(f'debug', cv2.resize(img, (500, 500)))

            if cv2.waitKey(0) == 27:  # ESC
                break


if __name__ == "__main__":
    main()
