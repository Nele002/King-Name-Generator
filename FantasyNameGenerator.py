import random

sub = [
    "Michael",
    "John",
    "Luke",
    "Evan",
    "Jim",
    "Joel",
    "Saul",
    "Donald",
    "Jeffery",
    "Craig",
    "Troy",
    "Andrew",
    "Ron",
    "Chris",
    "Leonard",
    "Felix"
]

adj = [
    "Great",
    "Terrible",
    "Evil",
    "Strong",
    "Big",
    "Small",
    "Hairy",
    "Dark",
    "Brave"
]

num = [
    "I",
    "II",
    "III",
    "IV",
    "V",
    "VI",
    "VII",
    "VIII",
    "IX",
    "X",
    "XI",
    "XII",
    "XIII",
    "XIV",
    "XV",
    "XVI"
]

print("Your new name is: " + adj[random.randrange(0, 9)] + " " +
      sub[random.randrange(0, 16)] + " " + num[random.randrange(0, 16)])
