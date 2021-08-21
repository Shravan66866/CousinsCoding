# Requirements for today's lesson
You should have built a small enclosure to hold up your Rasberry Pi Camera. We used lego. 

# What you will learn today
In this lesson we will do some coding to send messages to the Minecraft chat line. This is important, as it's our first contact into the MineCraft world from Python. 

**Step 1:**
Make sure your Rasberry Pi is switched on and that you can see the desktop. 

**Step 2:**
Open MineCraft. Create a new world. Now minimize the MineCraft window - don't close it. We need MineCraft running in the background for what we're going to do next. 

**Step 3:**
Open a new file in MuEditor and save it as "Lesson2.py". Ensure that Mu is set to **Python** mode and not to **PyGameZero** mode:

 Let's start by importing a MineCraft library into Python.

    from mcpi.minecraft import Minecraft

We will also import the library that controls our camera and the sleep timer:

    from picamera import PiCamera
    from time import sleep

Now let's create an instance of Minecraft in Python:

    mc = Minecraft.create()

    ## This code posts a message to Minecraft
        mc.postToChat("Hello World")

Maximize that Minecraft Window that you had minimized in Step 2. You should now see a message displayed in the Minecraft world. 

Let's spend just a bit of time on BlackBox thinking. 
you'll understand the concept of Black Box thinking. This is useful for simplifying complicated things. In your homework from Lesson 1, you built a box around the camera
While the black box protects the camera, you can also use it for a thinking experiment - black box thinking.
