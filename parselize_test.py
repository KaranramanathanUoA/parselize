import unittest
from parselize import Parcel

class ParselizeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.parcel = Parcel(10,15,20)
    
    def test_parcel_dimensions_are_initialized(self):
        self.assertEqual(self.parcel.height, 20)
        self.assertEqual(self.parcel.length, 10)
        self.assertEqual(self.parcel.breadth, 15)

if __name__ == "__main__":
    unittest.main()
        