trail_list = []
distance_list = []
height_list = []
i = 0
while(True):
    name = input("Enter the trail name:")
    trail_list.insert(i,name)
    distance = int(input("Enter the trail distance:"))
    distance_list.insert(i, distance)
    height =int(input("Enter the elevation of the trail:"))
    height_list.insert(i, height)
    condition = input("Enter END to quit...to continue press any other key")
    if condition =="END":
        break
print("The trail(s) you entered:")
print(','.join(trail_list))
total_distance = sum(distance_list)
total_height = sum(height_list)
print("The total distance of the trail is:", total_distance, "KM")
print("The total height of the trail is:", total_height, "KM")
    