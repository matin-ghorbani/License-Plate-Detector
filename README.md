# License Plate Detector
Implement a Iranian license plate detector


## Installing Dependencies
```bash
pip install -r requirements.txt
```
## Iranian License Plate Detection
**I trained Yolov8 on Iranian License Plates on this [dataset](https://app.roboflow.com/sajjad-aemmi/persian-license-plate-detection)**

### Training And Validation Information
- Metrics / Precision(B): ***0.8172***
- Metrics / Recall(B): ***0.7004***
- Metrics / mAP50(B): ***0.7431***
- Metrics / mAP50-95(B): ***0.4032***
- Fitness : ***0.4372***

### speed:
- Preprocess: ***0.898***
- Inference : 2***7.0986***
- Loss: ***0.0007***
- Postprocess: ***5.7890***

### Inferences:
#### First Image
![First Image Result](./results/Iranian%20License%20Plate1%20Result.png)
#### First Image Plates
![First Image Plates](./results/Iranian%20License%20Plate1%20Plates.png)
---
#### Second Image
![Second Image Result](./results/Iranian%20License%20Plate2%20Result.png)
#### Second Image Plates
![Second Image Plates](./results/Iranian%20License%20Plate2%20Plates.png)

### Weight
You can download the
[License plate detector weight](https://drive.google.com/file/d/1oQe6WYsIMPh4b78FsoX1czTZX8jhXMRR/view?usp=sharing)
