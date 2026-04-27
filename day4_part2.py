# Day 4 Python - Ranking System

responses = [
    "Objects fall because of gravity.",
    "Objects fall due to gravity pulling them toward Earth.",
    "Objects fall due to gravitational force attracting masses."
]

# Rank by length (simple logic)
ranked = sorted(responses, key=len, reverse=True)

for i, r in enumerate(ranked, 1):
    print(f"{i}. {r}")
