"""A sequence of non-negative integers d_i >= ... >= d_n can be represented 
as the degree sequence of a finite simple graph on n vertices if and
only if d_i + ... + d_n is even and sum {i=1} to k = d_i <= (k(k-1) + (sum {j = k+1} to n min(d_i,k))
holds for every k in 1 <= k <= n. """

def edt(inputList):
    listSum = 0
    n = len(inputList)
    for i in inputList:
        listSum = listSum + i
    if (listSum % 2 == 0):
        k = 0
        d_i = 0
        #LHS
        for (i) in range(1, n+1):
            minVal = 0
            d_i = inputList[i-1]
            #RHS
            for (j) in range(1, n+1):
                minVal = minVal + min(inputList[j-1], k)
            if (d_i <= (k * (k-1) + minVal)):
                #List Done check
                if(i == n+1):
                    return True
            else:
                print("Failed on a d_i <= check. d_i = " + str(d_i) + " and k = " + str(k))
                return False
    print("Was not even")
    return False

#Tests
fail = [3,3,3,1]
pass1 = [3,2,2,1]
pass2 = [4,3,3,2,2,2]
print(not edt(fail))
print(edt(pass1))
print(edt(pass2))