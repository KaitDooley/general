#!/usr/bin/env python3

import collections

class FreeCellSolver:
    def __init__(self, initial_columns):
        # We store the state as (columns, free_cells, foundation)
        # Using tuples and frozensets makes the state hashable for the 'visited' set
        self.initial_state = (
            tuple(tuple(c) for c in initial_columns), 
            frozenset(), 
            (0, 0, 0, 0)  # S, D, H, C
        )
        self.suits = {'S': 0, 'D': 1, 'H': 2, 'C': 3}
        self.rank_map = {str(i): i for i in range(2, 10)}
        self.rank_map.update({'A': 1, '0': 10, 'J': 11, 'Q': 12, 'K': 13})

    def is_red(self, suit):
        return suit in ('H', 'D')

    def can_stack(self, card, target):
        """Check if 'card' can be placed on 'target' in the columns."""
        c_rank, c_suit = self.rank_map[card[:-1]], card[-1]
        t_rank, t_suit = self.rank_map[target[:-1]], target[-1]
        return (self.is_red(c_suit) != self.is_red(t_suit)) and (c_rank == t_rank - 1)

    def get_moves(self, state):
        cols, free, found = state
        cols = [list(c) for c in cols]
        free = set(free)
        found = list(found)
        possible_states = []

        # 1. IMMEDIATE MOVE: Can any card go to the Foundation?
        # This is a 'greedy' optimization. If we can move to foundation, we do it.
        for i, col in enumerate(cols):
            if col:
                card = col[-1]
                rank, suit_idx = self.rank_map[card[:-1]], self.suits[card[-1]]
                if rank == found[suit_idx] + 1:
                    new_cols = [tuple(c) for c in cols]
                    new_cols[i] = tuple(new_cols[i][:-1])
                    new_found = list(found)
                    new_found[suit_idx] += 1
                    return [(tuple(new_cols), frozenset(free), tuple(new_found))]

        # 2. MOVE: Column to FreeCell
        if len(free) < 4:
            for i, col in enumerate(cols):
                if col:
                    new_cols = [list(c) for c in cols]
                    card = new_cols[i].pop()
                    new_free = set(free)
                    new_free.add(card)
                    possible_states.append((tuple(tuple(c) for c in new_cols), frozenset(new_free), tuple(found)))

        # 3. MOVE: FreeCell to Column
        for card in free:
            for i, col in enumerate(cols):
                if not col or self.can_stack(card, col[-1]):
                    new_cols = [list(c) for c in cols]
                    new_cols[i].append(card)
                    new_free = set(free)
                    new_free.remove(card)
                    possible_states.append((tuple(tuple(c) for c in new_cols), frozenset(new_free), tuple(found)))

        # 4. MOVE: Column to Column (Single card only for simple version)
        for i, col_from in enumerate(cols):
            if not col_from: continue
            card_from = col_from[-1]
            for j, col_to in enumerate(cols):
                if i == j: continue
                if not col_to or self.can_stack(card_from, col_to[-1]):
                    new_cols = [list(c) for c in cols]
                    new_cols[j].append(new_cols[i].pop())
                    possible_states.append((tuple(tuple(c) for c in new_cols), frozenset(free), tuple(found)))

        return possible_states

    def solve(self):
        queue = collections.deque([(self.initial_state, [])])
        visited = {self.initial_state}

        while queue:
            state, path = queue.popleft()
            
            # Win condition: All 4 foundation piles have Kings (Rank 13)
            if state[2] == (13, 13, 13, 13):
                return path + [state]

            for next_state in self.get_moves(state):
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, path + [state]))
        
        return None

def parse_input():
    print("Enter the cards for each of the 8 columns (e.g., JS 5S 2S 5D 0D KS KH)")
    columns = []
    for i in range(8):
        col = input(f"Column {i+1}: ").strip().upper().split()
        columns.append(col)
    return columns

if __name__ == "__main__":
    initial_cols = parse_input()
    solver = FreeCellSolver(initial_cols)
    
    print("\nSearching for solution...")
    result = solver.solve()
    
    if result:
        print(f"Success! Solved in {len(result) - 1} moves.")
        # Optional: Print the last state to verify
        print("Final State Foundation:", result[-1][2])
    else:
        print("No solution found or too complex for basic BFS.")
