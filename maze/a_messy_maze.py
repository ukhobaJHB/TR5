import random

obstacles = []

def get_obstacles():
    global obstacles
    return obstacles

def create_random_obstacles():
    """Function to return list of obstacle starting point"""
    global obstacles
    maze_additions = []
    type_list = ['top','bottom']
    direction_list = ['right','left']
    
    number_of_obstacles = 250
    for number in range(number_of_obstacles):
        x_cord, y_cord = random.randrange(-90, 90, 5), random.randrange(-190, 190, 5)
        if (x_cord in range(-5,5) or y_cord in range(-5,5)):
            pass
        else:  
            obstacles.append((x_cord,y_cord))

    for obstacle in obstacles:
        typa = random.choice(type_list)
        direct = random.choice(direction_list)
        if direct == 'right':
            maze_additions.append((obstacle[0] + 4, obstacle[1]))  
            maze_additions.append((obstacle[0] + 8, obstacle[1]))
            #maze_additions.append((obstacle[0] + 16, obstacle[1]))
        else:
            maze_additions.append((obstacle[0] - 4, obstacle[1]))  
            maze_additions.append((obstacle[0] - 8, obstacle[1]))
            #maze_additions.append((obstacle[0] - 16, obstacle[1]))  
        if typa == 'top':
            maze_additions.append((obstacle[0], obstacle[1]+4))  
            maze_additions.append((obstacle[0], obstacle[1]+8))
            #maze_additions.append((obstacle[0], obstacle[1]+16))
        else:
            maze_additions.append((obstacle[0], obstacle[1]-4))  
            maze_additions.append((obstacle[0], obstacle[1]-8))
            #maze_additions.append((obstacle[0], obstacle[1]-16))

    for item in maze_additions:
        obstacles.append(item)

    return obstacles

def is_position_blocked(x, y):
    """Function to return true if position is blocked"""

    global obstacles
    counter = 0
    return_statement = False
    while counter < len(obstacles):
        item_f = obstacles[counter]
        if x in range(item_f[0], item_f[0]+5) and y in range(item_f[1],item_f[1]+5):
            return_statement = True
            break
        else:
            counter += 1      
    return return_statement

def is_path_blocked(x1,y1, x2, y2):
    """Function to check whether the path is blocked"""
    global obstacles

    return_statement = False
    obstacles = obstacles
    for obstacle in obstacles:
	    if y1 == y2:
		    for number in range(x1,x2+1):
			    if (number == obstacle[0] or number == obstacle[0]+4) and y1 in range(obstacle[1],obstacle[1]+4):
				    return_statement = True
	    elif x1 == x2:
		    for number in range(y1,y2+1):
			    if (number == obstacle[1] or number == obstacle[1]+4) and x1 in range(obstacle[0],obstacle[0]+4):
				    return_statement = True
    return return_statement