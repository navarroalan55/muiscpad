from tkinter import *
from tkinter import ttk
import os

# makes window
root = Tk()
root.title("MUSIC PAD")
n = ttk.Notebook(root)
n.grid()

f1 = ttk.Frame(n)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(n)   # second page

n.add(f1, text='MUSIC')
n.add(f2, text='PAD')
#music
dirL=ttk.Label(f1,text='DIRECTIONS:CREATE FOLDER OUTSIDE OF PROGRAM AND ADD .MP3 FILES TO IT')
dirL.grid()
addL=ttk.Label(f1,text='FIND THE MP3 FILES')
addL.grid()

song_dir_list=[]
def open_():
        root.fileName = filedialog.askopenfilename(filetypes=(("*","*.mp3"),("*","*.mp3")))
        song_dir=(root.fileName)
        global song_dir_list
        song_dir_list=song_dir_list+[song_dir]


openB=ttk.Button(f1,text="OPEN",command=open_)
openB.grid()
songs=[]
def all_():
    for song in song_dir_list:
        checkB=ttk.Checkbutton(f1,text=song)
        checkB.state(['!alternate'])
        checkB.grid()
        global songs
        songs.append(checkB)

def play_():
    for song in songs:
            if song.instate(['selected']):
                    checked=[song]
                    for song in checked:
                            directory=song.cget("text")
                            os.startfile(directory)


def clear():
        for button in songs:
                if button.instate(['selected']):
                        checked=[button]
                        for idk in checked:
                                idk.destroy()
                                songs.remove(idk)    


playB=ttk.Button(f1,text="PLAY",command=play_)        
sorryL=ttk.Label(f1,text="SORRY FOR THE WAY IT LOOKS, MAYBE IN THE NEXT UPDATE!!")
advisedL=ttk.Label(f1,text="IT IS ADVISED TO CHECK ONE AT A TIME  TO PLAY THE SONG :)")
clearB = ttk.Button(f1, text="CLEAR ALL CHECKED", command=clear)
allB=ttk.Button(f1,text="SEE ALL",command= all_)
playB.grid()
allB.grid()

def check():
    for button in  songs:
        button.state(['selected'])

def uncheckall():
        for button in songs:
                button.state(['!selected'])
checkall=ttk.Button(f1,text =" CHECK ALL", command=check)
uncheck=ttk.Button(f1,text="UNCHECK ALL" ,command=uncheckall)
checkall.grid()
uncheck.grid()
clearB.grid()
sorryL.grid()
advisedL.grid()
disclaimer = Label(f1,text="IF CLEAR ALL DOESNT CLEAR PRESS AGAIN")
disclaimer.grid()
#pad

# functions that will later be called
disclaimer = Label(f2,text="IF CLEAR ALL DOESNT CLEAR PRESS AGAIN")
w = Label(f2, text="Make new To-Do")
w.columnconfigure(0,weight=0)
w.grid(row=0, column=0,sticky=W+E+N+S,padx=5, pady=5)
blank = ttk.Entry(f2)
blank.grid(row=2,column=0)
def X():
    blank.delete(0, 'end')
XB = ttk.Button(f2, text="X", command=X)
XB.grid(row=2,column=1)
# make this be able to work on some buttons not all
buttons=[]
def print_list():
    words = (blank.get())
    checkB = ttk.Checkbutton(f2, text=words)
    checkB.state(['!alternate'])
    checkB.grid()
    global check
    buttons.append(checkB)
createB = ttk.Button(f2, text="CREATE", command=print_list)
createB.grid()
def clear():
    for button in buttons:
        if button.instate(['selected']):
            checked=[button]
            for idk in checked:
                idk.destroy()
                buttons.remove(idk) 
def check():
    for button in buttons:
        button.state(['selected'])
checkall=ttk.Button(f2,text =" CHECK ALL", command=check)

clearB = ttk.Button(f2, text="CLEAR ALL CHECKED", command=clear)

def uncheckall():
        for button in buttons:
                button.state(['!selected'])

uncheck=ttk.Button(f2,text="UNCHECK ALL" ,command=uncheckall)
checkall.grid()
uncheck.grid()
clearB.grid()
disclaimer.grid()

root.mainloop()





