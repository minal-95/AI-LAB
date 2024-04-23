def is_valid(assignment, course, day, constraints):
    """ Check if assigning a day to a course violates any constraints. """
    for neighbor in constraints[course]:
        if neighbor in assignment and assignment[neighbor] == day:
            return False
    return True

def backtrack(assignment, courses, domains, constraints):
    """ Recursive backtracking algorithm to find a valid assignment. """
    if len(assignment) == len(courses):
        return assignment  # All courses have been assigned without conflict

    for course in courses:
        if course not in assignment:
            for day in domains:
                if is_valid(assignment, course, day, constraints):
                    assignment[course] = day
                    result = backtrack(assignment, courses, domains, constraints)
                    if result:
                        return result
                    assignment.pop(course)
            return None  # No valid assignment found for this branch

def constraint_satisfaction(courses, domains, constraints):
    """ Sets up the CSP and calls the backtracking algorithm. """
    assignment = {}
    return backtrack(assignment, courses, domains, constraints)

# Define the variables (courses)
courses = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Define the domains (days available)
domains = ['Monday', 'Tuesday', 'Wednesday']

# Define the constraints (which courses cannot be on the same day)
constraints = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'F'],
    'E': ['C', 'G'],
    'F': ['D'],
    'G': ['E']
}

# Solve the CSP
solution = constraint_satisfaction(courses, domains, constraints)
if solution:
    print("Solution found:")
    for course, day in solution.items():
        print(f"Course {course}: {day}")
else:
    print("No solution exists.")

