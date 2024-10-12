import customtkinter as ctk


class MyScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        self.label = ctk.CTkLabel(self, text=title, bg_color='purple', corner_radius=6)
        self.label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='ew')

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


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title = 'Scrollable Frame'
        self.geometry('440x220')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        values = ['Value 1', 'Value 2', 'Value 3', 'Value 4', 'Value 5', 'Value 6']
        self.scrollable_checkbox_frame = MyScrollableFrame(self, title='Values', values=values)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nsew')

        self.button = ctk.CTkButton(self, text='Click me', command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky='ew', columnspan=2)

    def button_callback(self):
        print(f'Checkbox frame:')


app = App()
app.mainloop()
