def fact(n):
    '''Hey there this a a doc string'''
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

print(fact.__doc__)
n=int(input(("ENter the number")))
print(fact(n))
