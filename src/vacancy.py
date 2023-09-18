
class Vacancy:

    def __init__(self, profession, requirements, city, employer, salary=0):
        self.profession = profession
        self.minimal_salary = salary
        try:
            self.minimal_salary < 9
        except TypeError:
            self.minimal_salary = 0
        self.requirements = requirements
        self.city = city
        self.employer = employer

    def __lt__(self, other):
        return self.minimal_salary < other.minimal_salary

    def __str__(self):
        return f"{self.profession}"

    def __repr__(self):
        return f"{self.minimal_salary}"

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




