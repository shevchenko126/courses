from person import Person
from employee import Employee

class Client(Person):
    project_name = ""

    def __init__(self, project_name, **kwargs):
        Person.__init__(self, **kwargs)
        self.project_name = project_name

    def get_name(self):
        return self.first_name + ' ' + self.last_name + ' client ' + self.project_name

petro_client = Client(first_name="Petro1", last_name="Petrenko", project_name="I")
print(petro_client.get_name())

dima_employee = Employee(first_name="Dima", last_name="Shevchenko", experience=8, program_langs=["Python", "HTML"])

persons = [petro_client, dima_employee]
for person in persons:
    print(person.get_name())