import os
import json
import xml.etree.ElementTree as ET
from PIL import Image
from tqdm import tqdm
from glob import glob

im_files_normal = glob("Normal_Insulators/images/*")
im_files_defective = glob("Defective_Insulators/images/*")

json_coco = json.loads("{}")
json_coco["info"] = {
    "description": "CPLID: Chinese power line insulator dataset.",
    "url": "https://github.com/InsulatorData/InsulatorDataSet",
    "version": "1.0",
    "year": 2018,
    "contributor": " State Grid Corporation of China and WANG Zi-Hao",
    "date_created": "2018/09/15"
}
json_coco["licenses"] = [
    {
        "url": "free",
        "id": 0,
        "name": "free"
    }
]
json_coco["categories"] = [
    {
        "supercategory": "insulator",
        "id": 0,
        "name": "normal_insulator"
    },
    {
        "supercategory": "insulator",
        "id": 1,
        "name": "defective_insulator"
    },
    {
        "supercategory": "insulator",
        "id": 2,
        "name": "insulator_fault"
    }
]

json_coco["images"] = []
json_coco["annotations"] = []
labels_count = 0

print("CREATING LABELS FOR INSULATORS IMAGES")
for index in tqdm(range(len(im_files_normal))):
    img_path = im_files_normal[index]
    img_id = os.path.basename(img_path.replace('.jpg', ''))
    img = Image.open(img_path)
    json_coco["images"].append({
        "licence": 0,
        "file_name": img_path,
        "coco_url": "",
        "height": img.height,
        "width": img.width,
        "date_captured": "2019-11-01 00:00:00",
        "flickr_url": "",
        "id": img_id
    })

    mytree = ET.parse(img_path.replace('images', 'labels').replace('jpg', 'xml'))
    myroot = mytree.getroot()
    for obj in myroot.iter('object'):
        xmin = int(obj.find('bndbox').find('xmin').text)
        xmax = int(obj.find('bndbox').find('xmax').text)
        ymin = int(obj.find('bndbox').find('ymin').text)
        ymax = int(obj.find('bndbox').find('ymax').text)
    
        roi_h = ymax-ymin
        roi_w = xmax-xmin

        json_coco["annotations"].append({
            "segmentation": [],
            "area": roi_h * roi_w,
            "iscrowd": 0,
            "image_id": img_id,
            "bbox": [xmin, ymin, roi_w, roi_h],
            "category_id": 0,
            "id": labels_count
        })
        labels_count += 1

output = open("labels_normal" + ".json", "w")
json.dump(json_coco, output)
output.close()

json_coco["images"] = []
json_coco["annotations"] = []

print("CREATING LABELS FOR DEFECTIVES IMAGES")
for index in tqdm(range(len(im_files_defective))):
    img_path = im_files_defective[index]
    img_id = os.path.basename(img_path.replace('.jpg', ''))
    img = Image.open(img_path)
    json_coco["images"].append({
        "licence": 0,
        "file_name": img_path,
        "coco_url": "",
        "height": img.height,
        "width": img.width,
        "date_captured": "2019-11-01 00:00:00",
        "flickr_url": "",
        "id": img_id
    })

    mytree = ET.parse(img_path.replace('images', 'labels/insulator').replace('jpg', 'xml'))
    myroot = mytree.getroot()
    for obj in myroot.iter('object'):
        xmin = int(obj.find('bndbox').find('xmin').text)
        xmax = int(obj.find('bndbox').find('xmax').text)
        ymin = int(obj.find('bndbox').find('ymin').text)
        ymax = int(obj.find('bndbox').find('ymax').text)
    
        roi_h = ymax-ymin
        roi_w = xmax-xmin

        json_coco["annotations"].append({
            "segmentation": [],
            "area": roi_h * roi_w,
            "iscrowd": 0,
            "image_id": img_id,
            "bbox": [xmin, ymin, roi_w, roi_h],
            "category_id": 1,
            "id": labels_count
        })
        labels_count += 1
    
    mytree = ET.parse(img_path.replace('images', 'labels/defect').replace('jpg', 'xml'))
    myroot = mytree.getroot()
    for obj in myroot.iter('object'):
        xmin = int(obj.find('bndbox').find('xmin').text)
        xmax = int(obj.find('bndbox').find('xmax').text)
        ymin = int(obj.find('bndbox').find('ymin').text)
        ymax = int(obj.find('bndbox').find('ymax').text)
    
        roi_h = ymax-ymin
        roi_w = xmax-xmin

        json_coco["annotations"].append({
            "segmentation": [],
            "area": roi_h * roi_w,
            "iscrowd": 0,
            "image_id": img_id,
            "bbox": [xmin, ymin, roi_w, roi_h],
            "category_id": 2,
            "id": labels_count
        })
        labels_count += 1

output = open("labels_defective" + ".json", "w")
json.dump(json_coco, output)
output.close()
print("FINISHED")