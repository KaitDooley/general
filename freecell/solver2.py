#!/usr/bin/env python3
import heapq
import collections

class FreeCellSolver:
    def __init__(self, initial_columns):
        # State: (columns, free_cells, foundation)
        self.initial_cols = tuple(tuple(c) for c in initial_columns)
        self.initial_state = (self.initial_cols, frozenset(), (0, 0, 0, 0))
        self.suits = {'S': 0, 'D': 1, 'H': 2, 'C': 3}
        self.rank_map = {str(i): i for i in range(2, 10)}
        self.rank_map.update({'A': 1, '0': 10, 'J': 11, 'Q': 12, 'K': 13})

    def heuristic(self, state):
        # Priority: Higher foundation count = Lower score (better)
        return 52 - sum(state[2])

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
        possible_states = []

        # 1. Foundation (Highest Priority)
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

        # 2. From Freecell to Foundation
        for card in free:
            rank, s_idx = self.rank_map[card[:-1]], self.suits[card[-1]]
            if rank == found[s_idx] + 1:
                new_free = set(free)
                new_free.remove(card)
                new_found = list(found)
                new_found[s_idx] = rank
                return [(tuple(tuple(c) for c in cols), frozenset(new_free), tuple(new_found))]

        # 3. Column to Column
        for i, col_from in enumerate(cols):
            if not col_from: continue
            card_from = col_from[-1]
            for j, col_to in enumerate(cols):
                if i == j: continue
                if not col_to or self.can_stack(card_from, col_to[-1]):
                    new_cols = [list(c) for c in cols]
                    new_cols[j].append(new_cols[i].pop())
                    possible_states.append((tuple(tuple(c) for c in new_cols), frozenset(free), tuple(found)))

        # 4. FreeCell to Column
        for card in free:
            for i, col in enumerate(cols):
                if not col or self.can_stack(card, col[-1]):
                    new_cols = [list(c) for c in cols]
                    new_cols[i].append(card)
                    new_free = set(free)
                    new_free.remove(card)
                    possible_states.append((tuple(tuple(c) for c in new_cols), frozenset(new_free), tuple(found)))

        # 5. Column to FreeCell (Lowest Priority)
        if len(free) < 4:
            for i, col in enumerate(cols):
                if col:
                    new_cols = [list(c) for c in cols]
                    card = new_cols[i].pop()
                    new_free = set(free)
                    new_free.add(card)
                    possible_states.append((tuple(tuple(c) for c in new_cols), frozenset(new_free), tuple(found)))

        return possible_states

    def solve(self):
        # Priority Queue stores: (priority_score, actual_steps, state, path)
        start_node = (self.heuristic(self.initial_state), 0, self.initial_state, [])
        pq = [start_node]
        visited = {self.initial_state: 0}

        count = 0
        while pq:
            _, steps, state, path = heapq.heappop(pq)
            count += 1
            
            if count % 5000 == 0:
                print(f"Checked {count} states... Current path depth: {steps}")

            if state[2] == (13, 13, 13, 13):
                return path + [state]

            for next_state in self.get_moves(state):
                new_steps = steps + 1
                # If we haven't seen this state OR found a shorter way to get here
                if next_state not in visited or new_steps < visited[next_state]:
                    visited[next_state] = new_steps
                    priority = new_steps + self.heuristic(next_state)
                    heapq.heappush(pq, (priority, new_steps, next_state, path + [state]))
        return None

# Use the same validate_and_parse function from previous response
def validate_and_parse():
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K']
    suits = ['S', 'D', 'H', 'C']
    full_deck = {r + s for r in ranks for s in suits}
    while True:
        print("\n--- Memory Efficient Solver ---")
        columns = []
        all_cards = []
        for i in range(8):
            col = input(f"Col {i+1}: ").strip().upper().split()
            columns.append(col)
            all_cards.extend(col)
        if len(all_cards) == 52 and len(set(all_cards)) == 52 and all(c in full_deck for c in all_cards):
            return columns
        print("❌ Invalid deck. Please ensure exactly 52 unique cards are entered.")

if __name__ == "__main__":
    initial_cols = validate_and_parse()
    solver = FreeCellSolver(initial_cols)
    result = solver.solve()
    if result:
        print(f"Success! Solved in {len(result)-1} moves.")
    else:
        print("No solution found.")
