#!/usr/local/bin/python3.4
player = int(input())


def thefunc(players):
    if players in (1, 2):
        return 1
    if players == 3:
        return 2

    min_players_on_before_level = 2
    min_players_on_this_level = 3
    rounds = 1
    while min_players_on_this_level <= player:
        temp = min_players_on_before_level
        min_players_on_before_level = min_players_on_this_level
        min_players_on_this_level = temp + min_players_on_this_level
        rounds += 1

    return rounds


print(thefunc(player))
