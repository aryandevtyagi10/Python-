my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Slicing with only start, stop

slice1 = my_list[2:6]       

# Slicing with start, stop, and step

slice2 = my_list[1:8:2]   

# Slicing from the start to a specific position

slice3 = my_list[:5]     

# Slicing from a specific position to the end

slice4 = my_list[5:]   

     

# Slicing with a negative step to reverse the list

slice5 = my_list[::-1]        

print(“slice1:”, slice1)                # Output: [2, 3, 4, 5]

print(“slice2:”, slice2)

                                                 # Output: [1, 3, 5, 7]

print(“slice3:”, slice3)

                                                # Output: [0, 1, 2, 3, 4]

print(“slice4:”, slice4)

print(“slice5:”, slice5)

                                              # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]