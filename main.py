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
    global defaultPlayerImage, dImgLabel, dImgCLabel, defaultComputerImage, winnerLable
    options = ["paper", 'rock', 'scissors']
    userSelect = event.widget.cget("text")
    computerSelect = random.choice(options)
    print(userSelect, computerSelect)
    try:
        userImage = PhotoImage(file=f"{str(userSelect.lower())}.png")
        computerImage = PhotoImage(file=f"{str(computerSelect.lower())}.png")

        dImgLabel.configure(image=userImage)
        dImgLabel.image = userImage

        dImgCLabel.configure(image=computerImage)
        dImgCLabel.image = computerImage

        if userSelect==computerSelect:
            winnerLable.configure(text="Game Draw")
            # game() # for debug
        elif(userSelect=='paper' and computerSelect=="rock") or(userSelect=="rock"and computerSelect=="scissors")or(userSelect=="scissots"and computerSelect=="paper"):
            winnerLable.configure(text="You Win")
            # game() # for debug
        else:
            winnerLable.configure(text="Computer Win")
            # game() # for debug

    except Exception as err:
        print(err)

if __name__=="__main__":
    root = Tk()

    root.geometry("1330x1000")
    root.title("Rock Paer Scissors Game - Jocefyneroot")

    heading = Label(text="Rock Paper Scessors Game", font='Algerian 20 bold', fg='#280036')
    heading.grid(row=0, column=0, pady=10)

    frame = Frame(root)
    frame.grid(row=1, column=0)

    title = Label(frame, text="Player", font="Sitka 20 bold")
    title.grid(row=2, column=0, padx=150)

    title = Label(frame, text="Computer", font="Sitka 20 bold")
    title.grid(row=2, column=3, padx=150)

    defaultPlayerImage = PhotoImage(file="default.png")
    dImgLabel = Label(frame, image=defaultPlayerImage, bg="#ffffff", width=500, height=470)
    dImgLabel.grid(row=3, column=0)

    vsImage = PhotoImage(file="vs.png")
    vsImgLabel = Label(frame, image=vsImage)
    vsImgLabel.grid(row=3, column=1, padx=10, pady=50)

    defaultComputerImage = PhotoImage(file="default.png")
    dImgCLabel = Label(frame, image=defaultPlayerImage, bg="#ffffff", width=500, height=470)
    dImgCLabel.grid(row=3, column=3)

    buttonFrame = Frame(root)
    buttonFrame.grid(row=5, column=0)
    
    winnerLable = Label(buttonFrame, text="Winner", font="Sitka 20 bold")
    winnerLable.grid(row=0, column=1)

    r = Button(buttonFrame, text="rock", width=6, height=1, font="Ariel 20 bold")
    r.grid(row=2, column=0)
    r.bind("<Button-1>", game)

    p = Button(buttonFrame, text="paper", width=6, height=1, font="Ariel 20 bold")
    p.grid(row=2, column=1)
    p.bind("<Button-1>", game)

    s = Button(buttonFrame, text="scissors", width=6, height=1, font="Ariel 20 bold")
    s.grid(row=2, column=2)
    s.bind("<Button-1>", game)

    root.mainloop()
