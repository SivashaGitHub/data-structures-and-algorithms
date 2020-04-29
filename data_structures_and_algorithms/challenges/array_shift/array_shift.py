def insertShiftArray(in_lst,in_num): 
    
    #create new empty list
    new_list = []
    
    count = 0
    #call while loop to insert the array value to new array 
    # also check and insert the input nuber where its fits in 
    while count <  len(in_lst):
        
        if in_lst[count-1] <= in_num and in_lst[count] > in_num: 
            new_list.append(in_num)
            new_list.append(in_lst[count])
        else:     
            new_list.append(in_lst[count])
        count +=1
    
    return new_list
                
if __name__ == "__main__":
        
    # creating array and assing values 
    
    # input list
    #lst = [4,8,15,23,42] #, 16
    lst = [2,4,6,8] #, 5
    
    # number of list/array value as input 
    n = int(input(f"Enter number between  {lst[0]} and {lst[len(lst)-1]} :")) 

    new_list = insertShiftArray(lst,n)
    print ("Here is the new list with inserted value", new_list)         
   
    


