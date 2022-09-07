import os
import click
from glob import glob

import cv2
from tqdm import tqdm
import moviepy.editor as moviepy


@click.command()
@click.option('--fps', default=10)
def main(fps):
    files = sorted(glob('data/raw/*.jpg'))
    height, width, layers = cv2.imread(files[0]).shape
    size = (width, height)

    arr = [cv2.imread(file) for file in files]

    avi = f'data/processed/timelapse-fps{fps}.avi'
    mp4 = f'data/processed/timelapse-fps{fps}.mp4'

    if os.path.exists(avi):
        print('Skip AVI')
    else:
        out = cv2.VideoWriter(
            filename=avi,
            fourcc=cv2.VideoWriter_fourcc(*'DIVX'),
            fps=fps, frameSize=size
        )
        for elem in tqdm(arr, desc='Building video'):
            out.write(elem)
        out.release()

    if os.path.exists(mp4):
        print('Skip MP4')
    else:
        clip = moviepy.VideoFileClip(avi)
        clip.write_videofile(filename=mp4, codec='mpeg4')
        clip.close()


if __name__ == '__main__':
    main()
