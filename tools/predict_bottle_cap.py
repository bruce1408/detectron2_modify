from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from detectron2.data.catalog import MetadataCatalog, DatasetCatalog
from detectron2.data.datasets.coco import load_coco_json
import os
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


# Inference with a keypoint detection model
WINDOW_NAME = "COCO detections"
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_1x.yaml"))
cfg.MODEL.WEIGHTS = "/home/bruce/PycharmProjects/detectron2/tools/output/model_0001784.pth"
print('loading from: {}'.format(cfg.MODEL.WEIGHTS))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5   # set the testing threshold for this model
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 11
cfg.DATASETS.TEST = ("coco_my_val", )
predictor = DefaultPredictor(cfg)


cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)  # 调整图像
# cv2.imshow(WINDOW_NAME, visualized_output.get_image()[:, :, ::-1])
im = cv2.imread('/home/bruce/bigVolumn/Datasets/2.Dataset/images/img_0005861.jpg')[:, :, ::-1]
cv2.imshow(WINDOW_NAME, im[:, :, ::-1])
cv2.waitKey(0)
outputs = predictor(im)
v = Visualizer(im, fruits_nuts_metadata, scale=1.2)
v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
cv2.imshow(WINDOW_NAME, v.get_image()[:, :, ::-1])
cv2.waitKey(0)