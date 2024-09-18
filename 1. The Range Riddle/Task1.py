# Write a program that prints off different moods for each day of the week.
# Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". 
# Using the range() function, loop through every day of the week and for each day, 
# randomly select a mood from the list and print it. 
# Ensure that your program includes the use of the random module to select the mood.

moods = ['Peaceful','Happy', 'Sad', 'Hungry', 'Tired', 'Lackisdaisical', 'Motivated', 'Burnt Out']
days_of_the_week = ['Monday', 'Tuesday','Wednesday', 'Thursday','Friday','Saturday','Sunday']
# Any feedback on list vs tuple? Advantages, disadvantages, etc. I discovered tuples when reading through some "Geeks for Geeks" articles. I sometimes find it beneficial to listen to the lesson,
# attempt the exercises, and refer to G4Gs for more of a step-by-step breakdown.  


for day in days_of_the_week: 
    import random
    print((("Today is " + day)+ "." + " I'm feeling " + random.choice(moods)) + ".") 


for days in range(1,8,1):
  import random
  print(("It's day #" + str(days) + "." + " I'm feeling " + random.choice(moods)) + ".") 


for day1 in range(len(days_of_the_week)):
    import random
    print(("Today is " + days_of_the_week[day1] + "." + " I'm feeling " + random.choice(moods)) + ".") 


# My thought process:
# loop #1: everything worked, but I didn't use range()
# loop #2: I was struggling to remember and find how to 
# loop #3: The bones of this came from ChatGPT. I cleaned it up and simplified it. Why is it necessicary to 