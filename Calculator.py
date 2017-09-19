def push(stack,value):
    stack.append(value)
def checkstack(stack):
    if(len(stack)<2):
        return "input more than two numbers"
def add(stack):
    num_1=stack.pop()
    num_2=stack.pop()
    answer=num_2+num_1
    push(stack,answer)
    return answer
def mult(stack):
    num_1=stack.pop()
    num_2=stack.pop()
    answer=num_2*num_1
    push(stack,answer)
    return answer
def sub(stack):
    num_1=stack.pop()
    num_2=stack.pop()
    answer=num_2-num_1
    push(stack,answer)
    return answer
def divide(stack):
    num_1=stack.pop()
    num_2=stack.pop()
    answer=num_2/num_1
    push(stack,answer)
    return answer
stack=[]


while(True):
    answer=input("")
    if (answer=="+"):
        print(add(stack))
    elif(answer=="*"):
        print(mult(stack))
    elif(answer=="-"):
        print(sub(stack))
    elif(answer=="/"):
        print(divide(stack))
    else:
        push(stack,int(answer))

