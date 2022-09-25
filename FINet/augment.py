"""
Generate Synthetic Foggy Insulator Dataset (SFID) by augment Unifying Public Datasets for Insulator Detection (UPID) [1] using \
synthetic fog method.
[1] https://github.com/heitorcfelix/public-insulator-datasets
"""
import os, sys
import shutil
from pathlib import Path
import numpy as np
from pycocotools.coco import COCO
from tqdm import tqdm
import cv2
import random
from copy import deepcopy

from scripts.synthetic_fog import SyntheticFog


class AugmentInsulatorDataset(object):
    def __init__(self, UPID_root):
        """
        :param UPID_root: Unifying Public Insulator Datasets root path, which contains two folds: augmented_images, labels.
        """
        self.sp = UPID_root  # source path
        self.tp = f'{Path(self.sp).parent}/SFID/fogged'  # target path

        self.sf = SyntheticFog()  # synthetic fog object

        train_json_file = f'{self.sp}/labels/augmented_train.json'  # UPID是用CPLID增强得来的
        # test_json_file = f'{self.sp}/labels/augmented_test.json'  # invalid
        self.train_dataset = COCO(train_json_file)
        # self.test_dataset = COCO(test_json_file)

    def augment(self, trte=None):
        assert trte in ['train', 'test', None]
        # 逐张进行增强
        sp = self.sp
        # imgs = [x for x in os.listdir(f'{sp}/augmented_images')]
        # imgss_with_jpg = [x for x in imgs if str(Path(x).suffix).lower() == '.jpg']
        # print(f'{len(imgs)} {len(imgss_with_jpg)}')  # 验证数据集都是.jpg结尾的
        tp = self.tp
        print(f'fogged data will be saved to: {tp}')
        if os.path.exists(self.tp):
            shutil.rmtree(self.tp)
        # os.makedirs(f'{self.tp}/images/train')
        # os.makedirs(f'{self.tp}/images/test')
        # os.makedirs(f'{self.tp}/labels/train')
        # os.makedirs(f'{self.tp}/labels/test')
        os.makedirs(f'{self.tp}/images')
        os.makedirs(f'{self.tp}/labels')

        # dataset = self.train_dataset if trte == 'train' else self.test_dataset
        dataset = self.train_dataset

        annss = dataset.imgToAnns  # annotations of all images and all targets
        bar = tqdm(range(len(annss)))
        for i in bar:
            img_id = list(annss.keys())[i]  # key
            anns = annss[img_id]  # value , list, annotations of all targets
            img_name = Path(dataset.imgs[img_id]['file_name']).name
            if img_name == '049_2.jpg':  # UPID数据集中的该图标注是错误的，忽略。
                continue
            # img_info: file_name, licence, cocourl, height, width, date_captured, id
            img_path = f'{sp}/augmented_images/{img_name}'
            assert os.path.exists(img_path), f'img does not exists {img_path}'
            img = cv2.imread(img_path)
            h, w, c = img.shape

            save_string = ''
            for ann in anns:
                cls = int(ann['category_id'])  # 0: prefect insulator 1: insulator with defect 2: defect
                if cls == 0:
                    pass
                elif cls == 1:  # 1-->0
                    cls = 0
                elif cls == 2:  # 2-->1
                    cls = 1
                else:
                    raise NameError(f'cls error: {cls}')

                bbox = deepcopy(ann['bbox'])  # bounding box in pixels, x1y1wh
                bbox[0] = (bbox[0] + bbox[2]/2)/w
                bbox[1] = (bbox[1] + bbox[3]/2)/h
                bbox[2] /= w
                bbox[3] /= h  # bbox in fraction proportion, 转为xc yc w h
                bbox_str = ' '.join([f'{x:6f}' for x in bbox])
                save_string += f'{int(cls)} {bbox_str}\n'

                if np.any(np.array(bbox) > 1):
                    print(f'img_path: {img_path}')
                    print(img.shape, anns)
                    print(f'orgin_bbox: {ann["bbox"]} new: {bbox}')
                    exit()

            # print(f'{img_name} {img.shape} raw_box: {ann["bbox"]} save str: {save_string}')
            # exit()
            # 先保存原始图像和标注
            # src_img_save_path = f'{tp}/images/{trte}/{img_id:0>6}.jpg'
            src_img_save_path = f'{tp}/images/{img_id:0>6}.jpg'
            src_txt_save_path = f'{tp}/labels/{img_id:0>6}.txt'
            self.save(src_img_save_path, img, src_txt_save_path, save_string)

            # 保存fogged图像和标注
            fogged_img_save_path = f'{tp}/images/fogged_{img_id:0>6}.jpg'
            fogged_txt_save_path = f'{tp}/labels/fogged_{img_id:0>6}.txt'
            fogged_txt = save_string  # 不变

            # random brightness and thickness
            br = np.clip(0.2 * np.random.randn() + 0.5, 0.1, 0.9)  # 0.1~0.9
            th = np.clip(0.01 * np.random.randn() + 0.05, 0.01, 0.09)
            normed_img = img.copy()/255.0
            fogged_img = self.sf.fogging_img(
                normed_img, brightness=br, thickness=th, high_efficiency=True)
            fogged_img = np.array(fogged_img*255, dtype=np.uint8)
            self.save(fogged_img_save_path, fogged_img, fogged_txt_save_path, fogged_txt)

            show = False
            if show:
                print(f'img_name: {Path(img_path).name} img: {img.shape} br: {br} th: {th} max: {np.max(fogged_img)}')
                self.show(img, name='src', wait=False)
                self.show(fogged_img, wait=False)
                if cv2.waitKey(0) == ord('q'):
                    break

            bar.set_description(f'file and label {img_name} saved.')

    def split_to_train_and_test(self, test_propotion):
        """
        :param test_propotion: sample ratios of validate dataset, i.e. test/(train+test)
        :return:
        """
        dp = self.tp  # synthetich foggy insulator dataset path
        tp = f'{Path(dp).parent}/fogged_v5_format'
        assert os.path.exists(dp)
        assert 0 <= test_propotion < 1
        if os.path.exists(tp):
            shutil.rmtree(tp)
        os.makedirs(f'{tp}/images/train')
        os.makedirs(f'{tp}/images/test')
        os.makedirs(f'{tp}/labels/train')
        os.makedirs(f'{tp}/labels/test')

        imgs = sorted([x for x in os.listdir(f'{dp}/images') if x.endswith('jpg')])

        random.seed(930429)
        random.shuffle(imgs)
        slices = int(test_propotion*len(imgs))
        test_imgs = imgs[:slices]
        train_imgs = imgs[slices::]
        print(f'split into train and test datasets: \n'
              f'all images: {len(imgs)} train images: {len(train_imgs)} test_images: {len(test_imgs)}')

        for i, img in enumerate(tqdm(train_imgs)):
            p = Path(img)
            shutil.copy(f'{dp}/images/{p.stem}.jpg', f'{tp}/images/train/{p.stem}.jpg')
            shutil.copy(f'{dp}/labels/{p.stem}.txt', f'{tp}/labels/train/{p.stem}.txt')

        for i, img in enumerate(tqdm(test_imgs)):
            p = Path(img)
            shutil.copy(f'{dp}/images/{p.stem}.jpg', f'{tp}/images/test/{p.stem}.jpg')
            shutil.copy(f'{dp}/labels/{p.stem}.txt', f'{tp}/labels/test/{p.stem}.txt')

    def save(self, imp, img, txtp, txt):
        cv2.imwrite(imp, img)
        with open(txtp, 'w') as f:
            f.writelines(txt)

    def show(self, img, name='xx', wait=True):
        show_img = cv2.resize(img, (500, 500))
        cv2.imshow(name, show_img)
        if wait:
            cv2.waitKey(0)


if __name__ == '__main__':
    upid_root = '/home/zzd/datasets/insulator/UPID'
    aid = AugmentInsulatorDataset(upid_root)
    aid.augment()
    aid.split_to_train_and_test(test_propotion=0.2)









