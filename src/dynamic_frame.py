import customtkinter as ctk


class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = ctk.CTkLabel(self, text=self.title, fg_color='gray30', text_color='white', corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='ew')

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky='w')
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget('text'))
        return checked_checkboxes


class MyRadiobuttonFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = ctk.StringVar(value='')

        self.title = ctk.CTkLabel(self, text=self.title, fg_color='gray30', corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='ew')

        for i, value in enumerate(self.values):
            radiobutton = ctk.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky='w')
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)


class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Dynamic Frame')
        self.geometry('400x200')
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = MyCheckboxFrame(self, title='Hobbies', values=['Mobile Dev', 'Web Dev', 'Cybersecurity'])
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nsew')

        self.radiobutton_frame = MyRadiobuttonFrame(self, title='Prog Lang', values=['Kotlin', 'Python'])
        self.radiobutton_frame.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky='nsew')

        self.button = ctk.CTkButton(self, text='Click Me', command=self.command_text)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky='ew', columnspan=2)

    def command_text(self):
        print(f'Checkbox Value: {self.checkbox_frame.get()}')
        print(f'Radiobutton Value: {self.radiobutton_frame.get()}')


app = MyApp()
app.mainloop()
