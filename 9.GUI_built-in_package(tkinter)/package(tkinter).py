#USE BUILT-IN PACKAGE(tkinter) TO MAKE GUI
import tkinter  # <-- Package (tkinter) ini adalah built-in package yang ada secara default pada Python.

main_window = tkinter.Tk()

def event_tekan(): # <-- function untuk event button saat di klik.
    label2 = tkinter.Label(main_window, text="This's your command ^_^")
    label2.pack() # <-- karna ini mainloop, makan label2.pack() ini otomatis akan berada di bawah button.pack()

label = tkinter.Label(main_window, text="Hello, I'm Bot created by Pradipta Ramadhan, \nI'll show you a simple GUI(Graphical User Interface, \n made by Python program language.")
button = tkinter.Button(main_window, text="Loop Button", command=event_tekan)

#RUNNING SYNTAX
label.pack()
button.pack()

#LOOPING SYNTAX
main_window.mainloop() # <-- Agar program terus berulang dan tidak berhenti/tanpa batas.