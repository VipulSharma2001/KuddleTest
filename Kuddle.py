from random import randrange                  # For using randrange function to get any random number in a range
class Yoga():                                 # Yoga Class. Same naming pattern is followed for all classes
    def __init__(self):
        self.list = []                        # List of members
        self.current = 0                      # Number of currently enrolled students
        self.capacity = 50                    # Maximum possible strength of class
        self.start_time = 50                  # Start time of the class. Here just integers are using to demonstrate time.
    
class Gym():                                 # Gym Class
    def __init__(self):
        self.list = []
        self.current = 0
        self.capacity = 60
        self.start_time = 65

class Dance():                               # Dance Class
    def __init__(self):
        self.list = []
        self.current = 0
        self.capacity = 70
        self.start_time = 70

# Waiting list to store the list of students who are in line to get in class if anyone cancels
waiting_listY = []        
waiting_listG = []
waiting_listD = []

# Objects of each classes
y = Yoga()
g = Gym()
d = Dance()

# Just a variable to ask user if he wants to add more data or remove any data
st = 1

while st==1:

    print("Enter your name")
    name = input()
    print("Enter your interest which you want to register for :")
    interest = input()
    
    # Y or y represents Yoga, G or g represents Gym and D or d represents Dance in interest variable
    if interest=="Y" or interest == "y":
        # If condition to check if capacity of class is full
        if y.current == y.capacity:
            waiting_listY.append(name)
            print("Name added in wait list because no more capacity is available")
        else:
            y.current += 1
            y.list.append(name)
            print("Booking successfully completed")

    elif interest=="G" or interest == "g":
        # If condition to check if capacity of class is full
        if g.current == g.capacity:
            waiting_listG.append(name)
        else:
            g.current += 1
            g.list.append(name)
            print("Booking successfully completed")

    elif interest=="D" or interest=="d":
        # If condition to check if capacity of class is full
        if d.current == d.capacity:
            waiting_listD.append(name)
        else:
            d.current += 1
            d.list.append(name)
            print("Booking successfully completed")
    else:
        print("Wrong input")

    print("Do you want to continue Press 1 if Yes, Press 0 if No, Press 2 if you want to remove?")

    st = int(input())

    # st = 2 represents user wants to remove data
    if st==2:
        st = 1
        print("Enter your name to remove")
        name = input()
        print("Enter interest where you want your name to be removed from")
        interest = input()

        # Exception handling in case user enters a name which doesn't exist
        try:
            time = randrange(80)    # Time is represent as integers. Random integer from 0 to 150.
            print("Time is ", time)

            if interest=="Y" or interest =="y" :
                if y.start_time - 30 < time:
                    y.list.remove(name)
                    y.current -= 1
                    print("Member removed. If anyone is in waiting list, then they got enrolled")
                    # Checking if waiting list for this particular class has anyone waiting
                    if len(waiting_listY)!=0:
                        x = waiting_listY.pop(0)
                        y.list.append(x)
                        y.current += 1
                else:
                    print("Time exceeded to remove the name. Less than 30 minutes left.")

            if interest=="G" or interest =="g":
                if g.start_time - 30 < time:
                    g.list.remove(name)
                    g.current -= 1
                    print("Member removed. If anyone is in waiting list, then they got enrolled")
                    # Checking if waiting list for this particular class has anyone waiting
                    if len(waiting_listG)!=0:
                        x = waiting_listG.pop(0)
                        g.list.append(x)
                        g.current += 1
                else:
                    print("Time exceeded to remove the name. Less than 30 minutes left.")

            if interest=="D" or interest=="d":
                # If start time is 30 mins before the time user tried to remove his name, then remove the name else print time exceeded.
                if d.start_time - 30 < time:
                    d.list.remove(name)
                    d.current -= 1
                    print("Member removed. If anyone is in waiting list, then they got enrolled")
                    # Checking if waiting list for this particular class has anyone waiting
                    if len(waiting_listD)!=0:
                        x = waiting_listD.pop(0)
                        d.list.append(x)
                        d.current += 1
                else:
                    print("Time exceeded to remove the name. Less than 30 minutes left.")

        except:
            print("The name to remove doesn't exist")
    

# Printing all the present members in each of the classes
print("Yoga students are ",y.list)
print("Gym students are ",g.list)
print("Dance students are ",d.list)




