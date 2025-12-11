# simulator.py
from algorithms import fifo, lru, optimal

def run_simulation(pages, frames_count, algorithm):
    if algorithm == "FIFO":
        hits, misses = fifo(pages, frames_count)
    elif algorithm == "LRU":
        hits, misses = lru(pages, frames_count)
    elif algorithm == "Optimal":
        hits, misses = optimal(pages, frames_count)
    else:
        raise ValueError("Unknown algorithm")

    hit_ratio = hits / len(pages)
    miss_ratio = misses / len(pages)

    return {
        "Algorithm": algorithm,
        "Frames": frames_count,
        "Hits": hits,
        "Misses": misses,
        "Hit Ratio": f"{hit_ratio:.2f}",
        "Miss Ratio": f"{miss_ratio:.2f}"
    }
if __name__ == "__main__":
    print("Simulator module loaded successfully!")
