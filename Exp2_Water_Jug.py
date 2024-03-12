def water_jug_solver(jug1, jug2, aim):
    visited_states = set()

    def pour_water(x, y):
        if (x, y) in visited_states:
            return False
        visited_states.add((x, y))

        print(f"({x}, {y})")

        if y == aim:
            print(f"Goal reached in {len(visited_states) - 1} steps!")
            return True

        # Applying the production rules
        if x < jug1:
            if pour_water(jug1, y):
                return True

        if y < jug2:
            if pour_water(x, jug2):
                return True

        if x > 0:
            if pour_water(0, y):
                return True

        if y > 0:
            if pour_water(x, 0):
                return True

        if x + y < jug1:
            if pour_water(x + y, 0):
                return True

        if x + y < jug2:
            if pour_water(0, x + y):
                return True

        if x + y >= jug1 and y > 0:
            if pour_water(jug1, y - (jug1 - x)):
                return True

        if x + y >= jug2 and x > 0:
            if pour_water(x - (jug2 - y), jug2):
                return True

        if x + y < jug1 and y > 0:
            if pour_water(0, x + y):
                return True

        if x + y < jug2 and x > 0:
            if pour_water(x + y, 0):
                return True

        return False

    print("\nSteps to achieve the goal:")
    if not pour_water(0, 0):
        print("Goal cannot be reached!")

# Main program
jug1 = int(input("Enter the capacity of jug 1: "))
jug2 = int(input("Enter the capacity of jug 2: "))
aim = int(input("Enter the amount of water to be present in jug 2: "))

water_jug_solver(jug1, jug2, aim)
