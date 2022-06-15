from person import Person, PETRO_PERSON


class Employee(Person):
    years_experience = 0
    program_langs = []

    def __init__(self, experience=0, program_langs=[], **kwargs):
        Person.__init__(self, **kwargs)
        self.years_experience = experience
        self.program_langs = program_langs
        # print(experience)


dima_employee = Employee(first_name="Dima", last_name="Shevchenko", experience=8, program_langs=["Python", "HTML"])
petro_employee = Employee(first_name="Petro", last_name="Petrenko", experience=10, program_langs=["Java", "CSS"])
print(dima_employee.program_langs)
print(dima_employee)
print(dima_employee.get_name())
print( PETRO_PERSON )