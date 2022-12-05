import unittest
from main import *


class ColorConvertTests(unittest.TestCase):
    """Класс для тестирования перевода цвета"""

    def test_rgb_to_hex(self):
        self.assertEqual(('0x0', '0x0', '0x0'), rgb_to_hex(0, 0, 0))
        self.assertEqual(('0xff', '0xff', '0xff'), rgb_to_hex(255, 255, 255))
        self.assertEqual(('0x1e', '0x90', '0xff'), rgb_to_hex(30, 144, 255))

    def test_rgb_to_cmyk(self):
        self.assertEqual((0, 0, 0, 100), rgb_to_cmyk(0, 0, 0))
        self.assertEqual((0, 0, 0, 0), rgb_to_cmyk(255, 255, 255))
        self.assertEqual((88, 44, 0, 0), rgb_to_cmyk(30, 144, 255))

    def test_rgb_to_hsl(self):
        self.assertEqual((0, 0, 0), rgb_to_hsl(0, 0, 0))
        self.assertEqual((0, 0, 100), rgb_to_hsl(255, 255, 255))
        self.assertEqual((210, 100, 56), rgb_to_hsl(30, 144, 255))

    def test_rgb_to_hsv(self):
        self.assertEqual((0, 0, 0), rgb_to_hsv(0, 0, 0))
        self.assertEqual((0, 0, 100), rgb_to_hsv(255, 255, 255))
        self.assertEqual((210, 88, 100), rgb_to_hsv(30, 144, 255))

    def test_cmyk_to_rgb(self):
        self.assertEqual((0, 0, 0), cmyk_to_rgb(0, 0, 0, 100))
        self.assertEqual((255, 255, 255), cmyk_to_rgb(0, 0, 0, 0))
        self.assertEqual((30, 144, 255), cmyk_to_rgb(88, 44, 0, 0))

    def test_hsl_to_rgb(self):
        self.assertEqual((0, 0, 0), hsl_to_rgb(0, 0, 0))
        self.assertEqual((255, 255, 255), hsl_to_rgb(0, 0, 100))
        self.assertEqual((30, 144, 255), hsl_to_rgb(210, 100, 56))

    def test_hsv_to_rgb(self):
        self.assertEqual((0, 0, 0), hsv_to_rgb(0, 0, 0))
        self.assertEqual((255, 255, 255), hsv_to_rgb(0, 0, 100))
        self.assertEqual((30, 144, 255), hsv_to_rgb(210, 88, 100))


if __name__ == '__main__':
    unittest.main()