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

def summed_matrix(matrix):
    
    Summed_Matrix =[]

    for row in matrix:
        #print (row)
        add = 0
        for int in row: 
            add += int
        Summed_Matrix.append(add)
    return (Summed_Matrix)        

if __name__ == "__main__":
    
    #X =    summed_matrix ([ [1, 2, 3], [3, 5, 7], [1, 7, 10] ])
    #X =    summed_matrix ([ [0, 1, 5], [-4, 7, 2], [-3, 12, 11] ])
    X = get_matrix()
    Y = summed_matrix(X) 
    print (Y)
