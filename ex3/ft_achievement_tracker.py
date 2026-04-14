# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/05 17:14:28 by sulon           #+#    #+#               #
#  Updated: 2026/03/05 17:16:18 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


from typing import Set
import random


def gen_player_achievements() -> Set[str]:
    achivement_list = ['Boss Slayer', 'Collector Supreme', 'Crafting Genius',
                       'First Steps', 'Master Explorer', 'Sharp Mind',
                       'Speed Runner', 'Strategist', 'Survivor',
                       'Treasure Hunter', 'Untouchable', 'Unstoppable',
                       'World Savior']
    res = set()
    rand_len = random.randrange(1, len(achivement_list))
    while rand_len > 0:
        res.add(random.choice(achivement_list))
        rand_len -= 1

    return res


print("=== Achievement Tracker System ===\n")

alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()

print(f"Player Alice achievements: {alice}")
print(f"Player Bob achievements: {bob}")
print(f"Player Charlie achievements: {charlie}")
print(f"Player Dharlie achievements: {dylan}\n")

# # All unique achievements
all_achievement = alice.union(bob, charlie, dylan)

print(f"All distinct achievements: {all_achievement}\n")

# # Common achievements
print(
    f"Common to all players: "
    f"{alice.intersection(bob).intersection(charlie).intersection(dylan)}\n")

# Unique achivements by players
print(f"Only Alice has: {alice.difference(bob.union(charlie, dylan))}")
print(f"Only Bob has: {bob.difference(alice.union(charlie, dylan))}")
print(f"Only Charlie has: {charlie.difference(bob.union(alice, dylan))}")
print(f"Only Dylan has: {dylan.difference(bob.union(charlie, alice))}\n")


print(f"Alice is missing: {all_achievement - alice}")
print(f"Bob is missing: {all_achievement - bob}")
print(f"Charlie is missing: {all_achievement - charlie}")
print(f"Dylan is missing: {all_achievement - dylan}")
