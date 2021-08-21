# Requirements for today's lesson
You should have built a small enclosure to hold up your Rasberry Pi Camera. We used lego for ours: 

<p align="center">
  <img alt="First Case" src="Assets/L2 Case1.jpg">
</p>

You might have found that you need to design the enclosure, or box, in a way that the cables can still connect to it. 

<p align="center">
  <img alt="Second Case" src="Assets/L2 Case2.jpg">
</p>

If your box blocks all the cables, then you can't connect the cables for  __Power__, __HDMI__,__Mouse__ and the __Keyboard__. 

You also need to ensure that you have MineCraft installed on your Rasberry Pi and that your screen allows Minecraft to run in a way that it doesn't stretch across the screen. 

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

Maximize that Minecraft Window that you had minimized in __Step 2__. You should now see a message displayed in the Minecraft world. 

Let's spend just a bit of time on a concept called BlackBox thinking. It's an easy concept which you actually learned while building your box. But it's a Super-Powerful way of thinking, which will help you to design hardware in future. 

# What's BlackBox Thinking?

When you built your box for the camera, you needed to make sure that you didn't block the lens. And you also needed to make sure that all the cables could still be connected to the Rasberry Pi.

You put a box around this complex thing called the Rasberry Pi, and made sure that the inputs and outputs worked. 

Let's for a second think about other complicated things, which have inputs and outputs, and put a black box around them. 

Think about a Baby. If you put a black box around a baby, what inputs does the baby need to work? What outputs does a baby make?

Think about a television. What inputs does it need to work? What outputs does it make?

Think about an XBox - not the games, just think about the hardware. That white box. What inputs does it need to work? What outputs does it make?

**Here's the thing to remember from all this: Any electronic device, and most other things, no matter how complicated, can be simplified by thinking about a Black Box, and then simplifying what goes in and what comes out.**

Minecraft is a game, and we've used the chat window to get something into MineCraft. There are other objects in MineCraft that we can change from outside, from Python. We will investigate these further in Lesson 3. 