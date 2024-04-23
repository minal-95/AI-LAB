def solve_crypt_arithmetic(puzzle):
    import re
    from itertools import permutations

    # Extracting all words (operands and result)
    words = re.findall(r'[A-Z]+', puzzle)
    unique_letters = set(''.join(words))
    
    if len(unique_letters) > 10:
        return "Invalid puzzle: More than 10 unique letters"
    
    # Generate all possible digit assignments
    for perm in permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))
        
        # Ensure no word has a leading zero
        if any(mapping[word[0]] == 0 for word in words):
            continue

        if is_solution_valid(words, mapping):
            return mapping

    return "No solution found"

def is_solution_valid(words, mapping):
    # Compute integer values of each word
    values = [sum(mapping[letter] * (10 ** idx) for idx, letter in enumerate(reversed(word)))
              for word in words]

    # Check the last word is the sum of the others
    return sum(values[:-1]) == values[-1]

def print_solution(solution):
    if isinstance(solution, dict):
        print("Solution found:")
        for letter, digit in solution.items():
            print(f"{letter}: {digit}")
    else:
        print(solution)

# Example usage:
puzzle = "SEND + MORE = MONEY"
solution = solve_crypt_arithmetic(puzzle)
print_solution(solution)

