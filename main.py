import pandas as pd
import speech_recognition as sr
import pyttsx3
engine=pyttsx3.init()

def takecommand():
  recognizer = sr.Recognizer()

  with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("start speaking")
    audio=recognizer.listen(source)
  try:
     print("Recorded")
     speech=recognizer.recognize_google(audio)
     speech = speech.lower()
     print(f"user said: {speech}")
  except:
      print("say again")
      return "None"
  return speech

while True:
      dataset = pd.read_csv('Data.csv')

      query = takecommand().lower()
      if "tell me column names" in query:
        print(dataset.columns)

      elif "null values" in query:
        print(dataset.isnull().sum())
      elif "shape of data set" in query:
        print(dataset.shape)
      elif "first 10 rows" in query:
        print(dataset.head(10))
      elif "sleep" in query:
          break




