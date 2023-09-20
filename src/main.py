from src.api_class import APIhh, APISuperJob
from src.file_creating import JSONFile
from src.vacancy import Vacancy
from src.config import URL, HH
"""
The main function to control and regulate all code
"""


def user_input():
    choice = input('Введите ключевое слово для поиска вакансий: ')
    hh_ = APIhh(HH, choice)
    super_job = APISuperJob(URL, choice)
    get_hh_info = hh_.getting_info()
    get_super_job_info = super_job.getting_info()
    hh_json = JSONFile("hh_vacancies.json")
    super_json = JSONFile("superjob_vacancies.json")
    hh_json.writing(get_hh_info)
    super_json.writing(get_super_job_info)
    hh_basis = hh_json.reading()
    super_job_basis = super_json.reading()
    hh_jobs = Vacancy.hh_error_filtering(hh_basis)
    super_jobs = Vacancy.super_job_error_filtering(super_job_basis)
    for job in hh_jobs:
        if choice.lower() in job.profession.lower():
            print(f"""HH: Профессия: {job.profession}
Минимальная зарплата: {job.minimal_salary}
Город: {job.city}
Требования: {job.requirements}
Работодатель: {job.employer}""")
    for s_job in super_jobs:
        if choice.lower() in s_job.profession.lower():
            print(f"""SJ: Профессия: {s_job.profession}
Минимальная зарплата: {s_job.minimal_salary}
Город: {s_job.city}
Требования: {s_job.requirements}
Работодатель: {s_job.employer}""")
    hh_json.deleting()
    super_json.deleting()


user_input()
