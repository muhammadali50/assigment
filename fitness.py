#Fitness Tracker: You're building a fitness tracker app. Create variables to store daily steps, 
#distance walked, and calories burned. Write expressions to calculate average steps per week 
#and total distance covered in a month.

daily_steps=int(input("Enter your daily steps: "))
distance_per_step=float(input("Enter your Step Length: "))
average_steps_per_week=daily_steps*7
print("Average Step In Week: ",average_steps_per_week)
total_steps_covered_in_month=daily_steps*30
print("Total Steps Covered In Month: ",total_steps_covered_in_month)
total_distance_walked=total_steps_covered_in_month*distance_per_step
print("The Total Distance Is: ",total_distance_walked)
calories_burned=total_distance_walked*0.04
print("Burned Calories: ",calories_burned)
