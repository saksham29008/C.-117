import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
frame = cv2.imread(images(0))
weight, width, channels = frame.shape
size = (width, height)
print(size)

out = VideoWriter('project.np4',cv2.VideoWriter_fource(*'DIVK'),5, size)

for i in range

