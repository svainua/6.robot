def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right() == True:
        move()
        if right_is_clear() == True:
            turn_right()
            move()
            turn_right()
            while not wall_in_front() == True:
                move()
            if wall_in_front() == True:
                turn_left()
                break


while not at_goal():
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        jump()
    else:
        move()
