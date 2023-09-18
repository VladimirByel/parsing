from abc import ABC, abstractmethod
from file_creating import JSONFile
from vacancy import Vacancy
import requests


class APIProcessing(ABC):

    @abstractmethod
    def __init__(self):
        self.url = 0
        self.key = 0
        self.basis = 0

    @abstractmethod
    def getting_info(self):
        pass

    @abstractmethod
    def sorted_return(self):
        pass

    @abstractmethod
    def process(self):
        pass


class APIhh(APIProcessing):

    def __init__(self, url):
        self.url = url
        self.key = ""
        self.basis = self.getting_info()

    def getting_info(self):
        payload = {}
        headers = {
            "User_Agent": ''
        }

        vacancies = []
        for page in range(10):
            params = {
                "per_page": 50,
                "page": page,
                "text": "python"
            }
            response = requests.request("GET", self.url, headers=headers, data=payload, params=params)
            print(response.json())
            vacancies.extend(response.json()['items'])
            if response.json()["pages"] - 1 == page:
                break
        return vacancies

    @staticmethod
    def error_filtering():
        basis = JSONFile.hh_reading()
        vacancies_list = []
        for one in basis['items']:
            try:
                vacancies_list.append(Vacancy(one['name'], one['snippet']['requirement'],
                                              one['area']['name'], one['employer']['name'], one['salary']['from']))
            except TypeError:
                vacancies_list.append(Vacancy(one['name'], one['snippet']['requirement'],
                                              one['area']['name'], one['employer']['name'], 0))
        return vacancies_list

    def sorted_return(self):
        return sorted(self.error_filtering(), reverse=True)

    def process(self):
        JSONFile().hh_writing(self.basis)

    # def excel(self):
    #     JSONFile().excel(basis)


class APISuperJob(APIProcessing):

    def __init__(self, url):
        self.url = url
        self.key = "v3.r.137820686.bb7cea71565ef2c0772ec7a3222fa8271ef68e3d.902b5431bf9b023b53a3fce279bbed18d04ba9b0"
        self.basis = self.getting_info()

    def getting_info(self):
        payload = {}
        headers = {
            "X-Api-App-Id": self.key
        }
        params = {
            "count": 100
        }

        response = requests.request("GET", self.url, headers=headers, data=payload, params=params)
        return response.json()

    @staticmethod
    def error_filtering():
        vacancies_list = []
        basis = JSONFile.super_reading()
        for one in basis['objects']:
            try:
                try:
                    vacancies_list.append(Vacancy(one['profession'], one['vacancyRichText'],
                                                  one['town']['title'], one['client']['title'], one['payment_from']))
                except KeyError:
                    vacancies_list.append(Vacancy(one['profession'], one['vacancyRichText'],
                                                  one['town']['title'], "Работодатель неизвестен", one['payment_from']))
            except TypeError:
                vacancies_list.append(Vacancy(one['profession'], one['vacancyRichText'],
                                              one['town']['title'], one['client']['title'], 0))
        return vacancies_list

    def sorted_return(self):
        return sorted(self.error_filtering(), reverse=True)

    def process(self):
        JSONFile().super_job_writing(self.basis)
