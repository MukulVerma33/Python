import random as r
import os, sys, time, threading, multiprocessing


writefp = open('test.csv', 'w') 

for numberOfCores in range(1, 1000):
    startTime = time.time()
    def task(cmd):
        fr = open('D:\\wrkshp\\files\\Input\\'+cmd)
        fw = open('D:\\wrkshp\\files\\Output\\'+cmd, 'w')
        for line in fr:
            fw.write(line.upper())
        fr.close()
        fw.close()
        return

    # Run Multiple Thread
    files = os.listdir('D:\\wrkshp\\files\\Input')
    
    for f in files:
        cmd=f
        msg="...Thread %s start...."%(cmd)
        print(msg)
        t = threading.Thread(target=task , args=(cmd,))
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
        print ("Thread Left ... ",threading.activeCount() - 1)

    print("\n...All Thread ends....")

    endTime = time.time()
    print("Execution time is: ", endTime - startTime)
    writefp.write(f"{numberOfCores},{endTime - startTime}\n")
writefp.close()
