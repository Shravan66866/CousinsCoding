## This lesson introduces Minecraft and puts a message into Minecraft

from mcpi.minecraft import Minecraft
from picamera import PiCamera
from time import sleep

mc = Minecraft.create()

## This code posts a message to Minecraft
mc.postToChat("Hello World")