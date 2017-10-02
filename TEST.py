warehouse={}
while(True):
    answer=str(input("Insert Command: "))
    if answer=="add":
        print("What To Add?")
        item=input("Insert Item: ")
        if item in warehouse:
            print("The item is in the list")
            number=int(input("How much will you add?: "))
            warehouse[item]= warehouse[item]+ number
        else:
            number=int(input("How much will you add?: "))
            warehouse[item]=number
        print(warehouse)
    if answer=="search":
        search =input("What Do You Want To Search?: ")
        for x,y in warehouse.items():
            if x == search:
                print(x,"=",y)
    if answer=="remove":
        print("What To Remove? ")
        item=input("Insert Item: ")
        while True:
            if item in warehouse:
                number=input("How Much Will You Remove?: ")
                if number == "all":
                    warehouse.pop(item)
                    break
                elif number.isdigit():
                    warehouse[item]= warehouse[item]-int(number)
                    if warehouse[item]<=0:
                        del warehouse[item]
                    break
                else :
                    print('Try Again!')
            if item not in warehouse:
                print("There is no item named: " +item)
                print("Try again!")
                break
        print(warehouse)
    if answer=="print":
        print(warehouse)
    if answer=="end":
        print("Thank You For Your Time")
        break
