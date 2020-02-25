def staircase(n):
    k = " "
    l = "#"
    for i in range(1,n+1):
        print(k*(n-i)+l*i,end="")

        print("\r")
if __name__ == '__main__':
    n = int(input())

    staircase(n)
