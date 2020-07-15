'''
##Comparators

In programming, often times we need to compara data with eachother in order to make a decision on what to do next. a real world example of this is say we are putting on socks in the morning, we reach into our sock drawer and grab any two socks. In order for us to not look like rushed out of the house, we need to compare the two socks and see if they are the same. if they are the same, then we will put on both socks, otherwise we will keep searching until we find the matching sock, to make a complete pair. 



There are 3 main comparators:
greater than >
less than <
exactly equal == 

_______
example:

leftSock = "grey"
rightSock = "black"

if leftSock == rightSock:
	print("I can leave the house, becasue i have matching socks")
else:
	print("i must keep searching for a matching pair")

___________

When comparing, oftentimes we will be comparing the value stored inside of a variable. We can compare variable to variable, or variable to any data type directly.
______
Quiz:

What is the appropriate comparator operator to compare things to see if they are exactly eqqual?

a) =
b) == 
c) < >


'''

leftSock = "grey"


if leftSock == "grey":
	print("I can leave the house, becasue i have matching socks")
else:
	print("i must keep searching for a matching pair")