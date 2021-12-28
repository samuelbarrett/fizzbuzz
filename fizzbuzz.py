# coding the FizzBuzz game as an exercise for Tom Scott's video:
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
	play()


# my attempt, upon being introduced to the game rules
def play() :
	current = 1
	while(current <= maximum) :
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

# this is my second attempt after watching the rest of Tom's video
# note the efficiency and cleanliness of the code, this is much better.
def playBetter() :
	current = 1
	while(current <= maximum) :
		output = ""
		if(current % firstMultiple == 0) :
			output += "fizz"
		if(current % secondMultiple == 0) :
			output += "buzz"
		if(output == "") :
			output = current
		print(output)
		current+=1

main()