import unittest
from unittest.mock import patch
from io import StringIO
# import robot
import world.text.world as world

class WorldTestCases(unittest.TestCase):

    # @patch('world.position_x', 180)
    def test_show_position(self):

        world.position_x = 180
        world.position_y = 0

        with patch('sys.stdout', new = StringIO()) as output:
            world.show_position("ath")

            self.assertEqual(output.getvalue().strip("\n"), " > ath now at position (180,0).")

    
    def test_is_position_allowed_true(self):
        self.assertTrue(world.is_position_allowed(100,200))
        self.assertTrue(world.is_position_allowed(-100,-200))


    def test_is_position_allowed_false(self):
        self.assertFalse(world.is_position_allowed(-101,200))
        self.assertFalse(world.is_position_allowed(-100,201))
        self.assertFalse(world.is_position_allowed(101,200))
        self.assertFalse(world.is_position_allowed(100,201))


    # @patch('world.position_x', 0)
    # @patch('world.position_y', 0)
    # @patch('world.current_direction_index', 0)
    def test_update_position_true(self):

        world.position_x = 0
        world.position_y = 0
        world.current_direction_index = 0

        self.assertTrue(world.update_position(200))
        world.do_right_turn('ath')
        self.assertTrue(world.update_position(100))
        world.do_right_turn('ath')
        self.assertTrue(world.update_position(400))
        world.do_right_turn('ath')
        self.assertTrue(world.update_position(200))
        world.do_right_turn('ath')


    # @patch('world.position_x', 100)
    # @patch('world.position_y', 200)
    # @patch('world.current_direction_index', 0)
    def test_update_position_false(self):

        world.position_x = 100
        world.position_y = 200
        world.current_direction_index = 0
        
        self.assertFalse(world.update_position(1))
        world.do_right_turn('ath')
        self.assertFalse(world.update_position(1))
        world.do_right_turn('ath')
        self.assertFalse(world.update_position(401))
        world.do_right_turn('ath')
        self.assertFalse(world.update_position(201))
        world.do_right_turn('ath')


    # @patch('world.position_x', 0)
    # @patch('world.position_y', 0)
    # @patch('world.current_direction_index', 0)
    def test_do_forward_within_safe_zone(self):
        
        world.position_x = 0
        world.position_y = 0
        world.current_direction_index = 0

        self.assertLessEqual(world.do_forward('ATH', 20), (True, ' > ATH moved forward by 20 steps.'))
        world.do_right_turn('ath')
        self.assertLessEqual(world.do_forward('ATH', 20), (True, ' > ATH moved forward by 20 steps.'))
        world.do_right_turn('ath')
        self.assertLessEqual(world.do_forward('ATH', 20), (True, ' > ATH moved forward by 20 steps.'))
        world.do_right_turn('ath')
        self.assertLessEqual(world.do_forward('ATH', 20), (True, ' > ATH moved forward by 20 steps.'))
        world.do_right_turn('ath')


    # @patch('world.position_x', 0)
    # @patch('world.position_y', 0)
    # @patch('world.current_direction_index', 0)
    def test_do_forward_outside_the_safe_zone(self):

        world.position_x = 0
        world.position_y = 0
        world.current_direction_index = 0

        self.assertLessEqual(world.do_forward('ATH', 250), (True, 'ATH: Sorry, I cannot go outside my safe zone.'))
        world.do_right_turn('ath')
        self.assertLessEqual(world.do_forward('ATH', 110), (True, 'ATH: Sorry, I cannot go outside my safe zone.'))
        world.do_right_turn('ath')
        self.assertLessEqual(world.do_forward('ATH', 205), (True, 'ATH: Sorry, I cannot go outside my safe zone.'))
        world.do_right_turn('ath')
        self.assertLessEqual(world.do_forward('ATH', 120), (True, 'ATH: Sorry, I cannot go outside my safe zone.'))
        world.do_right_turn('ath')


    # @patch('world.position_x', 0)
    # @patch('world.position_y', 0)
    # @patch('world.current_direction_index', 0)
    def test_do_back_within_safe_zone(self):

        world.position_x = 0
        world.position_y = 0
        world.current_direction_index = 0

        self.assertLessEqual(world.do_back('ATH', 20), (True, ' > ATH moved back by 20 steps.'))
        world.do_right_turn('ath')
        self.assertLessEqual(world.do_back('ATH', 20), (True, ' > ATH moved back by 20 steps.'))
        world.do_right_turn('ath')
        self.assertLessEqual(world.do_back('ATH', 20), (True, ' > ATH moved back by 20 steps.'))
        world.do_right_turn('ath')
        self.assertLessEqual(world.do_back('ATH', 20), (True, ' > ATH moved back by 20 steps.'))
        world.do_right_turn('ath')


    # @patch('world.position_x', 0)
    # @patch('world.position_y', 0)
    # @patch('world.current_direction_index', 0)
    def test_do_back_outside_the_safe_zone(self):

        world.position_x = 0
        world.position_y = 0
        world.current_direction_index = 0

        self.assertLessEqual(world.do_back('ATH', 250), (True, 'ATH: Sorry, I cannot go outside my safe zone.'))
        world.do_right_turn('ath')
        self.assertLessEqual(world.do_back('ATH', 110), (True, 'ATH: Sorry, I cannot go outside my safe zone.'))
        world.do_right_turn('ath')
        self.assertLessEqual(world.do_back('ATH', 205), (True, 'ATH: Sorry, I cannot go outside my safe zone.'))
        world.do_right_turn('ath')
        self.assertLessEqual(world.do_back('ATH', 120), (True, 'ATH: Sorry, I cannot go outside my safe zone.'))
        world.do_right_turn('ath')

    
    # @patch('world.current_direction_index', 0)
    def test_do_right_turn(self):

        world.current_direction_index = 0

        world.do_right_turn('ATH')
        self.assertEqual(world.current_direction_index, 1)
        world.do_right_turn('ATH')
        self.assertEqual(world.current_direction_index, 2)
        world.do_right_turn('ATH')
        self.assertEqual(world.current_direction_index, 3)
        world.do_right_turn('ATH')
        self.assertEqual(world.current_direction_index, 0)
        world.do_right_turn('ATH')
        self.assertEqual(world.current_direction_index, 1)

    
    # @patch('world.current_direction_index', 0)
    def test_do_left_turn(self):

        world.current_direction_index = 0

        world.do_left_turn('ATH')
        self.assertEqual(world.current_direction_index, 3)
        world.do_left_turn('ATH')
        self.assertEqual(world.current_direction_index, 2)
        world.do_left_turn('ATH')
        self.assertEqual(world.current_direction_index, 1)
        world.do_left_turn('ATH')
        self.assertEqual(world.current_direction_index, 0)
        world.do_left_turn('ATH')
        self.assertEqual(world.current_direction_index, 3)


    # @patch('world.position_x', 0)
    # @patch('world.position_y', 0)
    # @patch('world.current_direction_index', 0)
    def test_do_sprint(self):

        world.position_x = 0
        world.position_y = 0
        world.current_direction_index = 0

        world.do_sprint("ATH", 10)
        self.assertEqual(world.position_y, 55)
        world.do_sprint("ATH", 5)
        self.assertEqual(world.position_y, 70)
    

if __name__ == "__main__":
    unittest.main()