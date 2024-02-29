bad_grade = int(input())
sum_grade = 0
count_grade = 0
count_fail = 0
last_task = None

while True:
    name_task = input()
    if name_task == 'Enough':
        print(f"Average score: {sum_grade / count_grade:.2f}")
        print(f"Number of problems: {count_grade}")
        print(f"Last problem: {last_task}")
        break

    grade = int(input())
    sum_grade += grade
    count_grade += 1
    last_task = name_task

    if grade <= 4:
        count_fail += 1
    if count_fail == bad_grade:
        print(f"You need a break, {count_fail} poor grades.")
        break