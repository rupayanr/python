# To Find Smallest No. in List 
input_list = input("Enter list elements to be inserted: ")
print("\n")
print("Finding smallest element......")
input_list = input_list.split()
main_list = []

for val in input_list:
    val = int(val)
    main_list.append(val)
print(main_list)
smallest = main_list[0]
for val in main_list:
   
    if smallest > val:
    
        smallest = val
     

print("Smallest no. is: ",smallest)    

