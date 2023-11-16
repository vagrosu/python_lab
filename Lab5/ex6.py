class LibraryItem:
    def __init__(self, title, author, pages, copies):
        self.title = title
        self.author = author
        self.pages = pages
        self.copies = copies

    def display_item(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Pages: ", self.pages)
        print("Copies: ", self.copies)

    def check_out(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"You have checked out the book. There are now {self.copies} copies left.")
        else:
            print("There are no more copies left.")

    def return_item(self):
        self.copies += 1
        print(f"You have returned the book. There are now {self.copies} copies left.")


class Book(LibraryItem):
    def __init__(self, title, author, pages, copies, genre):
        super().__init__(title, author, pages, copies)
        self.genre = genre

    def display_item(self):
        super().display_item()
        print("Genre: ", self.genre)


class DVD(LibraryItem):
    def __init__(self, title, author, pages, copies, length):
        super().__init__(title, author, pages, copies)
        self.length = length

    def display_item(self):
        super().display_item()
        print("Length: ", self.length)


class Magazine(LibraryItem):
    def __init__(self, title, author, pages, copies, launch_date):
        super().__init__(title, author, pages, copies)
        self.launch_date = launch_date

    def display_item(self):
        super().display_item()
        print("Issue: ", self.launch_date)


if __name__ == '__main__':
    book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1000, 2, "Fantasy")
    book.display_item()
    book.check_out()
    book.return_item()
    book.check_out()
    book.check_out()
    book.check_out()
    book.return_item()

    print()
    dvd = DVD("The Matrix", "The Wachowskis", 200, 1, 120)
    dvd.display_item()
    dvd.check_out()
    dvd.return_item()
    dvd.check_out()
    dvd.check_out()
    dvd.return_item()

    print()
    magazine = Magazine("National Geographic", "National Geographic Society", 100, 4, "January 2017")
    magazine.display_item()
    magazine.check_out()
    magazine.return_item()
    magazine.check_out()
    magazine.check_out()
