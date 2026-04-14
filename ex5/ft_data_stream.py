# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/06 15:19:55 by sulon           #+#    #+#               #
#  Updated: 2026/04/14 19:05:28 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["eat", "sleep", "run", "grab", "move", "climb", "swim"]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(list: dict[str, str]) -> None:
    pass


print("=== Game Data Stream Processor ===\n")

for id in range(1000):
    player, action = next(gen_event())
    print(f"Event {id}: Player {player} action {action}")
