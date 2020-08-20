import random

print("Welcome to employee wage problem")

RATE_PER_HOUR = 20
FULL_TIME = 1
PART_TIME = 2


def switch(attendance):
    return {
        FULL_TIME: 8,
        PART_TIME: 4
    }.get(attendance, 0)


def compute_monthly_wage():
    total_days = 0
    emp_hrs = 0
    MAX_WORKING_DAYS = 20
    MAX_WORKING_HRS = 100
    while total_days < MAX_WORKING_DAYS and emp_hrs < MAX_WORKING_HRS:
        total_days += 1
        employee_attendance = random.randint(0, 2)
        emp_hrs = emp_hrs + switch(employee_attendance)
    return emp_hrs


print("Monthly Wage = ", compute_monthly_wage() * RATE_PER_HOUR)
