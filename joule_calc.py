#!/usr/bin/env python3
metric = False #Change this to 'True' if you want to use the metric values.


ft2m = 0.3048 #The conversion factor for turning feet into meters.

mass = float(input("\nPlease enter ammo weight: (in grams) ")) #Getting the weight of the ammo used. Can only be entered in grams.

if metric:
    speed = float(input("\nPlease enter velocity of weapon: (in meters per second) ")) #Getting the speed ot the weapon. Can only be entered in metere per second.
else:
    speed = float(input("\nPlease enter FPS of weapon: (in feet per second) ")) #Getting the speed of the ammo when fired. Can only be entered in Feet Per Second.

#The basic formula for caculating joules: Joules = 0.5 x mass x velocity^2.
#Mass must be in kilograms, and velocity must be in meters per second.

#Hence, all the conversions below.
if metric:
    joules = 0.5*((mass*0.001)*(speed**2))
else:
    joules = 0.5*((mass*0.001)*((speed*ft2m)**2))

#Print all the outputs in a nice user-friendly message.
if metric:
    print("\nAt {} m/s with {} gram ammo, your energy output is {} joules.".format(speed, mass, joules))
else:
    print("\nAt {} FPS with {} gram ammo, your energy output is {} joules.".format(speed, mass, joules))
