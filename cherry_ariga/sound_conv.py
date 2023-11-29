from gtts import gTTS
import os

file_name = "summary.txt"  # Change this to your file's name
try:
    with open(file_name, "r") as file:
        # Read the content of the file
        file_content = file.read()

        # Initialize the text-to-speech engine
        tts = gTTS(text=file_content, lang='en')
        # Save the generated speech as an audio file (e.g., "output.mp3")
        tts.save("output.mp3")

        # Play the generated audio file
        os.system("start output.mp3")
except FileNotFoundError:
    print(f"File '{file_name}' not found. Please make sure the file exists.")
except Exception as e:
    print(f"An error occurred: {e}")