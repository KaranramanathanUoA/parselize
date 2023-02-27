PARCEL_TYPE_TO_COST_MAPPING = {"XL": 25, "Large": 15, "Medium": 8, "Small": 3}

class Parcel:
    def __init__(self, length: float, breadth: float, height: float) -> None:
        self.length = length
        self.breadth = breadth
        self.height = height

    def get_biggest_dimension_of_parcel(self, parcel: tuple) -> float:
        return max(parcel)

    def return_parcel_type(self, biggest_dimension : float) -> str:
        if (biggest_dimension >= 100):
            return "XL"
        
        if (biggest_dimension < 100 and biggest_dimension > 50):
            return "Large"

        if (biggest_dimension < 50 and biggest_dimension > 10):
            return "Medium"
        
        if (biggest_dimension < 10):
            return "Small"

    def calculate_cost_of_shipping(self, parcel_type: str) -> int:
        return PARCEL_TYPE_TO_COST_MAPPING.get(parcel_type)


def get_input_from_user():
    print("Please enter parcel dimensions in the form of length, breadth, height.")
    print("To enter multiple parcel dimensions, please enter the next parcel dimensions seperated by a space. For example - 1,2,3 4,5,6.")
    user_input = input("Parcel Dimensions: ")
    return user_input
    
def parse_user_input(input):
    try:
        # split by space to check for multiple parcels
        parcel_dimension = input.split(" ")
        # returns a list of parcel dimension tuples for eg - [(1,2,3), (4,5,6)]
        return [tuple(int(x) for x in i.split(",")) for i in parcel_dimension]
    except ValueError:
        print("Please enter only numbers as parcel dimensions!")
        exit()

def main():
    input = get_input_from_user()
    parcel_dimensions = parse_user_input(input)

    for parcel_dimension in parcel_dimensions:
        try:
            parcel = Parcel(*parcel_dimension)
        except TypeError:
            print("Input has not been entered in valid format!")
            print("For multiple parcels, please enter parcel dimensions separated by a space!")
            exit()

        max_dimension = parcel.get_biggest_dimension_of_parcel(parcel_dimension)
        parcel_type = parcel.return_parcel_type(max_dimension)
        cost = parcel.calculate_cost_of_shipping(parcel_type)

if __name__ == "__main__":
    main()