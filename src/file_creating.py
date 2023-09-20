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
            #print(json.loads(file.read()))
            return json.loads(file.read())

    def deleting(self):
        os.remove(self.path)
