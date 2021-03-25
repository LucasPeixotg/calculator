import tkinter as tk
from tkinter import ttk

BUTTONS = [
   ['(', ')', 'CE', 'C'],
   ['7', '8', '9', '/'],
   ['4', '5', '6', '*'],
   ['1', '2', '3', '-'],
   ['0', '.', '=', '+'],
]

class MainApp(tk.Frame):
   def __init__(self, master=None):
      super().__init__(master)
      self.master = master

      self.screen = tk.Entry(
         bg='#333', 
         fg='#eee',
         font=('Arial', 15),
         justify=tk.RIGHT,
         highlightthickness=5,
         highlightcolor='#333',
         highlightbackground='#333',
         bd=0
      )
      self.screen.bind('<1>', self.clean_when_error)
      self.screen.grid(columnspan=len(BUTTONS[0]), sticky=tk.N+tk.S+tk.E+tk.W)

      for x in range(len(BUTTONS)+1):
         tk.Grid.rowconfigure(self.master, x, weight=1)
      for y in range(len(BUTTONS[0])):
         tk.Grid.columnconfigure(self.master, y, weight=1)

      self.create_buttons(buttons=BUTTONS)


   def create_buttons(self, buttons):
      '''
      Function that creates the Button objects based on a matrix
      '''
      for i in range(len(buttons)):
         for j in range(len(buttons[i])):
            btn = tk.Button(
               text=buttons[i][j],
               bg='#111',
               fg='#eee',
               font=('Arial', 15),
               bd=0,
               command=lambda text=buttons[i][j]: self.button_actions(text),
            )
            btn.grid(row=i+1, column=j, sticky=tk.N+tk.S+tk.E+tk.W)

   def clean_when_error(self, *args):
      '''
      Function that clean the screen when clicked
      if the message is an error message.
      '''
      if self.screen.get() == 'ERROR':
         self.screen.delete(0, len(self.screen.get()))

   def button_actions(self, btn_text):
      if(self.screen.get() == 'ERROR'):
         self.screen.delete(0, len(self.screen.get()))

      if btn_text == 'C':
         self.screen.delete(0, len(self.screen.get()))
      elif btn_text == 'CE':
         self.screen.delete(len(self.screen.get())-1, len(self.screen.get()))
      elif btn_text == '=':
         self.master.focus()
         if self.screen.get():
            try:
               result = eval(self.screen.get())
            except (NameError, SyntaxError):
               print('ERROR')
               result = 'ERROR'
            self.screen.delete(0, len(self.screen.get()))
            self.screen.insert(0, result)
      else:
         self.screen.insert(len(self.screen.get()), btn_text)

root = tk.Tk()
root.config(bg='#111')
root.resizable(True, True)

app = MainApp(master=root)
app.mainloop()
