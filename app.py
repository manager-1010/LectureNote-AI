import os
import tkinter as tk
from tkinter import filedialog, messagebox
from faster_whisper import WhisperModel
from tkinterdnd2 import TkinterDnD, DND_FILES

selected_file = None

SUPPORTED_EXTENSIONS = (".mp3", ".wav", ".m4a", ".mp4")


def set_selected_file(file_path):
    global selected_file

    file_path = file_path.strip().strip("{}")

    if not file_path.lower().endswith(SUPPORTED_EXTENSIONS):
        messagebox.showwarning(
            "Unsupported file",
            "Please select an MP3, WAV, M4A, or MP4 file."
        )
        return

    selected_file = file_path
    selected_file_label.config(text=file_path)
    status_label.config(text="Ready to transcribe")


def select_file():
    file_path = filedialog.askopenfilename(
        title="Select lecture audio or video",
        filetypes=[
            ("Audio/Video Files", "*.mp3 *.wav *.m4a *.mp4"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        set_selected_file(file_path)


def handle_drop(event):
    dropped_data = event.data

    if not dropped_data:
        return

    if dropped_data.startswith("{"):
        end = dropped_data.find("}")
        if end != -1:
            dropped_file = dropped_data[1:end]
        else:
            dropped_file = dropped_data.strip("{}")
    else:
        dropped_file = dropped_data.split()[0]

    set_selected_file(dropped_file)


def transcribe_file():
    if not selected_file:
        messagebox.showwarning(
            "No file selected",
            "Please select an audio or video file first."
        )
        return

    try:
        transcribe_button.config(state="disabled")

        status_label.config(text="Loading AI model...")
        progress_label.config(text="Step 1 of 3")
        root.update()

        model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )

        status_label.config(text="Transcribing...")
        progress_label.config(text="Step 2 of 3")
        root.update()

        segments, info = model.transcribe(
            selected_file,
            beam_size=5
        )

        transcript_lines = []

        for segment in segments:
            transcript_lines.append(segment.text.strip())

        transcript = "\n".join(transcript_lines)

        status_label.config(text="Saving transcript...")
        progress_label.config(text="Step 3 of 3")
        root.update()

        base_name = os.path.splitext(selected_file)[0]
        output_file = base_name + "_transcript.txt"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcript)

        status_label.config(text="Transcription completed!")
        progress_label.config(text="Completed")

        messagebox.showinfo(
            "Completed",
            f"Transcript saved to:\n{output_file}"
        )

    except Exception as e:
        status_label.config(text="Something went wrong")
        progress_label.config(text="Failed")

        messagebox.showerror(
            "Error",
            str(e)
        )

    finally:
        transcribe_button.config(state="normal")


root = TkinterDnD.Tk()
root.title("LectureNote AI")
root.geometry("650x470")

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

drop_area = tk.Label(
    root,
    text="Drag & Drop Audio / Video File Here",
    relief="groove",
    width=45,
    height=5
)
drop_area.pack(pady=15)

drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind("<<Drop>>", handle_drop)

select_button = tk.Button(
    root,
    text="Or Select Audio / Video File",
    command=select_file,
    width=28,
    height=2
)
select_button.pack(pady=10)

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
status_label.pack(pady=8)

progress_label = tk.Label(
    root,
    text=""
)
progress_label.pack(pady=5)

root.mainloop()
