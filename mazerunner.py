obstacles = []
steps = 10
explored = []
new_obstacles = []
corners = []


def check_is_loop(robot_name, env, direction):
    """Checks if the robot is in a loop

    Args:
        robot_name (str): name given to the robot
        env (module): The world module used in the program
        direction (int): the direction which the robot is facing

    Returns:
        (boolean, list): True if its in a loop, A list of the loop coordinates 
    """

    global corners

    x, y = get_current_location(env)

    loop_points = list(
        filter(
            # lambda corner: corner[0] == x and corner[1] == y, corners
            lambda corner: corner == (x, y), corners
        )
    )

    print("loop points", loop_points)
    if len(loop_points) > 1: # 2
        print("is loop")
        loop_indexes = [
            i for i in range(len(corners))
            if corners[i] == (x, y)
        ]

        last_index  = loop_indexes[-1]
        loop_indexes = [
            loop_indexes[i] for i in range(len(loop_indexes) - 1)
            if loop_indexes[i + 1] - loop_indexes[i] > 1
        ]
        loop_indexes.append(last_index)

        print("indexes", loop_indexes)
        if len(loop_indexes) > 1:
            print("segment", corners[loop_indexes[0]:loop_indexes[1]])
            return True, corners[loop_indexes[0]:loop_indexes[1]]
        elif len(loop_indexes) == 1:
            print("segment", corners[loop_indexes[0]])
            return True, corners[loop_indexes[0]:]

    return False, []


def reduce_path(direction, x, y, combined_obstacles):

    global steps

    # left hand side cells
    top_left_cell = (x - steps, y + steps) in combined_obstacles
    left_cell = (x - steps, y) in combined_obstacles
    bottom_left_cell = (x - steps, y - steps) in combined_obstacles

    # centre cells
    top_cell = (x, y + steps) in combined_obstacles
    bottom_cell = (x, y - steps) in combined_obstacles

    # right hand side cells
    top_right_cell = (x + steps, y + steps) in combined_obstacles
    right_cell = (x + steps, y) in combined_obstacles
    bottom_right_cell = (x + steps, y - steps) in combined_obstacles

    print(direction)

    if direction == 0 and not left_cell and right_cell:
        if not top_left_cell and not bottom_left_cell:
            return True

    if direction == 0 and left_cell and not right_cell:
        if not top_right_cell and not bottom_right_cell:
            return True
        
    elif direction == 1 and not top_cell and bottom_cell:
        if not top_right_cell and not top_left_cell:
            return True
        
    elif direction == 1 and top_cell and not bottom_cell:
        if not bottom_right_cell and not bottom_left_cell:
            return True
        
    elif direction == 2 and not right_cell and left_cell:
        if not bottom_right_cell and not top_right_cell:
            return True
        
    elif direction == 2 and right_cell and not left_cell:
        if not bottom_left_cell and not top_left_cell:
            return True

    elif direction == 3 and not bottom_cell and top_cell:
        if not bottom_left_cell and not bottom_right_cell:
            return True

    elif direction == 3 and bottom_cell and not top_cell:
        if not top_left_cell and not top_right_cell:
            return True

    return False


# def explored_all_turns(direction, x, y, combined_obstacles):
#     """Checks if all turns have been explored

#     Args:
#         direction (int): the direction which the robot is facing
#         x (int): current x co-ordinate
#         y (int): current y co-ordinate
#         combined_obstacles (list): A comnined list of maze obstacles and new obstacles

#     Returns:
#         boolean: True is all turns have been made
#     """

#     global steps, explored

#     is_blocked = False

#     if direction == 0 and (x, y - steps) in combined_obstacles:
#         # ^
#         is_blocked = True

#     if direction == 1 and (x - steps, y) in combined_obstacles:
#         # >
#         is_blocked = True

#     if direction == 2 and (x, y + steps) in combined_obstacles:
#         # v
#         is_blocked = True

#     if direction == 3 and (x + steps, y) in combined_obstacles:
#         # >
#         is_blocked = True
        

#     count = 0
#     if is_blocked:
#         if (x - steps, y) in explored:
#             count += 1
        
#         if (x + steps, y) in explored:
#             count += 1
        
#         if (x, y - steps) in explored:
#             count += 1
        
#         if (x, y + steps) in explored:
#             count += 1
    
#     return count == 3


def is_dead_end(env, direction, x, y, combined_obstacles):
    """Finds available sides to turn to

    Args:
        direction (int): the direction which the robot is facing
        x (int): current x co-ordinate
        y (int): current y co-ordinate
        combined_obstacles (list): A comnined list of maze obstacles and new obstacles

    Returns:
        boolean: True if walls == 3
    """

    global steps

    # if y == -200:
    #     add_obstacle(env, x, y - steps)
    # elif y == 200 - steps:
    #     add_obstacle(env,  x, y + steps)
    # elif x == -100:
    #     add_obstacle(env, x - steps, y)
    # elif x == 100 - steps:
    #     add_obstacle(env, x + steps, y)

    walls = 0

    if direction == 0:
        # ^
        if (x - steps, y) in combined_obstacles:
            walls += 1

        if (x + steps, y) in combined_obstacles:
            walls += 1

        if (x, y - steps) in combined_obstacles:
            walls += 1

    if direction == 1:
        # >
        if (x, y + steps) in combined_obstacles:
            walls += 1

        if (x, y - steps) in combined_obstacles:
            walls += 1
        
        if (x - steps, y) in combined_obstacles:
            walls += 1

    if direction == 2:
        # v
        if (x + steps, y) in combined_obstacles:
            walls += 1

        if (x - steps, y) in combined_obstacles:
            walls += 1

        if (x, y + steps) in combined_obstacles:
            walls += 1

    if direction == 3:
        # <
        if (x, y - steps) in combined_obstacles:
            walls += 1

        if (x, y + steps) in combined_obstacles:
            walls += 1

        if (x + steps, y) in combined_obstacles:
            walls += 1

    return walls == 3


def do_forward(robot_name, env):
    """Moves the robot forward

    Args:
        robot_name (str): name given to the robot
        env (module): The world module used in the program
    """

    global explored

    (do_next, command_output) = env.do_forward(robot_name, steps)
    print(command_output)
    x, y = get_current_location(env)
    print(f"> HAL now at position ({x},{y}).")
    explored.append((x, y))


def get_path_ways(direction, x, y, combined_obstacles):
    """Finds available sides to turn to

    Args:
        direction (int): the direction which the robot is facing
        x (int): current x co-ordinate
        y (int): current y co-ordinate
        combined_obstacles (list): A comnined list of maze obstacles and new obstacles

    Returns:
        str: available turn
    """

    global explored, steps

    path_ways = []

    if direction == 0:
        # ^
        if (x, y + steps) not in combined_obstacles and \
            (x, y + steps) not in explored:
                return ["forward"]

        if (x - steps, y) not in combined_obstacles and \
            (x - steps, y) not in explored:
                return ["left"]

        if (x + steps, y) not in combined_obstacles and \
            (x + steps, y) not in explored:
                return ["right"]

        if (x, y + steps) not in combined_obstacles:
            path_ways.append("forward")

        if (x - steps, y) not in combined_obstacles:
            path_ways.append("left")

        if (x + steps, y) not in combined_obstacles:
            path_ways.append("right")

    if direction == 1:
        # >
        if (x + steps, y) not in combined_obstacles and \
            (x + steps, y) not in explored:
                return ["forward"]

        if (x, y + steps) not in combined_obstacles and \
            (x, y + steps) not in explored:
                return ["left"]

        if (x, y - steps) not in combined_obstacles and \
            (x, y - steps) not in explored:
                return ["right"]

        if (x + steps, y) not in combined_obstacles:
            path_ways.append("forward")

        if (x, y + steps) not in combined_obstacles:
            path_ways.append("left")

        if (x, y - steps) not in combined_obstacles:
            path_ways.append("right")

    if direction == 2:
        # v
        if (x, y - steps) not in combined_obstacles and \
            (x, y - steps) not in explored:
                return ["forward"]

        if (x + steps, y) not in combined_obstacles and \
            (x + steps, y) not in explored:
                return ["left"]

        if (x - steps, y) not in combined_obstacles and \
            (x - steps, y) not in explored:
                return ["right"]

        if (x, y - steps) not in combined_obstacles:
            path_ways.append("forward")
            
        if (x + steps, y) not in combined_obstacles:
            path_ways.append("left")

        if (x - steps, y) not in combined_obstacles:
            path_ways.append("right")

    if direction == 3:
        # <
        if (x - steps, y) not in combined_obstacles and \
            (x - steps, y) not in explored:
                return ["forward"]

        if (x, y - steps) not in combined_obstacles and \
            (x, y - steps) not in explored:
                return ["left"]

        if (x, y + steps) not in combined_obstacles and \
            (x, y + steps) not in explored:
                return ["right"]

        if (x - steps, y) not in combined_obstacles:
            path_ways.append("forward")
            
        if (x, y - steps) not in combined_obstacles:
            path_ways.append("left")

        if (x, y + steps) not in combined_obstacles:
            path_ways.append("right")

    return path_ways


def do_turn(robot_name, env, direction, x, y, combined_obstacles):
    """Turns the robot in either left or right

    Args:
        robot_name (str): name given to the robot
        env (module): The world module used in the program
        direction (int): the direction which the robot is facing
        x (int): current x coordinate
        y (int): current y coordinate
        combined_obstacles (list): A comnined list of maze obstacles and new obstacles

    Returns:
        boolean: True if turn was complete
    """

    global corners

    path_way = get_path_ways(direction, x, y, combined_obstacles)

    if len(path_way) >= 1:
        if "left" == path_way[0]:
            (do_next, command_output) = env.do_left_turn(robot_name)
            print(command_output)
            corners.append(get_current_location(env))
            # turn_index == 0
            return True
        elif "right" == path_way[0]:
            (do_next, command_output) = env.do_right_turn(robot_name)
            print(command_output)
            corners.append(get_current_location(env))
            # turn_index == 1
            return True
        elif "forward" == path_way[0]:
            return True

    return False


def in_new_obstacles(direction, x, y, combined_obstacles):
    """Determines if the position to be moved to is blocked using the updated obstacles

    Args:
        direction (int): the direction which the robot is facing
        x (int): The x co-ordinate of the position being moved to.
        y (int): The y co-ordinate of the position being moved to.
        combined_obstacles (list): A comnined list of maze obstacles and new obstacles
        """

    global steps

    for xcor, ycor in combined_obstacles:
        if direction == 0:
            if \
            (
                x in range(xcor, xcor + steps - 1) and \
                y + steps in range(ycor, ycor + steps - 1)
            ):
                return True
        elif direction == 1:
            if \
            (
                x + steps in range(xcor, xcor + steps - 1) and \
                y in range(ycor, ycor + steps - 1)
            ):  
                return True
        elif direction == 2:
            if \
            (
                x in range(xcor, xcor + steps - 1) and \
                y - steps in range(ycor, ycor + steps - 1)
            ):
                return True
        elif direction == 3:
            if \
            (
                x - steps in range(xcor, xcor + steps - 1) and \
                y in range(ycor, ycor + steps - 1)
            ):
                return True
    return False


def add_obstacle(env, x, y):
    """Adds a marker to avoid reaching same dead end

    Args:
        env (module): The world module used in the program
        x (int): current x co-ordinate
        y (int): current y co-ordinate

    Returns:
        None
    """
    global obstacles, new_obstacles, corners

    if ((x,y) not in obstacles) and ((x,y) not in new_obstacles):
        new_obstacles.append((x, y))
        env.show_dead_end(x, y, steps)
        corners = []

    return


def navigate(robot_name, env, mazerunner):

    global obstacles, steps, explored, new_obstacles
    
    x, y = get_current_location(env)
    direction = env.current_direction_index
    combined_obstacles = obstacles + new_obstacles

    # if y == -200:
    #     print("bottom")
    #     add_obstacle(env, x, y - steps)
    # elif y == (200 - steps):
    #     print("top")
    #     add_obstacle(env, x, y + steps)
    # elif x == -100:
    #     print("left")
    #     add_obstacle(env, x - steps, y)
    # elif x == (100 - steps):
    #     print("right")
    #     add_obstacle(env, x + steps, y)

    if not do_turn(robot_name, env, direction, x, y, combined_obstacles):
        (do_next, command_output) = env.do_left_turn(robot_name)
        print(command_output)
        env.show_position(robot_name)
        (do_next, command_output) = env.do_left_turn(robot_name)
        print(command_output)
        env.show_position(robot_name)

    (is_loop, segment) = check_is_loop(robot_name, env, direction)
    
    do_forward(robot_name, env)

    if is_loop:
        print("found a loop")
        # print(explored)
        reversed_explored = explored[::-1]
        loop_point = reversed_explored[0]
        indexes = list(
            filter(
                lambda i:
                reversed_explored[i] == loop_point, range(len(reversed_explored))
            )
        )

        if len(indexes) > 1:
            segment = reversed_explored[indexes[0]:indexes[1]]
            segments = [reversed_explored[i:i + (len(segment))] for i in range(len(reversed_explored))]
            segment_count = 0
            for sub_segment in segments:
                if sub_segment == segment:
                    segment_count += 1
            
            if segment_count > 1:
                mid_segment = (len(segment) // 2)
                loop_x = segment[mid_segment][0]
                loop_y = segment[mid_segment][1]
                add_obstacle(env, loop_x, loop_y)

            # explored = []

    if reduce_path(direction, x, y, combined_obstacles):
        add_obstacle(env, x, y)
    
    new_direction = env.current_direction_index
    combined_obstacles = obstacles + new_obstacles
    
    if is_dead_end(env, new_direction, x, y, combined_obstacles):
        add_obstacle(env, x, y)
    
    x,y = get_current_location(env)

    if y == -200:
        print("bottom")
        if ((x,y) not in obstacles) and ((x,y) not in new_obstacles):
            obstacles.append((x, y - steps))
            env.show_dead_end(x, y - steps, steps)
            corners = []
    
    if y == (200 - steps):
        print("top")
        if ((x,y) not in obstacles) and ((x,y) not in new_obstacles):
            obstacles.append((x, y + steps))
            env.show_dead_end(x, y + steps, steps)
            corners = []
    
    if x == -100:
        print("left")
        if ((x,y) not in obstacles) and ((x,y) not in new_obstacles):
            obstacles.append((x - steps, y))
            env.show_dead_end(x - steps, y, steps)
            corners = []
    
    if x == (100 - steps):
        print("right")
        if ((x,y) not in obstacles) and ((x,y) not in new_obstacles):
            obstacles.append((x + steps, y))
            env.show_dead_end(x + steps, y, steps)
            corners = []

    # if explored_all_turns(direction, x, y, combined_obstacles):
    #         add_obstacle(env, x, y)


def get_end_point(edge, env):
    """Mark stopping location for mazerunner

    Args:
        edge (string): the edge the robot should travel to
        env (module): The world module used in the program

    Returns:
        (range): location to stop mazerunner
    """
    global steps

    if edge == 'top' or edge == '':
        return range(env.max_y - steps, env.max_y)

    if edge == 'bottom':
        return range(env.min_y, env.min_y + steps)

    if edge == 'left':
        return range(env.min_x, env.min_x + steps)

    if edge == 'right':
        return range(env.max_x - steps, env.max_x)


def get_current_location(env):
    """Retrieves the current position of the robot

    Args:
        env (module): The world module used in the program

    Returns:
        tuple: x and y coordinate
    """
    return env.position_x, env.position_y


def do_mazerun(robot_name, edge, env):
    """Initializes variables for thr robot to automatically solve maze

    Args:
        robot_name (str): name given to the robot
        edge (string): the edge the robot should travel to
        env (module): The world module used in the program
    """

    global obstacles, steps, corners, turn_index, explored, new_obstacles

    print(f"> {robot_name} starting maze run..")

    maze = env.obstacles
    explored = []
    new_obstacles = []
    obstacles = maze.get_obstacles()

    mazerunner = env.i_robot
    mazerunner.clear()
    mazerunner.speed(0)

    env.new_wall.clear()

    x, y = get_current_location(env)

    if (x, y) == (0, 0):
        steps = env.get_steps()
        mazerunner.up()
        mazerunner.goto(x + (env.get_steps() / 2), (x + env.get_steps() / 2))
        mazerunner.down()

    finish = get_end_point(edge, env)

    if edge == '' or edge == 'top' or edge == 'bottom':
        print(finish)
        while env.position_y not in finish:
            navigate(robot_name, env, mazerunner)
    else:
        print(finish)
        while env.position_x not in finish:
            navigate(robot_name, env, mazerunner)

    return True, robot_name