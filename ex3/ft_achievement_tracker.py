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

print("=== Achievement Tracker System ===\n")

alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
           'speed_demon', 'perfectionist'}


print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}\n")

print("=== Achievement Analytics ===")
# Unique achievement
all_achievement = alice.union(bob).union(charlie)
print(f"All unique achievement: {all_achievement}")
print(f"Total unique achievements: {len(all_achievement)}\n")

# Common achievement
print(
    f"Common to all players: {alice.intersection(bob).intersection(charlie)}")

# Set the shared achievements between Alice, Bob and Charlie
shared = alice.intersection(bob).union(
    bob.intersection(charlie)).union(alice.intersection(charlie))

print(f"Rare achievements (1 player): {all_achievement.difference(shared)}\n")

print(f"Alice vs Bob common {alice.intersection(bob)}")
print(f"Alice unique: {alice.difference(bob, charlie)}")
print(f"Bob unique: {bob.difference(alice, charlie)}")
