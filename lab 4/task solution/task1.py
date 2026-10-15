name=(
    ("person1",15),
    ("person2",20),
    ("person3",23),
    ("person4",52),
    ("person5",12),
    ("person6",13),
    ("person7",90)
)
def tup():
    for i in name:
        if i[1]>=20:
            print(i[0])
tup()