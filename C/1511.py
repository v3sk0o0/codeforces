# http://codeforces.com/contest/1511/problem/C
from typing import List, Dict


def build_first_hit_hash(cards_colors: List[int]) -> Dict[int, int]:

    first_hit_location = dict()

    for index, value in enumerate(cards_colors, start=1):

        if value not in first_hit_location:
            first_hit_location[value] = index

    return first_hit_location


def solve(cards_colors: List[int], queries: List[int]) -> int:

    already_draw_card = []

    card_state = build_first_hit_hash(cards_colors)

    for query in queries:

        if query in already_draw_card:
            # we count from 1 the card index
            print(already_draw_card.index(query) + 1)
            already_draw_card.remove(query)
            already_draw_card.insert(0, query)
            continue

        location = card_state[query]
        print(location)
        already_draw_card.insert(0, query)
        # update state
        card_state = {
            key: value if value > location else value + 1
            for key, value in card_state.items()
        }
        card_state[query] = 1


if __name__ == "__main__":

    _n, _q = map(int, input().split())

    cards_colors = list(map(int, input().split()))

    queries = list(map(int, input().split()))

    solve(cards_colors, queries)
