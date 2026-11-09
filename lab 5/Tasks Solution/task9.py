num1=[1,2,3,4,5,6]
num2=[2,3,9,10,5,11]
set1=set(num1)
set2=set(num2)
ins=set1.intersection(set2)
if ins:
    print("Common elements are:",ins)
else:
    print("No common elements")
