**Step 1:**
Create a new world in Minecraft, and build a small structure that looks like a photobooth.

**Step 2:**
Choose an area on the floor where you will stand, to initiate a photo on the camera. You might want to choose a different block for this.

**Step 3:**
Get Steve to walk onto the different coloured block. Now, write down the x,y,and z coordinates of the place where he is standing. We will use these values to tell Python when Steve is at the right place to take a Selfie. 

**Step 4:**
Now Minimize Minecraft - don't close it. We need it running in the background. 

Here's the code for Lesson 3. Open a new MuEditor Window and type in the following:

    ## This lesson introduces Minecraft and takes a picture in a photobooth
    ## 1. Open Minecraft, and a build a photobooth. Then note the x, y and z coordinates of a place in your photobooth

We do need to import the right libraries into Mu:

    from mcpi.minecraft import Minecraft
    from picamera import PiCamera
    from time import sleep

Now we will create an instance of the camera and an instance of Minecraft:

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

Now go to the File Explorer and open the file ***selfie.jpg***

Yay, you now have a photo of yourself. What's even cooler, is that you've actually got something out of the Minecraft world. You made a Minecraft event trigger something real to happen in the physical world. 

The possibilities are endless. Think about other things you would like to happen in the real world, in response to Minecraft. Think about other ways that this black box, called MineCraft, could be used to make physical things happen in the real world...