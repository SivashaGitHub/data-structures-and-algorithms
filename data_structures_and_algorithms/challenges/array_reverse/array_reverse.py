def reverseArray(Entered_list):

    new_array =[]
    #while loop will insert the list values in re the list/array value in revers order    
    while len(Entered_list):
       new_array.append(Entered_list.pop())

    return new_array           
        
                
if __name__ == "__main__":
        
    # creating an empty list 
    lst = [] 
    
    # number of list/array value as input 
    n = int(input("Enter number of elements : ")) 
    
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input()) 
        lst.append(ele) # adding the element 
    
    Entered_list = lst
    print ('\n')  
    
    #call the reverse function
    print ("Entered List :",Entered_list)
    new_array = reverseArray(lst)
    print ("Reversed List :", new_array)


