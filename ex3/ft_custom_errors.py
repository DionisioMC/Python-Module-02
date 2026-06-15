class GardenError(Exception):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def testing_PlantError(is_healthy: bool) -> None:
    if is_healthy is False:
        raise PlantError("The tomato plant is wilting!")


def testing_WaterError(water_level: int) -> None:
    if water_level < 60:
        raise WaterError("Not enough water in the tank!")


def testing_GardenError():
    print("Testing catching all garden errors...")
    try:
        testing_WaterError(50)
    except GardenError as e:
        print(f"Caught  GardenError: {e}")
    try:
        testing_PlantError(False)
    except GardenError as e:
        print(f"Caught  GardenError: {e}\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        testing_PlantError(False)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")
    try:
        print("Testing WaterError...")
        testing_WaterError(50)
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")
    testing_GardenError()
