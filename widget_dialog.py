import tkinter as tk
from tkinter import messagebox as mb


def resposta():
    mb.showerror("Answer", "Sorry, no answer available!")


def verificacao():
    if mb.askyesno('Verificar', 'Realmente quer sair?'):
        mb.showwarning('Yes', 'is not yet implemented')
    else:
        mb.showinfo('No', 'The exit option has been cancelled')

tk.Button(text='Sair', command=verificacao).pack(fill=tk.X)
tk.Button(text='Resposta', command=resposta).pack(fill=tk.X)
tk.mainloop()