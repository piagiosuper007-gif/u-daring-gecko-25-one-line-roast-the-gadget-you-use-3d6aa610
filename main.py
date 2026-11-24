import os

ROAST = "My phone has 128 gigs and still begs me to delete photos of food I ate in 2021, as if it were the one who paid for lunch."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ROAST)
