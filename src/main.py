from src.api_class import APIhh, APISuperJob
from src.file_creating import JSONFile
from src.vacancy import Vacancy
"""
The main function to control and regulate all code
"""


def user_input():
    url = "https://api.superjob.ru/2.0/vacancies/"
    hh = "https://api.hh.ru/vacancies"
    choice = input('Введите ключевое слово для поиска вакансий: ')
    hh_ = APIhh(hh, choice)
    super_job = APISuperJob(url, choice)
    get_hh_info = hh_.getting_info()
    get_super_job_info = super_job.getting_info()
    JSONFile.hh_writing(get_hh_info)
    JSONFile.super_job_writing(get_super_job_info)
    hh_basis = JSONFile.hh_reading()
    super_job_basis = JSONFile.super_reading()
    hh_jobs = Vacancy.hh_error_filtering(hh_basis)
    super_jobs = Vacancy.super_job_error_filtering(super_job_basis)
    for job in hh_jobs:
        if choice in job.profession:
            print(f"""HH: Профессия: {job.profession}
Минимальная зарплата: {job.minimal_salary}
Город: {job.city}
Требования: {job.requirements}
Работодатель: {job.employer}""")
    for s_job in super_jobs:
        if choice in s_job.profession:
            print(f"""SJ: Профессия: {s_job.profession}
Минимальная зарплата: {s_job.minimal_salary}
Город: {s_job.city}
Требования: {s_job.requirements}
Работодатель: {s_job.employer}""")


user_input()
