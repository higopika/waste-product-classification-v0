# Waste-Product-Classification

Step 1 : Create a virtual environement 
         Creating virtual enviroment for Ubuntu - https://youtu.be/DhLu8sI9uY4
         
Step 2 : Install yolo v5 inside the virtual environemnt
         pip install yolov5
         
Step 3 : Clone this repo into virtual environment
         
Step 4 : Replace the path variable in data.yaml file with the path of the root directory, the data folder is present in.

Some errors encountered : 
1) FileNotFoundError: [Errno 2] No such file or directory: 'yolo5s.pt' 
                      Solution - yolov5 train --data data.yaml --weights '' --cfg yolov5s.yaml --img 640


