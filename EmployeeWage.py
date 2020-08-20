import random

print("Welcome to employee wage problem")
employeeAttendance = random.randint(0, 1);
empHrs = 0;
RATE_PER_HOUR=20;

if employeeAttendance == 1:
    empHrs = 8
print("Daily Wage = ", empHrs*RATE_PER_HOUR);