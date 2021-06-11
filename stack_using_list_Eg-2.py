# Here we will set a limit for the list

stack=[]
def push():

    element = input("Enter the element : ")
    stack.append(element)
    print(stack)


def pop_element():

    if not stack:
        print("The stack is empty")
    else:
        e = stack.pop()
        print("Remove element is : ,e ")
        print(stack)

n = int(input("Enter the limit for the list : "))
while True:

    print("Enter the operation 1.push 2.pop 3.quit ")
    choice=int(input())
    if choice == 1:
        if len(stack)==n:
            print("stack is full")
        else:
            push()
            print(stack)
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct option!!!")
