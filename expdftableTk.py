# -*- coding: utf-8 -*-
"""
Frontend of expdftable

Created on Sun Aug  4 20:39:44 2024

@author: y_aka
"""

from os import path

from expdftable import expdftable
import fitz

import tkinter as tk
from tkinter import (
    BooleanVar, Button, Entry, filedialog, Frame, IntVar,Label, StringVar, Tk,
    messagebox
)

from tkinter.ttk import Checkbutton, Spinbox

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.initInFile()
        self.initPageControl()
        self.initOutFile()
        
        self.join = BooleanVar(value=False)
        Checkbutton(self, text='Join all tables',variable=self.join).pack()
        
        Button(self, text='Extract', command=self.extractButtonClick).pack()       
    
    def initInFile(self):
        frm = Frame(self)
        frm.pack()
        
        Label(frm, text='PDF').pack(side=tk.LEFT)
        
        self.inFile = StringVar()
        self.inFileEntry = Entry(frm, textvariable=self.inFile, width=50).pack(side=tk.LEFT)
        
        Button(frm, text='Reffer', command=self.inFileButtonClick).pack(side=tk.LEFT)
    
    def initPageControl(self):
        frm = Frame(self)
        frm.pack()
        
        Label(frm, text='Start').pack(side=tk.LEFT)
        self.start = IntVar(value=1)
        self.start.trace('w', self.startChanged)
        self.startSpin = Spinbox(frm, from_=1, to=1, textvariable=self.start)
        self.startSpin.pack(side=tk.LEFT)

        Label(frm, text='End').pack(side=tk.LEFT)
        self.end = IntVar(value=1)
        self.end.trace('w', self.endChanged)
        self.endSpin = Spinbox(frm, from_=1, to=1, textvariable=self.end)
        self.endSpin.pack(side=tk.LEFT)
    
    def initOutFile(self):
        frm = Frame(self)
        frm.pack()
        
        Label(frm, text='Excel').pack(side=tk.LEFT)
        
        self.outFile = StringVar()
        self.outFileEntry = Entry(frm, textvariable=self.outFile, width=50).pack(side=tk.LEFT)
        
        Button(frm, text='Reffer', command=self.outFileButtonClick).pack(side=tk.LEFT)
        
    
    def inFileButtonClick(self):
        self.inFile.set(filedialog.askopenfilename(filetypes=[('PDF File', '*.pdf')]))
        excel = path.splitext(self.inFile.get())[0] + '.xlsx'
        self.outFile.set(excel)
        
        doc = fitz.open(self.inFile.get())
        self.startSpin["to"] = doc.page_count
        self.endSpin["to"] = doc.page_count
        doc.close()

    def outFileButtonClick(self):
        self.outFile.set(filedialog.asksaveasfilename(filetypes=[('Excel File', '*.xlsx')]))
    
    def startChanged(self, *args):
        if self.start.get() > self.end.get():
            self.end.set(self.start.get())
    
    def endChanged(self, *args):
        if self.start.get() > self.end.get():
            self.start.set(self.end.get())
    
    def extractButtonClick(self):
        pdf = self.inFile.get()
        excel = self.outFile.get()
        start = self.start.get()
        end = self.end.get()
        join = self.join.get()
        
        isError = False
        errorMessage = ""
        
        if len(pdf) == 0:
            isError = True
            errorMessage = errorMessage + "- no selct pdf file.\n"
            
        if len(excel) == 0:
            isError = True
            errorMessage = errorMessage + "- no select excel file.\n"

        if isError:
            messagebox.showerror(title='expdftableTk', message=errorMessage)
            return
        
        try:
            expdftable(pdf, excel, start, end, join)
            messagebox.showinfo(title='expdftableTk', message='Complete extract')
        except Exception as ex:
            messagebox.showerror(title='expdftableTk', message=ex)


root = Tk()
root.title('Extract tables from PDF to Excel Book')
myapp = App(root)
myapp.mainloop()

