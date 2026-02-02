class Vehicle:
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, year: int, make: str, model: str, doors: int, roof: str) -> None:
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self) -> str:
        return (
            f"Vehicle type: {self.vehicle_type}\n"
            f"Year: {self.year}\n"
            f"Make: {self.make}\n"
            f"Model: {self.model}\n"
            f"Number of doors: {self.doors}\n"
            f"Type of roof: {self.roof}"
        )


def _normalize_doors(value: str):
    v = value.strip().lower()
    if v in {"2", "two"}:
        return 2
    if v in {"4", "four"}:
        return 4
    return None


def _normalize_roof(value: str):
    v = value.strip().lower()
    if v in {"solid", "solid roof"}:
        return "solid"
    if v in {"sun roof", "sunroof", "sun"}:
        return "sun roof"
    return None


def prompt_for_automobile() -> Automobile:
    # vehicle_type is always 'car' for this app
    while True:
        year_str = input("Enter year: ").strip()
        try:
            year = int(year_str)
            if year <= 0:
                print("Please enter a positive integer for year.")
                continue
        except ValueError:
            print("Invalid year. Please enter a number like 2022.")
            continue
        break

    make = input("Enter make: ").strip()
    while not make:
        print("Make cannot be empty.")
        make = input("Enter make: ").strip()

    model = input("Enter model: ").strip()
    while not model:
        print("Model cannot be empty.")
        model = input("Enter model: ").strip()

    doors = None
    while doors is None:
        doors_input = input("Enter number of doors (2 or 4): ")
        doors = _normalize_doors(doors_input)
        if doors is None:
            print("Please enter 2 or 4 (or 'two' / 'four').")

    roof = None
    while roof is None:
        roof_input = input("Enter type of roof ('solid' or 'sun roof'): ")
        roof = _normalize_roof(roof_input)
        if roof is None:
            print("Please enter 'solid' or 'sun roof' (or 'sunroof').")

    return Automobile(year=year, make=make, model=model, doors=doors, roof=roof)


def main() -> int:
    try:
        car = prompt_for_automobile()
    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled.")
        return 1

    print("\n--- Vehicle Summary ---")
    print(car)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



