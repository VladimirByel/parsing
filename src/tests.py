from api_class import APIhh


example = APIhh("https://api.hh.ru/vacancies").getting_info()
print(len(example))