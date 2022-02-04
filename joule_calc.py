#!/usr/bin/env python3

ft2m = 0.3048 #The conversion factor for turning feet into meters.

mass = float(input("\nPlease enter ammo weight: (in grams) ")) #Getting the weight of the ammo used. Can only be entered in grams.

speed = float(input("\nPlease enter FPS of weapon: (in feet per second) ")) #Getting the speed of the ammo when fired. Can only be entered in Feet Per Second.

#The basic formula for caculating joules: Joules = 0.5 x mass x velocity^2.
#Mass must be in kilograms, and velocity must be in meters per second.

#Hence, all the conversions below.
joules = 0.5*((mass*0.001)*((speed*ft2m)**2))

#Print all the outputs in a nice user-friendly message.
print("\nAt {} FPS with {} gram ammo, your energy output is {} joules.".format(speed, mass, joules))
