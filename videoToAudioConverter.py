####################################################################################################################
#   Before running the code please install moviepy library                                                         #
#   pip install moviepy           NOTE:- if it doesn't install try pip install moviepy --ignore-installed --user   #
####################################################################################################################
try:
    import sys
    from moviepy.editor import *
    video = VideoFileClip(sys.argv[1])      
    audio = video.audio
    audio.write_audiofile(sys.argv[2])
except:
    print("Usage: Type v2aConverter.py video_for_audio.mp4 audio_from_video.mp4/mp3(or any other format)")

#Type $v2aConverter.py video_for_audio.mp4 audio_from_video.mp4
