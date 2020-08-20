import random

print("Welcome to employee wage problem")
employeeAttendance = random.randint(0, 2);
empHrs = 0;
RATE_PER_HOUR = 20;
FULL_TIME = 1;
PART_TIME = 2;

if employeeAttendance == FULL_TIME:
    empHrs = 8
elif employeeAttendance == PART_TIME:
    empHrs = 4
print("Daily Wage = ", empHrs * RATE_PER_HOUR);
