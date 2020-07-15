import unittest

from color_code_converter import hex_to_rgb

class ColorCodeConverterTest(unittest.TestCase):
    def test_output_for_hex_to_rgb_is_string(self):
        pass

    def test_hex_to_rgb_can_handle_length_of_3(self):
        pass

    def test_hex_to_rgb_can_handle_length_of_6(self):
        pass

    def test_hex_to_rgb_cannot_handle_other_even_numbers_as_length(self):
        pass

    def test_hex_to_rgb_cannot_handle_odd_length_for_input(self):
        pass

if __name__ == '__main__':
    unittest.main()
