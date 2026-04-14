# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_alchemist.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/06 15:19:55 by sulon           #+#    #+#               #
#  Updated: 2026/04/14 22:30:13 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
import random

print("=== Game Analytics Dashboard ===")

players = ['Alice', 'bob', 'Charlie', 'dylan',
           'Emma', 'Gregory', 'john', 'kevin', 'Liam']

print(f"Initial list of players: {players}")

capitalized_list = []
for player in players:
    capitalized_list.append(player.capitalize())

print(f"New list with all names capitalized: {capitalized_list}")

upper_list = []
for player in players:
    if player[0].isupper():
        upper_list.append(player)

print(f"New list of capitalized names only {upper_list}")

scoreboard = {}

for player in capitalized_list:
    scoreboard.update({player: random.randint(0, 1000)})

print(f"Score dict : {scoreboard}")
total = sum(scoreboard.values())
average = total / len(scoreboard)
print(f"Score average is {average:.2f}")

high_scores = {}
for key, value in scoreboard.items():
    if value > average:
        high_scores.update({key: value})

print(f"High_scores: {high_scores}")
