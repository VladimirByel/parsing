from src.api_class import APIhh, APISuperJob


def user_input():
    url = "https://api.superjob.ru/2.0/vacancies/"
    hh = "https://api.hh.ru/vacancies"
    hh_ = APIhh(hh)
    super_job = APISuperJob(url)
    hh_.process()
    super_job.process()
    choice = input('Choose the key phrase for job-searching: ')
    hh_jobs = hh_.sorted_return()
    super_jobs = super_job.sorted_return()
    for job in hh_jobs:
        if choice in job.profession:
            print(job.profession, job.minimal_salary, job.city, job.requirements, job.employer)
    for s_job in super_jobs:
        if choice in s_job.profession:
            print(s_job.profession, s_job.minimal_salary, s_job.city, s_job.requirements, s_job.employer)


user_input()
