#dictionary to store trail with its respective distance
class hike_list(dict):
    def __init__(self):
        self = (dict)
    def add(self, trail, distance, height):
        self[trail] = distance
        self[trail] = height
dict_obj= hike_list()
while(True):
    
    trail =input("Enter the trail you would like to take:")
    print(len(trail))
    if len(trail)<1:
        print("Please enter a valid trail")
        continue
    else:
        print("\n")
    print("Enter the distance of the trail:")
    distance = int(input())
    print("Enter the elevation of the trail:")
    height = int(input())
    dict_obj.add(trail, distance, height)
    print("Do you want to stop?, if yes enter 'END'")
    condition = input()
    if condition == "END":
        """print("The trail(s) you chose:",trail, "and the overall distance will be :",distance)
        """
        print("The trail(s) you chose:")
        break
print("\n".join("{}\t{}".format(k, v) for k, v in dict_obj.items()))
print(", ".join(dict_obj))
total_distance = sum(dict_obj.values())
total_height = sum(dict_obj.values())
print("The total distance of the trail is:", total_distance ,"km")
print("The total height of the trail is:", total_distance ,"km")
    