# Stack can be implemented using different module 
#         1.list
#         2.Module
# Here we will learn about using list
# stack =====> LIFO
# Two basic operation push,pop
# we can use  1.push using -----> append method
#             2.pop using ------> pop method

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


while True:

    print("Enter the operation 1.push 2.pop 3.quit ")
    choice=int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct option!!!")




