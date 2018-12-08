from datetime import datetime, timedelta
from collections import defaultdict

print("advent of code 2018 - day 4")

with open("input.txt") as file:
    lines = [line.strip() for line in file]

# day 4 - part 1

activities = []

for line in lines:
    timestamp_string = line.split("[")[1].split("]")[0].strip()
    timestamp = datetime.strptime(timestamp_string, "%Y-%m-%d %H:%M")
    activity = line.split("]")[1].strip()

    activities.append((timestamp, activity))

activities.sort()

activities_by_guard = defaultdict(list)
sleep_by_guard = []
guard_id = 0

# build a dictionary { guard_id -> list of (timestamp, activity) }
for (timestamp, activity) in activities:
    if "Guard" in activity:
        guard_id = int(activity.split("#")[1].split(" ")[0])

    activities_by_guard[guard_id] += [(timestamp, activity)]

# for each guard, identify number of minutes sleeping
for guard_id in activities_by_guard.keys():
    time_sleeping = 0
    previous_timestamp = datetime(900, 1, 1)

    for (timestamp, activity) in activities_by_guard[guard_id]:
        current_timestamp = timestamp
        if activity == "wakes up":
            duration = int((current_timestamp - previous_timestamp).total_seconds()/60)
            time_sleeping += duration

        previous_timestamp = current_timestamp

    sleep_by_guard.append((guard_id, time_sleeping))

sleep_by_guard.sort(key=lambda t: t[1], reverse=True)
sleepy_guard_id = sleep_by_guard[0][0] # ID = 797

print(activities_by_guard[sleepy_guard_id])
sleeping_minutes = [0 for i in range(59)]
previous_timestamp = datetime(900, 1, 1)

for (timestamp, activity) in activities_by_guard[sleepy_guard_id]:
    current_timestamp = timestamp
    if activity == "wakes up":
        minute_falls_asleep = previous_timestamp.minute
        minute_wakes_up= current_timestamp.minute
        for i in range(minute_falls_asleep, minute_wakes_up):
            sleeping_minutes[i] += 1

    previous_timestamp = current_timestamp

max_value = max(sleeping_minutes)
max_index = sleeping_minutes.index(max_value)

print("part 1: " + str(sleepy_guard_id * max_index))

# day 4 - part 2

