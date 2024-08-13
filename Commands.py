from email.mime import image
from fileinput import filename
from imaplib import Commands
from tkinter import *
from tkinter.font import BOLD
from tkinter import PhotoImage
from turtle import color

from PIL import ImageTk,Image


class CommandGUI:

    
    def __init__(self,window):
        self.window=window
        self.window.title("Jarvis")
        self.window.configure(background = 'DeepSkyBlue4')
        self.window.geometry('899x654')
        self.window.resizable(False,False)
        
        
        
        img = ImageTk.PhotoImage(Image.open("D:\\Python\\Jarvis\\Png Files\\R.png"))
        label = Label(image= img)
        label.pack()
        label.place(y=89, x= 478)
        
        
        heading = Label(self.window, text= 'Commands:-',font= ('Goudy old Style bold',20,),fg='black',bg='DeepSkyBlue4')
        heading.place(x=10,y=10)
        cmd1 = Label(self.window,text="1. Say'Hello Jarvis','Hi Jarvis'or 'How are you'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=50)
        cmd2 = Label(self.window,text="2. Say'Open YouTube'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=80)
        cmd3 = Label(self.window,text="3. Say'Open Instagram'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=110)
        cmd4 = Label(self.window,text="4. Say'Open Google.','open wikipedia'or'stack Overflow'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=140)
        cmd5 = Label(self.window,text="5. Say'take a screenshot'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=170)
        cmd6 = Label(self.window,text="6. Say'tell me a joke'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=200)
        cmd7 = Label(self.window,text="7. Say'play some music'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=230)
        cmd8 = Label(self.window,text="8. Say'send email'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=260)
        cmd9 = Label(self.window,text="9. Say'empty recycle bin",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=290)
        cmd10 = Label(self.window,text="10. Say'tell me about weather'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=320)
        cmd11 = Label(self.window,text="11. Say'The time'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=350)
        cmd12= Label(self.window,text="12. Say'how much power we have?'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=380)
        cmd13 = Label(self.window,text="13. Say'where i am'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=410)
        cmd14 = Label(self.window,text="14. Say'opne drive'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=440)
        cmd15 = Label(self.window,text="15. Say'shut down' or 'shut up'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=470)
        cmd16 = Label(self.window,text="16. Say'give me a advice'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=500)
        cmd17 = Label(self.window,text="17. Say'write a note'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=530)
        cmd18 = Label(self.window,text="18. Say'can you calculate'",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=560)
        cmd19 = Label(self.window,text="19. For Internet searches you need to say'according to the internet' topic that you want to search.",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=590)
        cmd20 = Label(self.window,text ="20. You can do some basic conversation with friday.",font=('times new roman',15,),bg='DeepSkyBlue4').place(x=10, y=620)

        

window= Tk()
wind = CommandGUI(window)
window.mainloop()
        