import tkinter as tk
from tkinter import messagebox

class LanguageLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Learning App")

        self.word_label = tk.Label(root, text="Enter Word:")
        self.word_label.pack()

        self.word_entry = tk.Entry(root)
        self.word_entry.pack()

        self.translation_label = tk.Label(root, text="Enter Translation:")
        self.translation_label.pack()

        self.translation_entry = tk.Entry(root)
        self.translation_entry.pack()

        self.add_button = tk.Button(root, text="Add Word", command=self.add_word)
        self.add_button.pack()

        self.word_listbox = tk.Listbox(root)
        self.word_listbox.pack()

    def add_word(self):
        word = self.word_entry.get()
        translation = self.translation_entry.get()

        if word and translation:
            self.word_listbox.insert(tk.END, f"{word} - {translation}")
            self.word_entry.delete(0, tk.END)
            self.translation_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Both word and translation are required.")

def main():
    root = tk.Tk()
    app = LanguageLearningApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
