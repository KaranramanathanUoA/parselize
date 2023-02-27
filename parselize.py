PARCEL_TYPE_TO_COST_MAPPING = {"XL": 25, "Large": 15, "Medium": 8, "Small": 3}

class Parcel:
    def __init__(self, length: float, breadth: float, height: float) -> None:
        self.length = length
        self.breadth = breadth
        self.height = height