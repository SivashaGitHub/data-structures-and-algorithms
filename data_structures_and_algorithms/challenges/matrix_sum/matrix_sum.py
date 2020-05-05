def get_matrix():
    R= int(input("Enter the number of rows:"))
    C= int(input("Enter the number of columns :"))
    
    print("Enter the matrix values rowwise:")
    matrix = []
    for r in range(R):
        row = []
        for c in range(C):
            row.append(int(input())) 
        matrix.append(row)        

    return matrix

#using for loop
def sum_matrix_fn(matrix):
    
    Summed_Matrix =[]

    for row in matrix:
        #print (row)
        add = 0
        for int in row: 
            add += int
        Summed_Matrix.append(add)
    return (Summed_Matrix)        

#using sum function
def sum_matrix_using_sum_fn(matrix):
   
    Summed_Matrix =[]
    Summed_Matrix = [sum(row) for row in matrix]
    return (Summed_Matrix)        



if __name__ == "__main__":
    
    #X = get_matrix()
    X =    sum_matrix_fn ([ [1, 2, 3], [3, 5, 7], [1, 7, 10] ])
    #X =    sum_matrix_fn ([ [0, 1, 5], [-4, 7, 2], [-3, 12, 11] ])
    #X =    sum_matrix_using_sum_fn ([ [1, 2, 3], [3, 5, 7], [1, 7, 10] ])
    #X =    sum_matrix_using_sum_fn ([ [0, 1, 5], [-4, 7, 2], [-3, 12, 11] ])
    #Y = sum_matrix_fn(X) 
    #Y = sum_matrix_using_sum_fn(X) 
    print (X)
