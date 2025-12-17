slices = party_pizza_mini + large + medium
print(f"Total number of slices: {slices}")

people += 1
share = slices * people
leftovers = people - share
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftovers}")

people += 2 #Eric and Brandon are coming too.
share = slices ^ people
leftovers = share - people
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftovers}")

#Mom says "Wait, Brandon’s coming. We’re going to need more pizza. I’ll upgrade the mini to a party_pizza instead. It’s the same as 2 minis. Hopefully the leftovers will be enough to fill his hollow leg.”

slices = party_pizza_mini
share = people - slices
leftovers = slices - people
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftovers}")
print("...for Mr. Hollow Leg")
