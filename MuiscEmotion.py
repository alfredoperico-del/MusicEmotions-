import winsound  # to play audio
import os       # to handle file paths
import random   # to randomly select a song from a list


# Folder where your music files are stored
base_folder = "C:/Users/Asus/OneDrive/Desktop/Music"


# Manual mapping of keywords to emotions
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
    "calm": "calm",
    "relaxed": "calm",
    "peaceful": "calm",
    "chill": "calm"
}

# Prepare music files manually for each emotion
# Each emotion has a list of corresponding .wav files
music_files = {
    "happy": [os.path.join(base_folder, "happy i guess.wav")],
    "sad": [os.path.join(base_folder, "sad i guess.wav")],
    "romantic": [os.path.join(base_folder, "romantic i guess.wav")],
    "calm": [os.path.join(base_folder, "calm i guess.wav")]
}

# # Using relative path so the code works on any computer

base_folder = os.path.join(os.path.dirname(__file__), "Music") 


# Show available keywords to user

available_emotions = ", ".join(set(keyword_to_emotion.keys())) + ", stop"

# Main loop to ask user how they feel
while True:
    sentence = input(f"Tell me how you are feeling today! or type 'exit' to quit: ").lower()
    

    # Exit command
    if "exit" in sentence:
        winsound.PlaySound(None, winsound.SND_ASYNC)  # stop any music
        print("Goodbye!")
        break
    
    # Stop current music
    elif "stop" in sentence:
        winsound.PlaySound(None, winsound.SND_ASYNC)
        print("Music stopped.")
    
    # Detect emotion keywords and play music
    else:
        played = False
        for keyword, emotion in keyword_to_emotion.items():  # check each keyword
            if keyword in sentence and emotion in music_files and music_files[emotion]:  # if keyword detected
                winsound.PlaySound(None, winsound.SND_ASYNC)  # stop previous music
                song_path = random.choice(music_files[emotion])  # choose random song from list
                print(f"Detected '{keyword}' → Playing {emotion} music: {song_path}")
                winsound.PlaySound(song_path, winsound.SND_FILENAME | winsound.SND_ASYNC)  # play song asynchronously
                played = True
                break  # play only the first detected keyword
        
        # No emotion detected
        if not played:
            print("No recognizable emotion found in your sentence.")
