# coding the FizzBuzz game as a challenge for Tom Scott's video:
# https://youtu.be/QPZ0pIK_wsc
#
"""
 Created on Tue Dec 28 2021

 @author: Sam Barrett
"""

firstMultiple = 3
secondMultiple = 5
maximum = 100

def main() :
	print("ayo")
	play()


def play() :
	current = 1
	while(current < maximum) :
		if(current % firstMultiple != 0):
			if(current % secondMultiple != 0) :
				print(current)
			else :
				print("buzz")
		else :
			if(current % secondMultiple != 0) :
				print("fizz")
			else :
				print("fizzbuzz")
		current+=1
	return 0
	
