import tkinter as tk
from tkinter import scrolledtext
from summarizer import summarize_text
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def generate_summary():
    text = input_text.get("1.0", tk.END)

    if not text.strip():
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter some text!")
        return

    summary = summarize_text(text, 3)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, summary)


def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


# GUI Setup
root = tk.Tk()
root.title("Financial News Summarizer")
root.geometry("750x550")

tk.Label(root, text="Enter Financial News:", font=("Arial", 14)).pack(pady=5)

input_text = scrolledtext.ScrolledText(root, height=10, wrap=tk.WORD)
input_text.pack(padx=10, pady=10)

tk.Button(root, text="Summarize", command=generate_summary, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Clear", command=clear_text).pack(pady=5)

tk.Label(root, text="Summary:", font=("Arial", 14)).pack(pady=5)

output_text = scrolledtext.ScrolledText(root, height=10, wrap=tk.WORD)
output_text.pack(padx=10, pady=10)

root.mainloop()