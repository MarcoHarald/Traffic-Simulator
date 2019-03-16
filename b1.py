import numpy as np
#import matplotlib.pylab as plt
import random

# set boundary speed of cars
maxVelocity = 3
minVelocity = 0

# set initial conditions
road = [0,0,0,2,0,0,3,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# count how many cars and spaces
cars = 0
for i in road:
    if i !=0:
        cars = cars+1

print('spaces on road:', len(road)-1)
print('cars on road:', cars)
print('---main code---')


#set simulation: start, length and spacing counter
frame=0
length = 30
emptyCounter = 0

while frame < length:
    position = len(road) - 1

    while position >= 0:

       # print(position)

        if road[position] == 0:
            emptyCounter = emptyCounter + 1
            position = position - 1
            #print('OP. 1',position,road[position])

        elif road[position] < emptyCounter:
            #convert from state to real speed
            road[position] = road[position] - 1
            #save old speed & declare new speed
            oldVelocity = road[position]
            newVelocity = min(road[position]+1,maxVelocity)
            #set old position to zero as car has moved
            road[position] = 0
            #car has moved by newVelocity but state must be set to +1 (as state=0 means no car)
            #check if position loops around the track at edges
            if position+newVelocity > len(road)-1:
                newPosition = position+newVelocity - len(road)
                road[newPosition] = newVelocity+1
            else:
                road[position+newVelocity] = newVelocity+1
            #check how many empty spaces
            emptyCounter = newVelocity
            #iterate
            position = position - 1

            #print('OP. 2',position,road[position])

        elif road[position] > emptyCounter:
            #convert from state to real speed
            road[position] = road[position] - 1
            #save old speed & declare new speed
            oldVelocity = road[position]
            newVelocity = max(emptyCounter-1,minVelocity)
            #set old position to zero as car has moved
            road[position] = 0
            #check if position loops around the track at edges
            if position+newVelocity > len(road)-1:
                newPosition = position+newVelocity - len(road)
                road[newPosition] = newVelocity+1
            else:
                road[position+newVelocity] = newVelocity+1
            #check how many empty spaces
            emptyCounter = newVelocity
            #iterate
            position = position - 1

            #print('OP. 3',position,road[position])

        elif road[position] == emptyCounter:
            #convert from state to real speed
            road[position] = road[position] - 1
            # save old speed & declare new speed
            oldVelocity = road[position]
            newVelocity = oldVelocity
            # set old position to zero as car has moved
            road[position] = 0
            #check if position loops around the track at edges
            if position+newVelocity > len(road)-1:
                newPosition = position+newVelocity - len(road)
                road[newPosition] = newVelocity+1
            else:
                road[position+newVelocity] = newVelocity+1
            #check how many empty spaces
            emptyCounter = newVelocity
            #iterate
            position = position - 1



    #iterate frame
    print('instance:',frame,'   road status:',road)
    frame = frame+1

print('---end of main code---')
