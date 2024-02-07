#Time Management Tool: Develop a tool to track time spent on various activities. Use variables to 
#store task names and durations. Write expressions to calculate total time spent on each task and 
#identify areas for improvement.



task1=float(input("Enter your today's gym time: "))
print(f"Your today's gym time is: {task1} hours")
task2=float(input("Enter your today's study time: "))
print(f"Your today's study time is: {task2} hours: ")
task3=float(input("Enter your today's wached movies time: "))
print(f"Your today's watched movies time is: {task3} hours: ")

sum=(task1+task2+task3)
print(f"Your total time spent on all tasks: {sum} in hours")
