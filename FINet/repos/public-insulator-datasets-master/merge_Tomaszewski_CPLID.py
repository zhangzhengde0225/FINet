import json

json_out = json.loads("{}")
json_out["info"] = {
		"description": "PAID dataset: a Public Augmented Insulator Defect dataset",
		"url": "",
		"version": "1.0",
		"year": 2020,
		"contributor": "Voxar Labs - Centro de Informática - Universidade Federal de Pernambuco - Brazil",
		"date_created": "2020/01/17"
}
json_out["licenses"] = [
    {
        "url": "https://opensource.org/licenses/MIT",
        "id": 0,
        "name": "MIT"
    }
]
json_out["categories"] = [
    {
        "supercategory": "insulator",
        "id": 0,
        "name": "normal_insulator"
    },
    {
        "supercategory": "insulator",
        "id": 1,
        "name": "defective_insulators"
    },
    {
        "supercategory": "insulator",
        "id": 2,
        "name": "insulators_fault"
    }
]
json_out["images"] = []
json_out["annotations"] = []

ftr_Tom = open('Tomaszewski/labels_paid_train.json', 'r')
ftr_CPLID = open('CPLID/CPLID_train.json', 'r')
ftt_Tom = open('Tomaszewski/labels_paid_test.json', 'r')
ftt_CPLID = open('CPLID/CPLID_test.json', 'r')

json_tr_Tom = json.load(ftr_Tom)
json_tr_CPLID = json.load(ftr_CPLID)
json_tt_Tom = json.load(ftt_Tom)
json_tt_CPLID = json.load(ftt_CPLID)

ann_count = 0

for image in json_tr_Tom['images']:
    json_out['images'].append(
        {
            "licence": image["licence"],
            "file_name": "Tomaszewski/" + image["file_name"],
            "coco_url": image["coco_url"],
            "height": image["height"],
            "width": image["width"],
            "date_captured": image["date_captured"],
            "flickr_url": image["flickr_url"],
            "id": str(image["id"]) + '_T'
        }
    )
for image in json_tr_CPLID['images']:
    json_out['images'].append(
        {
            "licence": image["licence"],
            "file_name": "CPLID/" + image["file_name"],
            "coco_url": image["coco_url"],
            "height": image["height"],
            "width": image["width"],
            "date_captured": image["date_captured"],
            "flickr_url": image["flickr_url"],
            "id": image["id"] + '_C'
        }
    )

for ann in json_tr_Tom['annotations']:
    json_out['annotations'].append(
        {
            "segmentation": ann["segmentation"],
            "area": ann["area"],
            "iscrowd": ann["iscrowd"],
            "image_id": str(ann["image_id"]) + '_T',
            "bbox": ann["bbox"],
            "category_id": ann["category_id"],
            "id": ann_count
        }
    )
    ann_count += 1

for ann in json_tr_CPLID['annotations']:
    json_out['annotations'].append(
        {
            "segmentation": ann["segmentation"],
            "area": ann["area"],
            "iscrowd": ann["iscrowd"],
            "image_id": ann["image_id"] + '_C',
            "bbox": ann["bbox"],
            "category_id": ann["category_id"],
            "id": ann_count
        }
    )
    ann_count += 1


output = open("Tomaszewski_CPLID_train" + ".json", "w")
json.dump(json_out, output)
output.close()

json_out["images"] = []
json_out["annotations"] = []

for image in json_tt_Tom['images']:
    json_out['images'].append(
        {
            "licence": image["licence"],
            "file_name": "Tomaszewski/" + image["file_name"],
            "coco_url": image["coco_url"],
            "height": image["height"],
            "width": image["width"],
            "date_captured": image["date_captured"],
            "flickr_url": image["flickr_url"],
            "id": str(image["id"]) + '_T'
        }
    )
for image in json_tt_CPLID['images']:
    json_out['images'].append(
        {
            "licence": image["licence"],
            "file_name": "CPLID/" + image["file_name"],
            "coco_url": image["coco_url"],
            "height": image["height"],
            "width": image["width"],
            "date_captured": image["date_captured"],
            "flickr_url": image["flickr_url"],
            "id": image["id"] + '_C'
        }
    )

for ann in json_tt_Tom['annotations']:
    json_out['annotations'].append(
        {
            "segmentation": ann["segmentation"],
            "area": ann["area"],
            "iscrowd": ann["iscrowd"],
            "image_id": str(ann["image_id"]) + '_T',
            "bbox": ann["bbox"],
            "category_id": ann["category_id"],
            "id": ann_count
        }
    )
    ann_count += 1

for ann in json_tt_CPLID['annotations']:
    json_out['annotations'].append(
        {
            "segmentation": ann["segmentation"],
            "area": ann["area"],
            "iscrowd": ann["iscrowd"],
            "image_id": ann["image_id"] + '_C',
            "bbox": ann["bbox"],
            "category_id": ann["category_id"],
            "id": ann_count
        }
    )
    ann_count += 1

output = open("Tomaszewski_CPLID_test" + ".json", "w")
json.dump(json_out, output)
output.close()

ftr_Tom.close()
ftr_CPLID.close()
ftt_Tom.close()
ftt_CPLID.close()
