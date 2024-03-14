student = 0
standard = 0
kids = 0
while True:
    film_name = input()
    if film_name == 'Finish':
        break
    total_ticket = 0
    seats = int(input())

    for _ in range(seats):
        type_ticket = input()
        if type_ticket == 'End':
            break
        total_ticket += 1
        if type_ticket == 'standard':
            standard += 1
        elif type_ticket == 'student':
            student += 1
        elif type_ticket == 'kid':
            kids += 1
    print(f'{film_name} - {total_ticket / seats * 100:.2f}% full.')

sum_ticket = standard + student +kids
print(f'Total tickets: {sum_ticket}')
print(f'{student / sum_ticket * 100:.2f}% student tickets.')
print(f'{standard / sum_ticket * 100:.2f}% standard tickets.')
print(f'{kids / sum_ticket * 100:.2f}% kids tickets.')