class GardenError(Exception):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)

def water_plant(plant_name: str):
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("Testing valid plants...")
    valid = ["Tomato", "Lettuce", "Carrots"]
    try:
        print("Opening watering system")
        for plant in valid:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")
    print("Testing invalid plants...")
    invalid = ["Tomato", "lettuce"]
    try:
        print("Opening watering system")
        for plant in invalid:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")

if __name__ == "__main__":
    test_watering_system()
    print("Cleanup always happens, even with errors!")