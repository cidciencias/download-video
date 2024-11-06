import tkinter as tk
import logic as lg

# Function for the button
def on_download_click():
    link = video_link.get()
    lg.download_video(link)


# Create the main window
screen = tk.Tk()
screen.geometry("550x350")
screen.title("Youtube Video Downloader")

# Create a String variable to associate with the label
label_text = tk.StringVar()
label_text.set("Link do Video: ")

# Create the label widget
label = tk.Label(screen,
                 textvariable=label_text,
                 font=("Arial", 14),
                 fg="black",
                 anchor="w"
                 )

# Create an Entry widget for the text input
video_link = tk.StringVar()
entry = tk.Entry(screen,
                 textvariable=video_link,
                 font=("Arial", 14),
                 width=40,
                 bd=3,
                 relief=tk.SUNKEN
                 )

# Create a string variable to associate with the button
button_text = tk.StringVar()
button_text.set("Download")

# Create the button widget
button = tk.Button(screen,
                   textvariable=button_text,
                   font=("Arial", 14, "bold"),
                   fg="white",
                   bg="green",
                   height=2,
                   width=15,
                   command=on_download_click
                   )

# Pack the widgets into the window
label.pack(pady=20)
entry.pack(pady=20)
button.pack(pady=20)

screen.mainloop()



