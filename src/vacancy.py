
"""
The class for processing vacancies
"""


class Vacancy:

    def __init__(self, profession, requirements, city, employer, salary=0):
        self.profession = profession
        if salary is None:
            self.minimal_salary = 0
        else:
            self.minimal_salary = salary
        self.requirements = requirements
        self.city = city
        self.employer = employer

    def __lt__(self, other):
        return self.minimal_salary < other.minimal_salary

    def __str__(self):
        return f"{self.profession}"

    def __repr__(self):
        return f"{self.minimal_salary}"

    @staticmethod
    def hh_error_filtering(basis):
        vacancies_list = []
        for one in basis["items"]:
            if one.get('salary'):
                vacancies_list.append(Vacancy(one['name'], one['snippet']['requirement'],
                                              one['area']['name'], one['employer']['name'], one['salary']['from']))
            else:
                vacancies_list.append(Vacancy(one['name'], one['snippet']['requirement'],
                                              one['area']['name'], one['employer']['name'], 0))
        return sorted(vacancies_list, reverse=True)

    @staticmethod
    def super_job_error_filtering(basis):
        vacancies_list = []
        for one in basis['objects']:
        #for one in basis:
            if one.get('payment_from'):
                if one['client'].get('title'):
                    vacancies_list.append(Vacancy(one['profession'], one['vacancyRichText'],
                                                  one['town']['title'], one['client']['title'], one['payment_from']))
                else:
                    vacancies_list.append(Vacancy(one['profession'], one['vacancyRichText'],
                                                  one['town']['title'], "неизвестен", one['payment_from']))
            else:
                vacancies_list.append(Vacancy(one['profession'], one['vacancyRichText'],
                                              one['town']['title'], one['client']['title'], 0))
        return sorted(vacancies_list, reverse=True)

    def comparison(self, other):
        try:
            self.minimal_salary - other.minimal_salary
        except TypeError:
            raise TypeError("Oops, one of the objects you're trying to compare lacks the necessary method")
        else:
            if self.minimal_salary > other.minimal_salary:
                print(f"{self.profession}'s salary is bigger than that of "
                      f"{other.profession}'s by {self.minimal_salary - other.minimal_salary}")
                return self.minimal_salary - other.minimal_salary
            elif self.minimal_salary == other.minimal_salary:
                print(f"The salary of {self.profession} is equal to that of {other.profession}")
                return 0
            elif self.minimal_salary < other.minimal_salary:
                print(f"The salary of {other.profession} is bigger than the one of "
                      f"{self.profession} by {other.minimal_salary - self.minimal_salary}")
                return other.minimal_salary - self.minimal_salary

    def __add__(self, other):
        return self.minimal_salary + other.minimal_salary
