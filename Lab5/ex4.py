class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_employee(self):
        super().display_employee()
        print("Department: ", self.department)


class Engineer(Employee):
    def __init__(self, name, salary, specialization):
        super().__init__(name, salary)
        self.specialization = specialization

    def display_employee(self):
        super().display_employee()
        print("Specialization: ", self.specialization)


class Salesperson(Employee):
    def __init__(self, name, salary, region):
        super().__init__(name, salary)
        self.region = region

    def display_employee(self):
        super().display_employee()
        print("Region: ", self.region)


if __name__ == '__main__':
    manager = Manager("Johnut", 5000, "IT")
    manager.display_employee()

    print()
    engineer = Engineer("Mihaita", 3000, "Software")
    engineer.display_employee()

    print()
    salesperson = Salesperson("Ionut", 4000, "Bucharest")
    salesperson.display_employee()