## This lesson introduces Minecraft and takes a picture in a photobooth
## 1. Open Minecraft, and a build a photobooth. Then note the x, y and z coordinates of a place in your photobooth

from mcpi.minecraft import Minecraft
from picamera import PiCamera
from time import sleep

mc = Minecraft.create()
camera = PiCamera()

## This code posts a message to Minecraft
mc.postToChat("Find the Photobooth")

## This code takes a picture and saves it to a file
while True:
    x,y,z, = mc.player.getPos()
    sleep(2)
    if (round(x,1) >= 21.0) and (round(y,1) == 14.0) and (round(z,1) == 2.4):
        mc.postToChat("You are in the photobooth!")
        sleep(1)
        mc.postToChat("Smile!")
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/selfie.jpg')
        camera.stop_preview()