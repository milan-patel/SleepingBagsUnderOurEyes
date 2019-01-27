from pydub import AudioSegment, silence

myaudio = AudioSegment.from_wav("apnea_0_4.wav")

silence = silence.detect_silence(myaudio, min_silence_len=1000, silence_thresh=-70)

silence = [((start/1000),(stop/1000)) for start,stop in silence] #convert to sec

apnea = 0
realSilences = []
episodes = 0

for period in silence:
	if (period[1] - period[0]) > 10:
		realSilences.append(period)
		episodes+=1

print(realSilences)

if len(realSilences) > 15: # current audio is like 5 minutes
	apnea = 1

if (apnea):
    print("You likely have sleep apnea")
else:
    print("It in unlikely you have sleep apnea")
