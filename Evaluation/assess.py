from agh_vqis import process_single_mm_file, VQIs
from pathlib import Path


# video path 
video_path = Path('/test/a_horse_runs_on_the_Mars.mp4')

# setting 
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
    VQIs.blue_amount: True 
}

if __name__ == '__main__':
    process_single_mm_file(video_path, options=options)
