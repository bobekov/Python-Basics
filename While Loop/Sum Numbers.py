number = int(input())
numbers = 0

while True:
    num = int(input())
    numbers += num

    if numbers >= number:
        print(numbers)
        break