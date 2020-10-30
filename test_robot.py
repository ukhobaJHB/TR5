import unittest
from unittest.mock import patch
from io import StringIO
import robot
import sys
import world.obstacles as obstacles


class MyTestCases(unittest.TestCase):

    # TR 2 Test Cases
    @patch('sys.stdin', StringIO('\n \n123\njump of a bridge :D\noFf\noff\nOFF\nhelp\n'))
    def test_get_user_command_to_lower(self):
        self.assertEqual(robot.get_command('ath'), 'off')
        self.assertEqual(robot.get_command('ath'), 'off')
        self.assertEqual(robot.get_command('ath'), 'off')
        self.assertEqual(robot.get_command('ath'), 'help')


    def test_help_doc(self):
        self.assertEqual(robot.do_help(), (True, "I can understand these commands:\nOFF  - Shut down robot\nHELP - provide information about commands\nFORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'\nBACK - move backward by specified number of steps, e.g. 'BACK 10'\nRIGHT - turn right by 90 degrees\nLEFT - turn left by 90 degrees\nSPRINT - sprint forward according to a formula\nREPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]\n"))


    def test_move_forward(self):
        
        for i in range(1, 20, 3):
            self.assertEqual(robot.call_command('forward', str(i), 'ath'), (True, ' > ath moved forward by '+str(i)+' steps.'))


    @patch('sys.stdin', StringIO('ath\nForWArd 10\nForWArd 11\nForWArd 1\noff\n'))
    def test_move_forward_forward_forward(self):

        # with patch("sys.stdout", new = StringIO()) as out:
        sys.stdout = StringIO()
        robot.robot_start()
        output = sys.stdout.getvalue().strip()
        self.assertIn(' > ath moved forward by 10 steps.', output)
        self.assertIn(' > ath now at position (0,10).', output)
        self.assertIn(' > ath moved forward by 11 steps.', output)
        self.assertIn(' > ath now at position (0,21).', output)
        self.assertIn(' > ath moved forward by 1 steps.', output)
        self.assertIn(' > ath now at position (0,22).', output)

    
    def test_move_backward(self):

        for i in range(1, 20, 3):
            self.assertEqual(robot.call_command('back', str(i), 'ath'), (True, ' > ath moved back by '+str(i)+' steps.'))


    @patch('sys.stdin', StringIO('ath\nforward 1\nforward 5\nback 10\noff\n'))
    def test_move_forward_forward_back(self):

        # with captured_output() as (out, err):
        sys.stdout = StringIO()
        robot.robot_start()
        output = sys.stdout.getvalue()
        self.assertIn(' > ath moved forward by 1 steps.', output)
        self.assertIn(' > ath now at position (0,1).',output)
        self.assertIn(' > ath moved forward by 5 steps.', output)
        self.assertIn(' > ath now at position (0,6).',output)
        self.assertIn(' > ath moved back by 10 steps.', output)
        self.assertIn(' > ath now at position (0,-4).',output)


    def test_do_right_turn(self):

        robot.world.env.current_direction_index = 0
        self.assertEqual(robot.world.env.do_right_turn('ath'), (True, ' > ath turned right.'))
        self.assertEqual(robot.world.env.directions[robot.world.env.current_direction_index], 'right')
        self.assertEqual(robot.world.env.do_right_turn('ath'), (True, ' > ath turned right.'))
        self.assertEqual(robot.world.env.directions[robot.world.env.current_direction_index], 'back')
        self.assertEqual(robot.world.env.do_right_turn('ath'), (True, ' > ath turned right.'))
        self.assertEqual(robot.world.env.directions[robot.world.env.current_direction_index], 'left')
        self.assertEqual(robot.world.env.do_right_turn('ath'), (True, ' > ath turned right.'))
        self.assertEqual(robot.world.env.directions[robot.world.env.current_direction_index], 'forward')


    def test_do_left_turn(self):

        robot.world.env.current_direction_index = 0
        self.assertEqual(robot.world.env.do_left_turn('ath'), (True, ' > ath turned left.'))
        self.assertEqual(robot.world.env.directions[robot.world.env.current_direction_index], 'left')
        self.assertEqual(robot.world.env.do_left_turn('ath'), (True, ' > ath turned left.'))
        self.assertEqual(robot.world.env.directions[robot.world.env.current_direction_index], 'back')
        self.assertEqual(robot.world.env.do_left_turn('ath'), (True, ' > ath turned left.'))
        self.assertEqual(robot.world.env.directions[robot.world.env.current_direction_index], 'right')
        self.assertEqual(robot.world.env.do_left_turn('ath'), (True, ' > ath turned left.'))
        self.assertEqual(robot.world.env.directions[robot.world.env.current_direction_index], 'forward')


    @patch('sys.stdin', StringIO('ath\nforward 100\nforward 100\nback 10\nforward 100\nforward 1\noff\n'))
    def test_move_range(self):

        sys.stdout = StringIO()
        robot.robot_start()
        
        output = sys.stdout.getvalue()
        self.assertIn(' > ath now at position (0,100).', output)
        self.assertIn(' > ath now at position (0,200).', output)
        self.assertIn(' > ath now at position (0,190).', output)
        self.assertIn('ath: Sorry, I cannot go outside my safe zone.', output)
        self.assertIn(' > ath now at position (0,191).', output)

    @patch('sys.stdin', StringIO('ath\nsprint 5\noff\n'))
    def test_sprint(self):
        robot.world.env.current_direction_index = 0

        sys.stdout = StringIO()
        robot.robot_start()
        output = sys.stdout.getvalue()
        
        self.assertIn(' > ath moved forward by 5 steps.', output)
        self.assertIn(' > ath moved forward by 4 steps.', output)
        self.assertIn(' > ath moved forward by 3 steps.', output)
        self.assertIn(' > ath moved forward by 2 steps.', output)
        self.assertIn(' > ath moved forward by 1 steps.', output)
        self.assertIn(' > ath now at position (0,15).', output)


    # TR 3 Test Cases
    def test_add_to_history(self):
        robot.history = []
        robot.add_to_history("forward 10")
        self.assertEqual(robot.history, ['forward 10'])
        robot.add_to_history("right")
        self.assertEqual(robot.history, ['forward 10', 'right'])
        robot.add_to_history("forward 10")
        self.assertEqual(robot.history, ['forward 10', 'right', 'forward 10'])
        robot.add_to_history("left")
        self.assertEqual(robot.history, ['forward 10', 'right', 'forward 10', 'left'])
        robot.add_to_history("back 15")
        self.assertEqual(robot.history, ['forward 10', 'right', 'forward 10', 'left', 'back 15'])

    
    @patch('robot.history', ['forward 10'])
    @patch('robot.world.env.position_x', 0)
    @patch('robot.world.env.position_y', 10)
    @patch('robot.world.env.current_direction_index', 0)
    def test_replay(self):

        with patch('sys.stdout', new = StringIO()) as output:

            robot.do_replay('ath', '')
            self.assertEqual(output.getvalue().strip('\n'), """ > ath moved forward by 10 steps.
 > ath now at position (0,20).""")

    
    @patch('robot.history', ['forward 10'])
    @patch('robot.world.env.position_x', 0)
    @patch('robot.world.env.position_y', 10)
    @patch('robot.world.env.current_direction_index', 0)
    def test_replay_1_command_twice(self):

        with patch('sys.stdout', new = StringIO()) as output:

            robot.do_replay('ath', '')
            self.assertEqual(output.getvalue().strip('\n'), """ > ath moved forward by 10 steps.
 > ath now at position (0,20).""")

            robot.do_replay('ath', '')
            self.assertEqual(output.getvalue().strip('\n'), """ > ath moved forward by 10 steps.
 > ath now at position (0,20).
 > ath moved forward by 10 steps.
 > ath now at position (0,30).""")

    
    @patch('robot.history', ['forward 10', 'right'])
    @patch('robot.world.env.position_x', 0)
    @patch('robot.world.env.position_y', 10)
    @patch('robot.world.env.current_direction_index', 0)
    def test_replay_2_commands_twice(self):

        with patch('sys.stdout', new = StringIO()) as output:

            robot.do_replay('ath', '')
            self.assertEqual(output.getvalue().strip('\n'), """ > ath moved forward by 10 steps.
 > ath now at position (0,20).
 > ath turned right.
 > ath now at position (0,20).""")

            robot.do_replay('ath', '')
            self.assertEqual(output.getvalue().strip('\n'), """ > ath moved forward by 10 steps.
 > ath now at position (0,20).
 > ath turned right.
 > ath now at position (0,20).
 > ath moved forward by 10 steps.
 > ath now at position (10,20).
 > ath turned right.
 > ath now at position (10,20).""")

    
    def test_valid_command_replay_silent(self):
        self.assertTrue(robot.valid_command('replay silent'))

    
    def test_valid_command_replay_silent_upper(self):
        self.assertTrue(robot.valid_command('replay SILENT'))

    
    @patch('robot.history', ['forward 10', 'right'])
    @patch('robot.world.env.position_y', 10)
    def test_replay_silent(self):

        with patch('sys.stdout', new = StringIO()) as output:

            robot.do_replay('ath', 'silent')
            self.assertEqual(output.getvalue(), "")

    
    @patch('robot.history', ['forward 10', 'right'])
    @patch('robot.world.env.position_x', 0)
    @patch('robot.world.env.position_y', 10)
    @patch('robot.world.env.current_direction_index', 1)
    def test_replay_silent_replay(self):

        with patch('sys.stdout', new = StringIO()) as output:

            robot.do_replay('ath', 'silent')
            self.assertEqual(output.getvalue().strip('\n'), "")
            robot.do_replay('ath', '')
            self.assertEqual(output.getvalue().strip('\n'), """ > ath moved forward by 10 steps.
 > ath now at position (10,0).
 > ath turned right.
 > ath now at position (10,0).""")

    
    def test_valid_command_replay_reversed(self):
        self.assertTrue(robot.valid_command('replay reversed'))

    
    def test_valid_command_replay_reversed_upper(self):
        self.assertTrue(robot.valid_command('replay REVERSED'))

    
    # @patch('robot.history', ['forward 10', 'right'])
    # @patch('robot.world.env.position_x', 0)
    # @patch('robot.world.env.position_y', 10)
    # @patch('robot.world.env.current_direction_index', 0)
    def test_replay_reversed(self):
        robot.history = ['forward 10', 'right']
        robot.world.env.position_x = 0
        robot.world.env.position_y = 10
        robot.world.env.current_direction_index = 0
        
        with patch('sys.stdout', new = StringIO()) as output:

            robot.do_replay('ath', 'reversed')
            self.assertEqual(output.getvalue().strip('\n'), """ > ath turned right.
 > ath now at position (0,10).
 > ath moved forward by 10 steps.
 > ath now at position (10,10).""")
        obstacles.obstacles = []

    
    @patch('robot.history', ['forward 10', 'right'])
    @patch('robot.world.env.position_x', 0)
    @patch('robot.world.env.position_y', 10)
    @patch('robot.world.env.current_direction_index', 0)
    def test_replay_reversed_twice(self):

        with patch('sys.stdout', new = StringIO()) as output:

            robot.do_replay('ath', 'reversed')
            self.assertEqual(output.getvalue().strip('\n'), """ > ath turned right.
 > ath now at position (0,10).
 > ath moved forward by 10 steps.
 > ath now at position (10,10).""")

            robot.do_replay('ath', 'reversed')
            self.assertEqual(output.getvalue().strip('\n'), """ > ath turned right.
 > ath now at position (0,10).
 > ath moved forward by 10 steps.
 > ath now at position (10,10).
 > ath turned right.
 > ath now at position (10,10).
 > ath moved forward by 10 steps.
 > ath now at position (10,0).""")

    
    def test_valid_command_replay_reversed_silent(self):
        self.assertTrue(robot.valid_command('replay reversed silent'))

    
    def test_valid_command_replay_reversed_silent_upper(self):
        self.assertTrue(robot.valid_command('replay REVERSED silent'))

    
    @patch('robot.history', ['forward 10', 'right'])
    @patch('robot.world.env.position_x', 0)
    @patch('robot.world.env.position_y', 10)
    @patch('robot.world.env.current_direction_index', 0)
    def test_replay_reversed_silent(self):

        with patch('sys.stdout', new = StringIO()) as output:

            robot.do_replay('ath', 'reversed silent')
            self.assertEqual(output.getvalue().strip('\n'), "")

    
    @patch('robot.history', ['forward 10', 'right'])
    @patch('robot.world.env.position_x', 0)
    @patch('robot.world.env.position_y', 10)
    @patch('robot.world.env.current_direction_index', 0)
    def test_replay_reversed_reversedsilent_reversed(self):

        with patch('sys.stdout', new = StringIO()) as output:

            robot.do_replay('ath', 'reversed')
            self.assertEqual(output.getvalue().strip('\n'), """ > ath turned right.
 > ath now at position (0,10).
 > ath moved forward by 10 steps.
 > ath now at position (10,10).""")

            robot.do_replay('ath', 'reversed silent')
            self.assertEqual(output.getvalue().strip('\n'), """ > ath turned right.
 > ath now at position (0,10).
 > ath moved forward by 10 steps.
 > ath now at position (10,10).""")

            robot.do_replay('ath', 'reversed')
            self.assertEqual(output.getvalue().strip('\n'), """ > ath turned right.
 > ath now at position (0,10).
 > ath moved forward by 10 steps.
 > ath now at position (10,10).
 > ath turned right.
 > ath now at position (10,0).
 > ath moved forward by 10 steps.
 > ath now at position (0,0).""")

    
    def test_valid_command_replay_range(self):
        self.assertTrue(robot.valid_command('replay 5'))
        obstacles.obstacles = []


    @patch('robot.history', ['forward 1', 'forward 2', 'forward 3', 'forward 4', 'forward 5', 'forward 6', 'forward 7'])
    @patch('robot.world.env.position_x', 0)
    @patch('robot.world.env.position_y', 0)
    @patch('robot.world.env.current_direction_index', 0)
    def test_replay_5(self):
        
        with patch('sys.stdout', new = StringIO()) as output:
            robot.do_replay('ath', '5')
            self.assertEqual(output.getvalue().strip('\n'), """ > ath moved forward by 3 steps.
 > ath now at position (0,3).
 > ath moved forward by 4 steps.
 > ath now at position (0,7).
 > ath moved forward by 5 steps.
 > ath now at position (0,12).
 > ath moved forward by 6 steps.
 > ath now at position (0,18).
 > ath moved forward by 7 steps.
 > ath now at position (0,25).""")
        obstacles.obstacles = []


    @patch('robot.history', ['forward 1', 'forward 2', 'forward 3', 'forward 4', 'forward 5', 'forward 6', 'forward 7'])
    @patch('robot.world.env.position_x', 0)
    @patch('robot.world.env.position_y', 0)
    @patch('robot.world.env.current_direction_index', 0)
    def test_replay_5_to_2(self):
        
        with patch('sys.stdout', new = StringIO()) as output:
            robot.do_replay('ath', '5-2')
            self.assertEqual(output.getvalue().strip('\n'), """ > ath moved forward by 3 steps.
 > ath now at position (0,3).
 > ath moved forward by 4 steps.
 > ath now at position (0,7).
 > ath moved forward by 5 steps.
 > ath now at position (0,12).""")
        obstacles.obstacles = []

    
    # TR 4
    #TODO: Test arguments

    # @patch('sys.stdin', StringIO('ath\noff\nforward 100\nback 10\nforward 100\nforward 1\noff\n'))
    def test_no_arg_passed(self):
        from world.text import world as env

        robot.setup_environment()
        self.assertEqual(env, robot.world.env)
        obstacles.obstacles = []


    def test_passed_arg_text(self):
        
        from world.text import world as env

        robot.sys.argv.append('text')

        robot.setup_environment()
        self.assertEqual(env, robot.world.env)
        obstacles.obstacles = []
        

    def test_passed_arg_turtle(self):
        
        from world.turtle import world as env

        robot.sys.argv[1] = 'turtle'

        robot.setup_environment()
        self.assertEqual(robot.world.turtle.world, robot.world.env)




if __name__ == "__main__":
    unittest.main()