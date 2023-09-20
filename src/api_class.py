from abc import ABC, abstractmethod
import requests
import config
"""
Abstract function for API classes
"""


class APIProcessing(ABC):

    @abstractmethod
    def __init__(self):
        self.url = 0
        self.key = 0
        self.basis = 0

    @abstractmethod
    def getting_info(self):
        pass


"""
The API class for HeadHunter job offerings
"""


class APIhh(APIProcessing):

    def __init__(self, url, text):
        self.url = url
        self.key = ""
        self.text = text

    def getting_info(self):
        payload = {}
        headers = {
            "User_Agent": ''
        }

        vacancies = []
        for page in range(2):
            params = {
                "per_page": 50,
                "page": page,
                "text": self.text
            }
            response = requests.request("GET", self.url, headers=headers, data=payload, params=params)
            json_response = response.json()
            vacancies.extend(json_response['items'])
            if json_response["pages"] - 1 == page:
                break
        return {
            "items": vacancies
        }

    # def excel(self):
    #     JSONFile().excel(basis)


"""
The API class for SuperJob job offerings
"""


class APISuperJob(APIProcessing):

    def __init__(self, url, text):
        self.url = url
        self.key: str = config.KEY
        # self.key = "v3.r.137820686.bb7cea71565ef2c0772ec7a3222fa8271ef68e3d.902b5431bf9b023b53a3fce279bbed18d04ba9b0"
        self.text = text

    def getting_info(self):
        payload = {}
        headers = {
            "X-Api-App-Id": self.key
        }
        vacancies = []
        for page in range(1):
            params = {
                "count": 50,
                "page": page,
                "text": self.text
            }
            response = requests.request("GET", self.url, headers=headers, data=payload, params=params)
            json_response = response.json()
            vacancies.extend(json_response['objects'])
            if json_response["total"] - 1 == page:
                break
        return {
            "objects": vacancies
        }
