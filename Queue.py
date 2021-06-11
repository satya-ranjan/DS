# It is a linear data structure
# it follows FIFO methodology(first in first out)
# the element inserted first will leave first
# for    enqueue---->append function
#        dequeue----->pop function:list.pop(0)

queue=[]
def enqueue():

    element =input("Enter the element to add in queue : ")
    queue.append(element)
    print(queue)


def dequeue():

    if not queue:
        print("Queue is empty!!!")
    else:
        e = queue.pop(0)
        print("Removed element is", e )
        print(queue)


def display():

    print(queue)



n=int(input("enter the number of element you want to add \n"))
while True:
    choice = int(input("Select the operation 1.Add 2.Remove 3.Show 4.quite \n"))
    if choice==1:
        if len(queue)==n:
            print("Queue is full !!!")
        else:
            enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        print(queue)
        break
        
    else:
        print("You have Enter the wrong option")








