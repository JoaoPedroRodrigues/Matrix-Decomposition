from numpy import *

def svd_decomp(a):
    
    at = a.T.copy()

    #encontrando U
    aat = dot(a,at)

    aatvalor, aatvetor = linalg.eig(aat)

    quicksort(aatvalor,aatvetor,0,len(aatvalor)-1)

    u = aatvetor.copy()

    #encontrando Vtransposta

    ata = dot(at,a)

    atavalor, atavetor = linalg.eig(ata)

    quicksort(atavalor,atavetor,0,len(atavalor)-1)

    v = atavetor.copy()

    vt = v.T.copy()

    #encontrando S

    n = len(aatvalor)
    
    s = zeros((n,n))

    for i in range(n) :

        s[i,i] = sqrt(aatvalor[i])


    return u,s,vt






def quicksort(list, list2, start, end):
    if start < end:                            
        split = partition(list, list2, start, end)    
        quicksort(list, list2, start, split-1)        
        quicksort(list, list2, split+1, end)
    else:
        return


def partition(list, list2, start, end):
    pivot = list[end]                          
    pivot2 = list2[:,end].copy()
    bottom = start-1                         
    top = end                                 
    done = 0
    while not done:                           

        while not done:                        
            bottom = bottom+1                  

            if bottom == top:                 
                done = 1                      
                break

            if list[bottom] < pivot:           
                list[top] = list[bottom]     
                list2[:,top] = list2[:,bottom]
                break                          
        while not done:                       
            top = top-1                        
            
            if top == bottom:                  
                done = 1                       
                break

            if list[top] > pivot:              
                list[bottom] = list[top]      
                list2[:,bottom] = list2[:,top]
                break                         


    
    list[top] = pivot                          
    list2[:,top] = pivot2.copy()
    return top     





