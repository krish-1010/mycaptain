radius = float(input("Input the radius of the circle :"))

import math
PI = math.pi

def The_area():
	area = radius*radius*PI
	print( "The area of the circle with radius", radius ," is: %.2f" %area )
	
The_area()
