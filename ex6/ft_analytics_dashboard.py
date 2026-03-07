# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/06 15:19:55 by sulon           #+#    #+#               #
#  Updated: 2026/03/08 00:18:32 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

players = [
    {
        "name": "alice",
        "score": 2300,
        "active": True,
        "region": "north",
        "achievements": {
            "first_kill", "level_10", "treasure_hunter",
            "speed_demon", "combo_master"
        }
    },
    {
        "name": "bob",
        "score": 1800,
        "active": True,
        "region": "east",
        "achievements": {
            "first_kill", "level_10", "boss_slayer"
        }
    },
    {
        "name": "charlie",
        "score": 2150,
        "active": True,
        "region": "central",
        "achievements": {
            "level_10", "treasure_hunter", "boss_slayer",
            "speed_demon", "perfectionist", "arena_champion"
        }
    },
    {
        "name": "diana",
        "score": 2050,
        "active": False,
        "region": "west",
        "achievements": {
            "first_kill", "collector"
        }
    }
]

print("=== Game Analytics Dashboard ===")

high_scorers = [p["name"] for p in players if p["score"] > 2000]
scores_doubled = [p["score"] * 2 for p in players]
active_names = [p["name"] for p in players if p["active"]]

print("\n=== List Comprehension Examples ===")
print(f"High scorers (>2000): {high_scorers}")
print(f"Scores doubled: {scores_doubled}")
print(f"Active players: {active_names}")

player_scores = {p["name"]: p["score"] for p in players}

all_cats = ["high" if p["score"] > 2000 else "medium" if p["score"]
            > 1500 else "low" for p in players]
# On compte dynamiquement
score_categories = {cat: all_cats.count(
    cat) for cat in sorted(set(all_cats))}

achievement_counts = {p["name"]: len(p["achievements"]) for p in players}

print("\n=== Dict Comprehension Examples ===")
print(f"Player scores: {player_scores}")
print(f"Score categories: {score_categories}")
print(f"Achievement counts: {achievement_counts}")

unique_players = {p["name"] for p in players}
unique_achievements = {ach for p in players for ach in p["achievements"]}
active_regions = {p["region"] for p in players if p["active"]}

print("\n=== Set Comprehension Examples ===")
print(f"Unique players: {unique_players}")
print(f"Unique achievements: {unique_achievements}")
print(f"Active regions: {active_regions}")

total_p = len(players)
avg_score = sum([p["score"] for p in players]) / total_p
top_p = max(players, key=lambda x: x["score"])

print("\n=== Combined Analysis ===")
print(f"Total players: {total_p}")
print(f"Total unique achievements: {len(unique_achievements)}")
print(f"Average score: {avg_score}")
print(f"Top performer: {top_p['name']} ({top_p['score']} points)")
