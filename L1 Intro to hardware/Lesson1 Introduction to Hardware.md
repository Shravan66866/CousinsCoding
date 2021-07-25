# What we will learn in these lessons:
You're going to learn about hardware, and the basics of designing your own devices. Ever wondered how a GoPro actually works? What's inside that black box? Can you guess?

![GoPro](https://cdn.mos.cms.futurecdn.net/3CiExD3rnLr2cfKWoqXdaL-970-80.jpg.webp)

# Why is this useful?
With knowledge of how simple it is to design and build devices, you could one day start your own business to build and sell your ideas to the world. GoPro was started by a guy named Nick Woodman. While surfing in Australia, he noticed that surfers could not film their action shots effectively. This inspired him to start GoPro. Today he is worth many hundreds of millions of dollars.

# What else will we learn?
We will learn how to get information from the real world into the computer. You will get a feel for how sensors work to capture information, like a camera image or temperature, and how sensors send that data into the computer. 

This can be applied to almost any problem, like controlling a robot on the moon; or measuring blood for diseases and reading that into a computer for a doctor to figure out if you're sick. 

We'll do a simple project to capture some real data and feed that into Minecraft, using the Python language. 

# Getting started with Hardware
What does the word "hardware" mean to you? So far, you have used a computer to design the PyGame and to play it. 

For our lesson, we'll need to understand a bit more about how a computer works. How it gets information from the world and how you can use that information to create things like games, GoPro cameras, or robots.

# What's the Rasberry Pi?
It's a little computer. A really tiny baby computer, that has the building blocks of everything you would see on a laptop, iPad or MacBook. 

![Rasberry Pi](https://projects-static.raspberrypi.org/projects/raspberry-pi-setting-up/0d6033edf45ad2d4185ed05d6cd9a01e2f803034/en/images/pi-plug-in.gif)

Before we go any further, let's look at the main components of a real baby, because babies have many similar components to computers. 

![Baby](https://i.ytimg.com/vi/wfvxTyFJOiU/maxresdefault.jpg)

## **Understanding Babies and Computers**
When you were born, could you speak?  How did you communicate with the world?

While you couldn't speak right away, you could cry. In fact, all babies cry, right? They can all cry, because "crying" is nature's way of protecting babies. Crying is a way for babies to tell their parents when they are hungry, or cold, or have a poo nappy. 

Let's introduce a term called *Firmware*, because we will be using firmware to update the software that runs on components of the Rasberry Pi.

### **Crying is *Baby Firmware***

When you were a baby, did someone teach you the lanugage of how to cry? What made you learn to cry in a specific way for food, and in another way if you got injured?

You didn't have to learn to cry. Crying is standard software, that ships with every baby. Crying is like software language that comes standard with every baby. In computers, we call this type of software *firmware*. 

For your Apple Mac, firmware is very simple code which the factory that builds Apple computer loads into the electronics, to make it do the basic things you take for granted. Your keyboard uses firmware to do basic things like responding to keystrokes when you press them; your mouse uses firmware to take information from the laser about where the mouse is, and sends that to the computer to move the pointer on the screen. 

Cameras use firmware to take information from sensors that measure light, and send that information to memory, which the computer talks to, to figure out which pixels to light up on the screen to display your *selfie*.

A laptop computer has lots of little components inside, each running *Firmware* to control the electronics which powers it.

Let's go one step up from *Firmware*. There's another important concept in computer science, called an *Operating System*. This is high level software that brings together all the bits of firmware into one easy-to-use platform.

Rasberry Pi can use many different *Operating Systems*, and the one we will use is called *Raspian*.

### **The Digestive System is like an *Operating System* for eating**
![Digestive System](https://pixfeeds.com/images/biology/human-body-systems/1280-607651486-human-digestive-system-for-kids.jpg)

When you eat food, many body components come together to make it all work. With these components you chew it, swallow it, digest it, and ultimately, poo out the waste. Although your mouth, your stomach, and other body parts each have their functions controlled by their *Firmware*, the *Digestive System* is a a kind of *Operating System* that brings everything together to perform the high level task of eating. 

Teaching a baby to kick a ball and play the game of soccer, is like loading *MineCraft* onto a computer. You're installing a game onto your hardware.


# Take a closer look at your Rasberry Pi Hardware

![Pi perspective](https://www.raspberrypi.org/documentation/usage/gpio/images/raspio-portsplus.jpg)

See all those little black squares and rectangles? I am sure you have seen them on other devices if you've opened up a computer (which must be done with an adult). Ever wondered what the black boxes are?

Like the digestive system, they each perform a function that together, make it possible for the Rasberry Pi to move electricity around it, and to interact with the outside world through cameras and sensors. 

We will be connecting a Camera directly to the Rasberry Pi, which your parents have probably ordered already:

![Pi Camera](https://projects-static.raspberrypi.org/projects/getting-started-with-picamera/659a837aafb1ff69f222c16debae07be88459ab3/en/images/camera-module.png)

The camera connects into the Rasberry Pi Board as follows:

![Pi Camera Connection](https://projects-static.raspberrypi.org/projects/getting-started-with-picamera/659a837aafb1ff69f222c16debae07be88459ab3/en/images/pi-camera-attached.jpg)

You can learn more about how to connect the camera using this link: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

# Cautions on using your Rasberry Pi #
1. It uses electricity. You can get elecrocuted. Handle with care
2. It does not like static electricity. Be careful about touching it when you're wearing fuzzy clothes. Rather put in into a case.
3. Like baby eyes but without eyelids, the camera is naked. Watch you don't damage the lens. You can build a case for your camera to protect it.
4.  It can get hot. Like a baby that makes Poo in a Diaper, the Rasberry Pi takes electricity in and produces waste in the form of heat. That heat must go out of it, and fans and heat sinks perform this function.





