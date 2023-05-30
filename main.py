import tkinter as tk
import yt_dlp

import os
import sys

from config import *

BG = '#0f0f0f'
FG = '#f1f1f1'
TITE_FONT = ('monospace', 20, 'bold')
FONT = ('monospace', 15, 'normal')


class main(tk.Tk):
    """
    this is a main class for the program
    """
    def __init__(self):
        super().__init__()

        self.var = tk.StringVar()

        self.small_icon = os.path.join(os.path.dirname(__file__) , "logo.png")
        self.Icon = tk.PhotoImage(file=self.small_icon)
        self.iconphoto(False,self.Icon)

        self.title('Y-Download')
        self.resizable(False, False)
        self.config(
            background=BG
        )

        self.Title = tk.Label(
            text='Y-Download',
            font=TITE_FONT,
            padx=5,
            pady=5,
            fg=FG,
            bg=BG
        )
        self.Title.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            columnspan=2
        )

        self.Description = tk.Label(
            text="""
            Y-Download is a simple tool to download mp3 or mp4 youtube video content.
            You can start by putting some youtube links in the links.txt file in this
            folder , if you just wanna download one video you can put it in the file.
            """,
            font=FONT,
            fg=FG,
            bg=BG,
            pady=5,
            padx=5
        )

        self.Description.grid(
            row=1,
            column=1,
            columnspan=1
        )

        self.RadioPack = tk.Frame()

        self.mp4 = tk.Radiobutton(self.RadioPack,
                                  text='MP4',
                                  value='MP4',
                                  variable=self.var,
                                  font=FONT,
                                  activebackground=BG,
                                  activeforeground=FG,
                                  background=BG,
                                  foreground='red'
                                  )

        self.mp3 = tk.Radiobutton(self.RadioPack,
                                  text='MP3',
                                  value='MP3',
                                  variable=self.var,
                                  font=FONT,
                                  activebackground=BG,
                                  activeforeground=FG,
                                  background=BG,
                                  foreground='red'
                                  )

        self.mp3.select()

        self.mp4.grid(
            row=2,
            column=1
        )
        self.mp3.grid(
            row=2,
            column=2
        )

        self.RadioPack.grid(
            row=2,
            column=1,
            columnspan=1
        )

        self.download = tk.Button(
            text='Download',
            bg='red',
            fg=FG,
            padx=5,
            pady=5,
            width=50,
            command=lambda:self.Download()
        )
        self.download.grid(
            row=3,
            column=1,
            pady=10
        )

    def Download(self):
        urls = []
        with open(f"{YOUTUB_LINKS_DOWNLOAD_PATH}", "r", newline='') as file:
            for line in file:
                urls.append(line)
        if self.var.get() == "MP3":
            ydl_opts = {
                'format': 'bestaudio/mp3',
                'outtmpl': f'{MP3_DOWNLOAD_PATH}/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(urls)
            except Exception as e:
                print(f"An error occurred: {e}")
    

        if self.var.get() == "MP4":
            ydl_opts = {
                'format': 'mp4',
                'outtmpl': f'{MP4_DOWNLOAD_PATH}/%(title)s.%(ext)s',
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(urls)
            except Exception as e:
                print(f"An error occurred: {e}")
        print(urls)



Program = main()

Program.mainloop()