from glob import glob

import cv2
from tqdm import tqdm
import moviepy.editor as moviepy

files = glob('data/raw/*.jpg')
height, width, layers = cv2.imread(files[0]).shape
size = (width, height)

arr = [cv2.imread(file) for file in sorted(files)]

out = cv2.VideoWriter(
    filename='data/processed/timelapse.avi',
    fourcc=cv2.VideoWriter_fourcc(*'DIVX'),
    fps=10, frameSize=size
)
for elem in tqdm(arr, desc='Building video'):
    out.write(elem)
out.release()

clip = moviepy.VideoFileClip('data/processed/timelapse.avi')
clip.write_videofile(
    filename='data/processed/timelapse.mp4',
    codec='mpeg4'
)
clip.close()
