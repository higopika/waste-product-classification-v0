from yolov5 import train, export

if __name__ == '__main__':
    #train.run(imgsz = 416, data = 'data.yaml', weights = 'yolo5s.pt', epochs = 2, batch = 32, workers = 4)
    train.run(data='data.yaml', imgsz=320, weights='yolov5s.pt',epochs = 1)

