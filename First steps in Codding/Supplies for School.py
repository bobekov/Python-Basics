number_chemical_packets = int(input())
number_marker_packets = int(input())
liters_preparation = int(input())
discount = int(input()) / 100

chemical_packets = 5.80
marker_packets = 7.20
preparation = 1.20

sum_packets = (number_chemical_packets * chemical_packets) + \
              (number_marker_packets * marker_packets) + \
              (liters_preparation * preparation)
sum_packets_with_discount = sum_packets - (sum_packets * discount)

print(sum_packets_with_discount)