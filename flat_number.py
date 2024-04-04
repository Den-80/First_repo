FLOORS = 9
APPARTMENTS_PER_FLOOR = 5

apt_number = int(input('Enter appartment number: '))
apt_per_entrance = FLOORS * APPARTMENTS_PER_FLOOR

entrance_number = (apt_number - 1) // apt_per_entrance + 1
floor_number = ((apt_number - 1) % apt_per_entrance) // APPARTMENTS_PER_FLOOR + 1
print(f'Entrance number: {entrance_number}, Floor number: {floor_number}')