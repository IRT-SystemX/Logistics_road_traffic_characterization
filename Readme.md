# Characterization of logistics road traffic based on video analysis

Last mile logistics flows (both B2B and B2C) generate a great impact on road traffic. Monitoring these patterns out of traffic data video could help to understand traffic arrangements under spatiotemporal parameters.

This repository contains an end-to-end pipeline supporting the processing of road traffic videos to assess the composition of the different vehicles’ flows and highlight the specific contribution of logistics.

## Functional modules
The repository is structured into four functional modules:
1.	Video anonymization
2.	Vehicles tracking
3.	Vehicles classification
4.	Data visualization
These modules can be executed independently as long as correct inputs are provided for each module.


### 1/ Video anonymization module
Function: faces and registration plates blurring

Inputs: road traffic video files

Outputs: anonymized video files

We suggest the use of the following anonymization modules: 
* https://github.com/understand-ai/anonymizer
* https://github.com/ArtLabss/open-data-anonymizer

### 2/ Vehicles tracking module
Function: classification of road vehicles in a video file; uses DeepSort tracking algorithm and a Yolov5 model; vehicles’ classes (trucks, cars, bikes, motorbikes, buses)

Inputs: road traffic video files

Outputs: cropped images of all the vehicles identified for each frame of the video plus a new video containing bounding boxes around the identified vehicles

https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/tree/v5.0 


### 3/ Vehicles classification module
Function: classification of road vehicles in image files; uses a pre-trained ResNet50 model; vehicles’ classes (trucks, Light Commercial Vehicles, cars, bikes, motorbikes, buses)

Inputs: cropped images of identified road vehicles 

Outputs: associated class saved in a csv file
This module allows you to specialize the classification done by the yolov5 model during tracking for Light commercial vehicles (LCV).


### 4/ Data visualization module
Function: dashboarding road classification results to visualize traffic composition on different data collection spots and time ranges

Inputs: csv file of vehicle's id with their identified class

Outputs: streamlit web page


## Docker Environnement

Each module contains a dockerfile that allows you to generate a docker image to execute the code more easily.

Each module can be used independently or sequentially depending on your personnal use. To use them independently you can go to the documentation presented in the "Readme.md" on each folder of this repository. To use them sequentially you can follow this documentation:

First you'll need to clone this repository and go to it's parent directory:

```
git clone URL
cd Logistics_road_traffic_characterization
```

Then, if you want to anonymize your video data (faces and/or license plates) you can use the code present in this repository: [understand.ai Anonymizer](https://github.com/understand-ai/anonymizer).

### Vehicles tracking module:

To use the tracking module first build and run the docker container: 
```
docker build -t detector -f 2_Vehicles_tracking_module/Dockerfile .

and

docker run -v ./results:/app/data -it detector

```
Then use the following commands: 
```
cd app

python track.py --source ./video --project ./data --imgsz 1920 --save-vid --save-crop --classes 1 2 3 5 7
```

### Vehicles classification module:
To use the classification module first build and run the docker container: 
```
docker build -t classifier -f 3_Vehicles_classification_module/Dockerfile .

and

docker run -v results:/app/data -it classifier
```

then use the following commands:

```
cd app

and

python inference_classifier.py --model model_ResNet50.h5 --img_size 224*224 --data ./video/tracking/ --max_img_in_memory 32
```
### Data visualization module:
To use the visualization module first build and run the docker container: 
```
docker build -t comptage -f ./4_Data_visualization_module/Dockerfile .

and

docker run -p 8501:8501 -it comptage
```

then use the following commands:

```
streamlit run main.py
```

When the command is executed, you can then visualize the streamlit web page by opening a web browser to the following url:

```
http://localhost:8501
```

## Credits 
This work has been supported by two research and development frameworks:

### European project LEAD
LEAD is a H2020 European collaborative project focusing on the development of digital twins for low emission last mile logistics. In that context IRT SystemX explored the generation of new urban logistics dataset to support the development of dedicated analysis and management capacities.

https://www.leadproject.eu/

![LEAD project logo](images/logo_lead.png) 

### Paris2Connect
Paris2Connect is an initiative supporting the demonstration of advanced digital infrastructures and solutions in urban areas.

https://paris2connect.agorize.com/fr/challenges/appel-a-experimentations

![Paris2connect logo](images/logo_paris2connect.png) 
 
## IRT SystemX
The Institute for Technological Research SystemX is a Research and Technical Organization positioned as an accelerator for the digital transition of industries and territories.
IRT SystemX is based in France and operates different technological platforms in the field of digital engineering.

www.irt-systemx.fr/en 

![IRT SystemX logo](images/logo_systemX.jpg) 

