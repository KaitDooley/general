#!/usr/bin/env python3

import heapq
import collections
import sys

class FreeCellSolver:
    def __init__(self, initial_columns):
        # State: (tuple of columns, frozenset of freecells, tuple of foundation ranks)
        self.initial_state = (tuple(tuple(c) for c in initial_columns), frozenset(), (0, 0, 0, 0))
        self.suits = {'S': 0, 'D': 1, 'H': 2, 'C': 3}
        self.rank_map = {str(i): i for i in range(2, 10)}
        self.rank_map.update({'A': 1, '0': 10, 'J': 11, 'Q': 12, 'K': 13})

    def heuristic(self, state):
        # Greedy: Focus on cards NOT in the foundation.
        # We also penalize cards stuck in FreeCells slightly to encourage clearing them.
        return (52 - sum(state[2])) + (len(state[1]) * 0.5)

    def is_red(self, suit):
        return suit in ('H', 'D')

    def can_stack(self, card, target):
        c_rank, c_suit = self.rank_map[card[:-1]], card[-1]
        t_rank, t_suit = self.rank_map[target[:-1]], target[-1]
        return (self.is_red(c_suit) != self.is_red(t_suit)) and (c_rank == t_rank - 1)

    def get_moves(self, state):
        cols, free, found = state
        cols = list(list(c) for c in cols)
        free = set(free)
        found = list(found)

        # 1. PRIORITY: Foundation Moves (Immediate Return)
        # Moving to foundation is almost always the right move.
        for i, col in enumerate(cols):
            if col:
                card = col[-1]
                rank, s_idx = self.rank_map[card[:-1]], self.suits[card[-1]]
                if rank == found[s_idx] + 1:
                    new_cols = [list(c) for c in cols]
                    new_cols[i].pop()
                    new_found = list(found)
                    new_found[s_idx] = rank
                    return [(tuple(tuple(c) for c in new_cols), frozenset(free), tuple(new_found))]

        for card in free:
            rank, s_idx = self.rank_map[card[:-1]], self.suits[card[-1]]
            if rank == found[s_idx] + 1:
                new_free = set(free)
                new_free.remove(card)
                new_found = list(found)
                new_found[s_idx] = rank
                return [(tuple(tuple(c) for c in cols), frozenset(new_free), tuple(new_found))]

        # 2. OTHER MOVES: Organized by general "usefulness"
        possible = []

        # From FreeCell back to Columns (Clearing space)
        for card in free:
            for i, col in enumerate(cols):
                if not col or self.can_stack(card, col[-1]):
                    new_cols = [list(c) for c in cols]
                    new_cols[i].append(card)
                    new_free = set(free)
                    new_free.remove(card)
                    possible.append((tuple(tuple(c) for c in new_cols), frozenset(new_free), tuple(found)))

        # Column to Column
        for i, col_from in enumerate(cols):
            if not col_from: continue
            for j, col_to in enumerate(cols):
                if i == j: continue
                if not col_to or self.can_stack(col_from[-1], col_to[-1]):
                    new_cols = [list(c) for c in cols]
                    new_cols[j].append(new_cols[i].pop())
                    possible.append((tuple(tuple(c) for c in new_cols), frozenset(free), tuple(found)))

        # Column to FreeCell (Only if we have space)
        if len(free) < 4:
            for i, col in enumerate(cols):
                if col:
                    new_cols = [list(c) for c in cols]
                    card = new_cols[i].pop()
                    new_free = set(free)
                    new_free.add(card)
                    possible.append((tuple(tuple(c) for c in new_cols), frozenset(new_free), tuple(found)))

        return possible

    def solve(self):
        # WEIGHT: Higher number = faster solve, less memory, but longer solution path.
        # 1.0 is standard A*; 5.0+ is very greedy.
        weight = 15.0 
        
        # (Priority, Steps, Current State, Path)
        start_node = (weight * self.heuristic(self.initial_state), 0, self.initial_state, [])
        pq = [start_node]
        visited = {self.initial_state: 0}

        count = 0
        while pq:
            _, steps, state, path = heapq.heappop(pq)
            count += 1
            
            if count % 10000 == 0:
                f_total = sum(state[2])
                print(f"States: {count} | Foundation: {f_total}/52 | RAM Saved: {len(visited)} nodes", end='\r')

            if state[2] == (13, 13, 13, 13):
                print(f"\nSolved! Explored {count} states.")
                return path + [state]

            for next_state in self.get_moves(state):
                new_steps = steps + 1
                if next_state not in visited or new_steps < visited[next_state]:
                    visited[next_state] = new_steps
                    priority = new_steps + (weight * self.heuristic(next_state))
                    heapq.heappush(pq, (priority, new_steps, next_state, path + [state]))
        
        return None

def validate_and_parse():
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K']
    suits = ['S', 'D', 'H', 'C']
    full_deck = {r + s for r in ranks for s in suits}

    while True:
        print("\n--- Greedy FreeCell Solver ---")
        columns = []
        all_entered = []
        for i in range(8):
            col = input(f"Column {i+1}: ").strip().upper().split()
            columns.append(col)
            all_entered.extend(col)
        
        if len(all_entered) != 52:
            print(f"Error: {len(all_entered)} cards found. Need 52.")
            continue
        if len(set(all_entered)) != 52:
            dupes = [item for item, count in collections.Counter(all_entered).items() if count > 1]
            print(f"Error: Duplicates found {dupes}")
            continue
        if not all(c in full_deck for c in all_entered):
            print("Error: Invalid card names detected.")
            continue
        return columns

if __name__ == "__main__":
    cols = validate_and_parse()
    solver = FreeCellSolver(cols)
    print("Solving (this should be much faster)...")
    result = solver.solve()
    
    if result:
        print(f"Success! Won in {len(result)-1} moves.")
    else:
        print("\nCould not find a solution.")
