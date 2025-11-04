# MusicEmotions-
**1. Project Title & Short Description**

Title: Music Emotion 

Description: Python program that plays .wav music based on user-inputted emotions or keywords, such as happy, sad, romantic, angry, and calm. Users can type sentences like "I feel joyful today," and the program will detect keywords and play the corresponding music.

**2. Features / Functionality (in paragraph form)**

Detects emotions from typed words and plays matching .wav files.

Accepts full sentences and recognizes keywords or synonyms (e.g., "joyful" → happy, "love" → romantic).

Allows stopping music with stop and exiting the program with exit.

Randomly selects a song if multiple tracks exist for the same emotion.

Uses relative paths, so the project works on any computer with the same folder structure.

**3. Folder Structure**
MusicEmotionProject/
├─ MuiscEmotion.py      <-- Python script
├─ Music/               <-- Folder containing all .wav files
│  ├─ happy.wav
│  ├─ sad.wav
│  ├─ romantic.wav
│  ├─ angry.wav
│  └─ calm.wav
├─ ConceptMap1.jpg      <-- optional visual for reflection
└─ JournalNotes.pdf     <-- optional visual for reflection

4. How to Run

Make sure Python 3.x is installed on Windows.

Keep all .wav files in the Music folder.

Open a terminal in the project folder.

Run the script:

python MuiscEmotion.py


Type a sentence describing your emotion (e.g., "I feel happy today").

Type stop to stop music or exit to close the program
