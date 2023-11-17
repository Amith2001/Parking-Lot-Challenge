import random

class ParkingLot:
    def __init__(self, size, spot_size):
        self.size = size
        self.spot_size = spot_size
        self.array = [None] * (size // spot_size)

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return self.license_plate

    def park(self, parking_lot, spot):
        if parking_lot.array[spot] is None:
            parking_lot.array[spot] = self
            return f"Car with license plate {self} parked successfully in spot {spot + 1}."
        else:
            return f"Car with license plate {self} was not parked successfully in spot {spot + 1} because it was occupied."

def main():
    size = 2000
    spot_size = 96
    parking_lot = ParkingLot(size, spot_size)

    license_plates = [str(random.randint(1000000, 9999999)) for _ in range(20)]
    cars = [Car(license_plate) for license_plate in license_plates]

    for car in cars:
        spot = random.randint(0, len(parking_lot.array) - 1)
        if parking_lot.array[spot] is None:
            print(car.park(parking_lot, spot))
        else:
            for attempt in range(1, len(parking_lot.array)):
                spot = (spot + 1) % len(parking_lot.array)
                if parking_lot.array[spot] is None:
                    print(car.park(parking_lot, spot))
                    break

if __name__ == "__main__":
    main()