from inference import run_inference

input_img = 'input/royce.jpg'

run_inference(input_path=input_img,
              model_path='original.pth',
              output_dir='output/', # whether need intermediate results for animation.
              need_animation=True,  # resize original input to this size. None means do not resize.
              resize_h=None,        # resize original input to this size. None means do not resize.
              resize_w=None,
              serial=True)          # if need animation, serial must be True.

# Create gif from individual steps
import glob
from PIL import Image


# Set to dir with output images
in_dir = 'output/royce/*.jpg'
out_path = 'output/royce.gif'

img, *imgs = [Image.open(f) for f in sorted(glob.glob(in_dir))]
img.save(fp=out_path, format='GIF', append_images=imgs,
          save_all=True, duration=100, loop=0)

