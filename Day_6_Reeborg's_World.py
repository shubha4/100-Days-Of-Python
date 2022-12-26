#Reeborg's World - The Maze Problem

#Here, I have a work-in-progress code for Reeborg's world's Maze problem. 
#The goal of the problem is to get Reeborg to reach the end of the maze, regardless of where they start on the map.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        if front_is_clear():
            move()
    elif front_is_clear():
        move()
    else:
        turn_left()