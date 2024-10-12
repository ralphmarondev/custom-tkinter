import customtkinter as ctk

class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.checkbox_1 = ctk.CTkCheckBox(self, text='Checkbox 1')
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')
        self.checkbox_2 = ctk.CTkCheckBox(self, text='Checkbox 2')
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky='w')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Frames CTK')
        self.geometry('400x180')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nsw')

        self.button = ctk.CTkButton(self, text='Say Hi', command=self.say_hi)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

    @staticmethod
    def say_hi():
        print('Hi there!')

app = App()
app.mainloop()