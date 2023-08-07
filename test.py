import unittest
from main import Rover, Movement

class TestRover(unittest.TestCase):
    def test_turn_r(self): # Testa o código para a mudança de direção para a direita
        rover = Rover(0, 0, "N", [])
        self.assertEqual(rover.turn_r("N"), "E")
        self.assertEqual(rover.turn_r("E"), "S")
        self.assertEqual(rover.turn_r("S"), "W")
        self.assertEqual(rover.turn_r("W"), "N")

    def test_turn_l(self): # Testa o código para a mudança de direção para a esquerda
        rover = Rover(0, 0, "N", [])
        self.assertEqual(rover.turn_l("N"), "W")
        self.assertEqual(rover.turn_l("W"), "S")
        self.assertEqual(rover.turn_l("S"), "E")
        self.assertEqual(rover.turn_l("E"), "N")

class TestMovement(unittest.TestCase): # Testa o código para o movimento do Rover
    def test_move(self):
        command_list1 = ["L", "M", "L", "M", "L", "M", "L", "M", "M"]
        rover1 = Movement(1, 2, "N", command_list1)
        x, y, a = rover1.move()
        self.assertEqual((x, y, a), (1, 3, "N"))

        command_list2 = ["M", "M", "R", "M", "M", "R", "M", "R", "R", "M"]
        rover2 = Movement(3, 3, "E", command_list2)
        x, y, a = rover2.move()
        self.assertEqual((x, y, a), (5, 1, "E"))

if __name__ == '__main__':
    unittest.main()
