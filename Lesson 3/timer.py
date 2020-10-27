from datetime import timedelta
import time



print("Timer version 0.1")
print("Available values: seconds")
print("Timer receives values from 1 to 60 in seconds")

timer_value = int(input("Enter timer value: "))

assert timer_value <= 60, "You have entered more than 60 seconds"
assert timer_value > 0, "You have entered less than 1 second"

time_delta = timedelta(seconds=timer_value)

print(time_delta)

start = input("Start timer? [y/n] ")

if start == "y":

	start_time = round(time.time())
	end_time = start_time + timer_value
	print(time_delta)

	while start_time != end_time:
		start_time += 1
		timer_value -= 1
		time_delta = timedelta(seconds=timer_value)
		time.sleep(1)
		print(time_delta)

elif start == "n":
	print("Exiting program")
else:
	print("You didn't enter y or n")
