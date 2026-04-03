# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/26 05:49:55 by asulon          #+#    #+#               #
#  Updated: 2026/02/26 06:22:59 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

print("=== Command Quest ===")

print(f"Program name: {sys.argv[0].split('/')[1]}")
if len(sys.argv) > 1:
    print(f"Arguments received: {len(sys.argv) - 1}")
    i = 1
    while i < len(sys.argv):
        print(f"Argument {i}: ", end="")
        print(sys.argv[i])
        i += 1
else:
    print("No arguments provided!")

print(f"Total arguments: {len(sys.argv)}")
