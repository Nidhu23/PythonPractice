import random

print("Welcome to employee wage problem")

totalDays = 0
empHrs = 0
MAX_WORKING_DAYS = 20
MAX_WORKING_HRS = 100
RATE_PER_HOUR = 20
FULL_TIME = 1
PART_TIME = 2


def switch(attendance):
    return {
        FULL_TIME: 8,
        PART_TIME: 4
    }.get(attendance, 0)


while totalDays < MAX_WORKING_DAYS and empHrs < MAX_WORKING_HRS:
    totalDays += 1
    employeeAttendance = random.randint(0, 2)
    empHrs = empHrs + switch(employeeAttendance)
print("Monthly Wage = ", empHrs * RATE_PER_HOUR)
