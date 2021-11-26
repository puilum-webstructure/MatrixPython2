 

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
    for i in range(len(lst1)):
        value = lst1[i] + lst2[i] 
        result.append(value)

    return result


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
    start = timer()
    print("Output for 1D addition" + str(addition_1D(lst1, lst2)))
    end = timer()
    print(end-start)

    lst1 = [[1,2],[3,4]]
    lst2 = [[0,1],[4,5]]
    print("Output for 2D addition" + str(addition_2D(lst1, lst2)))

    lst1 = [[1,2],[3,4]] #2x2 
    lst2 = [[0,1],[4,5]]
    print("Output for 2D multiplication" + str(multiplication_2D(lst1, lst2)))


# implementing multithreading version
import threading 
#import concurrent.futures 
from timeit import default_timer as timer 

# addition 1d
def threading_addition_1D(n):  
    res[n] = matrix1[n] + matrix2[n]

#matrix1 = [3,4,5]
#matrix2 = [7,7,3] 
#start = timer()
#with concurrent.futures.ThreadPoolExecutor() as executor: 
#    for i in range(len(matrix1)):
#        f1 = executor.submit(threading_addition_1D, i)
    
#    print(res)

#end = timer()
#print(end-start)

def threading_addition_2D(i, j): 
    '''
    function for 2x2 matrix additionn using Threading 
    '''
    res[i][j] = matrix1[i][j] + matrix2[i][j]


def threading_multiplication_2D(i,j,k): 
    '''
    function for 2x2 matrix multiplication using Threading 
    '''
    res[i][j] += matrix1[i][k] * matrix2[k][j]
   

if __name__ == "__main__":
    # creating threads
    # threads for addition 1D matrix 
    matrix1 = [3,4,5]
    matrix2 = [7,7,3] 
    res = [0 for x in range(len(matrix1))]
    
    start = timer()
    threads = []
    for i in range(len(matrix1)): 
        x = threading.Thread(target=threading_addition_1D, args = (i,))
        x.start()
        threads.append(x) 

    for thread in threads: 
        thread.join()
    print("Output for 1D addition using threading" + str(res))
    end = timer() 
    print(end-start)

    # threads for addition 2D matrix 
    matrix1 = [[1,2],[3,4]]
    matrix2 = [[0,1],[4,5]]  
    res = [[0 for x in range(2)] for y in range(2)] 

    for i in range(2): 
        for j in range(2): 
            x = threading.Thread(target=threading_addition_2D, args = (i,j,))
            x.start()
            x.join()
    print("Output for 2D addition using threading" + str(res))


    # threads for multiplication 2D matrix 
    matrix1 = [[1,2],[3,4]]
    matrix2 = [[0,1],[4,5]]  
    res = [[0 for x in range(2)] for y in range(2)] 

    for i in range(2): 
            for j in range(2): 
                for k in range(2): 
                    x = threading.Thread(target=threading_multiplication_2D, args = (i,j,k, ))
                    x.start()
                    x.join()
    print("Output for 2D multiplication using threading" + str(res))


# https://medium.com/python-experiments/parallelising-in-python-mutithreading-and-mutiprocessing-with-practical-templates-c81d593c1c49
