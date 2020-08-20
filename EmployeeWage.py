import random

print("Welcome to employee wage problem")

empHrs = 0
WORKING_DAYS = 20
RATE_PER_HOUR = 20
FULL_TIME = 1
PART_TIME = 2


def switch(attendance):
    return {
        FULL_TIME: 8,
        PART_TIME: 4
    }.get(attendance, 0)


for day in range(1, WORKING_DAYS):
    employeeAttendance = random.randint(0, 2)
    empHrs = empHrs + switch(employeeAttendance)
print("Monthly Wage = ", empHrs * RATE_PER_HOUR)
