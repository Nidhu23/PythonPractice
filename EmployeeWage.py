import random


class WageComputation:
    FULL_TIME = 1
    PART_TIME = 2

    def switch(attendance):
        return {
            WageComputation.FULL_TIME: 8,
            WageComputation.PART_TIME: 4
        }.get(attendance, 0)

    def compute_monthly_wage(employee):
        total_days = 0
        emp_hrs = 0
        while total_days < employee.max_days and emp_hrs < employee.max_hrs:
            total_days += 1
            employee_attendance = random.randint(0, 2)
            emp_hrs = emp_hrs + WageComputation.switch(employee_attendance)
        print("Monthly Wage of employee in " + employee.COMP_NAME, emp_hrs * employee.rate_per_hr)
