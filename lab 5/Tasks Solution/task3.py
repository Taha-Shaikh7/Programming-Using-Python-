# #Method 1
list1=[]
for i in range(5):
    num1=int(input(f"Enter the integer {i+1} of list 1: "))
    list1.append(num1)

list2=[]
for i in range(5):
    num1=int(input(f"Enter the integer {i+1} of list 2: "))
    list2.append(num1)

final=list1+list2
final.sort()
print("Final list is:",final)

# Method 2
list1 = list(map(int,input("Enter first list: ")))
list2 = list(map(int,input("Enter second list: ")))

merged_list = list1 + list2
merged_list.sort()

print("Merged and sorted list:", merged_list)