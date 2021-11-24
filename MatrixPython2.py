import multiprocessing 

# 1D array matrix addition 
def addition_1D(lst1, lst2): 
    # check if both matrix are of the same length
    if len(lst1) != len(lst2): 
        raise exception("lenght of both matrix needs to be the same.")

    # check if it's a one dimension integer only array 
    for i in range(len(lst1)): 
        x = isinstance(lst1[i], int)
        if not x:
            raise exception("matrix 1 should be of type integer and is one dimensional only")
   
    for i in range(len(lst2)): 
        x = isinstance(lst2[i], int)
        if not x:
            raise exception("matrix 2 should be of type integer and is one dimensional only")
   
    result = []
    #value = lst1 + lst2
    #result.append(value)
    for i in range(len(lst1)):
        value = lst1[i] + lst2[i] 
        result.append(value)

    # print(result)  #[10,11,8]
    return result

#if __name__ == "__main__": 
#    lst1 = [3,4,5]
#    lst2 = [7,7,3] 
#    print(addition_1d(lst1, lst2))

#    processes = []
#    for i in range(3): 
#          p = multiprocessing.process(target = addition_1d(lst1[i], lst2[i]))
#          p.start()
#          processes.append(p)

#    for process in processes: 
#        process.join()



#2d array matrix addition
def addition_2D(lst1, lst2): 
    # check if both matrix are of the same length
     if len(lst1) != len(lst2): 
        raise Exception("Lenght of both matrix needs to be the same.")

     #check if it's a two dimension array 
     if len(lst1) != 2: 
         raise Exception("Matrix 1 should be two dimensional")

     if len(lst2) != 2: 
         raise Exception("Matrix 2 should be two dimensional")

     # check if number of elements in the matrix is equal respectively 
     if len(lst1[0]) != len(lst1[1]): 
         raise Exception("Number of elements in each sub matrix should be equal")
     if len(lst2[0]) != len(lst2[1]): 
         raise Exception("Number of elements in each sub matrix should be equal")
     
     # check if number of elements in matrix 1 equals to matrix 2 
     if len(lst1[0]) != len(lst2[0]): 
         raise Exception("Number of elements in both sub matrix should be equal")


     #check if all values are in type integer 
     for i in range(2):
         for j in range(len(lst1[0])): 
             if type(lst1[i][j]) != int: 
                 raise Exception("Matrix 1 should only include integers only")
     for i in range(2):
         for j in range(len(lst2[0])): 
             if type(lst2[i][j]) != int: 
                 raise Exception("Matrix 2 should only include integers only")

    # the algo: 
     output = [[0,0],[0,0]] #[[1,3],[7,9]]
     for i in range(2): 
        for j in range(len(lst1[0])): 
            output[i][j] = lst1[i][j] + lst2[i][j] 

     return output  
   

# 2d array matrix multiplication 
def multiplication_2D(lst1, lst2): 
     # check if both matrix are of the same length
     if len(lst1) != len(lst2): 
        raise Exception("Lenght of both matrix needs to be the same.")

     #check if it's a two dimension array 
     if len(lst1) != 2: 
         raise Exception("Matrix 1 should be two dimensional")

     if len(lst2) != 2: 
         raise Exception("Matrix 2 should be two dimensional")

     # check if number of elements in the matrix is equal respectively 
     if len(lst1[0]) != len(lst1[1]): 
         raise Exception("Number of elements in each sub matrix should be equal")
     if len(lst2[0]) != len(lst2[1]): 
         raise Exception("Number of elements in each sub matrix should be equal")
     
     # check if number of elements in matrix 1 equals to matrix 2 
     if len(lst1[0]) != len(lst2[0]): 
         raise Exception("Number of elements in both sub matrix should be equal")


     #check if all values are in type integer 
     for i in range(2):
         for j in range(len(lst1[0])): 
             if type(lst1[i][j]) != int: 
                 raise Exception("Matrix 1 should only include integers only")
     for i in range(2):
         for j in range(len(lst2[0])): 
             if type(lst2[i][j]) != int: 
                 raise Exception("Matrix 2 should only include integers only")
  
     final_output = [[0 for x in range(2)] for y in range(2)] 
    # explicit for loops
     for i in range(len(lst1)): 
        for j in range(len(lst2[0])): 
            for k in range(len(lst2)): 
  
                # resulted matrix
                final_output[i][j] += lst1[i][k] * lst2[k][j]
     return final_output


if __name__ == "__main__": 
    lst1 = [3,4,5]
    lst2 = [7,7,3] 
    print("Output for 1D addition" + str(addition_1D(lst1, lst2)))

    lst1 = [[1,2],[3,4]]
    lst2 = [[0,1],[4,5]]
    print("Output for 2D addition" + str(addition_2D(lst1, lst2)))

    lst1 = [[1,2],[3,4]] #2x2 
    lst2 = [[0,1],[4,5]]
    print("Output for 2D multiplication" + str(multiplication_2D(lst1, lst2)))

    