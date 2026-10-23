
import random
import itertools

def get_cost(state):
    """Calculates the number of attacking pairs of queens."""
    cost = 0
    n = len(state)
    for i, j in itertools.combinations(range(n), 2):
        # Same row or same diagonal
        if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
            cost += 1
    return cost

def get_best_neighbor(state):
    """Generates all neighbors and returns the one with the lowest cost."""
    n = len(state)
    current_cost = get_cost(state)
    best_neighbor = state
    best_cost = current_cost

    # Iterate through every column
    for col in range(n):
        # Try every other row position in that column
        for row in range(n):
            if row != state[col]:
                neighbor = list(state)
                neighbor[col] = row
                neighbor_cost = get_cost(neighbor)

                # We want the absolute lowest cost neighbor
                if neighbor_cost < best_cost:
                    best_cost = neighbor_cost
                    best_neighbor = neighbor

    return best_neighbor, best_cost

def hill_climbing_n_queens(n=4, initial_state=None):
    """Solves N-Queens using steepest-ascent Hill Climbing."""
    if initial_state is None:
        current_state = [random.randint(0, n - 1) for _ in range(n)]
    else:
        current_state = list(initial_state)

    print(f"Initial State: {current_state} | Initial Cost: {get_cost(current_state)}")

    step = 1
    while True:
        neighbor, neighbor_cost = get_best_neighbor(current_state)

        # If the best neighbor isn't better than current, we hit a local/global optimum
        if neighbor_cost >= get_cost(current_state):
            break

        current_state = neighbor
        print(f"Step {step}: Moved to {current_state} | Cost: {neighbor_cost}")
        print_board(current_state)
        step += 1

    final_cost = get_cost(current_state)
    if final_cost == 0:
        print(f"\nSuccess! Goal Configuration Found: {current_state}")
    else:
        print(f"\nStuck in Local Minimum at state: {current_state} with Cost: {final_cost}")

    return current_state, final_cost

def print_board(state):
    """Prints a visual representation of the chess board."""
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)

if __name__ == "__main__":

    example_initial = [0, 0, 0, 0]

    print("--- Running 4-Queens Hill Climbing")
    final_state, cost = hill_climbing_n_queens(n=4, initial_state=example_initial)

    print("\nVisual Board Layout:")
    print_board(final_state)

