PARCEL_TYPE_TO_COST_MAPPING = {"XL": 25, "Large": 15, "Medium": 8, "Small": 3}

class Parcel:
    def __init__(self, length: float, breadth: float, height: float) -> None:
        self.length = length
        self.breadth = breadth
        self.height = height

def get_input_from_user():
    print("Please enter parcel dimensions in the form of length, breadth, height.")
    print("To enter multiple parcel dimensions, please enter the next parcel dimensions seperated by a space. For example - 1,2,3 4,5,6.")
    user_input = input("Parcel Dimensions: ")
    return user_input
    
def parse_user_input(input):
    try:
        # split by space to check for multiple parcels
        parcel_dimension = input.split(" ")
        # returns a list of parcel dimension tuples
        return [tuple(int(x) for x in i.split(",")) for i in parcel_dimension]
    except ValueError:
        print("Please enter only numbers as parcel dimensions!")

def main():
    input = get_input_from_user()
    parcel_dimension = parse_user_input(input)


if __name__ == "__main__":
    main()