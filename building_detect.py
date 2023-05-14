from ultralytics import YOLO
from PIL import Image

model = YOLO('yolo_custom.pt')
im1 = Image.open("building8.png")
results = model.predict(source=im1, conf=0.4, save=True)