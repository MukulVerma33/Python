import threading
activeThread = threading.activeCount()
print("Num of threads:", activeThread)
