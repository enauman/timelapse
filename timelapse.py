from time import sleep
from picamera import PiCamera
import argparse
parser = argparse.ArgumentParser(description="timelapse capture script")
parser.add_argument('-hf','--hflip', help='flip horizontally if True, default False',required=False)
parser.add_argument('-vf','--vflip',help='flip vertically if True, default False', required=False)
parser.add_argument('-i','--interval',help='timelapse interval in seconds',required=True)
parser.add_argument('-n','--number',help='total number of captures',required=True)
args = parser.parse_args()
camera = PiCamera(resolution=(1280, 720), framerate=30)
# Set ISO to the desired value
camera.iso = 200
# Wait for the automatic gain control to settle
sleep(2)
# Now fix the values
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g
camera.hflip = args.hflip
camera.vflip = args.vflip
interval = int(args.interval) # In seconds
number = int(args.number) #Total number of pictures
sleep(2)
try:
        for i, filename in enumerate(
                camera.capture_continuous('image{counter:04d}.jpg')):
            print(filename)
            sleep(interval)
            if i == number:
                break
finally:
	camera.close()
