"""A sequence of non-negative integers d_i >= ... >= d_n can be represented 
as the degree sequence of a finite simple graph on n vertices if and
only if d_i + ... + d_n is even and sum {i=1} to k = d_i <= (k(k-1) + (sum {j = k+1} to n min(d_i,k))
holds for every k in 1 <= k <= n. """

def getRHS(k, n, inputList):
    minVal = 0
    d_j = 0
    for j in range(k+1, n+1):
        d_j = inputList[j-1]
        minVal = minVal + min(d_j, k)
    return minVal

def edt(inputList):
    n = len(inputList)
    listDone = 1
    if (sum(inputList) % 2 == 0):
        k = 1
        d_i = 0
        #LHS
        for (i) in range(1, n):
            d_i = d_i + inputList[i-1]
            #RHS
            RHS = getRHS(k,n,inputList)
            """print("d_i: " + str(d_i))
            print("k: " + str(k))
            print("k - 1: " + str(k - 1))
            print("k * (k-1): " + str(k * (k-1)))
            print("RHS: " + str(RHS))"""
            if (d_i <= (k * (k-1) + RHS)):
                if(listDone == n):
                    return True
            else:
                print("Failed on a d_i check " + str(d_i) + " was not <= " + str((k * (k-1)) + RHS))
                return False
            listDone = listDone + 1
            k = k + 1
            #print("###############")
    else:
        print("Was not even")
        return False
    print("Error")


#Tests

#print(getRHS(2,4,[3,3,3,1]) == 3)

#fail = [3,3,3,1]
#print(not edt(fail))
#pass1 = [3,2,2,1]
#print(edt(pass1))
#pass2 = [4,3,3,2,2,2]
#print(edt(pass2))