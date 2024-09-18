# Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day
# (morning, afternoon, evening) for each day of the week. 
# Use nested loops to implement this: the outer loop should iterate over the days, 
# and the inner loop should iterate over the times of the day. 
# For each time, randomly select a mood from a predefined list and print it.
# Use the random module again to randomly select the mood.

import random

time_of_day = ['Morning', 'Afternoon', 'Evening']
days_of_the_week = ['Monday', 'Tuesday','Wednesday', 'Thursday','Friday','Saturday','Sunday']
moods = ['Peaceful','Happy', 'Sad', 'Hungry', 'Tired', 'Lackisdaisical', 'Motivated', 'Burnt Out']

for day in days_of_the_week:
    for time in time_of_day:
        print(("It is " + day + " " + time + ".") + (" It looks like you are " + random.choice(moods) + "!"))


# I wanted to experiment:
moods = []

for day in days_of_the_week:
    for time in time_of_day:
        print(("It is " + day + " " + time + ".") + (" How are you feeling?"))
        mood = input()
        moods.append(mood)
print(moods)