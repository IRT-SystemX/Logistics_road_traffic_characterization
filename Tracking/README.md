# Vehicle tracking

This repository contains the code from https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/tree/v5.0 

It uses the DeepSort tracking algorithm as well as a Yolov5 model to create a first classification of a traffic road video. 

The output will be in the form of cropped images of all the vehicles identified for each frame of the video as well as a new video containing bounding boxes around the vehicles identified. 

## Docker environnement 

The easiest way to execute the following code is with a docker environnement.

To do this first build the docker image from the parent directory 
```
docker build -t detector -f logistic_vehicles_detection/Dockerfile .
```
Then you can run the docker image, be sure to add a permanent volume - with the -v argument - so that the results of the classifier are kept when the docker image is closed:
```
docker run -v data:/data -it detector
```
Inside the docker image, go to the detector folder :

```
cd detector
```

You can then execute the code with:

```
python track.py --source <path_to_the_video_folder> --project <path_to_save_the_output> --imgsz 1920  --save-vid --save-crop --classes 1 2 3 5 7
```
for cpu use add --device cpu to the command line.
