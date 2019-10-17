#extract the date and time from the inverted images
from scipy import ndimage, misc
from PIL import Image
from PIL import ImageFilter
import pytesseract as pt
import numpy as np
import os
import cv2	
def main():
    
    path="E:\\internshala\\videos\\invert"

    tempPath="E:\\internshala\\videos\\data files\\time2"
    for image_path in os.listdir(path):
            
            input_path = os.path.join(path, image_path)
            img=Image.open(input_path)
            text=pt.image_to_string(img,lang="eng")
            image_path=image_path[0:-4]
            fulltemppath = os.path.join(tempPath, 'time_'+image_path+".txt")
            print(fulltemppath)
            file1 = open(fulltemppath,"w")
            print(text)
            file1.write(text)
            file1.close() 
            


if __name__ == '__main__':
    main()

