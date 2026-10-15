num=[]
for i in range(2):
    num.append(int(input(f"Enter num {i+1}: ")))
print(f"Sum of {num[0]} + {num[1]} is:",sum(num))
print(f"Sum of {num[0]} - {num[1]} is:",num[0]-num[1])
print(f"Sum of {num[0]} * {num[1]} is:",num[0]*num[1])
if num[1]==0:
    print("Math Error")
else:
    print(f"Sum of {num[0]} / {num[1]} is:",num[0]/num[1])



