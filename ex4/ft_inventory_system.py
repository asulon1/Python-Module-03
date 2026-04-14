# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/06 01:07:24 by sulon           #+#    #+#               #
#  Updated: 2026/04/14 17:35:14 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def parse_item(item: str) -> list[str]:
    return item.split(':')


def get_total(inventory: dict) -> int:
    total = 0
    for quantity in inventory.values():
        total += quantity
    return total


def get_max_item(inventory: dict) -> str:
    max_value = list(inventory.values())[0]
    key_value = list(inventory.keys())[0]
    for key, value in inventory.items():
        if max_value < value:
            max_value = value
            key_value = key
    return key_value


def get_min_item(inventory: dict) -> str:
    min_value = list(inventory.values())[0]
    key_value = list(inventory.keys())[0]
    for key, value in inventory.items():
        if min_value > value:
            min_value = value
            key_value = key
    return key_value


print("=== Inventory System Analysis ==")
i = 1
inventory = {}

while i < len(sys.argv):
    parsed_arg = parse_item(sys.argv[i])
    if parsed_arg[0] not in inventory:
        if len(parsed_arg) == 2:
            try:
                inventory.update({parsed_arg[0]: int(parsed_arg[1])})
            except ValueError as error:
                print(f"Quantity error for '{parsed_arg[0]}' {error}")
        else:
            print(f"Error - invalid parameter: '{sys.argv[i]}'")
    else:
        print(f"Redundant item '{parsed_arg[0]}' - discarding")
    i += 1

# Inventory
print(f"Got inventory: {inventory}")

# Item list
items = []
for key in inventory.keys():
    items.append(key)
print(f"Item list: {items}")

total = get_total(inventory)
print(f"Total quantity of the {len(inventory)} items: {total}")

# Percent by item
for key, value in inventory.items():
    print(f"Item {key} represents "
          f"{(value / total * 100):.1f}%")

# # Most and less item in inventory
most_abundant = get_max_item(inventory)
least_abundant = get_min_item(inventory)
print(
    f"Item most abundant: "
    f"{most_abundant} with quantity {inventory[most_abundant]}")

print(
    f"Item least abundant: "
    f"{least_abundant} with quantity {inventory[least_abundant]}")

# Update with magic_item : 1
inventory.update({"magic_item": 1})
print(f"Updated inventory: {inventory}")
