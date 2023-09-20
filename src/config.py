import os

URL = "https://api.superjob.ru/2.0/vacancies/"
HH = "https://api.hh.ru/vacancies"
key = "SUPER_JOB"
KEY = os.getenv(key)
json_hh = "hh_vacancies.json"
json_super_job = "superjob_vacancies.json"
HH_PATH = os.path.abspath(json_hh)
SUPER_JOB_PATH = os.path.abspath(json_super_job)
