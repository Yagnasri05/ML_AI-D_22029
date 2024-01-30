#Question 1
def count_ele(a,n,sum):
    count=0
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i]+a[j]==sum:
                count=count+1
    return count
        
a=[2,7,4,1,3,6]
n=len(a)
sum=10
print("The number of pairs that have sum as 10 are : ", count_ele(a,n,sum))

#Question 2 
def range_of_list(n):
    if len(n) < 3:
        return "Range determination not possible"
    else:
        m=min(n)
        ma=max(n)
        res=ma-m
        return res
    
n=[5,3,8,1,0,4]
print("The range is : ", range_of_list(n))

#Question 3
def Am(A, m):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        result[i][i] = 1
    
    while m > 0:
        if m % 2 == 1:
            result = matmul(result, A)
        A = matmul(A, A)
        m //= 2
    
    return result

def matmul(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[1, 2], [1, 4]]  
m = 2
result = Am(A, m)
for row in result:
    print(row)

#Question 4
def count_char(str):
    count={}
    for char in str:
        if char.isalpha():
            char=char.lower()
            count[char]=count.get(char,0)+1
    
    maxch = max(count, key=count.get)
    maxc = count[maxch]
    return maxch, maxc

str=input("Enter the string:")
ch,c=count_char(str)

print("The highest occuring character is :",ch)
print("The number of occurences are :",c)
