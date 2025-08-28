n=int(input())

for i in range(0,n):
    print("*",end=" ")
    for j in range(n-i):
        print("_",end=" ")
    print("*")


# * _ _ _ _ _ *
# * _ _ _ _ *
# * _ _ _ *
# * _ _ *
# * _ *