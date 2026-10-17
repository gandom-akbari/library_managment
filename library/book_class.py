from openpyxl import load_workbook
import os


class Library:
    def __init__(self, name, writer, date):
        self.name = name
        self.writer = writer
        self.date = date
