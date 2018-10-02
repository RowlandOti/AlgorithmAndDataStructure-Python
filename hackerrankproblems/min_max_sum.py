# Given five positive integers, find the minimum and maximum values that can be
# calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
#simple way without any load to the interpretor and without importing library can be 
#!/bin/python3
l=[]
u=0
n=5
l=list(map(int,input().split()))
for i in range(0,n):
    u+=l[i]
z=max(l)
x=min(l)
print(u-z,u-x)


