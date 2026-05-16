# Record Datatype

# Book:
# Title: STRING
# Author: STRING
# ISBN: INTEGER


class Book:
    # PUBLIC Title: STRING
    # PUBLIC Author: STRING
    # PUBLIC ISBN: INTEGER

    def __init__(self, Title: str, Author: str, ISBN: int):
        self.Title = Title
        self.Author = Author
        self.ISBN = ISBN


mybook = Book("Papersdock", "Taha", 123456)
mybook.Author = "Anas"
print(mybook.Author)
