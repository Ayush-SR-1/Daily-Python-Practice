import os
import string
import pickle
import random
from datetime import datetime

History_File = "code_history.dat"

def encode_word(word):
    
    if len(word) >= 3:
        
        pool = string.ascii_letters
        random_char1 = "".join(random.choices(pool, k=3))
        random_char2 = "".join(random.choices(pool, k=3))
        return random_char1 + word[1:] + word[0] + random_char2
    return word[::-1]

def decode_word(word):
    
    if len(word) >= 3:
        
        core = word[3:-3]
        return core[-1] + core[:-1]
    return word[::-1]

def encode_text(text):
    return " ".join(encode_word(w) for w in text.split())

def decode_text(text):
    return " ".join(decode_word(w) for w in text.split())

def load_history():
    
    if os.path.exists(History_File):
        try:
            with open(History_File, "rb") as f:
                return pickle.load(f)
        except EOFError:
            return []
    return []

def save_history(history):
    
    with open(History_File, "wb") as f:
        pickle.dump(history, f)

def log_entry(history, action, original, result):
    
    history.append({
        "Action": action,
        "Original": original,
        "Result": result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_history(history)

def show_history(history):
    
    if not history:
        print("No History Found.")
        return
    for i, entry in enumerate(history, start=1):
        print(f"{i}. [{entry['timestamp']}] {entry['Action']}: " f" '{entry['Original']}' -> {entry['Result']}")

def main():
    
    history = load_history()
    while True:
        
        print("\nChoose the option you want to continue with: ")
        print("1. Convert Text into Secert Code")
        print("2. Convert Secert Code into Text")
        print("3. View History")
        print("4. Exit")
    
        choice = int(input("Choice (1-4): "))
        
        if choice == 1:
            text = input("Enter the text to convert: ")
            result = encode_text(text)
            print("Secert Code:", result)
            log_entry(history, "encode", text, result)
        
        elif choice == 2:
            text = input("Enter the Secert Code to convert: ")
            result = decode_text(text)
            print("Decoded Code:", result)
            log_entry(history, "decode", text, result)
        
        elif choice == 3:
            show_history(history)
        
        elif choice == 4:
            print("---------- GoodBye !! -----------")
            break
        
        else:
            print("Invalid Input. Please Choose between (1-4).")

if __name__ == "__main__":
    main()

