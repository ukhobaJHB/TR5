import random

obstacles = []

def create_random_obstacles():
    """Creates a list of obstacles"""

    global obstacles

    print('Creating new obstacles')
    obstacles = [(random.randint(-100, 100), random.randint(-200, 200)) for obstacle in range(random.randint(1, 10))]

    return obstacles


def is_position_blocked(x: int, y: int):
    """Determines if the position to be moved to is blocked

    Args:
        x (int): The x co-ordinate of the position being moved to.
        y (int): The y co-ordinate of the position being moved to.
    """

    for obstacle in get_obstacles():
        if x in range(obstacle[0], obstacle[0] + 4) and y in range(obstacle[1], obstacle[1] + 4): return True
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
        if x1 == x2 and x1 in range(obstacle[0], obstacle[0] + 5):
            for i in (range(y1, y2 + 1) or range(y2, y1 + 1)):
                if i in range(obstacle[1], obstacle[1] + 5):
                    return True
        elif y1 == y2 and (y1 in range(obstacle[1], obstacle[1] + 5)):
            for i in (range(x1, x2 + 1) or range(x2, x1 + 1)):
                if i in range(obstacle[0], obstacle[0] + 5):
                    return True
    return False

def get_obstacles():

    global obstacles

    return obstacles