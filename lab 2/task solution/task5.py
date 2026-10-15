collection=[]
def create():
    collection=[]
    print("Collection Created")

def insert(add):
    collection.append(add)
    print("Added Sucessfully")

def delete(Delete):
    collection.remove(Delete)
    print("Deleted Successfully")

def search(Search):
    if Search in collection:
        print("Element Exist")
    else:
        print("Element Doesnot Exist")

def traverse():
    for i in collection:
        print(i)

create()
insert("apple")
insert("banana")
insert("oops")
search("Apple")
delete("oops")
traverse()