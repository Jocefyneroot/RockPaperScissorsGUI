from tkinter import *
import random

'''
    COMPUTER            USER            WINNER
      ROCK              ROCK             DRAW
      PAPER             PAPER            DRAW
      SCISSOR           SCISSOR          DRAW
      PAPER             ROCK             COMPUTER
      ROCK              SCISSOR          COMPUTER
      SCISSOR           PAPER            COMPUTER
      
      ROCK              PAPER            USER
      SCISSOR           ROCK             USER
      PAPER             SCISSOR          USER
'''

def game(event):
    global defaultPlayerImage, dImgLabel, dImgCLabel, defaultComputerImage, vsImage, vsImgLabel, winnerLabel
    options = ['Paper', "Rock", "Scissor"]
    userSelect = event.widget.cget('text')
    computerSelect = random.choice(options)
    print(userSelect, computerSelect)
    try:
        if (userSelect=='Paper' and computerSelect=='Paper') or (userSelect=='Rock' and computerSelect=='Rock') or (userSelect=='Scissor' and computerSelect=='Scissor') :
            userImage = PhotoImage(file=f"{str(userSelect.lower())}.png")
            computerImage = PhotoImage(file=f"{str(computerSelect.lower())}.png")
            
            dImgLabel.configure(image=userImage)
            dImgLabel.image = userImage
            
            
            dImgCLabel.configure(image=computerImage)
            dImgCLabel.image = computerImage
            
            winnerLabel.configure(text="Game Draw")
            game()            
        elif (userSelect=='Paper'and computerSelect=="Rock")or(userSelect=="Rock"and computerSelect=="Scissor")or(userSelect=="Scissor" and computerSelect=="Paper"):
            userImage = PhotoImage(file=f"{str(userSelect.lower())}.png")
            computerImage = PhotoImage(file=f"{str(computerSelect.lower())}.png")
            
            dImgLabel.configure(image=userImage)
            dImgLabel.image = userImage
            
            
            dImgCLabel.configure(image=computerImage)
            dImgCLabel.image = computerImage
            
            winnerLabel.configure(text="You Win")
            game()  
        else:
            userImage = PhotoImage(file=f"{str(userSelect.lower())}.png")
            computerImage = PhotoImage(file=f"{str(computerSelect.lower())}.png")
            
            dImgLabel.configure(image=userImage)
            dImgLabel.image = userImage
            
            
            dImgCLabel.configure(image=computerImage)
            dImgCLabel.image = computerImage
            
            winnerLabel.configure(text="Computer Win")
            game()  
            
    except Exception as error:
        pass


if __name__ == '__main__':
    root = Tk()
    
    root.geometry('1330x1000')
    
    heading = Label(text="Rock Paper Scessors Game", font='Algerian 20 bold', fg='#280036')
    heading.grid(row=0, column=0, pady=10)
    
    frame = Frame(root)
    frame.grid(row=1, column=0)
    
    title = Label(frame, text='Player' ,font='Sitka 20 bold')
    title.grid(row=2, column=0,  padx=150)
    
    title = Label(frame, text='Computer' ,font='Sitka 20 bold')
    title.grid(row=2, column=3,  padx=150)
    
    defaultPlayerImage = PhotoImage(file='default.png')
    dImgLabel = Label(frame, image=defaultPlayerImage, bg='#ffffff', width=500, height=470)
    dImgLabel.grid(row=3,column=0)

    vsImage = PhotoImage(file='vs.png')
    vsImgLabel = Label(frame, image=vsImage)
    vsImgLabel.grid(row=3,column=1, padx=10,pady=50)
    
    defaultComputerImage = PhotoImage(file='default.png')
    dImgCLabel = Label(frame, image=defaultPlayerImage, bg='#ffffff', width=500, height=470)
    dImgCLabel.grid(row=3,column=3)

    buttonFrame = Frame(root)
    buttonFrame.grid(row=5, column=0)

    winnerLabel = Label(buttonFrame, text="Winner",font='Sitka 20 bold')
    winnerLabel.grid(row=0, column=1, pady=10)

    r = Button(buttonFrame, text='Rock', width=7, height=1, font='Ariel 20 bold' )
    r.grid(row=2, column=0)
    r.bind("<Button-1>", game)
    
    p = Button(buttonFrame, text='Paper', width=7, height=1, font='Ariel 20 bold')
    p.grid(row=2, column=1)
    p.bind("<Button-1>", game)
    
    s = Button(buttonFrame, text='Scissor', width=7, height=1, font='Ariel 20 bold')
    s.grid(row=2, column=2)
    s.bind("<Button-1>", game)
    
    
        
    root.mainloop()
