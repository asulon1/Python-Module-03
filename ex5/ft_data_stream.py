# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/06 15:19:55 by sulon           #+#    #+#               #
#  Updated: 2026/03/06 16:30:22 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Generator
import time


def event_generator(limit: int) -> Generator[dict, None, None]:
    names = ["alice", "bob", "charlie", "david", "eve"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, limit + 1):
        name = names[i % len(names)]
        action = actions[i % len(actions)]
        level = (i * 7) % 20 + 1

        yield {
            "id": i,
            "player": name,
            "level": level,
            "action": action
        }


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_number():
    num = 2
    while True:
        for d in range(2, num):
            if num % d == 0:
                break
        else:
            yield num
        num += 1


print("=== Game Data Stream Processor ===\n")
limit = 1000
print(f"Processing {limit} game events...\n")
total_events = 0
high_level_players = 0
treasures = 0
level_ups = 0

start_time = time.time()

for event in event_generator(limit):
    total_events += 1

    # Affichage des 3 premiers pour l'exemple
    if total_events <= 3:
        print(f"Event {event['id']}: Player {event['player']} "
              f"(level {event['level']}) {event['action']}")

    # Analyse à la volée
    if event['level'] >= 10:
        high_level_players += 1
    if event['action'] == "found treasure":
        treasures += 1
    if event['action'] == "leveled up":
        level_ups += 1

end_time = time.time()
print("...\n")
print("=== Stream Analytics ===")
print(f"Total events processed: {total_events}")
print(f"High-level players (10+): {high_level_players}")
print(f"Treasure events: {treasures}")
print(f"Level-up events: {level_ups}\n")
print("Memory usage: Constant (streaming)")
print(f"Processing time: {end_time - start_time:.3f} seconds\n")

print("=== Generator Demonstration ===")
print("Fibonacci sequence (first 10):", end=' ')
gen_fibonacci = fibonacci()
for i in range(10):
    print(next(gen_fibonacci), end='')
    if i < 9:
        print(",", end=" ")
    else:
        print()

print("Prime numbers (first 5):", end=' ')
gen_prime_number = prime_number()
for i in range(5):
    print(next(gen_prime_number), end='')
    if i < 4:
        print(",", end=" ")
    else:
        print()
