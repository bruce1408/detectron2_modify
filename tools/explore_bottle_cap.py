import random
import os
from detectron2.utils.visualizer import Visualizer
from detectron2.data.catalog import MetadataCatalog, DatasetCatalog
from detectron2.data.datasets.coco import load_coco_json

import cv2

DATASET_ROOT = '/home/bruce/bigVolumn/Datasets/2.Dataset'
ANN_ROOT = os.path.join(DATASET_ROOT, 'annotations')

TRAIN_PATH = os.path.join(DATASET_ROOT, 'images')
VAL_PATH = os.path.join(DATASET_ROOT, 'images')

TRAIN_JSON = os.path.join(ANN_ROOT, 'train_cap.json')
VAL_JSON = os.path.join(ANN_ROOT, 'test_cap.json')


def plain_register_dataset():
    DatasetCatalog.register("coco_my_train", lambda: load_coco_json(TRAIN_JSON, TRAIN_PATH))
    MetadataCatalog.get("coco_my_train").set(  # thing_classes=CLASS_NAMES,  # 可以选择开启，但是不能显示中文，所以本人关闭
        evaluator_type='coco',  # 指定评估方式
        json_file=TRAIN_JSON,
        image_root=TRAIN_PATH)

    # DatasetCatalog.register("coco_my_val", lambda: load_coco_json(VAL_JSON, VAL_PATH, "coco_2017_val"))
    DatasetCatalog.register("coco_my_val", lambda: load_coco_json(VAL_JSON, VAL_PATH))
    MetadataCatalog.get("coco_my_val").set(  # thing_classes=CLASS_NAMES, # 可以选择开启，但是不能显示中文，所以本人关闭
        evaluator_type='coco',  # 指定评估方式
        json_file=VAL_JSON,
        image_root=VAL_PATH)


plain_register_dataset()
fruits_nuts_metadata = MetadataCatalog.get("coco_my_train")
print(fruits_nuts_metadata)
dataset_dicts = DatasetCatalog.get("coco_my_train")


for d in random.sample(dataset_dicts, 12):
    img = cv2.imread(d["file_name"])
    visualizer = Visualizer(img[:, :, ::-1], metadata=fruits_nuts_metadata, scale=0.95)
    vis = visualizer.draw_dataset_dict(d)
    img = vis.get_image()[:, :, ::-1]
    cv2.imshow('rr', img)
    cv2.waitKey(0)