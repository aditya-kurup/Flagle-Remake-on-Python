

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from turtle import title
import PIL 
from PIL import ImageTk, Image
import random

countries = ['canada','japan','india','UAE','romania','sudan', 'ecuador', 'bangladesh','portugal','greece','france','argentina','algeria','afghanistan','albania',
'austria','bangladesh','chile','croatia','ecuador','indonesia']
def randcountry():
    global countries
    s = random.choice(countries)
    countries.remove(s)
    #print(countries)
    return s

target = randcountry()
m = tk.Tk()
m.geometry("1280x720")
m.title('Flagle Remake')
img = ImageTk.PhotoImage(Image.open(target +".png"))
intro = ImageTk.PhotoImage(Image.open("intro.png"))
label12 = tk.Label(m,image = intro)
label12.place(x= 0,y = 27)

label1 = tk.Label(m, image= img)
label1.place(x = 640,y = 160,anchor="center")

cover = ImageTk.PhotoImage(Image.open("cover.png"))
label2 = tk.Label(m, image = cover)
label2.place(x = 372,y = 27)
label3 = tk.Label(m, image = cover)
label3.place(x = 372,y = 92+27)
label4 = tk.Label(m, image = cover)
label4.place(x = 372,y = 92+92+27)
label5 = tk.Label(m, image = cover)
label5.place(x = 372+183,y = 0+27)
label6 = tk.Label(m, image = cover)
label6.place(x = 372+183,y = 92+27)
label7 = tk.Label(m, image = cover)
label7.place(x = 372+183,y = 92+92+27)
label8 = tk.Label(m, image = cover)
label8.place(x =372+183+183 ,y = 0+27)
label9 = tk.Label(m, image = cover)
label9.place(x = 372+183+183,y = 92+27)
label10 = tk.Label(m, image = cover)
label10.place(x = 372+183+183,y = 92+92+27)





'''def start1(guess):
    target = randcountry()
    for i in range(6):
            #guess = input("guess country")
            if guess == target:
                print("congrats")
            elif i == 1:
                label2.place_forget()
            elif i == 2:
                label3.place_forget()
            elif i == 3:
                label4.place_forget()
            elif i == 4:
                label5.place_forget()
            elif i == 5:
                label6.place_forget()
   


'''
L= []
inputtxt = tk.Text(m,height = 2, width = 20)
  
inputtxt.place(anchor = "center", x = 640, y = 400)
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    L.append(inp)
    return inp


'''def forget():
    label2.place_forget()'''
data = list(range(1, 10))
random.shuffle(data)
def hide():
    label2.place_forget()
    label3.place_forget()
    label4.place_forget()
    label5.place_forget()         
    label6.place_forget()           
    label7.place_forget()           
    label8.place_forget()
    label9.place_forget()
    label10.place_forget() 
def show():
    
    label2.place(x = 372,y = 27)
   
    label3.place(x = 372,y = 92+27)
   
    label4.place(x = 372,y = 92+92+27)
 
    label5.place(x = 372+183,y = 0+27)
   
    label6.place(x = 372+183,y = 92+27)
  
    label7.place(x = 372+183,y = 92+92+27)
 
    label8.place(x =372+183+183 ,y = 0+27)
  
    label9.place(x = 372+183+183,y = 92+27)

    label10.place(x = 372+183+183,y = 92+92+27)
    
guesses = -1
scoreS = "score: "
score = 0
label11 = tk.Label(m,  text= scoreS)
label11.place(anchor = "center", x = 640, y = 460)
def start():
    global score
    global guesses 
    guesses = guesses + 1
    if guesses == 9:

        msgL ='You have ran out of guesses, the correct answer is ' + target.upper() +". Note: you must guess the country before the whole flag is visible."
        tk.messagebox.showinfo(title='.', message= msgL)
        inputtxt.delete("1.0","end")
        #print(L)
        restart1()
    elif guesses<9:
        inp = printInput()
        if inp.lower() == target.lower():       
           score = score + (9 - guesses) 
           hide() 
           #inputtxt.delete("1.0","end")
           tk.messagebox.showinfo(title='.', message='congrats thats the right country')
           global scoreS
           scoreS1 = scoreS + str(score)
           label11.configure(text=scoreS1)
           restart1()
        else:
            #rad = random.randint(1,10)
            rad = random.choice(data)
            data.remove(rad)
            if rad == 1:
             label2.place_forget()
            elif rad == 2:
             label3.place_forget()
            elif rad == 3:
             label4.place_forget()
            elif rad == 4:
             label5.place_forget()
            elif rad == 5:
             label6.place_forget()
            elif rad == 6:
             label7.place_forget()
            elif rad == 7:
             label8.place_forget()
            elif rad == 8:
             label9.place_forget()
            elif rad == 9:
             label10.place_forget() 
            inputtxt.delete("1.0","end")

button = tk.Button(m, text='guess', width=25, command=start)
button.place(anchor = "center", x = 640, y = 360)

'''def restart():
    target1 = randcountry()
    while True:
       if target == target1:
           target1 = randcountry()
       else:
        break
    img = ImageTk.PhotoImage(Image.open(target1 +".png"))
    label1 = tk.Label(m, image= img)
    label1.place(x = 640,y = 160)   '''






'''button = tk.Button(m, text='reset', width=25, command=restart)
button.place(anchor = "center", x = 640, y = 660)'''

'''def reset():
    m.destroy()
    os.startfile("COMPPROJECT.py")

button = tk.Button(m, text='reset', width=25, command=reset)
button.place(anchor = "center", x = 640, y = 660)'''


"""print(label2.winfo_height(),label2.winfo_width())
to find dimensions of black label covering original flag.
"""
"""def restart():
    target1 = randcountry()
    while True:
        if target1 in L2:
            target1 = randcountry()
        else:
            break
    img2 = ImageTk.PhotoImage(Image.open(target1 +".png"))
    label1.configure(image=img2)
    L=[]
    hide()
    show()"""


def restart1():
    if countries == []:
        asa = 'game over, your final score is:' + str(score)
        tk.messagebox.showinfo(title='.', message=asa)
    global guesses
    guesses = -1
    inputtxt.delete("1.0","end")
    target1 = randcountry()
    img2 = ImageTk.PhotoImage(Image.open(target1 +".png"))
    hide()
    show()
    label1.configure(image=img2)
    label1.image = img2
    global target
    target = target1 
    global data 
    data = list(range(1, 10))
    random.shuffle(data)
    #print(data)

'''button = tk.Button(m, text='next', width=25, command=restart1)
button.place(anchor = "se", x = 1100, y = 560)'''





#print(label1.winfo_width(),label1.winfo_height(),label1.winfo_x(),label1.winfo_y(),label2.winfo_height(),label2.winfo_width())
m.mainloop()

