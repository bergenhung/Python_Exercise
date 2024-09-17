import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the audio file
audio_file = sr.AudioFile("./Downloads/se braquer.wav")

# Transcribe audio file
with audio_file as source:
    recognizer.pause_threshold = 0.8
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio_data = recognizer.record(source, duration=200)
try:
    transcription = recognizer.recognize_google(audio_data, language = 'fr')
    f = open("./Downloads/se braquer.txt", "w")
    f.write("Text:"+transcription)
    f.close()
except Exception as error:
    print("Exception:"+str(error))
