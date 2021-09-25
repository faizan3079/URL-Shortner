from tkinter import *
import pyshorteners

fai = Tk()
fai.geometry('800x600+330+130')
fai.title('URL Shortner')
fai.config(bg = '#cc99ff')
pho=PhotoImage(file=r'F:\Mini Projects\URL Shortner\urlpic.png')
fai.iconphoto(False,pho)

#function to convert:

def convert():
    s = pyshorteners.Shortener().tinyurl.short(url.get())
    shorturl.set(s)

#Declaring variables:

url = StringVar()
shorturl = StringVar()

Label(fai,text = 'URL Shortner',bg = '#ffff99',fg = 'Black', font="Helvetica 26 ").place(x=300,y=20)
Label(fai,text = 'Enter the URL Which you want to shorten',font="Helvetica 16 ",bg='#ffff99' ).place(x=220,y=150)
Entry(fai,textvariable = url, font= 'Helvetica 16',width = 30).place(x=230,y=200)
Label(fai,text = 'Here is your Shortened URL',font="Helvetica 16 ",bg='#ffff99' ).place(x=275,y=350)
Entry(fai,textvariable = shorturl, font= 'Helvetica 16',width = 30).place(x=230,y=400)
Button(fai,text = 'Convert it!', font= 'Helvetica 16', command = convert , bg= '#1a1a1a',fg='#ffff00').place(x=344,y=270)
mainloop()