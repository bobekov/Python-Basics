lenght = int(input())
widht = int(input())
height = int(input())
percent = float(input()) / 100

volume = lenght * widht * height / 1000
volume -= percent * volume

print(volume)