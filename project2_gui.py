#gui file
from project2_logic import *
from tkinter import *

class MenuGUI:
    def __init__(self, window):
        '''
        Initialize all objects in the GUI window
        :param window: GUI instance
        '''
        self.__window = window
        self.__voting_system = VotingSystem()

        self.__frame1 = Frame(self.__window)
        self.__frame2 = Frame(self.__window)
        self.__frame3 = Frame(self.__window)
        self.__frame4 = Frame(self.__window)
        self.__frame5 = Frame(self.__window)
        self.__frame6 = Frame(self.__window)
        self.__frame7 = Frame(self.__window)

        self.__title_label = Label(self.__frame1,text='VOTE BALLOT')
        self.__id_label = Label(self.__frame2, text='Your ID:')
        self.__id_entry = Entry(self.__frame3)
        self.__cand_label = Label(self.__frame4, text='Candidates:')
        self.__options = ('Maria', 'Howard', 'Joseph')
        self.__x = IntVar(value=-1)
        for choice in range(len(self.__options)):
            self.__radiobutton = Radiobutton(self.__frame5, text=self.__options[choice], variable=self.__x,
                                             value=choice)
            self.__radiobutton.pack(padx=10) #contains packing of radio buttons
        self.__submit_button = Button(self.__frame6, text='Submit', command=self.submit_vote)
        self.__display_results_button = Button(self.__frame6, text='Display Results', command=self.display_results)
        self.__color_label = Label(self.__frame7, text='', fg='red')

        #The packing
        self.__frame1.pack(fill=X, padx=20, pady=5)
        self.__frame2.pack(fill=X, padx=20, pady=5)
        self.__frame3.pack(fill=X, padx=20, pady=5)
        self.__frame4.pack(fill=X, padx=20, pady=5)
        self.__frame5.pack(fill=X, padx=10, pady=3)
        self.__frame6.pack(fill=X, padx=20, pady=5)
        self.__frame7.pack(fill=X, padx=40, pady=50)

        self.__title_label.pack()
        self.__id_label.pack()
        self.__id_entry.pack()
        self.__cand_label.pack()
        self.__submit_button.pack()
        self.__display_results_button.pack()
        self.__color_label.pack(fill=X, expand=True)


    def get_id(self) -> str:
        '''
        Gets the ID entry
        :return: None
        '''
        return self.__id_entry.get()

    def submit_vote(self) -> None:
        '''
        Method when Submit button is clicked, stores vote information in CSV file.
        Catches error and displays errors when necessary.
        :return: None
        '''
        num: str = self.get_id()
        candidate: str = self.__options[self.__x.get()]
        try:
            self.__voting_system.store_vote(ID=num, candidate=candidate)
            self.__color_label.config(text='Vote submitted.', fg='green')
        except TypeError as e:
            self.__color_label.config(text=str(e), fg='red')
        except ValueError as v:
            self.__color_label.config(text=str(v), fg='red')

    def display_results(self) -> None:
        """
        Grabs results from external result getter, displays them on the bottom of vote ballot.
        :return: None
        """
        self.__results = self.__voting_system.get_results()
        message: str = "Election Results:\n"

        for candidate, votes in self.__results.items():
            if candidate != "Candidate":
                message += f"{candidate}: {votes},"


        self.__color_label.config(text=message, fg='black')

