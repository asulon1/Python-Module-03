# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/06 01:07:24 by sulon           #+#    #+#               #
#  Updated: 2026/03/06 02:48:50 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def parse_item(item: str):
    return item.split(':')


def get_total(inventory: dict):
    total = 0
    for value in inventory.values():
        total += value
    return total


def get_max_item(inventory: dict):
    max_value = list(inventory.values())[0]
    key_value = list(inventory.keys())[0]
    for key, value in inventory.items():
        if max_value < value:
            max_value = value
            key_value = key
    return key_value


def get_min_item(inventory: dict):
    min_value = list(inventory.values())[0]
    min_key = list(inventory.keys())[0]
    for key, value in inventory.items():
        if min_value > value:
            min_value = value
            min_key = key
    return min_key


print("=== Inventory System Analysis ==")
i = 1
inventory = {}
while i < len(sys.argv):
    parsed_arg = parse_item(sys.argv[i])
    inventory.update({parsed_arg[0]: int(parsed_arg[1])})
    i += 1

# Total and unique items
total = get_total(inventory)
print(f"Unique item types: {total}")
print(f"Unique item types: {len(inventory)}\n")

# Percent by item
print("=== Current Inventory ===")
for key, value in inventory.items():
    print(f"{key}: {value} unit{'s' if value > 1 else ''} "
          f"({(value / total * 100):.1f}%)")

# Most and less item in inventory
print("\n=== Inventory Statistics ===")
most_abundant = get_max_item(inventory)
least_abundant = get_min_item(inventory)
print(
    f"Most abundant:  {most_abundant} "
    f"({inventory[most_abundant]} "
    f"unit{'s' if inventory[most_abundant] > 1 else ''})")
print(
    f"Least abundant: {least_abundant} "
    f"({inventory[least_abundant]} "
    f"unit{'s' if inventory[least_abundant] > 1 else ''})\n")

# Moderate and scarce nested dict
print("=== Item Categories ===")
# TODO: nested dict
# Get produts whose restock's needed
print("=== Management Suggestions ===")
# TODO: in scarce dict key the min values

# Print keys, values
print("=== Dictionary Properties Demo ===")
print("Dictionary keys: ", end="")
for key in inventory.keys():
    print(key, end="")
    if key is not list(inventory.keys())[len(inventory) - 1]:
        print(",", end=" ")

print("\nDictionary values: ", end="")
for key, value in inventory.items():
    print(value, end="")
    if key is not list(inventory.keys())[len(inventory) - 1]:
        print(",", end=" ")

# inventory keys checker
lookup_str = "sword"
lookup_bool = False
if lookup_str in inventory:
    lookup_bool = True
print(f"\nSample lookup - '{lookup_str}' in inventory: {lookup_bool}")
