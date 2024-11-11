import re
import tkinter as tk
from tkinter import messagebox
import os
from pytube import YouTube


def check_link(link):
    # Use a raw string (r"") to handle special characters in the regex pattern
    youtube_regex = (
        r"^(https?://)?(www\.)?"
        r"(youtube|youtu|youtube-nocookie)\.(com|be)/"
        r"(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})"
    )

    # Verifica se o link corresponde ao regex
    if not re.match(youtube_regex, link):
        messagebox.showwarning("Link inválido", "Por favor, insira um link válido do YouTube!")
        return False
    return True


def download_video(link):
    if not check_link(link):
        return  # Jumps out if the link is not valid
    print("Link válido, iniciando o download:", link)

    try:
        # Define the download path to "Downloads" folder
        transfer_path = os.path.join(os.path.expanduser("~"), "Downloads")

        # Prints a message showing the download is starting
        messagebox.showinfo("Download", "O download vai começar em instantes.")

        # Downloads the video using pytube
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=transfer_path)

        # Prints a message showing the download is done
        messagebox.showinfo("Download Succesful", f"Download done and saved in folder {transfer_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occured during the download: {e}")
