#method 1
tup=(29,34,59,24,65,67,21,15,66,88,12)
print("Even number: ",end="")
for i in tup:
    if i%2==0:
        print(i,end=" ")

print("\nOdd number: ",end="")
for j in tup:
    if j%2!=0:
        print(j,end=" ")

#method 2

even=tuple(i for i in tup if i%2==0)
print("\nEven numbers:",even) 

odd=tuple(i for i in tup if i%2!=0)
print("Odd numbers:",odd)
