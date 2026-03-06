# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/06 01:07:24 by sulon           #+#    #+#               #
#  Updated: 2026/03/06 15:14:12 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

ITEM_TYPE = {
    "sword": "weapon",
    "potion": "consumable",
    "shield": "armor",
    "armor": "armor",
    "helmet": "armor"
}

ITEM_VALUES = {
    "sword": 100,
    "potion": 25,
    "shield": 80,
    "armor": 200,
    "helmet": 50
}


def parse_item(item: str):
    return item.split(':')


def get_total(inventory: dict):
    total = 0
    for data in inventory.values():
        total += data.get("quantity", 0)
    return total


def get_max_item(inventory: dict):
    max_value = list(inventory.values())[0]["quantity"]
    key_value = list(inventory.keys())[0]
    for item in inventory.values():
        if max_value < item["quantity"]:
            max_value = item["quantity"]
            key_value = item["name"]
    return key_value


def get_min_item(inventory: dict):
    min_value = list(inventory.values())[0]["quantity"]
    key_value = list(inventory.keys())[0]
    for item in inventory.values():
        if min_value > item["quantity"]:
            min_value = item["quantity"]
            key_value = item["name"]
    return key_value


def create_inventory(item: list[str]):
    return {item[0]: {
        "name": item[0],
        "type": ITEM_TYPE.get(item[0], "unknown"),
        "quantity": int(item[1]),
        "value": ITEM_VALUES.get(item[0], 0)
    }}


print("=== Inventory System Analysis ==")
i = 1
inventory = {}
category = {"Moderate": {}, "Scarce": {}}
restock = {}
while i < len(sys.argv):
    parsed_arg = parse_item(sys.argv[i])
    inventory.update(create_inventory(parsed_arg))
    if int(parsed_arg[1]) > 3:
        category["Moderate"].update({parsed_arg[0]: int(parsed_arg[1])})
    else:
        category["Scarce"].update({parsed_arg[0]: int(parsed_arg[1])})
        if int(parsed_arg[1]) <= 1:
            restock.update({parsed_arg[0]: {"name": parsed_arg[0]}})
    i += 1


# Total and unique items
total = get_total(inventory)
print(f"Unique item types: {total}")
print(f"Unique item types: {len(inventory)}\n")

# Percent by item
print("=== Current Inventory ===")
for item in inventory.values():
    print(f"{item["name"]}: {item["quantity"]} "
          f"unit{'s' if item["quantity"] > 1 else ''} "
          f"({(item["quantity"] / total * 100):.1f}%)")

# Most and less item in inventory
print("\n=== Inventory Statistics ===")
most_abundant = get_max_item(inventory)
least_abundant = get_min_item(inventory)
print(
    f"Most abundant:  {most_abundant} "
    f"({inventory[most_abundant]["quantity"]} "
    f"unit{'s' if inventory[most_abundant]["quantity"] > 1 else ''})")
print(
    f"Least abundant: {least_abundant} "
    f"({inventory[least_abundant]["quantity"]} "
    f"unit{'s' if inventory[least_abundant]["quantity"] > 1 else ''})\n")

# Moderate and scarce nested dict
print("=== Item Categories ===")
print(f"Moderate: {category["Moderate"]}")
print(f"Scarce: {category["Scarce"]}\n")

# Get produts whose restock's needed
print("=== Management Suggestions ===")
print("Restock needed: ", end="")
for item in restock.values():
    print(item["name"], end="")
    if item["name"] is not list(restock.keys())[len(restock) - 1]:
        print(",", end=" ")

# Print keys, values
print("\n=== Dictionary Properties Demo ===")
print("Dictionary keys: ", end="")
for key in inventory.keys():
    print(key, end="")
    if key is not list(inventory.keys())[len(inventory) - 1]:
        print(",", end=" ")

print("\nDictionary values: ", end="")
for item in inventory.values():
    print(item["quantity"], end="")
    if item["name"] is not list(inventory.keys())[len(inventory) - 1]:
        print(",", end=" ")

# inventory keys checker
lookup_str = "sword"
lookup_bool = False
if lookup_str in inventory:
    lookup_bool = True
print(f"\nSample lookup - '{lookup_str}' in inventory: {lookup_bool}")
