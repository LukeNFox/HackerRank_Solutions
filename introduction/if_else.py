#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird
#!/bin/python3

N = int(input())

if N%2 != 0:
    print('Weird')
else:
    if N in range(2,5):
        print('Not Weird')
    elif N in range(6,21):
        print('Weird')
    else:
        print('Not Weird')
