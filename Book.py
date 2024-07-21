class Book:
    def __init__(self, title, author, ISBN, publicationYear, status):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publicationYear = publicationYear
        self.status = status

    def borrows(self):
        if self.status == "available":
            self.status = "borrowed"
        else:
            print(f"Sorry,{self.title}  is not available")

    def returns(self):
        if self.status == "borrowed":
            self.status = "available"
        else:
            print(f"{self.title} is already on shelf")

    def getDetails(self):
        print(
            f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Publication Year: {self.publicationYear}, status:{self.status}")

    def status_check(self):
        print(f"{self.title} is {self.status}")

    def __str__(self):
        return f"{self.title} by {self.author}"
