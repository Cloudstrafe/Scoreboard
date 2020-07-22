from tkinter import Tk, StringVar, Frame, Label, Entry, SOLID, Button, IntVar, NSEW, E, W


# borderwidth=1, relief=SOLID    Good for debugging

class ScoreboardWindow:
    def __init__(self):
        self.root = Tk()
        self.team1 = StringVar()
        self.team2 = StringVar()
        self.team1.set("Team 1")
        self.team2.set("Team 2")
        self.team1score = IntVar()
        self.team2score = IntVar()
        self.teamnameframe = Frame(self.root)
        self.team1scoreframe = Frame(self.root)
        self.team2scoreframe = Frame(self.root)
        self.scoreboardframe = Frame(self.root)

        self.initializeWindow()
        self.gridFrames()
        self.initializeTeamNameFrame()
        self.initializeTeam1ScoreFrame()
        self.initializeTeam2ScoreFrame()
        self.initializeScoreboardFrame()

    def initializeWindow(self):
        self.root.geometry("430x210")
        self.root.resizable(width=False, height=False)
        self.root.title("Scoreboard")

    def gridFrames(self):
        self.teamnameframe.grid(row=0, column=0, columnspan=2, padx=4, pady=4)
        self.team1scoreframe.grid(row=1, column=0, padx=4, pady=4)
        self.team2scoreframe.grid(row=1, column=1, padx=4, pady=4)
        self.scoreboardframe.grid(row=2, column=0, columnspan=2, padx=4, pady=4, sticky=NSEW)
        self.scoreboardframe.grid_columnconfigure(0, weight=1)
        self.scoreboardframe.grid_columnconfigure(1, weight=1)

    def initializeTeamNameFrame(self):
        labelteam1 = Label(self.teamnameframe, text="Team 1 Name:")
        labelteam1.grid(row=0, column=0, pady=(0, 4))
        entryteam1 = Entry(self.teamnameframe, textvariable=self.team1, width=25)
        entryteam1.grid(row=0, column=1, pady=(0, 4))
        labelteam2 = Label(self.teamnameframe, text="Team 2 Name:")
        labelteam2.grid(row=1, column=0)
        entryteam2 = Entry(self.teamnameframe, textvariable=self.team2, width=25)
        entryteam2.grid(row=1, column=1)

    def initializeTeam1ScoreFrame(self):
        labelteam1control = Label(self.team1scoreframe, text="Team 1 Controls:")
        labelteam1control.grid(row=0, columnspan=3, column=0)
        buttonteam1minus = Button(self.team1scoreframe, text="-1", width=8, command=lambda: self.decrement(self.team1score))
        buttonteam1minus.grid(row=1, column=0)
        buttonteam1plus = Button(self.team1scoreframe, text="+1", width=8, command=lambda: self.increment(self.team1score))
        buttonteam1plus.grid(row=1, column=1, padx=4)
        buttonteam1reset = Button(self.team1scoreframe, text="Reset", width=8, command=lambda: self.reset(self.team1score))
        buttonteam1reset.grid(row=1, column=2)

    def initializeTeam2ScoreFrame(self):
        labelteam2control = Label(self.team2scoreframe, text="Team 2 Controls:")
        labelteam2control.grid(row=0, columnspan=3, column=0)
        buttonteam2minus = Button(self.team2scoreframe, text="-1", width=8, command=lambda: self.decrement(self.team2score))
        buttonteam2minus.grid(row=1, column=0)
        buttonteam2plus = Button(self.team2scoreframe, text="+1", width=8, command=lambda: self.increment(self.team2score))
        buttonteam2plus.grid(row=1, column=1, padx=4)
        buttonteam2reset = Button(self.team2scoreframe, text="Reset", width=8, command=lambda: self.reset(self.team2score))
        buttonteam2reset.grid(row=1, column=2)

    def initializeScoreboardFrame(self):
        labelteam1name = Label(self.scoreboardframe, textvariable=self.team1, font=("Times New Roman", 18), fg="red", anchor=E, width=15)
        labelteam1name.grid(row=0, column=0, padx=4, pady=4, sticky=NSEW)
        labelteam1score = Label(self.scoreboardframe, textvariable=self.team1score, font=("Times New Roman", 24, "bold"), fg="red", anchor=E, width=3)
        labelteam1score.grid(row=1, column=0, padx=4, pady=4, sticky=NSEW)
        labelteam2name = Label(self.scoreboardframe, textvariable=self.team2, font=("Times New Roman", 18), fg="blue", anchor=W, width=15)
        labelteam2name.grid(row=0, column=1, padx=4, pady=4, sticky=NSEW)
        labelteam2score = Label(self.scoreboardframe, textvariable=self.team2score, font=("Times New Roman", 24, "bold"), fg="blue", anchor=W, width=3)
        labelteam2score.grid(row=1, column=1, padx=4, pady=4, sticky=NSEW)

    def decrement(self, team):
        team.set(team.get() - 1)

    def increment(self, team):
        team.set(team.get() + 1)

    def reset(self, team):
        team.set(0)
