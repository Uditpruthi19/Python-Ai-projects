import random
import time

def typing_speed_test():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a powerful and versatile programming language.",
        "Practice makes perfect when it comes to typing.",
        "Coding is like solving puzzles with your computer.",
        "Typing speed can be improved with consistent practice."
    ]
    
    sentence = random.choice(sentences)
    print("Type the following sentence:")
    print(sentence)
    
    input("Press Enter when you are ready to start...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    correct_chars = sum(a == b for a, b in zip(user_input, sentence))
    accuracy = (correct_chars / len(sentence)) * 100
    typing_speed = (len(sentence) / elapsed_time) * 60
    
    print("\nTime taken: {:.2f} seconds".format(elapsed_time))
    print("Accuracy: {:.2f}%".format(accuracy))
    print("Typing Speed: {:.2f} characters per minute".format(typing_speed))

if __name__ == "__main__":
    typing_speed_test()
