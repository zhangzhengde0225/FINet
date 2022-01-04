import os
import errno
import random
import json
import cv2
from matplotlib import pyplot as plt
from pycocotools.coco import COCO

def main():
    data_root = '/media/F82E2D6A2E2D235C/Heitor/datasets/Isoladores/Tomaszewski/'

    coco_file = COCO(data_root + 'labels_4q.json')

    coco_output = {
        "info": coco_file.dataset['info'],
        "licenses": coco_file.dataset['licenses'],
        "categories": coco_file.dataset['categories'],
        "images": [],
        "annotations": []
    }

    image_ids = coco_file.getImgIds()
    random.shuffle(image_ids)

    train_list = image_ids[:int(len(image_ids)*0.8)]
    for image_id in train_list:
        image_info = coco_file.loadImgs([image_id])[0]
        coco_output["images"].append(image_info)
        annotation_ids = coco_file.getAnnIds(imgIds=[image_id])
        for annotation_id in annotation_ids:
            annotation_info = coco_file.loadAnns(annotation_id)[0]
            coco_output["annotations"].append(annotation_info)
            
    output = open(data_root + "Tomaszewski_train" + ".json", "w")
    json.dump(coco_output, output)
    output.close()

    coco_output["images"] = []
    coco_output["annotations"] = []

    test_list = image_ids[int(len(image_ids)*0.8):]
    for image_id in test_list:
        image_info = coco_file.loadImgs([image_id])[0]
        coco_output["images"].append(image_info)
        annotation_ids = coco_file.getAnnIds(imgIds=[image_id])
        for annotation_id in annotation_ids:
            annotation_info = coco_file.loadAnns(annotation_id)[0]
            coco_output["annotations"].append(annotation_info)
            
    output = open(data_root + "Tomaszewski_test" + ".json", "w")
    json.dump(coco_output, output)
    output.close()

if __name__ == "__main__":
    main()