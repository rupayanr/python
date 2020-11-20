# To Find Smallest No. in List 
input_list = input("Enter list elements to be inserted: ")
print("\n")
print("Finding smallest element......")

# Splitting input string using space as delimiter 
input_list = input_list.split()
main_list = []

# Typecasting and appending string numbers to main list 
for val in input_list:
    val = int(val)
    main_list.append(val)

# Initializing smallest variable with the first values of main list 
smallest = main_list[0]

# Comparing and changing values of smallest
for val in main_list:
    if smallest > val:    
        smallest = val
        
     
print("Smallest no. is: ",smallest)    

