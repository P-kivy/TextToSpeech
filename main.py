import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import gtts
import webbrowser
from tkinter import filedialog as fd
from gtts import gTTS, gTTSError
from PIL import Image, ImageTk
from tool_tip import CreateToolTip
import os

# load supported languages
supported_langs = gtts.lang.tts_langs()

lang = []
for i in supported_langs:
    lang.append(f"{i}: {supported_langs[i]}")


# checkers and validators

def check_entry(event):
    c = "/|?*:\<>"
    s = str(name_txt.get())
    for char in c:
        if char in s:
            s1 = s.replace(char, '')
            name.delete(0, 'end')
            name.insert(0, s1)


def browse():
    directory = fd.askdirectory(initialdir="/", title="Select a directory")
    f = os.path.abspath(directory)
    path.config(state=NORMAL)
    path.insert(INSERT, f)
    path.config(state=DISABLED)


def github(event):
    webbrowser.open_new_tab("https://github.com/P-kivy")


def convert():
    try:
        if bool(name_txt.get()):
            s = str(name_txt.get())
            name.delete(0, 'end')
            name.insert(0, s)
        else:
            name.insert(0, "TTS-AUDIO")

        text_v = txt.get("1.0", 'end')
        var = spec_lang.get()
        x = var.split(":")
        language = 'ar'
        if bool(x):
            language = x[0]

        output = gTTS(text=text_v, lang=language, slow=False)
        p = path.get('1.0', 'end').replace('\n', '') + name_txt.get() + ".mp3"
        output.save(p)
        os.system("start " + p)

    except gTTSError:
        messagebox.showerror("Error", "Please check your internet connection!")

    except AssertionError:
        messagebox.showerror("Error", "Please type some text!")


# styling labels
def style_label(lb):
    lb.config(bg="cyan", fg="black", font='Georgia 14 bold italic')


# root of gui
win = tk.Tk()

# styling the root
win.resizable(0, 0)
win.config(bg="cyan")
win.iconbitmap("favicon.ico")
win.title("TextToSpeech")

# Centering Root Window on Screen

# Gets the requested values of the height and widht.
windowWidth = win.winfo_reqwidth()
windowHeight = win.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(win.winfo_screenwidth() / 4 - windowWidth / 2)
positionDown = int(win.winfo_screenheight() / 3 - windowHeight / 2)

# Positions the window in the center of the page.
win.geometry("+{}+{}".format(positionRight, positionDown))

# components
frame = tk.Frame(win)
frame.config(bg="cyan")
frame.pack(anchor='w')

frame1 = tk.Frame(win)
frame1.config(bg="cyan", padx=0)
frame1.pack(anchor='w')

frame2 = tk.Frame(win)
frame2.config(bg="cyan")
frame2.pack(anchor='w')

frame3 = tk.Frame(win)
frame3.config(bg="cyan")
frame3.pack(anchor='w')

frame4 = tk.Frame(win)
frame4.config(bg="cyan")
frame4.pack()

frame5 = tk.Frame(win)
frame5.config(bg="cyan")
frame5.pack()

name_txt = tk.StringVar()
lang_txt = tk.StringVar()
spec_lang = tk.StringVar()

label1 = tk.Label(frame, text="Text to convert:", height=10)
style_label(label1)
label1.grid(row=0, column=0, sticky='W')

txt = tk.Text(frame, width=50, height=10, font="Calibre 12 normal")
txt.grid(row=0, column=1, padx=85)

label2 = tk.Label(frame1, text="Select the language:")
style_label(label2)
label2.grid(row=0, column=0, sticky='W', padx=(0, 40))

lang_choosen = ttk.Combobox(frame1, width=48, textvariable=spec_lang, style="")
lang_choosen.config(font="Arial 12")
lang_choosen['values'] = lang
lang_choosen.current(1)
lang_choosen.grid(row=0, column=1, sticky='N', pady=(10, 0))

label3 = tk.Label(frame2, text="Select Folder:")
style_label(label3)
label3.grid(row=0, column=0, sticky='w', pady=(10, 0), padx=(0, 105))

t = os.getcwd()
path = tk.Text(frame2, width=61, height=1.25, font="Arial 10")
path.insert(INSERT, t)
path.config(state=DISABLED)
path.grid(row=0, column=1, sticky='w', pady=(15, 0))

img = Image.open('browse.png')
test = ImageTk.PhotoImage(img)
button = tk.Button(frame2, image=test, command=browse, width=16, height=15)
button2_ttp = CreateToolTip(button, "Browse")
button.grid(row=0, column=2, pady=(15, 0))

label4 = tk.Label(frame3, text="Save as:")
label4.grid(row=0, column=0, sticky='w', padx=(0, 160))
style_label(label4)

name = tk.Entry(frame3, width=75, textvariable=name_txt)
name.grid(row=0, column=1, sticky='W', pady=10)
name.bind('<KeyRelease>', check_entry)

img = Image.open('convert.png')
test1 = ImageTk.PhotoImage(img)
button1 = tk.Button(frame4, image=test1, text="Convert", command=convert, width=200, height=40,
                    compound="left", borderwidth=5, font="Georgia 14 bold")
button_ttp = CreateToolTip(button1, "convert to speech")
button1.grid(row=0, column=3, pady=10, sticky="E", padx=(120, 0))

label5 = tk.Label(frame5, text="©𝐻𝒪𝒰𝒜𝑅𝐼 𝒴𝑜𝓊𝓃𝑒𝓈𝓈 𝟤𝟢𝟤𝟣")
label5.grid(row=0, column=3, pady=(20, 0), sticky="S", padx=(120, 0))
label5.bind('<Button>', github)

win.mainloop()
