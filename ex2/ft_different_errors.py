def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        operation_number / 0
    elif operation_number == 2:
        open("file.txt")
    elif operation_number == 3:
        "abc" + operation_number
    elif operation_number == 4:
        print("Operation completed successfully\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    operations = [0, 1, 2, 3, 4]
    for op in operations:
        try:
            print(f"Testing operation {op}...")
            garden_operations(op)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    print("All error types tested successfully!")

if __name__ == "__main__":
    test_error_types()