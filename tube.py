from pytube import YouTube
import os
from moviepy.editor import *





a = input()
r = input('res:')
ress = r+'p' #畫質
print(ress)
yt = YouTube(a)
mb_ = yt.streams.filter(res=ress).first().filesize_mb #大小
print("download",f'{mb_} MB')

tvideo = yt.streams.filter(res=ress,type='video').first()
tvideo_filename = 'video'
tvideo.download(filename=tvideo_filename)
taudio = yt.streams.filter(type='audio').first()
taudio_filename = 'audio'
taudio.download(filename=taudio_filename)
filename_ = tvideo.default_filename

os.system(f'ffmpeg -i "{tvideo_filename}" -i "{taudio_filename}" -c copy "{tvideo.default_filename[:-4]}.mp4"')
os.remove(tvideo_filename)
os.remove(taudio_filename)
