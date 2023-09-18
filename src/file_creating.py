import json
import xlsxwriter
from abc import ABC, abstractmethod


class File(ABC):

    @classmethod
    @abstractmethod
    def hh_writing(cls, object_to_write):
        pass

    @classmethod
    @abstractmethod
    def super_job_writing(cls, object_to_write):
        pass


class JSONFile(File):

    @classmethod
    def hh_writing(cls, object_to_write):
        with open('hh_vacancies.json', 'a', encoding='UTF-8') as file:
            json.dump(object_to_write, file, indent=4)

    @classmethod
    def super_job_writing(cls, object_to_write):
        with open('superjob_vacancies.json', 'a') as file:
            json.dump(object_to_write, file, indent=4)

    @classmethod
    def hh_reading(cls):
        with open('hh_vacancies.json', 'r') as file:
            return json.load(file)

    @classmethod
    def super_reading(cls):
        with open('superjob_vacancies.json', 'r') as file:
            return json.load(file)

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
