from openpyxl import load_workbook
import os


class Library:
    def __init__(self, name, writer, date):
        self.name = name
        self.writer = writer
        self.date = date


book1 = Library("my old love", "shekspier", "1995")
book2 = Library("The Little Prince", "alberto", "1980")
book3 = Library("big dreams", "madem kamilo", "1884")
books = [book1, book2, book3]
r=int(input("how many books do u want to add?"))
for i in range (r):
 new_book = input("enter the new books name:")
 new_book2 = input("enter the new books writer:")
 new_book3 = int(input("enter the new books date:"))
 library_new_book = Library(new_book, new_book2, new_book3)
 books.append(library_new_book)
for book in books:
     print(f"book:{book.name},writer:{book.writer},date:{book.date}")
