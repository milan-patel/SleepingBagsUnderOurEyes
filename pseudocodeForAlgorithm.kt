


// App 
	/ Records breathing sound data -> csv
	/ accelorometer data -> csv (?)

	JAVA

	// Algorithm
		/ Identify disruptions in sleep patterns

	JAVA 

	// Sleep Tracker interface
		/ when and how long were you disrupted?







// 

establish a baseline, do you snore 

too loud -> go somewhere quieter


for entry in CSV:
	 noise_level <10 dB 
	 time 
	  if noise_level <10 dB 
	   time +=1 
	  if time > 10 
	  	disruptions += (begin_time, length)

	 return disruptions

DoYouHaveSleepApnea(disruptions):
	requiredNumberOfDisruptionsForSleepApnea = 15
	if(youSnore):
		requiredNumberOfDisruptionsForSleepApnea = 5
	numOfHours = convertToHours(csv[last].time - csv[0].time)
	if(disruptions.length/numOfHours >= requiredNumberOfDisruptionsForSleepApnea):
		return true
	else:
		return false




	