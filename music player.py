

import pygame

# Initialize pygame
pygame.init()

# Create a playlist of music filenames
playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]  # Replace with your actual song filenames

# Initialize the music player
pygame.mixer.init()

# Function to play music
def play_music(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

# Main loop
while True:
    print("Music Player")
    print("1. Play")
    print("2. Pause")
    print("3. Stop")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Select a song to play:")
        for idx, song in enumerate(playlist, start=1):
            print(f"{idx}. {song}")
        song_choice = int(input())
        if 1 <= song_choice <= len(playlist):
            play_music(playlist[song_choice - 1])
    elif choice == "2":
        pygame.mixer.music.pause()
    elif choice == "3":
        pygame.mixer.music.stop()
    elif choice == "4":
        pygame.mixer.music.stop()
        break

# Quit pygame
pygame.quit()
