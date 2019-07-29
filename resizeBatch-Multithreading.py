from PIL import Image
import os
import sys
import time
import threading
import multiprocessing
from os import listdir
from os.path import isfile, join
for numberOfCores in range(6,7):
    startTime = time.time()

    def task(cmd):
        img = Image.open('D:/wrkshp/ass2/downloads/Dog/'+cmd)
        basewidth = img.width/2
        baseheight = img.height/2
        img = img.resize((int(basewidth), int(baseheight)), Image.ANTIALIAS)
        img = img.convert('RGB')
        img.save('D:/wrkshp/ass2/Resized/'+cmd+'.jpg')
        return

    # Run Multiple Thread
    mypath = 'D:/wrkshp/ass2/downloads/Dog'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for im in onlyfiles:
        cmd = im
        msg = "...Thread %s start...." % (cmd)
        print(msg)
        t = threading.Thread(target=task, args=(cmd,))
        t.start()
        while True:
            if threading.activeCount()-1 <= numberOfCores:
                break
            #time.sleep(1)

    # Waiting to finish the thread
    while True:
        if threading.activeCount() == 1:
            break
        #time.sleep(1)
        print("Thread Left ... ", threading.activeCount() - 1)

    print("\n...All Thread ends....")

    endTime = time.time()
    print("Execution time is: ", endTime - startTime)