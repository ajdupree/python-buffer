import re

#Welcome to circular buffer simulator!


buffer = [None for x in range (0,5)]
SIZE = 5 
index = 0 
popIndex = 0 
num = 1

def next():
    if index < SIZE-1: return index+1
    else: return 0

def push():
    global index
    global popIndex
    global num
    buffer[index] = num
    num+=1

    #### index management ###
    #check if pop pointer needs to increment
    #condition: indices the same; buffer not empty
    if index==popIndex and buffer[next()] != None:
        popIndex+=1
    #increment index after a push
    index+=1
    #reset indices if necessary
    if index == SIZE:
        index = 0
    if popIndex == SIZE:
        popIndex = 0;
    
    state()
    return 

def pop():
    global popIndex

    if buffer[popIndex] == None:
        print "Buffer empty"
        return
    else:
        print buffer[popIndex]
        buffer[popIndex] = None
        popIndex+=1
        if popIndex == SIZE:
            popIndex=0;
        state()

def state():
    print buffer
    print "push index: " + str(index)
    print "pop index: " + str(popIndex)

while (1):

    input = raw_input("Enter 'push', 'pop', or 'exit'\n") 
    check = re.match("push|pop|exit",input)
    if check is None: 
        print "Please enter a valid input\n"
        continue;
    else:
        if input == "push":
            push()
        elif input == "pop":
            pop()
        else:
            break

