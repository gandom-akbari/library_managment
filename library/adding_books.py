import os
from book_class import Library
from existed_books import library_existing_books
from openpyxl import load_workbook

FILE_PATH = os.path.join(os.path.dirname(__file__), "data.xlsx")

def library_add_book():
    books = library_existing_books()
    wb = load_workbook('data.xlsx')
    ws = wb.active




    r = int(input("how many books do u want to add?"))
    for i in range(r):

       name = input("enter the new books name:")
       writer = input("enter the new books writer:")
       date = int(input("enter the new books date:"))
       library_new_book = Library(name,writer,date)
       books.append(library_new_book)
       ws.append([name,writer,date])
       wb.save(FILE_PATH)  # بدون این هیچی ذخیره نمی‌شه
       print("saved!")

       for book in books:
          print(f"book:{book.name},writer:{book.writer},date:{book.date}")
library_add_book()