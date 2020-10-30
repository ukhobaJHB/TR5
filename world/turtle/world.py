import turtle
import maze.naddis_maze as obstacles

# global obstacles

# Toy Robot Vars
# turtle.setworldcoordinates(-200, -200, 200, 200)
screen = turtle.Screen()
screen.title("Maze Runner")
screen.setup(250, 450)
i_robot = turtle.Turtle()
i_robot.left(90)

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars and obstacles list
min_y, max_y = -200, 200
min_x, max_x = -100, 100
obstacle_list = []

# Needed to show dead ends
new_wall = turtle.Turtle()
new_wall.hideturtle()


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_blocked(steps):
    "Checks if the robot will encounter an obstacle in the path."

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if obstacles.is_position_blocked(new_x, new_y):
        return True
    return False


def is_path_blocked(steps):
    "Checks if the robot will encounter an obstacle in the path."

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if obstacles.is_path_blocked(position_x, position_y, new_x, new_y):
        return True
    return False


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    global position_x, position_y

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
        
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    global i_robot

    if is_position_blocked(steps) or is_path_blocked(steps):
        return True, robot_name+': Sorry, there is an obstacle in the way.'

    if update_position(steps):
        i_robot.forward(steps)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    global i_robot

    if is_position_blocked(steps) or is_path_blocked(steps):
        return True, robot_name+': Sorry, there is an obstacle in the way.'

    if update_position(-steps):
        i_robot.back(steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index, i_robot

    i_robot.right(90)
    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index, i_robot

    i_robot.left(90)
    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def place_obstacles():
    global obstacle_list

    obstacle_list = obstacles.get_obstacles()
    obstacle = turtle.Turtle()
    obstacle.hideturtle()
    obstacle.up()
    obstacle.fillcolor("black")
    obstacle.speed(10)

    steps = get_steps()
    obstacle.shape("square")
    stamp_width = 0.05 * steps
    obstacle.shapesize(stamp_width, stamp_width, 0)

    for coordinate in obstacle_list:
        x = coordinate[0] + steps / 2
        y = coordinate[1] + steps / 2
        obstacle.goto(x, y)
        obstacle.stamp()
            

def setup_boundary():

    boundary = turtle.Turtle()
    boundary.hideturtle()
    boundary.up()
    boundary.pensize(1)
    boundary.pencolor("green")
    boundary.speed(10)
    boundary.goto(100,200)
    boundary.down()
    boundary.goto(100,-200)
    boundary.goto(-100,-200)
    boundary.goto(-100,200)
    boundary.goto(100,200)


def get_steps():
    """Calculates the number of steps the robot will move in the path

    Returns:
        int: forward steps
    """
    global obstacle_list

    x_values = list(set(map(lambda obstacle: obstacle[0], obstacle_list)))
    x_values.sort()

     
    return x_values[1] - x_values[0]


def show_dead_end(x, y, steps):
    global new_wall
    
    new_wall.color("red")
    new_wall.up()
    new_wall.goto(x + (steps / 2), y + (steps / 2))
    new_wall.shape("square")
    stamp_width = 0.05 * steps
    new_wall.shapesize(stamp_width, stamp_width, 0)
    new_wall.stamp()

    return