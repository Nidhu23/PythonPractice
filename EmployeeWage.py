import random

print("Welcome to employee wage problem")


class Employee:
    FULL_TIME = 1
    PART_TIME = 2

    def __init__(self, comp_name, max_hrs, max_days, rate_per_hr):
        self.rate_per_hr = rate_per_hr
        self.max_days = max_days
        self.max_hrs = max_hrs
        self.COMP_NAME = comp_name

    def switch(attendance):
        return {
            Employee.FULL_TIME: 8,
            Employee.PART_TIME: 4
        }.get(attendance, 0)

    def compute_monthly_wage(self):
        total_days = 0
        emp_hrs = 0
        while total_days < self.max_days and emp_hrs < self.max_hrs:
            total_days += 1
            employee_attendance = random.randint(0, 2)
            emp_hrs = emp_hrs + Employee.switch(employee_attendance)
        print("Monthly Wage of employee in " + self.COMP_NAME, emp_hrs * self.rate_per_hr)


def main():
    n = 1
    while n != 0:
        comp_name = input("Enter company name ")
        max_hours = int(input("Enter max working hours "))
        max_days = int(input("Enter max working days "))
        rate_per_hr = int(input("Enter rate per hour "))
        employee = Employee(comp_name, max_hours, max_days, rate_per_hr)
        employee.compute_monthly_wage()
        print("Enter 1 to continue, 0 to quit")
        n = int(input())


main()
