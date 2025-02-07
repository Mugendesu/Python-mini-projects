class Library:
    def __init__(self):
        self.no_of_books=0
        self.books=[]
    def show(self):
        if (len(self.books)==0):
            print("No nooks")
        else:
            print("The books are:")
            for i in self.books:
                print(i)
    def add(self, book):
        self.books.append(book)
        self.no_of_books+=1
        print("The book has been added")
    def number(self):
        print(f"The number of books are: {self.no_of_books}")
obj=Library()
obj.show()
obj.add("Harry Potter")
obj.add("Alice and Wonderland")
obj.show()
obj.number()