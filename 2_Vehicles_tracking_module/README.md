# Vehicle tracking

This repository contains the code from https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/tree/v5.0 

It uses the DeepSort tracking algorithm as well as a Yolov5 model to create a first classification of a traffic road video. 

The output will be in the form of cropped images of all the vehicles identified for each frame of the video as well as a new video containing bounding boxes around the vehicles identified. 

## Docker environnement 

The easiest way to execute the following code is with a docker environnement.

To do this first build the docker image from the parent directory. Note that the creation of the image can take a while.
```
docker build -t detector -f 2_Vehicles_tracking_module/Dockerfile .
```
Then you can run the docker image, be sure to add a permanent volume - with the -v argument - so that the results of the classifier are kept when the docker image is closed:
```
docker run -v <path_to_link_persistent_volume>:/app/data -it detector

# by default use: 
docker run -v ./results:/app/data -it detector
```
Inside the docker image, go to the detector folder :

```
cd app
```

You can then execute the code with:

```
python track.py --source <path_to_the_video_folder> --project <path_to_save_the_output> --imgsz 1920  --save-vid --save-crop --classes 1 2 3 5 7

# By default use:
python track.py --source ./video --project ./data --imgsz 1920 --save-vid --save-crop --classes 1 2 3 5 7

```
Be sure to specify the output path to the persistent folder of your docker image (by default data/).
for cpu use add --device cpu to the command line.

When the tracking is done, simply execute:
```
exit
```