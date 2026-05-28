d=str(input('Enter your directions:'))
x=0
y=0
while True:
    if 'NORTH' not in d or 'SOUTH' not in d or 'EAST' not in d or 'WEST' not in d or 'north' not in d or 'south' not in d or 'east' not in d or 'west' not in d:
        print('Invalid input. Please enter valid directions (NORTH, SOUTH, EAST, WEST, north, south, east, west).')
    else:
        y+=d.count('NORTH') + d.count('north')
        y-=d.count('SOUTH') + d.count('south')
        x+=d.count('EAST') + d.count('east')
        x-=d.count('WEST') + d.count('west')
        print(f'Final position: ({x}, {y})')
        break