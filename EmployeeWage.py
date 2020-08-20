import random

print("Welcome to employee wage problem")
employeeAttendance = random.randint(0, 2);
empHrs = 0;
RATE_PER_HOUR = 20;
FULL_TIME = 1;
PART_TIME = 2;


def switch(attendance):
    return {
        FULL_TIME: 8,
        PART_TIME: 4
    }.get(attendance, 0)


empHrs = switch(employeeAttendance);
print("Daily Wage = ", empHrs * RATE_PER_HOUR);
