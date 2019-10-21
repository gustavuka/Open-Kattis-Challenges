capacity, stations = input().split(' ')
capacity = int(capacity)
stations = int(stations)
users = 0
reading = True
pos = 'possible'

for i in range (stations):
    left, entered, stay = input().split(' ')
    users += int(entered)
    users -= int(left)
    if users < 0:
        pos = ('impossible')
    elif users > capacity:
        pos = ('impossible')
    elif int(stay) > 0 and capacity-users != 0:
        pos = ('impossible')

if users != 0 or int(entered) or int(stay) != 0:
    pos = ('impossible')
print (pos)