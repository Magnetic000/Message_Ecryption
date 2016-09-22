"             ____________________________________________________                  "
"            /                                                    \                 "
"           |    _____________________________________________     |                "
"           |   |#Andrew Xu                                   |    |                "
"           |   |#Semester 2                                  |    |                "
"           |   |#Coverter a message into an encrypted message|    |                "
"           |   |#which can then be decoded with the same     |    |                "
"           |   |#program                                     |    |                "
"           |   |                                             |    |                "
"           |   |#Each symbol (letter, number, punctuation)   |    |                "
"           |   |#has a corresponding number value assigned to|    |                "
"           |   |#it                                          |    |                "
"           |   |#Each symbol (letter, number, punctuation)   |    |                "
"           |   |#has a corresponding number value assigned to|    |                "
"           |   |#it                                          |    |                "
"           |   |#When the encryption process runs, addition, |    |                "
"           |   |#subtraction and multiplication is applied to|    |                "
"           |   |##these number values (division was taken out|    |                "
"           |   |#to eliminate decimals)                      |    |                "
"           |   |##The output are the symbols replaced with   |    |                "
"           |   |#their number values along with a 12 number  |    |                "
"           |   |#key at the start of the message             |    |                "
"           |   |#An ascii code                               |    |                "
"           |   |#Comments in all capitals are general        |    |                "
"           |   |#categories while lowercase comments are     |    |                "
"           |   |#messages                                    |    |                "
"           |   |_____________________________________________|    |                "
"           |                                                      |                "
"            \_____________________________________________________/                "
"                   \_______________________________________/                       "
"                _______________________________________________                    "
"             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_                 "
"          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_              "
"       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_           "
"    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_        "
" _-'.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.`-_     "
":-----------------------------------------------------------------------------:    "
"`---._.-----------------------------------------------------------------._.---'    "

#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>
#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>


#DECLARING ALL NORMAL SYMBOLS
#Assign variables to all lowercase letters of the alphabet (array values 0-25)
lowerLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#Assign variables to all uppercase letters of the alphabet (array values 0-25)
upperLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#Assign variables to all numbers (array values 0-9)
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#Assign variables to all punctuation (array values 0-12)
#The corresponding punctuation goes as follows
#0 = ' 1 = : 2 = , 3 = - 4 = ... 5 = ! 6 = _ 7 = ( 8 = ) 9 = . 10 = ? 11 = ; 12 = "
punctuation = ["'", ":", ",", "-", "...", "!", "_", "(", ")", ".", "?", ";", '"']

#Predeclare variables used in functions to make them accessible by all functions
operation1 = ""
operation2 = ""
operation3 = ""
operation4 = ""
change1 = ""
change2 = ""
change3 = ""
change4 = ""

#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>
#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>


#DECLARING BASIC FUNCTIONS/OPERATIONS

#Determine operation performed on coded values of symbols
#Check to see what operations to perform on coded values of symbol

def operationChecker():
        #Operation number 1
        #Make the amount value assescible outside of function
        global amount
        if operation1 == 0:
                amount = change1
                addOperation()
        elif operation1 == 1:
                amount = change1
                subtractOperation()
        elif operation1 == 2:
                amount = change1
                multiplyOperation()
        #Operation number 2
        if operation2 == 0:
                amount = change2
                addOperation()
        elif operation2 == 1:
                amount = change2
                subtractOperation()
        elif operation2 == 2:
                amount = change2
                multiplyOperation()
        #Operation number 3
        if operation3 == 0:
                amount = change3
                addOperation()
        elif operation3 == 1:
                amount = change3
                subtractOperation()
        elif operation3 == 2:
                amount = change3
                multiplyOperation()
        #Operation number 4
        if operation4 == 0:
                amount = change4
                addOperation()
        elif operation4 == 1:
                amount = change4
                subtractOperation()
        elif operation4 == 2:
                amount = change4
                multiplyOperation()

#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>

#Performing addition to number code values
def addOperation():
        #Loop through all values
        for x in range (0,26):
                codeLowerLetters[x] = int(codeLowerLetters[x]) + amount
                codeUpperLetters[x] = int(codeUpperLetters[x]) + amount
        for x in range (0,12):
                codePunctuation[x] = int(codePunctuation[x]) + amount

#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>

#Performing subtraction to number code values
def subtractOperation():
        #Loop through all values
        for x in range (0,26):
                codeLowerLetters[x] = int(codeLowerLetters[x]) - amount
                codeUpperLetters[x] = int(codeUpperLetters[x]) - amount
        for x in range (0,12):
                codePunctuation[x] = int(codePunctuation[x]) - amount

#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>

#Performing multiplication to number code values
def multiplyOperation():
        #Loop through all values
        for x in range (0,26):
                codeLowerLetters[x] = int(codeLowerLetters[x]) * amount
                codeUpperLetters[x] = int(codeUpperLetters[x]) * amount
        for x in range (0,12):
                codePunctuation[x] = int(codePunctuation[x]) * amount

#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>

#Assign code number values to create coded messages
#Assigned as a function as values need to be refreshed after each coded message or decoded message
def codeVariables():
        #Make variables available and accessible by all functions in the program
        global codeLowerLetters
        global codeUpperLetters
        global codePunctuation

        #Assign variables to all code values
    	#Assignment goes as follows a=10, b=11......z=35
        codeLowerLetters = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    	#Assignment goes as follows A=36, B=37......Z=61
        codeUpperLetters = [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]

    	#Assignment goes as follows '=72, :=73......"=
        codePunctuation = [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]

        #Declare variables for user inputed message
        userMessage = ""

#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>
#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>


#MAIN CODING AND DECODING FUNCTIONS

#The converter
def converter():
        #Refresh all code values to their original values
        codeVariables()
        #Randomize generator so that values are different each time
        import random
        #Generate the random numbers scrambling the code
        operation1 = random.randint(0,2)
        operation2 = random.randint(0,2)
        operation3 = random.randint(0,2)
        operation4 = random.randint(0,2)
        change1 = random.randint(10,20)
        change2 = random.randint(10,20)
        change3 = random.randint(10,20)
        change4 = random.randint(10,20)
        #Create the encryption key and save it as a key for future output
        codeInstructions = str(operation1) + str(change1) + str(operation2) + str(change2) + str(operation3) + str(change3) + str(operation4) + str(change4)
        #Read the key and perform the corresponding operations to the code values
        operationChecker()
        #Ask the user for the message they want to code
        userMessage = input("===========================Please input your message========================== \n")
        #Replace all values in the code with their corresponding code values
        for x in range (0,10):
                userMessage = userMessage.replace(numbers[x],chr(13) + str(numbers[x]) + chr(13))
        for x in range (0,26):
                userMessage = userMessage.replace(lowerLetters[x],chr(13) + str(codeLowerLetters[x]) + chr(13))
                userMessage = userMessage.replace(upperLetters[x],chr(13) + str(codeUpperLetters[x]) + chr(13))
        for x in range (0,12):
                userMessage = userMessage.replace(punctuation[x],
chr(13) + str(codePunctuation[x]) + chr(13))
        #Combine the encrpytion key and the message into a single string
        userMessage = str(codeInstructions + userMessage)
        #Output the coded message
        print("Please copy everything on the next line(s) \n" + userMessage)

#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>

#The deconverter
def deconverter():
        #Ask user for their coded message first to be able to obtain encryption key
        userMessage = input("=======================Please input your coded message======================== \n")
        #Refresh all code values in case multiple messages have gone through the program
        codeVariables()
        #Conver the user message into a readable format for the program
        userMessage = str(userMessage)
        #Read the encryption key at the start of the inputted message
        operation1 = userMessage[0]
        change1 = userMessage[1:3]
        operation2 = userMessage[3]
        change2 = userMessage[4:6]
        operation3 = userMessage[6]
        change3 = userMessage[7:9]
        operation4 = userMessage[9]
        change4 = userMessage[10:12]
        #Delete the encrpytion key from the start of the message
        userMessage = userMessage[12:len(userMessage)]
        #Perform operations on the code values in preparation for decoding
        operationChecker()
        #Replace code values with their corresponding numerical/alphabetical/punctuation smybols
        for x in range (0,10):
                userMessage = userMessage.replace(chr(13) + str(numbers[x]) + chr(13), numbers[x])
        for x in range (0,26):
                userMessage = userMessage.replace(chr(13) + str(codeLowerLetters[x]) + chr(13), lowerLetters[x])
                userMessage = userMessage.replace(chr(13) + str(codeUpperLetters[x]) + chr(13), upperLetters[x])
        for x in range (0,12):
                userMessage = userMessage.replace(chr(13) + str(codePunctuation[x]) + chr(13), punctuation[x])
        #Print the decoded message
        print("Your message is: " + userMessage)


#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>
#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>


#RUNNING PROGRAM CODE STARTS HERE
#This is the actual running of the program
#Basic prompt to begin the loop
print("===================Welcome to Andrew's Message Encryptor!!!===================\n\n")
choiceOfAction = input("====================Please type 1 for code or 2 for decode====================\n")
#Check to see whether user wants to code or decode
if choiceOfAction == "1":
        converter()
elif choiceOfAction == "2":
        deconverter()
else:print("***You did not input a value!***")

#Continuously loop the program after the converter/deconverter finishes running
while choiceOfAction != "1" or "2":
    choiceOfAction = input("====================Please type 1 for code or 2 for decode====================\n")
    if choiceOfAction == "1":
        converter()
    elif choiceOfAction == "2":
        deconverter()
    else:print("***You did not input a value!***")


#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>
#¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>
