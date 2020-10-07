# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#

def avg(user_list):
    # Insert code here
    average = sum(user_list)/len(user_list)
    return average


if __name__ == '__main__':
    num_list=[]
    print("Input a number to be averaged. When finished inputing numbers, type 'done'")
    while True:
        tba = (input("Number: "))
        if tba.isnumeric():
            num_list.append(int(tba))
        elif tba == "done":
            break
        else:
            print("That's Inavlid. Try again.")
    print(avg(num_list))

       
    #need to gather the numbers here, I proabably want the person to input each number individually 
    #because if they dont, then i need to separate them by commas and thats complicated
    #can I start a new function/variable? by combining two of them? for instance, 
    #I could do sum/len and call that average, and i could assign that the variable avg 
    #and I would need to do something where x, y, and z are substituted each time they do it with the inputs
    # so I need to do the f string
    # test your fucntion with this print statement before writing the input loop
     # Put the values you want to test in for x,y and z

    # Now, comment out the print statement and work on the code below
    # Remember to indent in this section
    # start with an empty list
    # Write a loop to allow the user to input the values to be averaged
