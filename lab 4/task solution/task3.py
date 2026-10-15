def libaray():
    books={
        "harry poter":("title1","author1","publication1","year1","genre1"),
        "Atomic habits":("title2","author2","publication2","year2","genre2"),
        "one piece":("title3","author3","publication3","year3","genre3")
    }
    def search():
        title=input("Enter the book title: ")
        if title in books:
            print(books[title])
        else:
            print("Book not found in libarary")
    search()

    def add():
        title=input("Enter the book title to add: ")
        if title in books:
            print("This book is already on library")
        else:
            author=input("Enter the book author to add: ")
            publication=input("Enter the publication title to add: ")
            year=int(input("Enter the book year to add: "))
            genre=input("Enter the book genre to add: ")
            books[title]=(author,publication,year,genre)
            print("Added successfully")
    add()

    def delete():
        title=input("Enter the book title to delete: ")
        if title in books:
            del books [title]
            print("Deleted Successfully")
        else:
            print("This book is not in libaray")
        
        print("Dictionary:",books)
    delete()


libaray()