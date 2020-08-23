from Employee import Employee
from EmployeeWage import WageComputation

print("Welcome to employee wage problem")


def main():
    choice = 1
    try:
        while choice != 0:
            comp_name = input("Enter company name ")
            max_hours = int(input("Enter max working hours "))
            max_days = int(input("Enter max working days "))
            rate_per_hr = int(input("Enter rate per hour "))
            employee = Employee(comp_name, max_hours, max_days, rate_per_hr)
            WageComputation.compute_monthly_wage(employee)
            print("Enter 1 to continue, 0 to quit")
            choice = int(input())
    except ValueError:
        print("Entered String value, Expecting numerical values")
    except TypeError:
        print("Expected object of employee type")


main()
