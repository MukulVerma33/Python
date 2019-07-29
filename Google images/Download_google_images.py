#########################################################################################################################
#   Before running the code please google_images_download library                                                       #
#   pip install google_images_download                                                                                  #      
#   The images would be downloaded in the current working directory in a folder having the category name downloads      #
#########################################################################################################################

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"PS Rana","limit":20,"print_urls":True}   # pass the Category of images you want and the number of images
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
