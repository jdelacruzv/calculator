"""
    A simple calculator with the basic operations

    Author: José De La Cruz
    Created: 2019-08-02
    Modified: 2024-12-23
"""
import tkinter as tk
from tkinter import StringVar, ttk
import math


def click_button(caption):
    """Insert the clicks given by the user (numbers and symbols)"""
    global indice
    ety_display.insert(indice, caption)
    indice += 1


def clear_display():
    """Clean text box"""
    ety_display.delete(0, tk.END)


def undo_button():
    """Delete the last character and/or number entered"""
    current_display = ety_display.get()
    clear_display()
    # remove the last character from the expression
    ety_display.insert(0, current_display[:-1])


def replace_button(value):
    """Replace 'x' by '*' and '÷' by '/'"""
    if value != '':
        temp = value.replace('÷', '/')
        temp = temp.replace('x', '*')
        temp = temp.replace(',', '.')
        temp = temp.replace('%', '/100')
        temp = temp.replace('\u00b2', '**2')
        temp = temp.replace('\u00bd', '**(1/2)')
        value = temp.replace('⁻¹', '**-1')
    return value


def replace_point_result(val):
    """Replace point by comma of the final result"""
    return str(val).replace('.', ',')


def equals_button():
    """Perform the data operation"""
    current_display = replace_button(ety_display.get())
    try:
        if '!' in current_display:
            math_exp = str(factorial(current_display[:-1]))
            result = replace_point_result(decimal_or_integer(eval(math_exp)))
            clear_display()
            ety_display.insert(0, result)
        else:
            # interprets an expression from a string and returns a mathematical expression
            math_exp = str(eval(current_display))
            result = replace_point_result(decimal_or_integer(eval(math_exp)))
            clear_display()
            ety_display.insert(0, result)
    except:
        clear_display()
        ety_display.insert(0, 'Error')


def decimal_or_integer(result):
    """Returns the integer part of the final result"""
    decimal, entera = math.modf(result)
    if decimal == .0:
        return int(entera)
    else:
        return result


def factorial(n):
    n = int(n)
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    # create main window
    root = tk.Tk()
    root.title('Calculator')
    root.resizable(False, False)
    root.configure(bg='#FFFFE0')

    # it is used to get the instance of input field
    ety_display = StringVar()

    # center window
    a = 335
    b = 405
    x = (root.winfo_screenwidth() - a) / 2
    y = (root.winfo_screenheight() - b) / 2
    root.geometry('%dx%d+%d+%d' % (a, b, x, y))

    # gets the index of the position within the input
    indice = 0

    # create display frame
    frm_display = ttk.Frame(root)
    frm_display.grid(row=0, column=0, padx=5, pady=5)

    # row 0: display
    ety_display = tk.Entry(
        frm_display, 
        width=21, 
        justify=tk.RIGHT, 
        takefocus=False, 
        font=('Consola', 20, 'bold'), 
        background='#282828',
        foreground='#FFFFE0',
        relief='flat'
    )
    
    ety_display.grid(row=0, column=0, columnspan=6, ipady=20)

    # row 1: button frame
    frmButtons = ttk.Frame(root)
    frmButtons.grid(row=1, column=0, padx=5, pady=5)

    # horizontal and vertical inner margin
    IPADX=6 
    IPADY=15

    # buttons style
    ttk.Style().configure(
        'TButton', 
        font=('Helvetica', 11),
        width=5,
        background='#FFFFE0',
    )
    
    # row 1
    ttk.Button(frmButtons, text='7', command=lambda: click_button(7)
               ).grid(row=1, column=0, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='8', command=lambda: click_button(8)
               ).grid(row=1, column=1, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='9', command=lambda: click_button(9)
               ).grid(row=1, column=2, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='÷', command=lambda: click_button('÷')
               ).grid(row=1, column=3, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='x²', command=lambda: click_button('\u00b2')
               ).grid(row=1, column=4, ipadx=IPADX, ipady=IPADY)

    # row 2
    ttk.Button(frmButtons, text='4', command=lambda: click_button(4)
               ).grid(row=2, column=0, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='5', command=lambda: click_button(5)
               ).grid(row=2, column=1, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='6', command=lambda: click_button(6)
               ).grid(row=2, column=2, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='x', command=lambda: click_button('x')
               ).grid(row=2, column=3, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='x⁻¹', command=lambda: click_button('⁻¹')
               ).grid(row=2, column=4, ipadx=IPADX, ipady=IPADY)

    # row 3
    ttk.Button(frmButtons, text='1', command=lambda: click_button(1)
               ).grid(row=3, column=0, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='2', command=lambda: click_button(2)
               ).grid(row=3, column=1, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='3', command=lambda: click_button(3)
               ).grid(row=3, column=2, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='-', command=lambda: click_button('-')
               ).grid(row=3, column=3, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='√x', command=lambda: click_button('\u00bd')
               ).grid(row=3, column=4, ipadx=IPADX, ipady=IPADY)

    # row 4
    ttk.Button(frmButtons, text='0', command=lambda: click_button(0)
               ).grid(row=4, column=0, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text=',', command=lambda: click_button(',')
               ).grid(row=4, column=1, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='%', command=lambda: click_button('%')
               ).grid(row=4, column=2, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='+', command=lambda: click_button('+')
                ).grid(row=4, column=3, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='x!', command=lambda: click_button('!')
               ).grid(row=4, column=4, ipadx=IPADX, ipady=IPADY)
    
    # row 5
    ttk.Button(frmButtons, text='C', command=lambda: clear_display()
               ).grid(row=5, column=0, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='🠔', command=lambda: undo_button()
               ).grid(row=5, column=1, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='(', command=lambda: click_button('(')
               ).grid(row=5, column=2, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text=')', command=lambda: click_button(')')
               ).grid(row=5, column=3, ipadx=IPADX, ipady=IPADY)
    ttk.Button(frmButtons, text='=', command=lambda: equals_button()
               ).grid(row=5, column=4, ipadx=IPADX, ipady=IPADY)

    # run main window loop
    root.mainloop()
