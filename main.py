'''
translating our problem into code:

writing the problem in code is very similar to how we do it in english...

if price < 400:
	print("we wil buy the iphone")
else:
	print("we will buy the android")

_________________________
how conditions are written

if [condition]:
	##when condition is True
	do this
else:
	##any case ouside of condition being True
	do this
_________________________

lets see this in action:
## try it 3 times, 350,400,450

Quiz:

Which of the following is an example of conditional decision making?

a) If i clean my room, i will play outside, otherwise i will stay inside and do my chores 
b) i will play videogames with my friends later today 
c) i can haz cheeseburger




price = float(input("How much is the phone?: $"))

if price <= 400:
	print("we will buy the iphone")
	print("Because it is equivalent or less than the money we have")
else:
	print("we will buy the android")
	print("Because the iphone is too expensive")

	'''

 #a) If i clean my room, i will play outside, otherwise i will stay inside and do my chores

'''
isRoomClean = True

if isRoomClean:
    print ("I will go and play outside")
	print ("Because I cleaned my room")

else:
    print ('I will stay inside and do my chores')
    print ("because I did not clean my room")
'''
'''
#b) i will play videogames with my friends later today , lets say we have a variable calld isLaterToday and it stores a boolean
isLaterToday = True
if isLaterToday:
	print("I will play videogames with my friends")
	print("Because it is later today")
	
	
else:	
	print("I will not play videogames with my friends")
'''
## c) i can haz cheeseburger
isHungry = False

if isHungry:
	print("i can haz cheeseburger")

else:
	print("find a new meme")//