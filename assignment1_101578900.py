"""
Author: Joshua Zaakir
Assignment: #1
"""

# Step b: Create 4 variables
#string
gym_member = "Alex Alliton"

#float
preferred_weight_kg = 20.5

#integer
highest_reps = 25

#boolean 
membership_active = True

# Step c: Create a dictionary named workout_stats
#dictionary for peoples workout stats
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 30, 35),
    "Taylor": (25, 50, 45)
}


# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend in list(workout_stats.keys()):
    total = sum(workout_stats[friend])
    workout_stats[friend + "_Total"] = total


# Step e: Create a 2D nested list called workout_list
workout_list = []

for friend in workout_stats:
    if "_Total" not in friend:
        workout_list.append(list(workout_stats[friend]))

# Step f: Slice the workout_list
print ("Yoga and Running minutes:")
for row in workout_list:
    print(row[0:2])

# Step g: Check if any friend's total >= 120
for friend in workout_stats:
    if "_Total" in friend:
        if workout_stats[friend] >= 120:
            name = friend.replace("_Total", "")
            print(f"Great job staying active, {name}!")

# Step h: User input to look up a friend
name = input("\nEnter a friend's name: ")

if name in workout_stats:
    data = workout_stats[name]
    total = workout_stats[name + "_Total"]

    print(f"\n{name}'s Workout Details:")
    print("Yoga:", data[0], "minutes")
    print("Running:", data[1], "minutes")
    print("Weightlifting:", data[2], "minutes")
    print("Total:", total, "minutes")

else:
    print(f"Friend {name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {}

for friend in workout_stats:
    if "_Total" in friend:
        name = friend.replace("_Total", "")
        totals[name] = workout_stats[friend]

highest = max(totals, key=totals.get)
lowest = min(totals, key=totals.get)

print("\nSummary:")
print("Highest total workout:", highest)
print("Lowest total workout:", lowest)
