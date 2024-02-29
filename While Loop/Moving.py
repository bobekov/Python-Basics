volume = int(input()) * int(input()) * int(input())

volume_box = 0

while volume > volume_box:
    box = input()
    if box == 'Done':
        print(f'{volume - volume_box} Cubic meters left.')
        break

    volume_box += int(box)

else:
    print(f'No more free space! You need {volume_box - volume} Cubic meters more.')