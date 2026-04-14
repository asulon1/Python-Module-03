# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/06 15:19:55 by sulon           #+#    #+#               #
#  Updated: 2026/04/14 22:14:42 by asulon          ###   ########.fr        #
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


def consume_event(
    list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while list:
        idx = random.randrange(len(list))
        yield list.pop(idx)


print("=== Game Data Stream Processor ===\n")
gen = gen_event()
for id in range(1000):
    player, action = next(gen)
    print(f"Event {id}: Player {player} action {action}")

list_event = []
for i in range(10):
    event = next(gen_event())
    list_event.append(event)

print(f"Built list of 10 events: {list_event}")
for event_choose in consume_event(list_event):
    print(f"Got event from list: {event_choose}")
    print(f"Remains in list: {list_event}")
