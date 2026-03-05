# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/26 06:29:40 by asulon          #+#    #+#               #
#  Updated: 2026/03/05 16:08:38 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

print("=== Player Score Analytics ===")
if len(sys.argv) == 1:
    print("No score provided."
          "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
    score_list = []

    i = 1
    while i < len(sys.argv):
        try:
            score_list.append(int(sys.argv[i]))
        except ValueError:
            print(f"oops, I typed '{sys.argv[i]}' instead of '1000'")
        i += 1
    print(f"Scores processed: {score_list}")
    print(f"Total players: {len(score_list)}")
    print(f"Total score: {sum(score_list)}")
    print(f"Average score: {sum(score_list) / len(score_list)}")
    print(f"High score: {max(score_list)}")
    print(f"Low score: {min(score_list)}")
    print(f"Score range: {max(score_list) - min(score_list)}")
