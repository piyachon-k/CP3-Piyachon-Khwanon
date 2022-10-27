from tkinter import *

def leftClickButton(event):
    height = int(textBoxHeight.get())
    weight = int(textBoxWeight.get())
    
    result = weight/(height/100)**2
    
    if result > 30:
        txt = 'very fat'
    elif result > 25:
        txt = 'fat'
    elif result > 23:
        txt = 'over weight'
    elif result > 18.6:
        txt = 'normal'
    else:
        txt = 'under weight'
    
    labelResult.configure(text = txt)

MainWindow = Tk()
labelHeight = Label(MainWindow, text = 'Height [cm.]')
labelWeight = Label(MainWindow, text = 'Weight [Kg.]')
textBoxHeight = Entry(MainWindow)
textBoxWeight = Entry(MainWindow)
labelHeight.grid(row=0,column=0)
labelWeight.grid(row=1,column=0)
textBoxHeight.grid(row=0,column=1)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow, text='calculate')
calculateButton.grid(row=2, column=0)
calculateButton.bind('<Button-1>',leftClickButton)

labelResult = Label(MainWindow, text='result')
labelResult.grid(row=2,column=1)

MainWindow.mainloop()
