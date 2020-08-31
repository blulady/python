class Book():
    def __init__ (self, title, author, date_published, genre):
        self.title = title
        self.author = author
        self.date_published = date_published
        self.genre = genre

    def info(self):
        msg = "\nPasses on information from person to person, generation to generation!"
        return msg


book = Book("Tooth From the Tiger's Mouth", 'Tom Bisio', 'October 12 2004', 'historical')
print(book.title)
print(book.info())

