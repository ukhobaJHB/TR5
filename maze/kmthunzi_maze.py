import turtle
import random
#######################################################
    
total_obs = []
mazes = ['']
chars = 'x '
maze2 = []


w = turtle.Screen()
w.bgcolor('grey')
w.title("THE A-MAZE-ING MAZE")
w.setup(700,700)

t = turtle.Turtle()
t.pencolor('white')
t.color('red')
t.fillcolor('black')
t.penup()
t.speed(8)



maze1= [
'x xxxxxx       xxxxxxxx x',
'x xxxx         xxxxxx    ',
'  x  x  xxxxxxx   x xx  x',
'x x x   xx  xx x       xx',
'x   xx xxx  xx  xxxxxx   ',
'xxx        xx   xxxx  xxx',
'x     xxxx  x  xxxx   xxx',
'xxxx    xx x      x     x',
'x  x x  xx x   xxx  xxxx ',
'   x  x      xxx      xxx',
'x  x  xx    xxx  x  xx  x',
'x  xx  xx   xxxxxx  xxx x',
'xxx    xxx xxxx   xx     ',
'x x x   xx  xx   x xxx xx',    
'x      xxx   x  xxxx  x  ',
'x xx  xxxx  x   xxxx    x',
'x  x x  xx     xxx   xxxx',
'   xxx  xx     xx x   xxx',
'x  x  x   xx  xx   xxxxx ',
'xxxx    xxx   x     x   x',
'x    xxxx     x  xxx   xx',
'x  xxxx           xxxx  x',
'   xxxx           xxxx   ',
'x   xxxxx     x  xxxxx  x',
'x   xx  x       xxxx x  x',
'x   xxx   xxx           x',
'x x  x  xxxxxx    x xx  x',
'x x x   xx  xxx        xx',
'xxx        xx   xxxxxx   ',
'x     xxxx      xxxx   xx',
'x  x x  xx x  xxxxx  xxxx',
'  xx    x xxxx      x    ',
'x  x  x      xxx   x   xx',
'x  x  xx   xxx  x  xx   x',
'x   x  xx   xxxxx   xxx  ',
'x x x  xxx   xx   x  x xx',
'  x    xxx  x   xxx  xxx ',
'x xxxx xxx  xx  xxx x   x',
'x      xxx   x   x      x',
'x  x x  xx   x   xx  xxxx',
'xxx    xxx  xxxx x       ',
'x   xx  x   xx xxxxx   xx',
'           x    xx     xx',
'xxxxxxxx   xx  xxxx   xxx',
'          xxx    xx     x',
'x  x  x        xx   xxxxx',
'x     xxxx  x  xxxxx     ',
'   xxxx   x           xxx',
'xx         x    xx     xx',
'x  xxxxx xxxxxxxxxx    xx'
]

maze2 = [
'xxxxxxxxxxxx  xxxxxxxxxxx',
'x xx   xx        xx  xx x',
'        x        x       ',
'   x                 x   ',
'xxxxxxx  xxxxxxxx  xxxxxx',
'x                       x',
'xxxxxxxxxxx    xxxxxxxxxx',
'x                       x',
'x                       x',
'xxxxxxx  xxxxxxxx  xxxxxx',
'x           xx          x',
'x                       x',
'xxxxxxxxxxx    xxxxxxxxxx',
'x                       x',
'xxxxxxxxxxxx  xxxxxxxxxxx',
'x xx  xx         xx  xx x',
'x                       x',
'xxxxxx  xxxxxxxxx  xxxxxx',
'x                       x',
'x                       x',
'xxxxxxx  xxxxxxxx  xxxxxx',
'x                       x',
'xxxxxxxxxxx    xxxxxxxxxx',
'x                       x',
'x                       x',
'xxxxxxx  xxxxxxxx  xxxxxx',
'x           xx          x',
'x                       x',
'x xxxxxxxxx    xxxxxxxx x',
'x                       x',
'x xxxxxxxxxx  xxxxxxxxx x',
'x xx  xx         xx  xx x',
'x                       x',
'xxxxxx  xxxxxxxxx  xxxxxx',
'x                       x',
'xxxxxxx  xxxxxxxx  xxxxxx',
'x                       x',
'x                       x',
'xxxxxxxxxxx    xxxxxxxxxx',
'x                       x',
'x xxxxxxxxxx  xxxxxxxxx x',
'x xx  xx         xx  xx x',
'x                       x',
'xxxxxx  xxxxxxxxx  xxxxxx',
'x                       x',
'xxx xxxxxxx    xxxxxx xxx',
'    x               x    ',
'        x        x       ',
'x xx   xxx      xxx  xx x',
'xxxxxxxxxxxx  xxxxxxxxxxx',

]

maze3 =[

'x xxxxxxxxxxxxxxxxxxxxx x',
'x                       x',
'xxxxxx  xxxxxxxxx  xxxxxx',
'x                       x',
'x                       x',
'xxxxxxx  xxxxxxxx  xxxxxx',
'x                       x',
'xxxxxxxxxxx    xxxxxxxxxx',
'x                       x',
'x                       x',
'xxxxxxx  xxxxxxxx  xxxxxx',
'x    x   x  xx  x     x x',
'   x                x   x',
'xxxxxxxxxxx    xxxxxxxxxx',
'x                       x',
'x xxxxxxxxxx   xxxxxxxx x',
'x  xx        x     xx  x',
'x  xx  xx   xxx     xxx x',
'x x    xxx xxxxx xxx    x',
'x x x   xx  xxx  xx   x x',    
'       xxx   x  xxxx     ',
'x xx  xxxx      xxxx   xx',
'x  x x  xx     xxx   xxxx',
'x  xxx  xx     xx x   xxx',
'   x  x   xx  xx   xxxxx ',
'xxxx    xxx   x     x   x',
'x    xxxx     x  xxx   xx',
'x  xxxx           xxxx   ',
'x xxxxxxxxx    xxxxxxxxxx',
'x                       x',
'x xxxxxxxxxx  xxxxxxxxx x',
'x xx   xx        xx  xx x',
'x                       x',
'xxx xx  xxxxxxxxx  xxxxxx',
'x                        ',
'xxxxxxx  xxxxxxxx  xxxxxx',
'x           xx          x',
'xxx    xxx  xxxx x       ',
'x   xx  x   xx xxxxx   xx',
'           x    xx     xx',
'xxxxxxxx   xx  xxxx   xxx',
'          xxx    xx     x',
'x  x  x   xx   xx   xxxxx',
'x     xxxx  x  xxxxx     ',
'   xxxx   x           xxx',
'xx         x    xx     xx',
'x                       x',
'x xxxxxxxxxx  xxxxxxxxx x',
'x xx   xx        xx  xx x',
'x xxxxxxxxxxxxxxxxxxxxx x',
]

maze4 = [
'xx xx xx xx x xx xx xx xx',
'x                        ',
'xxxxxxx xxxxxxxxxx xxxxxx',
'x                       x',
'x   x     x   xxxxxxx   x',  
'x   x     x      x      x',
'x   xxxxxxx      x      x',
'x   x     x      x      x',
'x   x     x   xxxxxxx   x',
'x                       x',
'xxxxx x x xxxxxxxxxxxxxxx',
'xx      x       xx    x  ',
'x  x  x     x           x',
'xxxxxxxxxxxxxxxxx xx xxxx',
'x                       x',
'x  xxxxxxxxxxxxxxxxxxx  x',
'x  x                 x  x',
'x    xxxxxxxxxxxxxxx    x',
'x    xx    xxx    xx    x',
'x       x       x       x',
'xxxxxxxxx       xxxxxxxxx',
'x                       x',
'x      xxx     xxx      x',
'   xxxxx         xxxxx  ',
'x      x         x      x',
'x      xxx     xxx      x',
'x                       x',
'xxxxxxxxxxx    xxxxxxxxxx',
'x                       x',
'xxxxxxx  xxxxxxxx  xxxxxx',
'x    x   x  xx  x     x x',
'   x                x   x',
'xxxxxxxxxxx    xxxxxxxxxx',
'x                       x',
'x xx x     x  x      xx x',
'x x  xxxxxxx  xxxxxxxx  x',
'x xx  xx         xx  xx x',
'x           xx          x',
'xxxxxx  xxxxxxxxx  xxxxxx',
'x  xx        x     xx   x',
'x  xx  xx   xxx     xxx x',
'x x    xxx xxxxx xxx    x',
'x                       x',
'x  xxxx  xx    x  xxx   x',
'x  x     x x   x  x  x  x',
'x  xxxx  x  x  x  x   x x',
'x  x     x   x x  x  x  x',
'x  xxxx  x    xx  xxx   x',
'x                       x',
'xxxxxxxxxx xxxxxxxx xxxxx',
]
mazes.append(maze1)
mazes.append(maze2)
mazes.append(maze3)
mazes.append(maze4)


def draw_border():
    t.goto(-100,200)
    t.pendown()
    for i in range(2):
        t.forward(200)
        t.right(90)
        t.forward(400)
        t.right(90)
    t.penup()


def create_maze():
    global maze

    chosen = mazes[random.randint(1,len(mazes)-1)]
    p = turtle.Turtle()
    p.shape('square')
    p.color('white')
    p.shapesize(0.33)
    p.penup()
    p.speed(10)
    for y in range(len(chosen)):
        
        for x in range(len(chosen[y])):
            x_cor = -100 + (x * 8)
            y_cor = 200 - (y * 8)
            if chosen[y][x] == 'x' and ((x_cor > 20 or x_cor < -20) or (y_cor > 20 or y_cor < -20)):
                total_obs.append((x_cor, y_cor, x_cor+8, y_cor+8))
                p.goto(x_cor+3, y_cor-3)
                p.stamp()


def check_obstacles(x, y, current_direction_index):
    '''
    checks if the robot will encounter a wall block(object) in the path between
    the starting coordinates and the new coordinates in accordance to the direction
    index.

    param:  x, y cordinates (new coordinates)
            current_direction_index
    
    return: True   (if obstacles are not in the way.)
            False  (if obstacle is encountered anywhere between the start 
                    point and the end point.)
    '''
    
    global total_obs
    
    for i in total_obs:

        if current_direction_index == 0 or current_direction_index == 2:
            if (x >= i[0] and x <= i[2]) and (y >= i[1] and y <= i[3]):
                return False

        elif current_direction_index == 1 or current_direction_index == 3:
            if (y >= i[1] and y <= i[3]) and (x >= i[0] and x <= i[2]):
                return False
         
    return True


def get_obstacles():

    global total_obs

    return total_obs


t.hideturtle()
draw_border()
create_maze()

