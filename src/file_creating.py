import json
import os

import xlsxwriter
from abc import ABC, abstractmethod

"""
The abstract class for getting information in and out of JSON-files
"""


class File(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def writing(self, object_to_write):
        pass

    @abstractmethod
    def reading(self):
        pass

    @abstractmethod
    def deleting(self):
        pass


class JSONFile(File):
    def writing(self, object_to_write):
        with open(self.path, 'a', encoding='UTF-8', ) as file:
            json.dump(object_to_write, file, indent=4, ensure_ascii=False)

    def reading(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            return json.loads(file.read())

    def deleting(self):
        os.remove(self.path)

    @classmethod
    def excel(cls, data):
        # Workbook() takes one, non-optional, argument
        # which is the filename that we want to create.
        workbook = xlsxwriter.Workbook('vacancies.xlsx')

        # The workbook object is then used to add new
        # worksheet via the add_worksheet() method.
        worksheet = workbook.add_worksheet()

        # Use the worksheet object to write
        # data via the write() method.
        excel_list = []
        for i in data['items'][0]:
            excel_list.append(i)
        print(excel_list)
        worksheet.write("A1", "10")

        workbook.close()
