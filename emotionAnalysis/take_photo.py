from cv2 import *
from random import randint
import time

def takePictureAndSave():
    # Initialise the camera
    cam = VideoCapture(0)   # 0 -> index of camera
    time.sleep(0.2)

    s, img = cam.read()
    if s:    # frame captured without any errors
        # create a window and show the image
        #namedWindow("cam-test", WINDOW_AUTOSIZE)
        #imshow("cam-test",img)
        #waitKey(0)
        #time.sleep(5)
        #destroyWindow("cam-test")

        # Generate a random number for the image file name
        index = randint(1000, 9999)
        filename = "emotionAnalysis/images/image" + str(index) + ".jpg"

        # Save image
        imwrite(filename, img)
        print("picture taken filename: " + filename)
        # Release the camera
        cam.release()

        # Return the filename
        return filename
    cam.release()


# filename = takePictureAndSave()
# print(filename)
