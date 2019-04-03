from tkinter import *
from bc import Database
# Make class Database availabe in the frontend

database = Database("books.db")

class Window(object):
# Create class oject called Window

    def __init__(self,window):
    # Definition of init method including window argument

        self.window = window
        # Defintion of window instance variable

        self.window.wm_title("Book Manager")
        # Defintion of title for instance variable

        l1 = Label(window, text="Title")
        l1.grid(row=0, column=0)
        # Defition of labels and set positions using grid method

        l2 = Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3 = Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4 = Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        self.title_text = StringVar()
        e1 = Entry(window, textvariable=self.title_text)
        e1.grid(row=0, column=1)
        # Definition of entry labels using StringVar() for text variables
        # Position is set using grid method

        self.author_text = StringVar()
        e2 = Entry(window, textvariable=self.author_text)
        e2.grid(row=0, column=3)

        self.year_text = StringVar()
        e3 = Entry(window, textvariable=self.year_text)
        e3.grid(row=1, column=1)

        self.isbn_text = StringVar()
        e4 = Entry(window, textvariable=self.isbn_text)
        e4.grid(row=1, column=3)

        self.list1=Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)
        # Defintion of the listbox that displays the books data
        # Set the position using grid method

        sb1=Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)
        # Defintion of the scrollbar for viewing the books data
        # Set the position using grid method

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)
        # Link listbox with the scrollbar using configure method

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)
        # Link listbox with get_selected_row method using bind method

        b1 = Button(window, text="View all", width=12, command=self.view_command)
        b1.grid(row=2, column=3)
        # Defintion of buttons with respective names and commands
        # Set the position of buttons using grid method

        b2 = Button(window, text="Search entry", width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3 = Button(window, text="Add entry", width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4 = Button(window, text="Update Selected", width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5 = Button(window, text="Delete Selected", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6 = Button(window, text="Close", width=12, command=window.destroy)
        b6.grid(row=7, column=3)

    def get_selected_row(self, event):
    # Definition of selected row method to click on the listbox
        index = self.list1.curselection()[0]
        self.selected_tuple = self.list1.get(index)
        if not self.list1.curselection():
            pass
        else:
            e1.delete(0,END)
            e1.insert(END,selected_tuple[1])
            e2.delete(0,END)
            e2.insert(END,selected_tuple[2])
            e3.delete(0,END)
            e3.insert(END,selected_tuple[3])
            e4.delete(0,END)
            e4.insert(END,selected_tuple[4])

    def view_command(self):
    # Definion of view command method that links view all button with bc
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)

    def search_command(self):
    # Definition of search method that links seach entry button with bc
        self.list1.delete(0,END)
        for row in database.search(self.title_text.get(),
        self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
            self.list1.insert(END,row)

    def add_command(self):
    # Definition of add method that links add entry button with bc
        self.list1.delete(0,END)
        database.insert(self.title_text.get(),self.author_text.get(),
        self.year_text.get(),self.isbn_text.get())
        list1.insert(END,(self.title_text.get(),self.author_text.get(),
        self.year_text.get(),self.isbn_text.get()))

    def delete_command(self):
    # Definition of delete method that links delete selected button with bc
        database.delete(self.selected_tuple[0])

    def update_command(self):
    # Define of update method that links update entry button with bc
        database.update(self.selfselected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

window = Tk()
Window(window)
window.mainloop()
