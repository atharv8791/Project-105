import os 
import cv2 

path="Images"
Image=[]
for i in os.listdir(path):
    name,ext=os.path.splitext(i)
    if ext in ['.gif','.png','.jpg','.jpeg']:
     file_name = path+"/"+i
     Image.append(file_name)
count=len(Image)
frame=cv2.imread(Image[0])
height,width,layers = frame.shape
size=(width,height)
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0,count-1):
    frame=cv2.imread(Image[i])
    out.write(frame)
out.release()