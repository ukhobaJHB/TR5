import random

obstacles = []


def get_obstacles():

    global obstacles

    return obstacles


def is_position_blocked(x: int, y: int):
    """Determines if the position to be moved to is blocked

    Args:
        x (int): The x co-ordinate of the position being moved to.
        y (int): The y co-ordinate of the position being moved to.
    """

    for obstacle in get_obstacles():
        if x in range(obstacle[0], obstacle[0] + 19) and y in range(obstacle[1], obstacle[1] + 19): return True
    return False


def is_path_blocked(x1: int, y1: int, x2: int, y2: int):
    """Determines if the path you're taking has an obstacle.

    Args:
        x1 (int): The x co-ordinate of the current position.
        y1 (int): The y co-ordinate of the current position.
        x2 (int): The x co-ordinate of the position being moved to.
        y2 (int): The y co-ordinate of the position being moved to.
        """

    for obstacle in get_obstacles():
        if x1 == x2 and x1 in range(obstacle[0], obstacle[0] + 20):
            for i in (range(y1, y2 + 1) or range(y2, y1 + 1)):
                if i in range(obstacle[1], obstacle[1] + 20):
                    return True
        elif y1 == y2 and (y1 in range(obstacle[1], obstacle[1] + 20)):
            for i in (range(x1, x2 + 1) or range(x2, x1 + 1)):
                if i in range(obstacle[0], obstacle[0] + 20):
                    return True
    return False


def in_obstacles(x, y):

    global obstacles

    return (x, y) in obstacles


def add_wall(x, y):

    walls = 0

    if  in_obstacles(x + 20, y + 20):
        walls += 1

    if in_obstacles(x + 20, y):
        walls += 1

    if in_obstacles(x + 20, y - 20):
        walls += 1

    if in_obstacles(x, y + 20):
        walls += 1

    if in_obstacles(x, y - 20):
        walls += 1

    if in_obstacles(x - 20, y + 20):
        walls += 1

    if in_obstacles(x - 20, y):
        walls += 1

    if in_obstacles(x - 20, y - 20):
        walls += 1

    if walls == 5:
        if not in_obstacles(x, y + 20) and not in_obstacles(x + 20, y + 20) and not in_obstacles(x + 20, y) and x != -90:
            return True, True

        if not in_obstacles(x, y + 20) and not in_obstacles(x + 20, y + 20) and not in_obstacles(x + 20, y):
            return False, False

    if walls == 4:
        if not in_obstacles(x - 20, y - 20) and not in_obstacles(x - 80, y - 20) and in_obstacles(x - 20, y):
            return True, False

    if walls == 3:
        if in_obstacles(x - 20, y) and in_obstacles(x + 20, y) and in_obstacles(x + 20, y - 20):
            return True, True

        if not in_obstacles(x, y - 20) and not in_obstacles(x, y - 40) and not in_obstacles(x, y - 60) and y != -190:
            return True, False

        if in_obstacles(x + 20, y - 20) and in_obstacles(x - 20, y - 20) and in_obstacles(x - 20, y + 20) and y == -190:
            return False, False

        if in_obstacles(x - 20, y - 20) and in_obstacles(x, y - 20) and in_obstacles(x + 20, y - 20) and not in_obstacles(x - 20, y):
            return True, False
    
        if in_obstacles(x - 20, y - 20) and in_obstacles(x - 20, y) and in_obstacles(x - 20, y + 20):
            return True, True

        if in_obstacles(x - 20, y - 20) and in_obstacles(x, y - 20) and in_obstacles(x + 20, y - 20):
            return True, True

        if in_obstacles(x - 20, y + 20) and in_obstacles(x, y + 20) and in_obstacles(x + 20, y + 20):
            return True, False

        if in_obstacles(x + 20, y + 20) and in_obstacles(x + 20, y) and in_obstacles(x + 20, y - 20):
            return True, False

    if walls == 2:
        if in_obstacles(x - 20, y - 20) and in_obstacles(x - 40, y) and in_obstacles(x - 20, y) and y == -190:
            return False, False

        if in_obstacles(x + 20, y - 20) and in_obstacles(x - 20, y - 20) and y == -190:
            return False, False

        if in_obstacles(x - 20, y - 20) and in_obstacles(x - 40, y) and in_obstacles(x - 20, y):
            return True, False

        if in_obstacles(x - 20, y - 20) and not in_obstacles(x - 40, y) and in_obstacles(x - 20, y):
            return True, True

        if in_obstacles(x, y - 20) and in_obstacles(x - 20, y):
            return True, False

        if in_obstacles(x - 40, y) and in_obstacles(x - 20, y):
            return True, True

        # if in_obstacles(x - 10, y - 10) and in_obstacles(x - 20, y) and in_obstacles(x - 10, y):
        #     return True, False

        if in_obstacles(x - 20, y - 20) and in_obstacles(x - 40, y - 20) and in_obstacles(x - 20, y - 20):
            return True, True

        if in_obstacles(x, y - 20) and in_obstacles(x - 20, y - 20):
            return True, True

    if walls == 1:
        if in_obstacles(x - 40, y) and in_obstacles(x - 20, y + 20) and in_obstacles(x - 40, y + 20):
            return True, False

        if in_obstacles(x - 20, y) and (not in_obstacles(x - 40, y) or not in_obstacles(x - 20, y - 40)):
            return True, False

        if not in_obstacles(x - 40, y) and in_obstacles(x - 20, y + 20):
            return True, False

        if in_obstacles(x - 20, y + 20) and in_obstacles(x - 40, y):
            return True, True

        if in_obstacles(x - 20, y + 20) or in_obstacles(x, y - 20):
            return True, False

    if walls == 0:
        if (x - 20, y - 20) in obstacles and (x - 20, y - 20) in obstacles:
            return True, True

        return True, False

    return False, False


def create_openings(coordinates):

    global obstacles

    # top_opening = random.randrange(-80, 60, 20)
    # left_opening = random.randrange(-200, 160, 20)
    # bottom_opening = random.randrange(-80, 60, 20)
    # right_opening = random.randrange(-180, 160, 20)
    top_opening = [random.randrange(-80, 60, 20) for i in range(random.randint(1,3))]
    left_opening = [random.randrange(-200, 160, 20) for i in range(random.randint(1,3))]
    bottom_opening = [random.randrange(-80, 60, 20) for i in range(random.randint(1,3))]
    right_opening = [random.randrange(-180, 160, 20) for i in range(random.randint(1,3))]

    for x, y in coordinates:
        if x == -100 and not y in left_opening:
            obstacles.append((x, y))

        if y == 180 and not x in top_opening:
            obstacles.append((x, y))
        
        if y == -200 and not x in bottom_opening:
            obstacles.append((x, y))
        
        if x == 80 and not y in right_opening:
            obstacles.append((x, y))


def create_random_obstacles():
    """Creates a list of obstacles"""

    global obstacles

    print('Creating new obstacles')

    coordinates = [(x, y) for x in range(-100, 91, 20) for y in range(-200, 191, 20) if not (x in range(-20, 20) and y in range(-20, 20))]

    create_openings(coordinates)

    for x, y in coordinates:

        if x in range(-90, 80) and y in range(-190, 180):
            is_wall = add_wall(x, y)
            if is_wall == (True, True):
                if random.randint(0, 2) == 1:
                    obstacles.append((x, y))
            elif is_wall == (True, False):
                obstacles.append((x, y))
    
    return obstacles