def BinarySearch(arr,svalue):
    """ find teh sidx value of serach key proivded on the array 
    
    Arguments 
        arr {list of sorted values}
        svalue {search value to look up on the array}
    Returns:
        sidx = Given svalue value exist sidx number if exist else -1  
    """
    lst = list(arr)
    
    sidx = -1 #search index
    min_idx = 0
    Cur_idx = len(lst)  // 2
    max_idx = len(lst) 

    # run the while loop as long as sidx = -1 
    # or untill reaching the indiex near to our serarch value
    
    while sidx == -1:
          
        if int(svalue) == int(lst[Cur_idx]):
            sidx =Cur_idx
            return sidx
            break

        if min_idx == Cur_idx:
           return -1
           break
        
        if int(svalue) < int(lst[Cur_idx]): 
            max_idx = Cur_idx
            Cur_idx = (min_idx + max_idx) // 2
        else:
            min_idx = Cur_idx
            Cur_idx = (min_idx+ max_idx) // 2

if __name__ == "__main__":
 
    #Get the array value as input
    Array = list(int(num) for num in input("Enter the array numbers separated by space: ").strip().split())

    #Get the serach key value as input
    searchkey = input("Enter search key value: ")

    #call Binary Search function
    x = BinarySearch (Array,searchkey)
    print(x)
    

    """ x = BinarySearch ([11,22,33,44,55,66,77], 90)
    print(x)
    
    x = BinarySearch ([4,8,15,16,23,42], 15)
    print(x) """








