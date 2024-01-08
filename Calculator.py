import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.geometry('400x400')
        self.resizable(False , False)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0,weight=1)

        # get the width and height of the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # calculate the x and y positions of the window to center it
        x_pos = (screen_width // 2) - (400 // 2)
        y_pos = (screen_height // 2) - (300 // 2)

        # set the position of the window
        self.geometry("+{}+{}".format(x_pos, y_pos))

        #Var that take the entry expresion to evaluate it with eval
        self.expresion = ''
        #Var for the text box (input)
        self.entry = None
        # Var to modify and update the entry text
        self.entry_text = tk.StringVar()

        self._Widgets()

        self.mainloop()

    #Methods
    def _deleteEvent(self):
        # init again for the expresion var to mod and restart the entry box
        self.expresion = ''
        self.entry_text.set(self.expresion)

    def _clickEvent(self, arg):

        self.expresion= f'{self.expresion}{arg}'
        self.entry_text.set(self.expresion)

    def _evalText(self):
        try:
            if self.expresion:
                result = str(eval(self.expresion))
                self.entry_text.set(result)
        except Exception as e:
            messagebox.showerror('Error', f'An error was found it:\n\n{e}')

            self.entry_text.set('')
        self.expresion = ''




    def _Widgets(self):
        # Frame creation
        frame1 = tk.Frame(self, width=400, height=80, bg='Grey')
        frame1.grid(row=0, column=0, sticky='NSWE')
        frame1.grid_columnconfigure(0, weight=1)
        frame1.grid_columnconfigure(2, weight=1)


        # Entry Creation
        entry = tk.Entry(frame1, width=32, font=('arial', 18, 'bold'), justify=tk.RIGHT, textvariable=self.entry_text)
        entry.grid(row=0, column=1, sticky='NSWE', ipadx=5, padx=5, columnspan= 3)
        entry.grid_rowconfigure(0, weight=1)

        frame2 = tk.Frame(self, width=400, bg='Grey')
        self.grid = frame2.grid(row=1, column=0, sticky='NSWE')
        frame2.grid_columnconfigure(0, weight=1)
        frame2.grid_columnconfigure(1, weight=1)
        frame2.grid_columnconfigure(2, weight=1)
        frame2.grid_columnconfigure(3, weight=1)
        frame2.grid_rowconfigure(0,weight=1)
        frame2.grid_rowconfigure(1, weight=1)
        frame2.grid_rowconfigure(2, weight=1)
        frame2.grid_rowconfigure(3, weight=1)
        frame2.grid_rowconfigure(4, weight=1)

        # Button Creation
        cb = tk.Button(frame2, text='C', bd=0, bg='lightgrey', cursor= 'hand2', command=self._deleteEvent)
        cb.grid(row=0, column=0, sticky='NSWE', columnspan=3, padx=2, pady=2)  # Assign sticky to buttons
        b1 = tk.Button(frame2, text='1', command=lambda: self._clickEvent('1'))
        b1.grid(row=3, column=0, sticky='NSWE')  
        b2 = tk.Button(frame2, text='2', command=lambda: self._clickEvent('2'))
        b2.grid(row=3, column=1, sticky='NSWE')  
        b3 = tk.Button(frame2, text='3', command=lambda: self._clickEvent('3'))
        b3.grid(row=3, column=2, sticky='NSWE')  
        b4 = tk.Button(frame2, text='4', command=lambda: self._clickEvent('4'))
        b4.grid(row=2, column=0, sticky='NSWE')  
        b5 = tk.Button(frame2, text='5', command=lambda: self._clickEvent('5'))
        b5.grid(row=2, column=1, sticky='NSWE')  
        b6 = tk.Button(frame2, text='6', command=lambda: self._clickEvent('6'))
        b6.grid(row=2, column=2, sticky='NSWE')  
        b7 = tk.Button(frame2, text='7', command=lambda: self._clickEvent('7'))
        b7.grid(row=1, column=0, sticky='NSWE')  
        b8 = tk.Button(frame2, text='8', command=lambda: self._clickEvent('8'))
        b8.grid(row=1, column=1, sticky='NSWE')  
        b9 = tk.Button(frame2, text='9', command=lambda: self._clickEvent('9'))
        b9.grid(row=1, column=2, sticky='NSWE')  
        b0 = tk.Button(frame2, text='0', command=lambda: self._clickEvent('0'))
        b0.grid(row=4, column=0, sticky='NSWE', columnspan=2)  

        #arithmetic operators buttons
        div=tk.Button(frame2, text='/', command=lambda: self._clickEvent('/')) #Use lambda to give arg without call the function
        div.grid(row=0, column=3, sticky='NSWE')
        multi = tk.Button(frame2, text='*', command=lambda: self._clickEvent('*'))
        multi.grid(row=1 ,column=3, sticky='NSWE')
        sum = tk.Button(frame2, text='+', command=lambda: self._clickEvent('+'))
        sum.grid(row=2, column=3, sticky='NSWE')
        rest = tk.Button(frame2, text='-', command=lambda: self._clickEvent('-'))
        rest.grid(row=3, column=3, sticky='NSWE')
        equal = tk.Button(frame2, text='=', command= self._evalText)
        equal.grid(row=4, column=3, sticky='NSWE')
        dot = tk.Button(frame2, text='.', command=lambda: self._clickEvent('.'))
        dot.grid(row=4, column=2, sticky='NSWE')

if __name__ == '__main__':
    obj1 = Calculator()