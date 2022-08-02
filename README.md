# KuddleTest

**About the program:**

The program contains 3 classes namely Yoga(), Gym() and Dance(). y, g and d are the class objects respectively.
They each have a list variable which contains name of all the students under the class object, current variable which shows the count of members enrolled, capacity variable which shows maximum capacity of each class object and start_time variable which shows the start time of classes.
The user is allowed to add more members to any class as long as the current variable is low than or equal to capacity.
The user is also allowed to remove names from class if the difference between start time and time of removal is 30 minutes.


**Assumptions:**

Here, we have considered time to be in integers and not the regular HH:MM:SS format.


**Instructions to run the program:**

1) You can enter any name for users. But if a user name is entered for removal and it doesn't exist then the exception handling code will kick in.
2) For interest enter Y or y for Yoga class, G or g for Gym class and D or d for Dance class.
3) If start_time and time has less than 30 minutes difference then no changes or removal of names will take place.
4) The program considers all possible edge cases and gives appropriate output at each stage.
5) For any details on variable or code, comments are added wherever necessary in the code itself.


**Input:**

1)A string - Name of the member
2)A string (Y,y,G,g,D,d) - The class first character to identify which class the name is getting enrolled in.
3)An Integer - 1 to continue adding more members to any class, 0 to exit the program and 2 if you want to remove data about an member.

4) If 2 is entered:
	A string - Name of the member whose name is to be removed
	A string (Y,y,G,g,D,d) - The class first character to identify which class the name should be removed from.

5) If 1 is entered then repeat from step 1.


**Output:**

list variable from every class is getting printed to show the enrolled members in each class object.
If a user name is getting removed then current time variable is also getting printed.


**Sample Test Case 1:**

Enter your name

-Vipul

Enter your interest which you want to register for :

-Y

Booking successfully completed

Do you want to continue Press 1 if Yes, Press 0 if No, Press 2 if you want to remove?

-2

Enter your name to remove

-Vipul

Enter interest where you want your name to be removed from

-Y

Time is  45

Do you want to continue Press 1 if Yes, Press 0 if No, Press 2 if you want to remove?

-0

Yoga students are ['Vipul]

Gym students are []

Dance students are []


**Sample Test Case 2:**

Enter your name

-Deepali

Enter your interest which you want to register for :

-D

Booking successfully completed

Do you want to continue Press 1 if Yes, Press 0 if No, Press 2 if you want to remove?

-1

Enter your name

-Shruti

Enter your interest which you want to register for :

-D

Booking successfully completed

Do you want to continue Press 1 if Yes, Press 0 if No, Press 2 if you want to remove?

-2

Enter your name to remove

-Shruti

Enter interest where you want your name to be removed from

-D

Booking successfully completed

Time is  138

Member removed. If anyone is in waiting list, then they got enrolled

Do you want to continue Press 1 if Yes, Press 0 if No, Press 2 if you want to remove?

-0

Yoga students are  []

Gym students are  []

Dance students are  ['Deepali']



