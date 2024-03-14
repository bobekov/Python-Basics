judges = int(input())
count_grade = 0
total_grade = 0

while True:
    presentation_name = input()
    if presentation_name == 'Finish':
        print(f"Student's final assessment is {total_grade / count_grade:.2f}.")
        break
    sum_grade = 0
    count = 0

    for _ in range(judges):
        grade = float(input())
        sum_grade += grade
        count_grade += 1

    count_grade += count
    total_grade += sum_grade

    print(f"{presentation_name} - {sum_grade / judges:.2f}.")