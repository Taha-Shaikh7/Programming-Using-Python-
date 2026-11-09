num1=[1,2,3,4,5,6]
num2=[2,3,9,10,5,11]
common=False
for i in num1:
    for j in num2:
        if i==j:
            common=True
if common:
    print("common element")
else:
    print("No common element")

#using Sets

set1=set(num1)
set2=set(num2)
if set1.intersection(set2):
    print("Common Elements")
else:
    print("No common elements")

