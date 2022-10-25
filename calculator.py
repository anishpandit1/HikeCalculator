#Python program to display names of hiking trails entered by user and calculating total distance and height
trail_list = []
distance_list = []
height_list = []
i = 0
while(True):
    name = input("Enter the name of the hiking trail:\n")
    #Simple validation as user should not provide empty input
    if len(name)<1:
        print("Please enter a valid trail name\n")
        continue
    else:
        print("\n")
    trail_list.insert(i,name)
    #Handling Exception as user might give input other than floats.
    while(True):
        try:                                                                       
            distance = float(input("Please enter the trail distance(in Kilometers):\n"))
        except ValueError:
            print("Enter numbers only(decimal allowed)")
            continue
        else:
            distance_list.insert(i, distance)
            break
        break

    while(True):
        try:
            height = float(input("Enter the trail elevation(in kilometers):\n"))
        except ValueError:
            print("Please enter numbers only(decimal allowed)")
            continue
        else:
            height_list.insert(i,height)
            break
        break
    print("\n")
    #Checking condition, if user enters END, the list should not continue
    condition = input("Enter END to quit...to continue press any other key\n")
    if condition =="END":
        break
#Printing out the user entered details:
print("The trail(s) you entered:")
print(','.join(trail_list)) #Using join to remove formatting from list 
total_distance = sum(distance_list) #total sum of trail distance
total_height = sum(height_list) #total sum of trail elevation
print("\nThe total distance of the trail:", total_distance, "KM")
print("The total height of the trail:", total_height, "KM")
    