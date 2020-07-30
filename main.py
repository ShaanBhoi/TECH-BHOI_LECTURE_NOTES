## codeRun01

def summaryOfSections01():
	print("\n----------\nLECTURE 01\n----------\n")
	
def sectionOutput():
	print("--OUTPUT--")
	text = "Whenever we use an app or website, we expect it to do something when we click/tap.\nThis is an example of what we call an output.\nIt shows back to us something useful whenever we do an action.\nIn python, we show outputs by using the print function as follows:\n\tprint(what we want to see)\nAnother example of an output is when we search something in google.com, we expect to see some search results, these results are called outputs.\n"
	print(text)
	return text

def quizQuestion():
	print("What do you need to use to show an output?")
	print("a) print()")
	print("b) printing()")
	print("c) print it now()")
def outputQuiz():
	quizQuestion()
	count = 0 
	userInput = input("What is your answer? : ")
	if userInput.lower().strip() != "a":
		outputQuiz()
def runLec01():

	summaryOfSections01()
	sectionOutput()
	outputQuiz()
	print("***** LECTURE 01 COMPLETE *****")
	
runLec01()