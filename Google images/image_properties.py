#########################################################################################################################
#   Before running the code please cv2 library                                                                          #
#   pip install cv2                                                                                                     #
#   The images would be downloaded in the current working directory in a folder having the category name downloads      #
#########################################################################################################################

#########################################################################################################################
#   Before running the code please cv2 library                                                                          #
#   pip install cv2                                                                                                     #
#   The images would be downloaded in the current working directory in a folder having the category name downloads      #
#########################################################################################################################

import cv2
import numpy as np

# read image into matrix.

from os import listdir
from os.path import isfile, join
# Location of the images folder
mypath = 'D:/wrkshp/Google images/downloads/Beaches'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

for i in onlyfiles:
    path = "D:/wrkshp/Google images/downloads/Beaches/" + i
    m = cv2.imread(path)

    # get image properties.
    h,w,bpp = np.shape(m)
    print(f"Properties of image: {i}")
    # print image properties.
    print("width: " + str(w))
    print("height: " + str(h))
    print("bpp: " + str(bpp))
