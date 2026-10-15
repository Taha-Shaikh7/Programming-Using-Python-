sub=[]
for i in range(5):
    sub.append(int(input(f"Enter mark of subject {i+1}: ")))

result=sum(sub)
print("Sum of all subjects is: ",result)

print("Average is: ",result/len(sub))