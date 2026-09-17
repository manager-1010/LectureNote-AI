import os
import tkinter as tk
from tkinter import filedialog, messagebox
from faster_whisper import WhisperModel

selected_file = None


def select_file():
    global selected_file

    file_path = filedialog.askopenfilename(
        title="Select lecture audio or video",
        filetypes=[
            ("Audio/Video Files", "*.mp3 *.wav *.m4a *.mp4"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        selected_file = file_path
        selected_file_label.config(text=file_path)
        status_label.config(text="Ready to transcribe")


def transcribe_file():
    if not selected_file:
        messagebox.showwarning(
            "No file selected",
            "Please select an audio or video file first."
        )
        return

    try:
        status_label.config(text="Loading AI model...")
        root.update()

        model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )

        status_label.config(text="Transcribing...")
        root.update()

        segments, info = model.transcribe(
            selected_file,
            beam_size=5
        )

        transcript_lines = []

        for segment in segments:
            transcript_lines.append(segment.text.strip())

        transcript = "\n".join(transcript_lines)

        base_name = os.path.splitext(selected_file)[0]
        output_file = base_name + "_transcript.txt"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcript)

        status_label.config(text="Transcription completed!")

        messagebox.showinfo(
            "Completed",
            f"Transcript saved to:\n{output_file}"
        )

    except Exception as e:
        status_label.config(text="Something went wrong")

        messagebox.showerror(
            "Error",
            str(e)
        )


root = tk.Tk()
root.title("LectureNote AI")
root.geometry("650x380")

title_label = tk.Label(
    root,
    text="LectureNote AI",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=20)

description_label = tk.Label(
    root,
    text="Privacy-first local lecture transcription tool",
    font=("Arial", 12)
)
description_label.pack(pady=5)

select_button = tk.Button(
    root,
    text="Select Audio / Video File",
    command=select_file,
    width=28,
    height=2
)
select_button.pack(pady=15)

selected_file_label = tk.Label(
    root,
    text="No file selected",
    wraplength=550
)
selected_file_label.pack(pady=10)

transcribe_button = tk.Button(
    root,
    text="Transcribe",
    command=transcribe_file,
    width=28,
    height=2
)
transcribe_button.pack(pady=15)

status_label = tk.Label(
    root,
    text="Waiting for file..."
)
status_label.pack(pady=10)

root.mainloop()
