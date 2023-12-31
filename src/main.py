from src.api_class import APIhh, APISuperJob
from src.file_creating import JSONFile
from src.vacancy import Vacancy
from src.config import URL, HH, HH_PATH, SUPER_JOB_PATH
"""
The main function to control and regulate all code
"""


def hh(choice):
    hh_ = APIhh(HH, choice)
    get_hh_info = hh_.getting_info()
    hh_json = JSONFile(HH_PATH)
    hh_json.writing(get_hh_info)
    hh_basis = hh_json.reading()
    hh_jobs = Vacancy.hh_error_filtering(hh_basis, "HH")
    for job in hh_jobs:
        if choice.lower() in job.profession.lower():
            print(job)
    hh_json.deleting()


def superjob(choice):
    super_job = APISuperJob(URL, choice)
    get_super_job_info = super_job.getting_info()
    super_json = JSONFile(SUPER_JOB_PATH)
    super_json.writing(get_super_job_info)
    super_job_basis = super_json.reading()
    super_jobs = Vacancy.super_job_error_filtering(super_job_basis, "SJ")
    for s_job in super_jobs:
        if choice.lower() in s_job.profession.lower():
            print(s_job)
    super_json.deleting()


def both(choice):
    hh(choice)
    superjob(choice)


def choose():
    while True:
        choice = input("Введите ключевое слово, по которому Вы хотите искать работу: ")
        site = input("Выберете сайт, на котором Вы хотите искать: 1 - hh.ru, 2 - SuperJob, 3 - на обоих сайтах: ")
        if site == "1":
            hh(choice)
            break
        elif site == "2":
            superjob(choice)
            break
        elif site == "3":
            both(choice)
            break
        else:
            print("Вы ввели неверный номер, попробуйте снова")
            continue


choose()
