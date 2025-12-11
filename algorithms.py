# algorithms.py
from collections import deque

def fifo(pages, frames_count):
    frames = deque()
    hits = 0
    misses = 0

    for page in pages:
        if page in frames:
            hits += 1
        else:
            misses += 1
            if len(frames) >= frames_count:
                frames.popleft()
            frames.append(page)
    return hits, misses

def lru(pages, frames_count):
    frames = []
    hits = 0
    misses = 0

    for page in pages:
        if page in frames:
            hits += 1
            frames.remove(page)
            frames.append(page)
        else:
            misses += 1
            if len(frames) >= frames_count:
                frames.pop(0)
            frames.append(page)
    return hits, misses

def optimal(pages, frames_count):
    frames = []
    hits = 0
    misses = 0

    for i, page in enumerate(pages):
        if page in frames:
            hits += 1
        else:
            misses += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                # Find the page to replace
                future_uses = []
                for f in frames:
                    if f in pages[i+1:]:
                        future_uses.append(pages[i+1:].index(f))
                    else:
                        future_uses.append(float('inf'))
                index_to_replace = future_uses.index(max(future_uses))
                frames[index_to_replace] = page
    return hits, misses
