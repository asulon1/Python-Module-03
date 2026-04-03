# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/05 17:14:28 by sulon           #+#    #+#               #
#  Updated: 2026/03/05 17:16:18 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math


def estimate_distance(base_coord: tuple, coord: tuple) -> float:
    """Calculate distance between 2 coord x,y,z"""
    return math.sqrt((coord[0] - base_coord[0])**2 +
                     (coord[1] - base_coord[1])**2 +
                     (coord[2] - base_coord[2])**2)


def get_player_pos() -> tuple[float, float, float]:
    """Asking user x,y,z player coordonate"""
    while True:
        try:
            raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        except KeyboardInterrupt:
            # Avoid error on interrupt
            return (0, 0, 0)

        # get coords
        parts = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(parts[0].strip())
            y = float(parts[1].strip())
            z = float(parts[2].strip())
        except ValueError as error:
            print("Error on parameter"
                  f"{str(error).rsplit(":", maxsplit=1)[-1]}: {error}")
            continue

        return (x, y, z)


print("=== Game Coordinate System ===\n")
print("Get a first set of coordinates")
center_coord: tuple[int, int, int] = (0, 0, 0)

try:
    # 1st pos
    player_pos = get_player_pos()
    print(f"Got a first tuple: {player_pos}")
    print(f"It includes: X={player_pos[0]}, "
          f"Y={player_pos[1]}, Z={player_pos[2]}")
    print("Distance to center: "
          f"{estimate_distance(player_pos, center_coord):.4f}\n")

    # 2nd pos
    print("Get a second set of coordinates")
    second_pos = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{estimate_distance(player_pos, center_coord):.4f}")
except (ValueError, KeyboardInterrupt) as error:
    print(error)
