def factorial(n):
    if n==0:
        return 1
    else:
        result=factorial(n-1)*n
    return result    
    
n=int(input())
print(factorial(n))