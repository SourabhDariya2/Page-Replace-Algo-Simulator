# main.py
from simulator import run_simulation

def main():
    print("=== Efficient Page Replacement Algorithm Simulator ===\n")

    pages_input = input("Enter page reference string (space-separated numbers): ")
    pages = [int(p) for p in pages_input.strip().split()]
    frames_count = int(input("Enter number of frames: "))

    print("\nSelect algorithm: ")
    print("1. FIFO")
    print("2. LRU")
    print("3. Optimal")
    choice = input("Enter choice (1/2/3): ")

    algorithm_map = {"1": "FIFO", "2": "LRU", "3": "Optimal"}
    algorithm = algorithm_map.get(choice, "FIFO")

    result = run_simulation(pages, frames_count, algorithm)

    print("\n=== Simulation Results ===")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
