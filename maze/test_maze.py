import unittest
from unittest.mock import patch
import naddis_maze as obstacles
import random


class ObstaclesTestCases(unittest.TestCase):

    def test_get_obstacles_is_tuples(self):
        for i in range(50):
            self.assertTrue(all(isinstance(obstacle, tuple) for obstacle in obstacles.get_obstacles()))

    
    # def test_get_obstacles_greater_than_0(self):
    #     for i in range(50):
    #         obstacles.random.randint = lambda a, b: random.randrange(1, 10, 1)
    #         obstacle_list = obstacles.create_random_obstacles()
    #         self.assertTrue(len(obstacle_list) >= 1, f'{obstacle_list}')
    
    
    def test_is_position_blocked_false(self):
        obstacles.obstacles = [(-100, 99)]
        self.assertFalse(obstacles.is_position_blocked(0, 22))
    
    
    def test_is_position_blocked_true(self):
        obstacles.obstacles = [(-2, 19)]
        self.assertTrue(obstacles.is_position_blocked(0, 22))
    

    def test_is_path_blocked_false(self):
        obstacles.obstacles = [(-100, 99)]
        self.assertFalse(obstacles.is_path_blocked(-100, 22, -100, 57))
    
    
    def test_is_position_path_true(self):
        obstacles.obstacles = [(-2, 19)]
        self.assertTrue(obstacles.is_path_blocked(0, -50, 0, 100))

if __name__ == "__main__":
    unittest.main()