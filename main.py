
from cv2 import imread, cvtColor
import cv2
import numpy



def maxsat():
    img = imread("img_18.png", cv2.IMREAD_UNCHANGED)
    A = False
    if len(cv2.split(img)) == 4:
        (_,_,_,A) = cv2.split(img)
    print(A)
    hsv = cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
    h,s,v = cv2.split(hsv)
    n = numpy.max(s)
    s[s>0] = 255
    for x in s:
        print(x)
    hsv = cv2.merge((h,s,v))
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR_FULL)
    if A is not False:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        img[:,:,3] = A
    cv2.imwrite("test_18.png",img)



    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    maxsat()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
