#!/usr/bin/env python3

import heapq
import collections

class FreeCellSolver:
    def __init__(self, initial_columns):
        # State: (tuple of columns, frozenset of freecells, tuple of foundation ranks)
        self.initial_state = (tuple(tuple(c) for c in initial_columns), frozenset(), (0, 0, 0, 0))
        self.suits_idx = {'S': 0, 'D': 1, 'H': 2, 'C': 3}
        self.idx_suits = {0: 'S', 1: 'D', 2: 'H', 3: 'C'}
        self.rank_map = {str(i): i for i in range(2, 10)}
        self.rank_map.update({'A': 1, '0': 10, 'J': 11, 'Q': 12, 'K': 13})

    def heuristic(self, state):
        # Priority: Cards not in foundation. 
        return (52 - sum(state[2])) + (len(state[1]) * 0.1)

    def is_red(self, suit):
        return suit in ('H', 'D')

    def can_stack(self, card, target):
        c_rank, c_suit = self.rank_map[card[:-1]], card[-1]
        t_rank, t_suit = self.rank_map[target[:-1]], target[-1]
        return (self.is_red(c_suit) != self.is_red(t_suit)) and (c_rank == t_rank - 1)

    def get_moves(self, state):
        cols, free, found = state
        cols = [list(c) for c in cols]
        free = set(free)
        found = list(found)
        possible = []

        # 1. Foundation Priority
        for i, col in enumerate(cols):
            if col:
                card = col[-1]
                rank, s_idx = self.rank_map[card[:-1]], self.suits_idx[card[-1]]
                if rank == found[s_idx] + 1:
                    new_cols = [list(c) for c in cols]
                    new_cols[i].pop()
                    new_found = list(found)
                    new_found[s_idx] = rank
                    move_desc = f"Move {card} from Col {i+1} to Foundation"
                    return [(tuple(tuple(c) for c in new_cols), frozenset(free), tuple(new_found), move_desc)]

        for card in free:
            rank, s_idx = self.rank_map[card[:-1]], self.suits_idx[card[-1]]
            if rank == found[s_idx] + 1:
                new_free = set(free)
                new_free.remove(card)
                new_found = list(found)
                new_found[s_idx] = rank
                move_desc = f"Move {card} from FreeCell to Foundation"
                return [(tuple(tuple(c) for c in cols), frozenset(new_free), tuple(new_found), move_desc)]

        # 2. Freecell to Column
        for card in free:
            for i, col in enumerate(cols):
                if not col or self.can_stack(card, col[-1]):
                    new_cols = [list(c) for c in cols]
                    new_cols[i].append(card)
                    new_free = set(free)
                    new_free.remove(card)
                    dest = f"Col {i+1}" if col else f"empty Col {i+1}"
                    possible.append((tuple(tuple(c) for c in new_cols), frozenset(new_free), tuple(found), f"Move {card} from FreeCell to {dest}"))

        # 3. Column to Column
        for i, col_from in enumerate(cols):
            if not col_from: continue
            card = col_from[-1]
            for j, col_to in enumerate(cols):
                if i == j: continue
                if not col_to or self.can_stack(card, col_to[-1]):
                    new_cols = [list(c) for c in cols]
                    new_cols[j].append(new_cols[i].pop())
                    dest = f"Col {j+1}" if col_to else f"empty Col {j+1}"
                    possible.append((tuple(tuple(c) for c in new_cols), frozenset(free), tuple(found), f"Move {card} from Col {i+1} to {dest}"))

        # 4. Column to Freecell
        if len(free) < 4:
            for i, col in enumerate(cols):
                if col:
                    new_cols = [list(c) for c in cols]
                    card = new_cols[i].pop()
                    new_free = set(free)
                    new_free.add(card)
                    possible.append((tuple(tuple(c) for c in new_cols), frozenset(new_free), tuple(found), f"Move {card} from Col {i+1} to FreeCell"))

        return possible

    def solve(self):
        weight = 15.0
        # (Priority, Steps, State, Path_of_Descriptions)
        start_node = (weight * self.heuristic(self.initial_state), 0, self.initial_state, [])
        pq = [start_node]
        visited = {self.initial_state: 0}

        count = 0
        while pq:
            _, steps, state, path = heapq.heappop(pq)
            count += 1
            
            if count % 10000 == 0:
                print(f"Searching... States: {count} | Foundation: {sum(state[2])}/52", end="\r")

            if state[2] == (13, 13, 13, 13):
                print(f"\nSolution found in {count} iterations")
                return path

            for next_state, next_free, next_found, move_text in self.get_moves(state):
                new_state = (next_state, next_free, next_found)
                new_steps = steps + 1
                if new_state not in visited or new_steps < visited[new_state]:
                    visited[new_state] = new_steps
                    priority = new_steps + (weight * self.heuristic(new_state))
                    heapq.heappush(pq, (priority, new_steps, new_state, path + [move_text]))
        
        return None

def validate_and_parse():
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K']
    suits = ['S', 'D', 'H', 'C']
    full_deck = {r + s for r in ranks for s in suits}
    while True:
        print("\n--- Enter Card Columns ---")
        cols, all_c = [], []
        for i in range(8):
            col = input(f"Col {i+1}: ").strip().upper().split()
            cols.append(col)
            all_c.extend(col)
        if len(all_c) == 52 and len(set(all_c)) == 52 and all(c in full_deck for c in all_c):
            return cols
        print("Error: Deck must contain exactly 52 unique cards.")

if __name__ == "__main__":
    initial_cols = validate_and_parse()
    solver = FreeCellSolver(initial_cols)
    print("Solving...")
    solution_path = solver.solve()
    
    if solution_path:
        print("\n--- STEP-BY-STEP SOLUTION ---")
        for i, move in enumerate(solution_path, 1):
            print(f"{i}. {move}")
        print("\nGame Over: All cards in Foundation!")
    else:
        print("\nNo solution found.")
