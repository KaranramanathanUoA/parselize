import unittest
from parselize import *

class ParselizeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.parcel_dimension = (10,15,20)
        self.parcel = Parcel(*self.parcel_dimension)
    
    def test_parcel_dimensions_are_initialized(self):
        self.assertEqual(self.parcel.height, 20)
        self.assertEqual(self.parcel.length, 10)
        self.assertEqual(self.parcel.breadth, 15)

    def test_parcel_dimensions_are_correctly_parsed_with_valid_input(self):
        input = "1,2,4"
        self.assertEqual(parse_user_input(input), [(1,2,4)])

    def test_parcel_dimensions_are_correctly_parsed_with_multiple_inputs(self):
        input = "12,15,85 6,45,100"
        self.assertEqual(parse_user_input(input), [(12,15,85),(6,45,100)])

    def test_exception_is_thrown_when_parsing_invalid_inputs(self):
        input = "a,b,c"
        with self.assertRaises(SystemExit):
            parse_user_input(input)

    def test_medium_parcel_type_is_returned_for_valid_dimensions(self):
        biggest_dimension = self.parcel.get_biggest_dimension_of_parcel(self.parcel_dimension)
        self.assertEqual(self.parcel.return_parcel_type(biggest_dimension), "Medium")

    def test_XL_parcel_type_is_returned_for_valid_dimensions(self):
        xl_parcel_dimension = (150,20,50)
        self.xl_parcel = Parcel(*xl_parcel_dimension)
        biggest_dimension = self.xl_parcel.get_biggest_dimension_of_parcel(xl_parcel_dimension)
        self.assertEqual(self.xl_parcel.return_parcel_type(biggest_dimension), "XL")

    

if __name__ == "__main__":
    unittest.main()
        