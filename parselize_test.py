import unittest
from parselize import *

class ParselizeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.parcel = Parcel(10,15,20)
    
    def test_parcel_dimensions_are_initialized(self):
        self.assertEqual(self.parcel.height, 20)
        self.assertEqual(self.parcel.length, 10)
        self.assertEqual(self.parcel.breadth, 15)

    def test_parcel_dimensions_are_correctly_parsed_with_valid_input(self):
        input = "1,2,4"
        self.assertEqual(parse_user_input(input), [(1,2,4)])

    def test_parcel_dimensions_are_correctly_parsed_with_multiple_dimensions(self):
        input = "12,15,85 6,45,100"
        self.assertEqual(parse_user_input(input), [(12,15,85), (6,45,100)])

    def test_exception_is_thrown_when_parsing_invalid_inputs(self):
        input = "a,b,c"
        with self.assertRaises(SystemExit):
            parse_user_input(input)

    

if __name__ == "__main__":
    unittest.main()
        