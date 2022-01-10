import json

json_out = json.loads("{}")
json_out["info"] = {
		"description": "THE COLLECTION OF IMAGES OF AN INSULATOR TAKEN OUTDOORS IN VARYING LIGHTING CONDITIONS WITH ADDITIONAL LASER SPOTS",
		"url": "https://cv.po.opole.pl/dataset1/",
		"version": "1.0",
		"year": 2018,
		"contributor": "Computer Vision Group - Institute of Computer Science - Opole University of Technology",
		"date_created": "2018/03/21"
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
    }
]
json_out["images"] = []
json_out["annotations"] = []


ftr_1 = open('Tomaszewski_train_1.json', 'r')
ftr_4 = open('Tomaszewski_train_4.json', 'r')
ftt_1 = open('Tomaszewski_test_1.json', 'r')
ftt_4 = open('Tomaszewski_test_4.json', 'r')

json_tr1 = json.load(ftr_1)
json_tr4 = json.load(ftr_4)
json_tt1 = json.load(ftt_1)
json_tt4 = json.load(ftt_4)

json_out['images'] = json_tr1['images'] + json_tr4['images']
json_out['annotations'] = json_tr1['annotations'] + json_tr4['annotations']

output = open("Tomaszewski_complete_train" + ".json", "w")
json.dump(json_out, output)
output.close()

json_out['images'] = json_tt1['images'] + json_tt4['images']
json_out['annotations'] = json_tt1['annotations'] + json_tt4['annotations']

output = open("Tomaszewski_complete_test" + ".json", "w")
json.dump(json_out, output)
output.close()

ftr_1.close()
ftr_4.close()
ftt_1.close()
ftt_4.close()