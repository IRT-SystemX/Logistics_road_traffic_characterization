# Comptage

This module allows you to visualize the outputs of both the tracking and the classification module. It is run by a simple streamlit that shows the bar plot of the classification as well as the video generated in the tracking module. 

## Docker environnement
To execute this module, the easiest way will be with the docker environnement.

First build the docker image from the parent directory :
```
docker build -t comptage -f ./4_Data_visualization_module/Dockerfile .

```

Then you can directly run the docker image, don't forget to specify the port 8501 so that the streamlit can be open on your localhost from the docker:
```
docker run -p 8501:8501 -it comptage
```

Inside of the docker image, simply execute the main.py file to open the streamlit web page with:

```
streamlit run main.py
```
When the command is executed, you can then visualize the streamlit web page by opening a web browser to the following url:

```
http://localhost:8501
```
