import cv2
from glob import glob
from tqdm import tqdm

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
