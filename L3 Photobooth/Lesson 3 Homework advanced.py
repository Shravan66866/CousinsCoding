## This lesson introduces Minecraft and takes a picture in a photobooth
## 1. Open Minecraft, and a build a photobooth. Then note the x, y and z coordinates of a place in your photobooth

from mcpi.minecraft import Minecraft
from picamera import PiCamera
from time import sleep

mc = Minecraft.create()
camera = PiCamera()
#******************************
TakingAPhoto = False
#******************************
## This code posts a message to Minecraft
mc.postToChat("Find the Photobooth")

## This code takes a picture and saves it to a file
while True:
    x,y,z, = mc.player.getPos()
    #******************************
    print(x,y,z)
    #******************************
    sleep(2)

    #******************************
    if (x>= 13.9) and (x<= 17.1) and (z>= 7.8) and (z<= 11.1) and (y == 7.0) and (TakingAPhoto == False):
        #******************************
        mc.postToChat("You are in the photobooth!")
        sleep(1)
        mc.postToChat("Smile!")
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/selfie.jpg')
        TakingAPhoto = True
        camera.stop_preview()
        #******************************
        mc.postToChat ("How can we reset this photobooth?")
        #******************************
