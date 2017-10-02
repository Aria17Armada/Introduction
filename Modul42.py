#input 10 numbers,calculate distinct answers from input modulo by 42
stack=[]
def numbers():
    for i in range(10):
        a = input()
        stack.append(int(a)%42)
        if len(stack)==10:
            print(len(set(stack)))
numbers()
