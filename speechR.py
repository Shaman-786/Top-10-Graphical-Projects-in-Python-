import speech_recognition as sr

def recognize_speech_from_mic():
    # Initialize the recognizer
    recognizer = sr.Recognizer()


    # Use the microphone as the source
    with sr.Microphone() as source:
        print("Please say something:")
        # Adjust for ambient noise and record audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results from the service.")

def recognize_speech_from_file(file_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)  # read the entire audio file

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results from the service.")

if __name__ == "__main__":
    # Uncomment the function you want to test
    
    # Recognize from microphone
    recognize_speech_from_mic()

    # Recognize from audio file
    # recognize_speech_from_file('path_to_your_audio_file.wav')
