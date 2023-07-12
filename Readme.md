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
https://github.com/understand-ai/anonymizer

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


## Logistics road traffic assessment
Last mile logistics flows (both B2B and B2C) generate a great impact on road traffic. Monitoring these patterns out of traffic data video could help to understand traffic arrangements under spatiotemporal parameters.

IRT SystemX implemented this demonstrator to tackle urban logistics challenges:
Development of urban logistics knowledge capacities based on video detection algorithms
Differentiation of logistics flows among road traffic
Categorisation of logistics vehicles

This experimentation has been conducted in Paris. Video data have been captured during spring 2022 and processed afterwards. The experimentation process has been supported by Paris2Connect initiative.

## Credits 
This work has been supported by two research and development frameworks:

### European project LEAD
LEAD is a H2020 European collaborative project focusing on the development of digital twins for low emission last mile logistics. In that context IRT SystemX explored the generation of new urban logistics dataset to support the development of dedicated analysis and management capacities.

https://www.leadproject.eu/

![LEAD project logo](images/logo_lead.png) 

### Paris2Connect
Paris2Connect is an initiative supporting the demonstration of advanced digital infrastructures and solutions in urban areas.

https://paris2connect.agorize.com/fr/challenges/appel-a-experimentations

![Paris2connect logo](images/logo_paris2connect.PNG) 
 
## IRT SystemX
The Institute for Technological Research SystemX is a Research and Technical Organization positioned as an accelerator for the digital transition of industries and territories.
IRT SystemX is based in France and operates different technological platforms in the field of digital engineering.

www.irt-systemx.fr/en 

![IRT SystemX logo](images/logo_systemX.jpeg) 

## Open source code

