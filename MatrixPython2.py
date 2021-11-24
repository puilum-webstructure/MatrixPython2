import multiprocessing 

# 1D array matrix addition 
def addition_1D(lst1, lst2): 
    # check if both matrix are of the same length
    if len(lst1) != len(lst2): 
        raise Exception("Lenght of both matrix needs to be the same.")

    # check if it's a one dimension integer only array 
    for i in range(len(lst1)): 
        x = isinstance(lst1[i], int)
        if not x:
            raise Exception("Matrix 1 should be of type integer and is one dimensional only")
   
    for i in range(len(lst1)): 
        x = isinstance(lst1[i], int)
        if not x:
            raise Exception("Matrix 2 should be of type integer and is one dimensional only")
   
    result = []
    for i in range(len(lst1)):
        result.append(lst1[i] + lst2[i])

    return result 

if __name__ == "__main__": 
    lst1 = [3,4,5]
    lst2 = [7,7,3] 
    print(addition_1D(lst1, lst2))

#processes = []
#for _ in range(len(lst1)): 
#      p = multiprocessing.Process(target = addition_1D(lst1, lst2))
#      p.start()
#      processes.append(p)

#for process in processes: 
#    process.join()

## 2D array matrix addition
#def addition_2D(lst1, lst2): 
#    # check if it's a two dimension array 

#    # check if all values are in type integer 
#    pass
## 2D array matrix multiplication 
#def addition_1D(lst1, lst2): 
#    # check if it's a two dimension array 

#    # check if all values are in type integer 
#    pass

## testing comment 
