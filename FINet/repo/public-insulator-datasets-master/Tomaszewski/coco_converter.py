import json
import pandas as pd
from PIL import Image
from tqdm import tqdm
"""
Script to convert a label to COCO Format

DATASET FORMAT USED:
{
	"info": {
		"description": "THE COLLECTION OF IMAGES OF AN INSULATOR TAKEN OUTDOORS IN VARYING LIGHTING CONDITIONS WITH ADDITIONAL LASER SPOTS",
		"url": "https://cv.po.opole.pl/dataset1/",
		"version": "1.0",
		"year": 2018,
		"contributor": "Computer Vision Group - Institute of Computer Science - Opole University of Technology",
		"date_created": "2018/03/21"
	},
	"licenses": [
		{
			"url": "https://opensource.org/licenses/MIT",
			"id": 0,
			"name": "MIT"
		}
	],
	"categories": [
		{
			"supercategory": "insulator",
			"id": 0,
			"name": "insulator"
		}
	],
	"images": [
		{
			"licence": 0,
			"file_name": IMAGE_NAME,
			"coco_url": "",
			"height": HEIGHT,
			"width": WIDTH,
			"date_captured": DATE_HOUR,
			"flickr_url": "",
			"id": 0
		}
	],
	"annotations": [
		{
			"segmentation": [],
			"area": WIDTH * HEIGHT,
			"iscrowd": 0,
			"image_id": 0,
			"bbox": [CORNER.X, CORNER.Y, WIDTH, HEIGHT],
			"category_id": 0,
			"id": 0
		}
	]
}
"""


if __name__ == "__main__":
	SCALE_FACTOR = 2.34
	
	data = pd.read_csv("insulator_complete.csv")

	json_coco = json.loads("{}")
	json_coco["info"] = {
		"description": "THE COLLECTION OF IMAGES OF AN INSULATOR TAKEN OUTDOORS IN VARYING LIGHTING CONDITIONS WITH ADDITIONAL LASER SPOTS",
		"url": "https://cv.po.opole.pl/dataset1/",
		"version": "1.0",
		"year": 2018,
		"contributor": "Computer Vision Group - Institute of Computer Science - Opole University of Technology",
		"date_created": "2018/03/21"
	}
	json_coco["licenses"] = [
		{
			"url": "https://opensource.org/licenses/MIT",
			"id": 0,
			"name": "MIT"
		}
	]
	json_coco["categories"] = [
		{
			"supercategory": "insulator",
			"id": 0,
			"name": "insulator"
		},
		{
			"supercategory": "insulator",
			"id": 1,
			"name": "insulator_fault"
		}
	]
	json_coco["images"] = []
	json_coco["annotations"] = []

	json_coco_1q = {
        "info": json_coco['info'],
        "licenses": json_coco['licenses'],
        "categories": json_coco['categories'],
        "images": [],
        "annotations": []
    }

	for row_index in tqdm(range(0, data.shape[0])):
		file_path = data['Folder'][row_index]

		file_name = file_path.split('/')[-1]

		# get the image size
		img = Image.open(file_path)
		img_width, img_height = img.size
		img.close()

		if ('I_trees_v' not in file_path) and ('E_trees_v' not in file_path):
			obj_left = int(data['ROI_x'][row_index] / SCALE_FACTOR)
			obj_top = int(data['ROI_y'][row_index] / SCALE_FACTOR)
			obj_width = int(data['ROI_w'][row_index] / SCALE_FACTOR)
			obj_height = int(data['ROI_h'][row_index] / SCALE_FACTOR)
		else:
			obj_width = int(data['ROI_w'][row_index] / SCALE_FACTOR)
			obj_height = int(data['ROI_h'][row_index] / SCALE_FACTOR)
			obj_left = img_width - int(data['ROI_x'][row_index] / SCALE_FACTOR) - obj_width
			obj_top = img_height - int(data['ROI_y'][row_index] / SCALE_FACTOR) - obj_height

		object_id = int(data['Fault'][row_index])


		if row_index % 5 != 0:
			json_coco["images"].append({
				"licence": 0,
				"file_name": file_path,
				"coco_url": "",
				"height": img_height,
				"width": img_width,
				"date_captured": "2019-11-01 00:00:00",
				"flickr_url": "",
				"id": row_index
			})

			json_coco["annotations"].append({
				"segmentation": [],
				"area": obj_width * obj_height,
				"iscrowd": 0,
				"image_id": row_index,
				"bbox": [obj_left, obj_top, obj_width, obj_height],
				"category_id": object_id,
				"id": row_index
			})
		else:
			json_coco_1q["images"].append({
				"licence": 0,
				"file_name": file_path,
				"coco_url": "",
				"height": img_height,
				"width": img_width,
				"date_captured": "2019-11-01 00:00:00",
				"flickr_url": "",
				"id": row_index
			})

			json_coco_1q["annotations"].append({
				"segmentation": [],
				"area": obj_width * obj_height,
				"iscrowd": 0,
				"image_id": row_index,
				"bbox": [obj_left, obj_top, obj_width, obj_height],
				"category_id": object_id,
				"id": row_index
			})
	output = open("labels_4q" + ".json", "w")
	json.dump(json_coco, output)
	output.close()

	output = open("labels_1q" + ".json", "w")
	json.dump(json_coco_1q, output)
	output.close()
	print("FINISHED")

