def fun():
    num=int(input("Enter a number: "))
    if num%2==0:
        print(f"The number {num} is even ")
    else:
        print(f"The number {num} is odd")
    print(f"The number {num} is greater than 5:",num>5)
fun()

#another way
def fun1():
    num2=int(input("Enter a number: "))
    print("even" if num2%2==0 else "odd")
    print(num2>5)
fun1()
