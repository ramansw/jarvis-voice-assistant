from audioop import findfactor
from email.mime import audio
import sys
from typing_extensions import Self
from unicodedata import name
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import urllib.request
import urllib.parse
import googlesearch
import pywhatkit
import time
import psutil
import webbrowser
import random
import winshell
import requests
from googletrans import Translator
import os
from tkinter import *
import smtplib
import subprocess
import pyjokes
import pyautogui
import instaloader
import operator
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisGUI import Ui_Jarvis



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
    
    

def wishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("good morning sir!")
     
        

    elif hour>=12 and hour<18:
        speak("Good afternoon Sir!")
        
        
    else:
        speak("Good evening Sir!")
       
       
    speak(" I am Ryan a virtual assistant. please tell me How can i help you :")
    
  
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('raman.sw1911024@gmail.com','officialraman123')
    server.sendmail('raman.sw1911024@gmail.com', to, content)
    server.close()     
    
    
class MainThread(QThread):
    def __init__(self) :
        super(MainThread,self).__init__()
        
    def run(self):
        self.TaskExecution()
        
    
        
        
   
    

    def takeCommand(self):
        r = sr.Recognizer()
        r.energy_threshold = 4000
        
        with sr.Microphone() as source:
            print("Ryan is Listening...")
            r.pause_threshold = 1
            audio = r.listen(source,phrase_time_limit=4) 
        


        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')   
            print(f"you said:{query}\n")
            
        except Exception as e:
            print(e)

            print("Say that again please.....")
            return"none"
        query = query.lower()

        return query

    def pdf_reader(self):
        book = open("C:/Users/Ayush/Downloads/Project/j.pdf",'rb')
        pdfReader = PyPDF.PdfFileReader(book)
        pages = pdfREader.numPages
        speak(f"total numbers of pages in this book {pages} ")
        speak("sir please enter the pages of number i have to read")
        pg = int(input("Please enter the page number: "))
        page = pdfReader.getPage(pg)
        text = page.extractText()
        speak(text)
        
    


    def TaskExecution(self):
        wishMe()
        
         
        
        
        
    
        while True:
            self.query = self.takeCommand().lower()
            
            
            if 'internet' in self.query:
                speak('Wait a Minute sir....')
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query,sentences =2)
                speak("According to the internet")
                print("friday:",results)
                speak(results)
                
                
            elif 'search' in self.query:
                speak('Wait a Minute sir......')
                self.query = self.query.replace("googlesearch","")
                results = wikipedia.summary(self.query,sentences=2)
                speak("According to the internet")
                print("friday:",results)
                speak(results)

            elif 'play music' in self.query or "play song"  in self.query:
                speak("Here you go with music")
                # music_dir = "G:\\Song"
                music_dir = "D:\Jarvis\Music"
                songs = os.listdir(music_dir)
                print(songs)   
                random = os.startfile(os.path.join(music_dir, songs[1]))
            
            elif 'who are you' in self.query:
                speak("I'm Ryaan a virtual assistant I crated by ramandeep singh,he is a very humble person")
            elif 'hello'in self.query or 'hello jarvis' in self.query:
                speak("hello sir  I am jarvis a virual assistant ?")
            elif "your name" in self.query:
                speak("i am already told tyou sir my name is Ryaan")
            elif 'who i am' in self.query:
                speak('yeah i know you, developed me and you are my boss, you name is ramandeep singh, status single, 18 year old, a software develper') 
            elif ' how are you'in self.query:
                speak("I'm fime fine sir")
            elif 'hey siri' in self.query:
                speak("I am not siri I am already told you i am Jarvis")
            elif'can you dance' in self.query:
                speak("No I am not")
            elif 'youtube' in self.query:
                speak("opening youtube")
                webbrowser.open ('youtube.com') 
            elif'open cmd'in self.query:
                speak("opening cmd")
                os.system('start cmd')
                
            elif 'instagram' in self.query:
            
                speak("opening instagram")
                webbrowser.open('instagram.com')
            elif 'google'in self.query:
                speak("opening google")
                webbrowser.open('google.com')
            elif 'read pdf' in self.query:
                self.pdf_reader()
            elif'who is your boss' in self.query:
                print("Ramandeep Singh he is very humble person and kind hearted and he is geniune.")

                speak("Rmandeep singh he is very hubble person and kind hearted and he is geninue.")

            

            elif 'can you calculate' in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("say what you want to calculate: ")
                    print("Ryan is listening......")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string =r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return{
                        '+' : operator.add,
                        '_' : operator.sub,
                        'x' : operator.mul,
                        'divided' : operator.__truediv__,

                    }[op]
                def eval_binary_expr(op1 , oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your result is ")
                speak(eval_binary_expr(*(my_string.split())))


           
            elif 'open wikipedia' in self.query:
                speak("openig wikipedias")
                webbrowser.open('wikipedia.com')
            elif'website' in self.query:
                speak('opening sliet website')
                webbrowser('sliet.ac.in')
            elif'videos' in self.query:
                
                speak("opening porn videos")
                webbrowser('www.xmaster.com')


            elif'age' in self.query:
                speak("I'm born in 2022 so you can calculate my age")

            elif 'do you have a girlfriend' in self.query:
                speak("i have no girfriend like my boss")


            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"sir time is the {strTime}")
                speak(f"sir time is the{strTime}")
            elif 'fine' in self.query or "good" in self.query:
                speak("It's good to know that your fine")
                
            elif'play some music' in self.query:
                speak("Which artist do you wanna listen")
                songOrArtist = self.takeCommand()
                speak("here you go with music")
                pywhatkit.playonyt(songOrArtist)

            elif 'joke' in self.query:
                speak(pyjokes.get_joke())
            
            
            elif 'take a screenshot' in self.query:
                speak("sir, please tell the name for this screenshot file")
                name = self.takeCommand().lower()
                speak("please sir hold the screen for the few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("I am done sir, the screenshot is saved in our main folder")

            elif 'play some' in self.query:
                speak('which song you wanna listen')

                msg = self.takeCommand().lower()
                song = urllib.parse.urlencode({"search_query" : msg})
                print(song)

                # fetch the ?v=query_string
                result = urllib.request.urlopen("http://www.youtube.com/results?" + song)
                print(result)

                # make the url of the first result song
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', result.read().decode())
                print(search_results)

                # make the final url of song selects the very first result from youtube result
                url = "http://www.youtube.com/watch?v="+search_results[0]

                # play the song using webBrowser module which opens the browser 
                # webbrowser.open(url, new = 1)
                webbrowser.open_new(url)
            
            elif 'send email' in self.query:

                try:

                    name = list(self.query.split()) # extract receiver's name

                   

                    speak("what should i say")

                    content = self.takeCommand().lower

                    to = dict['officialraman.sw@gmail.com']

                    sendEmail(to,content)

                    speak("email has been sent")

                except Exception as e:

                    print(e)

                    speak("sorry unable to send the email at the moment.Try again")
                
                """  elif'find my ip':
                speak('wait a second let me check sir')
                ip_address = requests.get('https://api64.ipify.org?format=json').json()
                return ip_address"""
            
            elif 'empty recycle bin' in self.query:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")
            elif 'translate' in self.query:
                translator = Translator()
                userSaid = self.takeCommand()
                out = translator.translate(self.takeCommand,dest='hi')
                print(out.txt)
                speak(out)
            elif " weather" in self.query:
                
                # Google Open weather website
                # to get API of Open weather
                api_key = "Api key"
                base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
                speak(" City name ")
                print("City name : ")
                city_name = self.takeCommand()
                complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                response = requests.get(complete_url)
                x = response.json()
                
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                
                else:
                    speak(" City Not Found ")
            elif "will you be my gf" in self.query or "will you be my bf" in self.query:  
                    speak("I'm not sure about, may be you should give me some time")
            elif "i love you" in self.query:
                speak("It's hard to understand")
            elif 'shut up' in  self.query:
                speak("That's nice to talk you sir have a nice day")
                quit()
            elif 'shutdown' in self.query:
                            speak("Hold On a Second ! Your system is on its way to shut down have a nice day")
                            os.system("shutdown /s /t 1")
                            
            elif 'advice' in self.query:
                res = requests.get("https://api.adviceslip.com/advice").json()
                return res['slip']['advice']
                            
            elif'where is' in self.query:
                self.query = self.query.replace("wehre is","")
                location = self.query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.n1 / maps / place/" + "")
                
            elif"write a note" in self.query:
                speak("what should i write sir")
                note = self.takeCommand()
                file = open('jarvis.txt', 'w')
                speak("sir, should i include date and time")
                snfm = self.takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("&H:&M:%S")
                    file.write(strTime)
                    file.wirte(" :- ")
                    file.write(note)
                else: 
                    file.write(note)
                
                
                
                
            elif 'thank you' in self.query :
                speak('It is my pleasure sir')

            elif 'thank you jarvis' in self.query:
                speak("it is my pleasure sir")

            elif 'power'in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir our system have {percentage} percent battery")
            
            elif 'where i am' in self.query:
                speak("wait a minute sir,let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').txt
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {city} city of {country}country")

                except Exception as e :
                    speak("sorry sir, Due to network issue i am not able to find where we are ")
                    pass


            elif 'who is created you' in self.query:
                speak("i am created by name Ramandeep Singh.he is a software engineer and he is  a very humble person")
            elif 'toffee' in self.query:
                speak("toffee is a good girl and she is very beautiful")
            elif 'drive'in self.query:
                speak("opening google drive")
                webbrowser.open('drive.google.com')
                
    
        
                

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.ui =Ui_Jarvis()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
      
    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/black.png")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/jarvis435.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/T8bahf.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/jarvisstand.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/zero.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/circle.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/jarvis.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/Iris.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/loading.gif")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/bottom.png")
        self.ui.label_10.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/titile.gif")
        self.ui.label_11.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/terminal4.gif")
        self.ui.label_12.setMovie(self.ui.movie)
        self.ui.movie.start()
       
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/loading4.gif")
        self.ui.label_13.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/J-A-R-V-I-S-thumb.png")
        self.ui.label_14.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/wibe.gif")
        self.ui.label_15.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("D:\Jarvis\Png Files/wibe.gif")
        self.ui.label_16.setMovie(self.ui.movie)
        self.ui.movie.start()
        
       

        startExecution.start()
  

   
    
app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())