from book_class import Library


def library_existing_books():
 book1 = Library("my old love", "shekspier", "1995")
 book2 = Library("The Little Prince", "alberto", "1980")
 book3 = Library("big dreams", "madem kamilo", "1884")
 books = [book1, book2, book3]
 return books