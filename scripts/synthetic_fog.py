"""
直接运行程序可以测试合成雾气效果
Produced by: zhangzhengde@sjtu.edu.cn
"""
import os
import argparse
import math
import cv2
import time
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


class SyntheticFog(object):
    def __init__(self):
        pass

    def __call__(self,speed_up, img_path , out_path):
        img_path = img_path
        # img_path = '../sources/IMG_6685.JPG'
        assert os.path.exists(img_path), f'error: img does not exists, {img_path}'
        img = cv2.imread(img_path)
        print(img.shape)
        img = img/255.0
        print(f'fogging...')
        t0 = time.time()
        br = 0.7
        th = 0.05
        fogged_img = self.fogging_img(
            img, brightness=br, thickness=th,
            high_efficiency = speed_up)
        print(f'fogging time: {(time.time()-t0)*1000:.4f}ms')
        rf = 1  # resize factor
        img = cv2.resize(img, (int(img.shape[1]*rf), int(img.shape[0]*rf)))
        fogged_img = cv2.resize(fogged_img, ((int(fogged_img.shape[1]*rf)), (int(fogged_img.shape[0]*rf))))
        fogged_img = np.array(fogged_img*255, dtype=np.uint8)
        # cv2.imshow('src', img)
        # cv2.imshow('fogged', fogged_img)
        # cv2.waitKey(0)
        cv2.imwrite(out_path+f'{Path(img_path).stem}_br{br}_th{th}.jpg', fogged_img)

    def fogging_img(self, img, brightness=0.7, thickness=0.05, high_efficiency = False):
        """
        fogging image
        :param img: src img
        :param brightness: brightness
        :param thickness: fog thickness, without fog when 0, max 0.1,
        :param high_efficiency: use matrix to improve fogging speed when high_efficiency is True, else use loops
                low efficiency: about 4000ms, high efficiency: about 80ms, tested in (864, 1152, 3) img
        :return: fogged image
        """
        assert 0 <= brightness <= 1
        assert 0 <= thickness <= 0.1
        fogged_img = img.copy()
        h, w, c = fogged_img.shape
        if not high_efficiency:  # use default loop to fogging, low efficiency
            size = np.sqrt(np.max(fogged_img.shape[:2]))  # 雾化尺寸
            center = (h // 2, w // 2)  # 雾化中心
            # print(f'shape: {img.shape} center: {center} size: {size}')  # 33
            # d_list = []
            for j in range(h):  #
                for l in range(w):
                    d = -0.04 * math.sqrt((j - center[0]) ** 2 + (l - center[1]) ** 2) + size
                    # print(f'd {d}')
                    td = math.exp(-thickness * d)
                    # d_list.append(td)
                    fogged_img[j][l][:] = fogged_img[j][l][:] * td + brightness * (1 - td)
                # x = np.arange(len(d_list))
                # plt.plot(x, d_list, 'o')
                # if j == 5:
                #     break
        else:  # use matrix  # TODO: 直接使用像素坐标，距离参数不适用于大分辨率图像，会变成鱼眼镜头的样子. done.
            use_pixel = True
            size = np.sqrt(np.max(fogged_img.shape[:2])) if use_pixel else 1  # 雾化尺寸，sqrt(w), (w, h, 3)
            h, w, c = fogged_img.shape
            hc, wc = h // 2, w // 2
            mask = self.get_mask(h=h, w=w, hc=hc, wc=wc, pixel=use_pixel)  # (h, w, 2)  # O(max(w, h))
            d = -0.04 * np.linalg.norm(mask, axis=2) + size  # (h, w, 2) -> (h, w), O(h*w)

            td = np.exp(-thickness * d)

            for cc in range(c):
                fogged_img[..., cc] = fogged_img[..., cc] * td + brightness*(1-td)

            # a = np.linalg.norm(mask, axis=2)
            # print(f'size: {fogged_img.shape} a: {a} max: {np.max(fogged_img)} {np.min(fogged_img)}')

            fogged_img = np.clip(fogged_img, 0, 1)  # 解决黑白噪点的问题
            # print(f'mask: {mask[:, :, 1]} {mask.shape}')
            # print(f'd: {d} {d.shape}')

        return fogged_img

    def get_mask(self, h, w, hc, wc, pixel=True):
        mask = np.zeros((h, w, 2), dtype=np.float32)
        if pixel:
            mask[:, :, 0] = np.repeat(np.arange(h).reshape((h, 1)), w, axis=1) - hc  # loop o(h)
            mask[:, :, 1] = np.repeat(np.arange(w).reshape((1, w)), h, axis=0) - wc  # loop o(w)
        else:
            mask[:, :, 0] = np.repeat(np.linspace(0, 1, h).reshape(h, 1), w, axis=1) - 0.5
            mask[:, :, 1] = np.repeat(np.linspace(0, 1, w).reshape((1, w)), h, axis=0) - 0.5
        return mask


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='synthetic_fog.py')
    parser.add_argument('--speed_up', type=bool, default= False, help='matrix optimization')
    parser.add_argument('--img', type=str, default= '../sources/insulator1.jpg', help='source img path')
    parser.add_argument('--out', type=str, default= '../sources/fogged/', help='output img path')
    opt = parser.parse_args()
    print(opt)
    synf = SyntheticFog()
    synf(opt.speed_up,opt.img,opt.out)



