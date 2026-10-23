
import random
import math
import itertools

def get_cost(state):
    """Calculates the number of mutually attacking pairs of queens (Energy E)."""
    cost = 0
    n = len(state)
    for i, j in itertools.combinations(range(n), 2):
        # Checks if queens share the same row or the same diagonal axis
        if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
            cost += 1
    return cost

def get_random_neighbor(state):
    """Generates a random neighbor state by shifting one queen's row."""
    neighbor = list(state)
    n = len(state)
    col = random.randint(0, n - 1)

    # Select a row position distinct from the current position
    available_rows = [r for r in range(n) if r != state[col]]
    neighbor[col] = random.choice(available_rows)

    return neighbor

def print_board(state):
    """Prints a visual ASCII representation of the 8x8 chess board."""
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)

def simulated_annealing_8_queens(initial_temp=100.0, cooling_rate=0.995, min_temp=0.001):
    """Solves the 8-Queens problem using the Simulated Annealing heuristic."""
    n = 8
    # 1. Initialize with a random state
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    current_cost = get_cost(current_state)
    T = initial_temp

    print(f"Initial State: {current_state} | Initial Attack Pairs: {current_cost}\n")

    iteration = 1
    while T > min_temp and current_cost > 0:
        # 2. Pick a random neighbor
        neighbor = get_random_neighbor(current_state)
        neighbor_cost = get_cost(neighbor)

        # 3. Calculate delta energy
        delta_E = neighbor_cost - current_cost

        # 4. Acceptance evaluation
        if delta_E < 0:
            # Better move: accept instantly
            current_state = neighbor
            current_cost = neighbor_cost
        else:
            # Worse move: compute transition probability
            probability = math.exp(-delta_E / T)
            if random.random() < probability:
                current_state = neighbor
                current_cost = neighbor_cost

        if iteration % 200 == 0 or current_cost == 0:
            print(f"Iteration {iteration:4d} | Temp: {T:7.3f} | Current Attacking Pairs: {current_cost}")
            print(f"Board Configuration: {current_state}")
            print("Board Visual:")
            print_board(current_state)
            print("-" * 30)

        # 5. Cool down the system
        T *= cooling_rate
        iteration += 1

    return current_state, current_cost

if __name__ == "__main__":
    print("--- Running 8-Queens Simulated Annealing Search ---")
    final_state, final_cost = simulated_annealing_8_queens()

    if final_cost == 0:
        print(f"\nSuccess! Goal Configuration Found: {final_state}")
        print("\nVisual Board Layout:")
        print_board(final_state)
    else:
        print(f"\nFailed to converge. Finished at state {final_state} with cost {final_cost}.")
        print("Try adjustments to the initial temperature or cooling rate parameters.")



