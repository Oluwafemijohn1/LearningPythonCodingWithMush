from operator import mul


class Employee:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def work(self):
        print(f"{self.name} is working.")


class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

    def manage(self):
        print(f"{self.name} is managing the {self.department} department.")


class Engineer(Employee):
    def __init__(self, specialization, **kwargs):
        super().__init__(**kwargs)
        self.specialization = specialization

    def design(self):
        print(f"{self.name} is designing in the field of {self.specialization}.")


class MultiRoleEmployee(Manager, Engineer):
    def __init__(self, name, department, specialization):
        super().__init__(name=name, department=department, specialization=specialization)

    def perform_roles(self):
        print(
            f"{self.name} is performing multiple roles:")
        self.work()
        self.manage()
        self.design()


multi_role_employee = MultiRoleEmployee("Alice", "IT", "Software Engineering")
multi_role_employee.perform_roles()
