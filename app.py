import tkinter
from tkinter import *
from PIL import Image, ImageTk
from chat import get_response, bot_name

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatBotApp:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat Bot")
        canvas = tkinter.Canvas(self.window, width=490, height=640,)
        canvas.grid(columnspan=1, rowspan=5)

        self.window.resizable(width=False, height=False)
        # head label
        head_label = Label(self.window, bg='white', fg='black',
                           text="Welcome To Royal Bank", font='Helvetica 14', pady=12)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg='Black')
        line.place(relwidth=1, relx=0.21, rely=0.07, relheight=0.01)

        # logo
        logo = Image.open('royal4.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label = tkinter.Label(image=logo)
        logo_label.image = logo
        logo_label.grid(column=0, row=0,)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg='#1ce3e0', fg='black',
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.65, relwidth=1, rely=0.33)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.98)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg='#d4f8fc', height=50)
        bottom_label.place(relwidth=1, rely=0.91)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="white", fg='black', font=FONT)
        self.msg_entry.place(relwidth=0.54, relheight=0.05, rely=0.009, relx=0.010)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=18, bg="#a15e64",
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.01, relheight=0.05, relwidth=0.20)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatBotApp()
    app.run()