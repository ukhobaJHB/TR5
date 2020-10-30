import random

#hold the obstacles locations
obstacles = []


def is_position_blocked(x, y):
    """
    Check if the robot has landed on an obsacle
    """
    for item in obstacles:
        if (item[0] <= x <= (item[0] + 9)) and (item[1] <= y <= (item[1] + 9)):
            return (True)
    return(False)


def is_path_blocked(x1, y1, x2, y2):
    """
    Check if the robot will pass over an obsacle
    """
    if x1 == x2:
        start = y1
        end = y2
        other = x1
        index_1 = 1
        index_2 = 0
    else:
        start = x1
        end = x2
        other = y1
        index_1 = 0
        index_2 = 1

    for item in obstacles:
        for i in range(10):
            if (start <= (item[index_1] + i) <= end) and (item[index_2] <= other <= item[index_2] + 9):
                return(True)
            elif (start >= (item[index_1] + i) >= end) and (item[index_2] >= other >= item[index_2] + 9):
                return(True)
            elif (start <= (item[index_1] + i) <= end) and (item[index_2] >= other >= item[index_2] + 9):
                return(True)
            elif (start >= (item[index_1] + i) >= end) and (item[index_2] <= other <= item[index_2] + 9):
                return(True)
    return(False)


def create_random_obstacles():
    """
    Generate the obstacle locations
    """
    global obstacles
    obstacles = [(-100,190),(-90,190),(-80,190),(-70,190),(-60,190),
                     (-50,190),(-40,190),(-30,190),(-20,190),(-10,190),
                     (10,190),(20,190),(30,190),(40,190),(50,190),(60,190),
                     (70,190),(80,190),(90,190),

                     (-100,180), (-90,180), (10,180), (20,180), (90,180),

                     (-100,170), (-90,170), (-70,170), (-50,170), 
                     (-40,170), (-30,170), (-20,170), (-10,170), (30,170), 
                     (40,170), (50,170), (60,170), (70,170), (90,170),

                     (-100,160), (-90,160), (-70,160), (-50,160), 
                     (-40,160), (-30, 160), (-20,160), (-10,160), (0,160), 
                     (10,160), (70,160), (90,160),

                     (-100,150), (-50,150), (10,150), (20,150), (30,150), 
                     (40,150), (50,150), (70,150), (90,150),
                     
                     (-100,140), (-90,140), (-80,140), (-70,140), (-60,140), 
                     (-50,140), (-30,140), (-20,140), (-10,140), (10,140), 
                     (50,140), (90,140),

                     (-100,130), (-70,130), (-30,130), (-20,130), (-10,130), 
                     (10,130), (20,130), (40,130), (50,130), (70,130), (80,130), 
                     (90,130),

                     (-100,120), (-80,120), (-70,120), (-50,120), (-40,120), 
                     (-30,120), (-20,120), (-10,120), (70,120), (80,120), 
                     (90,120),

                     (-100,110), (-10,110), (0,110), (10,110), (20,110), 
                     (30,110), (40,110), (50,110), (60,110), (70,110), (80,110), 
                     (90,110),

                     (-100,100), (-90,100), (-80,100), (-70,100), (-60,100), 
                     (-50,100), (-40,100), (-30,100), (40,100), (50,100), 
                     (90,100),

                     (-100,90), (-80, 90), (-10, 90), (0, 90), (20, 90), 
                     (40, 90), (50, 90), (70, 90), (80, 90), (90, 90),
                     (-100,80), (-80,80), (-60,80), (-50,80), (-40,80), 
                     (-30,80), (-20,80), (-10,80), (20,80), (80,80), (90,80),
                     (-100,70), (-80,70), (-10,70), (0,70), (10,70), (20,70), 
                     (30,70), (40,70), (50,70), (60,70), (70,70), (80,70), 
                     (90,70),
                     (-100,60), (-80,60), (-70,60), (-60,60), (-50,60), 
                     (-40,60), (-30,60), (40,60), (90,60),
                     (-100,50), (-60,50), (-40,50), (-30,50), (-20,50), 
                     (-10,50), (0,50), (10,50), (20,50), (40,50), (60,50), 
                     (70,50), (90,50),
                     (-100,40), (-80,40), (-60,40), (-10,40), (40,40), (80,40), 
                     (90,40),
                     (-100,30), (-80,30), (-30,30), (-20,30), (-10,30), (10,30), 
                     (20,30), (30,30), (40,30), (60,30), (80,30), (90,30),
                     (-100,20), (-80,20), (-70,20), (-50,20), (-30,20), 
                     (-20,20), (-10,20), (60,20), (70,20), (80,20), (90,20),
                     (-100,10), (-80,10), (-70,10), (-50,10), (-30,10), 
                     (-20,10), (20,10), (30,10), (40,10), (80,10), (90,10),
                     (-80,0), (-50,0), (40,0), (50,0), (60,0),
                     (-100,-10), (-90,-10), (-80,-10), (-70,-10), (-50,-10), 
                     (-40,-10), (-30,-10), (-20,-10), (20,-10), (40,-10), 
                     (50,-10), (60,-10), (80,-10), (90,-10),
                     (-100,-20), (-90,-20), (10,-20), (20,-20), (40,-20), 
                     (50,-20), (60,-20), (80,-20), (90,-20),
                     (-100,-30), (-90,-30), (-70,-30), (-60,-30), (-50,-30), 
                     (-40,-30), (-30,-30), (-20,-30), (-10,-30), (10,-30), 
                     (20,-30), (60,-30), (80,-30), (90,-30),
                     (-100,-40), (10,-40), (20,-40), (30,-40), (40,-40), 
                     (60,-40), (80,-40), (90,-40),
                     (-100,-50), (-80,-50), (-70,-50), (-60,-50), (-50,-50), 
                     (-40,-50), (-30,-50), (-20,-50), (-10,-50), (10,-50), 
                     (20,-50), (60,-50), (80,-50), (90,-50),
                     (-100,-60), (-80,-60), (-70,-60), (-10,-60), (10,-60), 
                     (20,-60), (40,-60), (50,-60), (60,-60), (80,-60), (90,-60),
                     (-100,-70), (-50,-70), (-30,-70), (-10,-70), (10,-70), 
                     (20,-70), (80,-70), (90,-70),
                     (-100,-80), (-90,-80), (-80,-80), (-70,-80), (-60,-80), 
                     (-50,-80), (-30,-80), (-10,-80), (30,-80), (40,-80), 
                     (50,-80), (60,-80), (70,-80), (80,-80), (90,-80),
                     (-100,-90), (-30,-90), (-10,-90), (0,-90), (10,-90), 
                     (20,-90), (90,-90),
                     (-100,-100), (-90, -100), (-80, -100), (-70, -100), 
                     (-60, -100), (-50, -100), (-40, -100), (-30, -100), 
                     (-10, -100), (0, -100), (10, -100), (20, -100), (40, -100), 
                     (50, -100), (70, -100), (90, -100),
                     (-100,-110), (-40,-110), (-30,-110), (40,-110), (50,-110), 
                     (70,-110), (90,-110),
                     (-100,-120), (-80,-120), (-60,-120), (-40,-120), 
                     (-30,-120), (-20,-120), (-10,-120), (0,-120), (10,-120), 
                     (20,-120), (30,-120), (40,-120), (50,-120), (70,-120), 
                     (90,-120),
                     (-100,-130), (-80,-130), (-60,-130), (-40,-130), 
                     (-30,-130), (-20,-130), (-10,-130), (70,-130), (90,-130),
                     (-100,-140), (-80,-140), (-60,-140), (-10,-140), (10,-140), 
                     (20,-140), (30,-140), (40,-140), (50,-140), (60,-140), 
                     (70,-140), (90,-140),
                     (-100,-150), (-80,-150), (-60,-150), (-40,-150), 
                     (-30,-150), (-20,-150), (-10,-150), (10,-150), (90,-150),
                     (-100,-160), (-80,-160), (-60,-160), (30,-160), (40,-160), 
                     (50,-160), (70,-160), (80,-160), (90,-160),
                     (-100,-170), (-80,-170), (-70,-170), (-60,-170), 
                     (-50,-170), (-40,-170), (-30,-170), (-20,-170), (-10,-170), 
                     (0,-170), (10,-170), (30,-170), (40,-170), (50,-170), 
                     (70,-170), (80,-170), (90,-170),
                     (-100,-180), (10,-180), (30,-180), (70,-180), (80,-180), 
                     (90,-180),
                     (-100,-190), (-90,-190), (-80,-190), (-70,-190), 
                     (-60,-190), (-50,-190), (-40,-190), (-30,-190), (-20,-190), 
                     (-10,-190), (10,-190), (30,-190), (40,-190), (50,-190), 
                     (60,-190), (70,-190), (80,-190), (90,-190),
                     (-100,-200), (-90,-200), (-80,-200), (-70,-200), 
                     (-60,-200), (-50,-200), (-40,-200), (-30,-200), (-20,-200), 
                     (-10,-200), (10,-200), (20,-200), (30,-200), (40,-200), 
                     (50,-200), (60,-200), (70,-200), (80,-200), (90,-200)
                     ]

    # obstacles = [(random.randint(-100, 100), random.randint(-200, 200)) for x in range(random.randint(1, 10))]
     
    return(obstacles)


def get_obstacles():

    global obstacles

    return obstacles