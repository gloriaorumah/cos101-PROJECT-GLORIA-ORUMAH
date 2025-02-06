import tkinter as tk
from tkinter import ttk

print("Welcome to the German language dictionary, written by Elvis Jatau")

# The dictionary for English to German translation
German_dict = {
    "HELLO": "HALLO",
    "COME": "KOMMEN",
    "GO": "GEHEN",
    "FATHER": "VATER",
    "MOTHER": "MUTTER",
    "WATER": "WASSER",
    "GOOD BYE": "AUF WIEDERSEHEN",
    "THANK YOU": "DANKE", 
    "FOOD": "ESSEN",
    "LOVE": "LIEBE",
    "CLAN": "CLAN",
    "GOD": "GOTT",
    "HEAVEN": "HIMMEL",
    "RAIN": "REGEN",
    "SUN": "SONNE",
    "NECK": "NACKEN", 
    "SLEEP": "SCHLAFEN",
    "EYE": "AUGE",
}

# Lowercase lookup dictionary for case-insensitive searching
lookup_dict = {key.lower(): value for key, value in German_dict.items()}

# Translate function to find word translations
def translate(word):
    word = word.lower()  # Convert word to lowercase for case-insensitive comparison
    if word in lookup_dict:
        return lookup_dict[word]  # If the word is found, return the translation
    else:
        return "Word not found"  # If word is not found

# Main function for interactive terminal-based translation
def main():
    while True:
        word = input("Enter an English word to translate to German (or type 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            print("Exiting the program...")
            break  # Break the loop and end the program
        translation = translate(word)  # Get the translation
        print(f"The German translation of '{word}' is: {translation}")

# Tkinter GUI application
def open_gui():
    window = tk.Tk()
    window.title("German Language Dictionary")
    window.geometry("600x400")

    # Label at the top
    label = tk.Label(window, text="German Language Dictionary", font=("Arial", 20))
    label.pack(pady=10)

    # Search functionality
    entry_text = tk.StringVar()

    def search_word():
        word = entry_text.get().lower()
        translation = translate(word)
        if translation == "Word not found":
            result.set("Word not found.")
        else:
            result.set(f"Translation: {translation}")

    entry_field = tk.Entry(window, textvariable=entry_text, font=('Arial', 16), width=40)
    entry_field.pack(pady=20)

    search_btn = tk.Button(window, text="Search", command=search_word, font=("Arial", 14))
    search_btn.pack(pady=10)

    result = tk.StringVar()
    result_label = tk.Label(window, textvariable=result, font=("Arial", 16), wraplength=500)
    result_label.pack(pady=20)

    window.mainloop()

# Run the terminal-based dictionary and the GUI in parallel (choose one based on your need)
if __name__ == "__main__":
    # Uncomment below to run the command line version:
    # main()

    # Uncomment below to run the Tkinter GUI version:
    open_gui()
