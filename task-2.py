def add(num_1,num_2):
    return num_1+num_2

def subtract(num_1,num_2):
    return num_1-num_2

def multiply(num_1,num_2):
    return num_1*num_2

def divide(num_1,num_2):
    if num_1!=0:
        return num_1/num_2 
    else:
        print("INFINITY")

def calculator():
    while True:
        num_1=int(input("\n ENTER FIRST NUMBER or exit for quit: "))
        if num_1=="exit":
            print("CALCULATOR STOPPED: ")
            break

        num_2=int(input("ENTER SECOND NUMBER: "))

        choice=input(" ENTER ANY OF THESE +,-,*,/: ")

        if choice=="+":
            print("THE ANSWER IS: ",add(num_1,num_2))
        elif choice=="-":
            print("THE ANSWER IS: ",subtract(num_1,num_2))
        elif choice=="*":
            print("THE ANSWER IS: ",multiply(num_1,num_2))
        elif choice=="/":
            print("THE ANSWER IS: ",divide(num_1,num_2))
        else:
            print("INPUT IS INCORRECT")
calculator()