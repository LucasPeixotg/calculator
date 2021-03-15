from tkinter import * 

class MainApp(Frame):
   def __init__(self, master=None):
      super().__init__(master)
      self.master = master

      self.screen = Entry(
         bg='#333', 
         fg='#eee',
         font=('Arial', 15),
         justify=RIGHT,
         bd=0,
      )
      self.screen.bind('<1>', self.entry_active)
      self.screen.grid(columnspan=4, ipadx=33 ,ipady=10)

      self.create_buttons()


   def create_buttons(self):
      buttons = [
         [
            Button(text='(', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('(')),
            Button(text=')', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text(')')),
            Button(text='CE', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('CE')),
            Button(text='C', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('C')),
         ],
         [
            Button(text='7', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('7')),
            Button(text='8', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('8')),
            Button(text='9', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('9')),
            Button(text='/', bg='#222', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('/')),
         ],
         [
            Button(text='4', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('4')),
            Button(text='5', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('5')),
            Button(text='6', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('6')),
            Button(text='*', bg='#222', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('*')),
         ],
         [
            Button(text='1', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('1')),
            Button(text='2', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('2')),
            Button(text='3', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('3')),
            Button(text='-', bg='#222', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('-')),
         ],
         [
            Button(text='0', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('0')),
            Button(text='.', bg='#111', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('.')),
            Button(text='=', bg='#ff3030', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('=')),
            Button(text='+', bg='#222', fg='#eee', font=('Arial', 15), width=6, height=2, bd=0, command=lambda: self.change_text('+'))
         ]
      ]

      for i in range(5):
         for j in range(4):
            buttons[i][j].grid(row=i+1, column=j)
      

   def entry_active(self, *args):
      print('Is it an ERROR message?')
      if self.screen.get() == 'ERROR':
         print("Yes, deleting...")
         self.screen.delete(0, len(self.screen.get()))
      else:
         print("No...")

   def change_text(self, value):
      if(self.screen.get() == 'ERROR'):
         self.screen.delete(0, len(self.screen.get()))

      if value == 'C':
         self.screen.delete(0, len(self.screen.get()))
      elif value == 'CE':
         self.screen.delete(len(self.screen.get())-1, len(self.screen.get()))
      elif value == '=':
         self.master.focus()
         if self.screen.get():
            try:
               result = eval(self.screen.get())
            except NameError or SyntaxError:
               print('ERROR')
               result = 'ERROR'
            self.screen.delete(0, len(self.screen.get()))
            self.screen.insert(0, result)
      else:
         self.screen.insert(len(self.screen.get()), value)

root = Tk()
root.config(bg='#111')
root.resizable(False, False)

app = MainApp(master=root)
app.mainloop()
