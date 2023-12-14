import os
import sys
os.environ['PATH'] += ":/Users/yuetingguan/Downloads/"

from pathlib import Path
from agh_vqis import process_single_mm_file, VQIs




video_path = Path('test/many_birds_fly_over_a_plaza(LAMP).mp4') #a_horse_runs_on_the_Mars(LAMP)

options = {
    VQIs.blockiness: True,
    VQIs.SA: True,
    VQIs.letterbox: True,
    VQIs.pillarbox: True,
    VQIs.blockloss: True,
    VQIs.blur: True,
    VQIs.TA: True,
    VQIs.blackout: True,
    VQIs.freezing: True,
    VQIs.exposure: True,
    VQIs.contrast: True,
    VQIs.interlace: True,
    VQIs.noise: True,
    VQIs.slice: True,
    VQIs.flickering: True,
    VQIs.colourfulness: True,
    VQIs.ugc: True,
    VQIs.blur_amount: False  
}

if __name__ == '__main__':
      process_single_mm_file(video_path, options=options)
