number_of_halls = int(input())
capacity = int(input())
number_of_viewers = int(input())

if number_of_viewers > (number_of_halls * capacity):
    print('False')
else:
    print('True')