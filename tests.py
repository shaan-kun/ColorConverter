import unittest
from main import *


class ColorConvertTests(unittest.TestCase):
    """Класс для тестирования перевода цвета"""

    def test_rgb_to_hex(self):
        self.assertEqual((0x0, 0x0, 0x0), rgb_to_hex(0, 0, 0))
        self.assertEqual((0xFF, 0xFF, 0xFF), rgb_to_hex(255, 255, 255))
        self.assertEqual((0x1E, 0x90, 0xFF), rgb_to_hex(30, 144, 255))

    def test_rgb_to_cmyk(self):
        black = [round(num, 2) for num in rgb_to_cmyk(0, 0, 0)]
        self.assertEqual([0.0, 0.0, 0.0, 1.00], black)

        white = [round(num, 2) for num in rgb_to_cmyk(255, 255, 255)]
        self.assertEqual([0.0, 0.0, 0.0, 0.0], white)

        dodger_blue = [round(num, 2) for num in rgb_to_cmyk(30, 144, 255)]
        self.assertEqual([0.88, 0.44, 0.0, 0.0], dodger_blue)

    def test_rgb_to_hsl(self):
        black = [round(num, 2) for num in rgb_to_hsl(0, 0, 0)]
        self.assertEqual([0.0, 0.0, 0.0], black)

        white = [round(num, 2) for num in rgb_to_hsl(255, 255, 255)]
        self.assertEqual([0.0, 0.0, 1], white)

        dodger_blue = [round(num, 2) for num in rgb_to_hsl(30, 144, 255)]
        self.assertEqual([210, 1.00, 0.56], dodger_blue)


if __name__ == '__main__':
    unittest.main()