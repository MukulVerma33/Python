####################################################################################################################
#   Before running the code please install youtube_dl library                                                      #
#   pip install youtube_dl                                                                                         #
#   This Program also tells the time taken to download and the total data downloaded during execution time         #
####################################################################################################################

from __future__ import unicode_literals
import youtube_dl
import os

ydl_opts = {}
os.chdir('D:\\wrkshp\\Download youtube videos')
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])  #ydl.download("Video link") The file will be downloaded in your current working directory
