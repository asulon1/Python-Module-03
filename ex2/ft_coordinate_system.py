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


def parse_coordinate(coord_str: str):
    parts = coord_str.split(',')
    res = tuple(int(part) for part in parts)
    return res


def estimate_distance(base_coord: tuple, coord: tuple):
    return math.sqrt((coord[0] - base_coord[0])**2 +
                     (coord[1] - base_coord[1])**2 +
                     (coord[2] - base_coord[2])**2).__round__(2)


print("=== Game Coordinate System ===\n")

base_coord = (0, 0, 0)
current_pos = ()

# coord1
coord1 = (10, 20, 5)
current_pos = coord1
print(f"Position created: {current_pos}")
print(
    f"Distance between {base_coord} and {current_pos}"
    f": {estimate_distance(base_coord, current_pos)}\n")

# coord2
coord2 = "3,4,0"
try:
    print(f'Parsing coordinates: "{coord2}"')
    current_pos = parse_coordinate(coord2)
    print(f"Parsed position: {current_pos}")
    print(
        f"Distance between {base_coord} and {current_pos}"
        f": {estimate_distance(base_coord, current_pos)}\n")
except ValueError as error:
    print(f"Error parsing coordinates: {error}")
    print(f"Error details - Type: {type(error).__name__}, Args: {error.args}")

# Coord3
coord3 = "abc,def,ghi"
try:
    print(f'Parsing invalid coordinates: "{coord3}"')
    current_pos = parse_coordinate(coord3)
    print(f"Parsed position: {current_pos}")
    print(
        f"Distance between {base_coord} and {current_pos}")
except ValueError as error:
    print(f"Error parsing coordinates: {error}")
    print(
        f"Error details - Type: {type(error).__name__}, Args: {error.args}\n")

# Unpacking demonstration:
x, y, z = current_pos
print("Unpacking demonstration:")
print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")
