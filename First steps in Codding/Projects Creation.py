name = input()
number_of_projects = int(input())

projects_per_hour = 3
count_hours = number_of_projects * projects_per_hour

print(f"The architect {name} will"
      f" need {count_hours} hours to complete"
      f" {number_of_projects} project/s.")