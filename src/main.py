import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title('Custom Tkinter Basics')
        self.geometry('500x400')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        button = ctk.CTkButton(self, text='Say Hello', command=self.say_hello)
        button.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    @staticmethod
    def say_hello():
        print('Hello')


app = App()
app.mainloop()
