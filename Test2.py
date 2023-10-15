import random
import time

# Morse code dictionary
morse_code_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.', 
    'G': '--.',    'H': '....',   'I': '..', 
    'J': '.---',   'K': '-.-',    'L': '.-..', 
    'M': '--',     'N': '-.',     'O': '---', 
    'P': '.--.',   'Q': '--.-',   'R': '.-.', 
    'S': '...',    'T': '-',      'U': '..-', 
    'V': '...-',   'W': '.--',    'X': '-..-', 
    'Y': '-.--',   'Z': '--..', 
}

def get_random_word():
    letters = list(morse_code_dict.keys())
    word_length = random.randint(2, 4)
    return ''.join(random.choice(letters) for _ in range(word_length))

def get_morse_code(word):
    return ' '.join(morse_code_dict[letter] for letter in word)

def get_user_input():
    return input("Enter the Morse code for the word: ")

def main():
    print("Morse Code Training - Enter 'exit' to quit.")
    while True:
        random_word = get_random_word()
        morse_code = get_morse_code(random_word)
        print("Word: ", random_word)
        start_time = time.time()
        user_input = get_user_input().upper()
        end_time = time.time()

        if user_input == "EXIT":
            break
        
        correct_answer = morse_code

        if user_input == correct_answer:
            print("Correct! Time taken: {:.2f} seconds".format(end_time - start_time))
        else:
            print("Incorrect. The correct Morse code is: {}".format(correct_answer))

if __name__ == "__main__":
    main()
