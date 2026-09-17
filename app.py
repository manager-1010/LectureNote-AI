import tkinter as tk
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select lecture audio or video",
        filetypes=[
            ("Audio/Video Files", "*.mp3 *.wav *.m4a *.mp4"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        selected_file_label.config(text=file_path)

root = tk.Tk()
root.title("LectureNote AI")
root.geometry("600x300")

title_label = tk.Label(
    root,
    text="LectureNote AI",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=20)

description_label = tk.Label(
    root,
    text="Local lecture transcription tool",
    font=("Arial", 12)
)
description_label.pack(pady=5)

select_button = tk.Button(
    root,
    text="Select Audio / Video File",
    command=select_file,
    width=25,
    height=2
)
select_button.pack(pady=20)

selected_file_label = tk.Label(
    root,
    text="No file selected",
    wraplength=500
)
selected_file_label.pack(pady=10)

root.mainloop()
