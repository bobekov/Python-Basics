sum_pages = int(input())
pages_hour = int(input())
sum_days = int(input())

sum_hour = sum_pages // pages_hour
hour_day = sum_hour / sum_days

print(hour_day)