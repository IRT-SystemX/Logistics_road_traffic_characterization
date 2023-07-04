# Light Commercial Vehicles - Video analysis

This repository contain an end-to-end pipeline allowing you to do some simple video analysis of vehicles - specifically LCV (Light Commercial Vehicles).

## Functionnal modules
It is separated into four different modules each doing a specific functional task :
1. Anonymization 
2. Tracking
3. Classification 
4. Visualization

These modules can be executed independently as long as you include the correct inputs for each module.
### Anonymization 
From https://github.com/understand-ai/anonymizer this module allows you to blur faces and registration plates from video data. 

### Tracking 
From https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/tree/v5.0 this module allows uses the DeepSort tracking algorithm as well as a Yolov5 model to create a simple classification of the vehicles from a traffic road video. The outputs will be in the form of cropped images of all the vehicles identified for each frame of the video as well as a new video containing bounding boxes around the vehicles identified.

### Classification
This module allows you to specialize the classification done by the yolov5 model during tracking for Light commercial vehicles (LCV).

### Visualization
This module generates a streamlit web page that allows you to visualize the number of vehicles identified during the tracking and classification as well as the video with the bounding boxes generated during tracking.

## Docker Environnement

Each module contains a dockerfile that allows you to generate a docker image to execute the code more easily.
