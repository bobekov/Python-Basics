area = int(input()) * int(input())
pieces_eaten = 0

while pieces_eaten <= area:
    piece = input()
    if piece == 'STOP':
        print(f'{area - pieces_eaten} pieces are left.')
        break

    pieces_eaten += int(piece)

else:
    print(f'No more cake left! You need {pieces_eaten - area} pieces more.')