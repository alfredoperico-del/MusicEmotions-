import winsound  # Module for playing sound on Windows
import os        # Module to handle file paths
import random    # Module to randomly choose a song if multiple exist


# 1. Define the folder containing your music
# Using relative path so the code works on any computer
base_folder = os.path.join(os.path.dirname(__file__), "Music")

# 2. Map keywords to emotions
# You can manually add more keywords for each emotion
keyword_to_emotion = {
    "happy": "happy",
    "joyful": "happy",
    "cheerful": "happy",
    "sad": "sad",
    "sadness": "sad",
    "down": "sad",
    "romantic": "romantic",
    "love": "romantic",
    "loving": "romantic",
    "angry": "angry",
    "mad": "angry",
    "frustrated": "angry",
    "calm": "calm",
    "relaxed": "calm",
    "peaceful": "calm"
}

# 3. Load WAV files from Music folder
music_files = {}  # dictionary: key=emotion, value=list of WAV file paths

# Scan folder for WAV files
for file in os.listdir(base_folder):
    if file.lower().endswith(".wav"):
        fname_lower = file.lower()
        # The first word of the file name is used as the emotion
        emotion = fname_lower.split()[0]
        if emotion not in music_files:
            music_files[emotion] = []
        music_files[emotion].append(os.path.join(base_folder, file))

# 4. Program loop
print("Welcome! Type how you are feeling (e.g., 'I feel happy today').")
print("Type 'stop' to stop music, or 'exit' to quit the program.\n")

while True:
    sentence = input("Your input: ").lower()

    # Exit program
    if "exit" in sentence:
        winsound.PlaySound(None, winsound.SND_ASYNC)  # stop music
        print("Goodbye!")
        break

    # Stop current music
    elif "stop" in sentence:
        winsound.PlaySound(None, winsound.SND_ASYNC)
        print("Music stopped.")

    # Detect emotion and play music
    else:
        played = False
        for keyword, emotion in keyword_to_emotion.items():
            if keyword in sentence and emotion in music_files and music_files[emotion]:
                # Stop any previous music
                winsound.PlaySound(None, winsound.SND_ASYNC)
                # Choose a random song for variety
                song_path = random.choice(music_files[emotion])
                print(f"Detected '{keyword}' → Playing {emotion} music: {song_path}")
                winsound.PlaySound(song_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
                played = True
                break  # play only the first detected keyword
        
        if not played:
            print("No recognizable emotion found in your sentence.")
