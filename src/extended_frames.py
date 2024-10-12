import customtkinter as ctk


class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.checkbox_1 = ctk.CTkCheckBox(self, text='First')
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')
        self.checkbox_2 = ctk.CTkCheckBox(self, text='Second')
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky='w')
        self.checkbox_3 = ctk.CTkCheckBox(self, text='Third')
        self.checkbox_3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky='w')

    def get(self):
        checked_checkboxes = []

        if self.checkbox_1.get() == 1:
            checked_checkboxes.append(self.checkbox_1.cget('text'))
        if self.checkbox_2.get() == 1:
            checked_checkboxes.append(self.checkbox_2.cget('text'))
        if self.checkbox_3.get() == 1:
            checked_checkboxes.append(self.checkbox_3.cget('text'))

        return checked_checkboxes


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Extended Frames')
        self.geometry('300x200')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nsw')

        self.button = ctk.CTkButton(self, text='CLICK', command=self.output)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

    def output(self):
        print(f'Content: {self.checkbox_frame.get()}')


app = App()
app.mainloop()
