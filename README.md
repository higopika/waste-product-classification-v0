# Waste-Product-Classification

Step 1 : Create a virtual environement 
         Creating virtual enviroment for Ubuntu - https://youtu.be/DhLu8sI9uY4
         
Step 2 : Install yolo v5 inside the virtual environemnt
         pip install yolov5
         
Step 3 : Clone this repo into virtual environment
         
Step 4 : Replace the path variable in data.yaml file with the path of the root directory, the data folder is present in.

Some errors encountered : 
1) FileNotFoundError: [Errno 2] No such file or directory: 'yolo5s.pt' 
                      Solution 1 - yolov5 train --data data.yaml --weights '' --cfg yolov5s.yaml --img 640
                      Solution 2 - replace weight parameter from yolo5s.pt to yolo5m.pt in train.run function in train.py
  
2) requests.exceptions.ConnectionError: HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /api/models/yolov5s.pt (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f3ecc413d60>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))
                     Solution - Check the internet connection
          
3) Exception: Dataset not found ❌
                     Solution - Check the path assigned to the path variable in data.yaml file.
                      


