# Classification

This module allows you to specialize the classification done by the yolov5 model during tracking for Light commercial vehicles (LCV). You can use our pre-trained ResNet50 model or a personal model. By default the code will use the pre-trained ResNet50 model trained on ImageNet (http://www.image-net.org), and then specialized on a small dataset containing LCV.

To use your personal model, you would need to specify it's path in the command line with the "--model" argument.

```
python inference_classifier.py --model <the_path_to_your_model>
```

## Docker environnement
To execute this module, the easiest way will be with the docker environnement.

First build the docker image from the parent directory :
```
docker build -t classifier -f Classification/Dockerfile .
```

Then you can run the docker image, be sure to add a permanent volume - with the -v argument - so that the results of the classifier are kept when the docker image is closed:
```
docker run -v data:/data -it classifier
```

Inside the docker image, go to the classification folder :

```
cd classification
```

You can then use the inference_classifier with:

```
python inference_classifier.py --model <the_path_to_your_model> --img_size <width*height> --data <path_to_the_vehicule_images> --max_img_in_memory <size_of_inference_batches>
```

Note that both the images and the predictions  have to be stored in memory for each batch. Depending on the RAM available, you might want to specify a small size for each batch of inference.
