import sys

total_credit = 0
total_grade = 0

for i in range(20):
    subject, credit, grade = sys.stdin.readline().split()
    credit = float(credit)

    if grade == 'A+':
        total_grade += 4.5 * credit
    elif grade == 'A0':
        total_grade += 4.0 * credit
    elif grade == 'B+':
        total_grade += 3.5 * credit
    elif grade == 'B0':
        total_grade += 3.0 * credit
    elif grade == 'C+':
        total_grade += 2.5 * credit
    elif grade == 'C0':
        total_grade += 2.0 * credit
    elif grade == 'D+':
        total_grade += 1.5 * credit
    elif grade == 'D0':
        total_grade += 1.0 * credit
    elif grade == 'P':
        continue

    total_credit += credit

print(total_grade / total_credit)