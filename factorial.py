from functools import reduce
n=int(input("Enter number fot which you want factorial"))
result= reduce(lambda x,y:x*y,[n for n in range(1,n+1)])
print(result)
