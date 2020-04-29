def insert_shift_array(arr,val):
    """ insert given value into array mid point
    
    Arguments 
        arr {sequence}
        val {[any]}
    Returns:
        [list] = [new value inserted into middle] 
    """

    lst = list(arr)
    mid = (len(lst) + 1 )  // 2
    return lst[:mid] + [val] + lst[mid:]
     
x = insert_shift_array([1,2,3,5,6,7],4)
print (x)
