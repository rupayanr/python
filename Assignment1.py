# Problem Statement : Given two lists merge them in such a way that first and last values of corresponding lists are concatenated only if they are not None

def merge_list(list1, list2):
    merged_data = ""
    list2 = list2[::-1]

    for i in range(0,len(list2)):

        if list1[i] == None:
            list1[i] = list2[i]

        elif list2[i] == None:
            list1[i] = list1[i]

        else:
            list1[i] = list1[i] + list2[i]
     
    merged_data = " ".join(list1)   

    return merged_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)