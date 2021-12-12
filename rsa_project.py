from tkinter import*
import tkinter as ttk
from tkinter import font
from types import resolve_bases
from typing import Collection, TextIO 

class chiffrement_rsa_estk:
    def __init__(self, root):
        self.root = root
        self.root.title("chiffrement RSA ESTK")
        self.root.geometry("1200x600+100+20")
    
        #?variables #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #-
        self.p = IntVar()
        self.q = IntVar()
        self.n = (self.p.get()*self.q.get())
        self.m = ((self.p.get()-1)*(self.q.get()-1))
        self.e = IntVar()
        message_entry.get(1.0 , "end-1c")
        
    #?functions #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #-
    
    def MessageInput(self):
        print("message input works")
        inp = self.inputmessage.get()
        ascii_values = []
        for character in inp:
            ascii_values.append(ord(character))
            print(ascii_values)
    
    
        #?frames #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #-
        #!mainframe
        mainframe = Frame(root, bd=5, width=1190,bg='#9eeeff', height=590, relief=RIDGE)
        mainframe.grid(padx=2, pady=2)
        
        #!topframe 
        topframe = Frame(mainframe,bd=5, height=40, width=1180, relief=RIDGE)
        topframe.pack(side=TOP, padx=3, pady=3, expand=True, fill=X)
        
        #!middleframe 
        middleframe = Frame(mainframe,bd=5, height=60, width=1180, relief=RIDGE)
        middleframe.pack(side=TOP, padx=3, pady=3, expand=True, fill=X)
        
        #!bottomframe
        bottomframe = Frame(mainframe,bd=5, height=80, width=680, relief=RIDGE)
        bottomframe.pack(side=BOTTOM, padx=3, pady=3, expand=True, fill=BOTH)
        
        #!rightframe
        rightframe = Frame(mainframe,bd=5, height=300, width=400, relief=RIDGE)
        rightframe.pack(side=RIGHT, padx=3, pady=3,expand=True, fill=Y)
        
        #!righttop
        righttop = Frame(rightframe,bd=5, height=100, width=400, relief=RIDGE)
        righttop.pack(side=TOP, padx=3, pady=3, expand=True, fill=X)
        
        #!right
        right = Frame(rightframe,bd=5, height=290, width=400, relief=RIDGE)
        right.pack(padx=3, pady=3, expand=True, fill=Y)
        
        #!leftframe
        leftframe = Frame(mainframe,bd=5, height=110, width=680, relief=RIDGE)
        leftframe.pack(side=TOP, padx=3, pady=3, expand=True, fill=BOTH)
        
        #!lefttop
        lefttop = Frame(leftframe,bd=5, height=190, width=680, relief=RIDGE)
        lefttop.pack(side=TOP, padx=3, pady=3, expand=True, fill=X)
        
        #!left
        left = Frame(leftframe,bd=5, height=90, width=680, relief=RIDGE)
        left.pack(side=TOP, padx=3, pady=3, expand=True, fill=X)
        
        #!messagelabel
        messagelabel = Frame(left,bd=5, height=90, width=339, relief=RIDGE)
        messagelabel.pack(side=LEFT, padx=3, pady=3, expand=True, fill=X)
        
        #!messagechifflabel
        messagechifflabel = Frame(left,bd=5, height=90, width=339, relief=RIDGE)
        messagechifflabel.pack(side=RIGHT, padx=3, pady=3, expand=True, fill=X)
        
        #!note 
        note_txt = Frame(righttop, bd=5, height=49, width=199, relief=RIDGE)
        note_txt.pack(side=TOP, expand=True, fill=X)
        
        #?Components #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #- #-
        #?TopFrame 
        #!TitleLabel 
        TitleLabel = Label(topframe, font=('arial', 20, 'bold'), text='Chiffrement RSA', relief=FLAT)
        TitleLabel.pack(expand=True)
        
        #?middleFrame
        #!P
        p_label = Label(middleframe, font=('arial', 15, 'bold'), text='P', relief=FLAT)
        p_label.grid(column=0, row=0, padx=5,pady=2)
        
        P_entry = Entry(middleframe, font=('arial', 13, 'italic'), textvariable='', relief=RIDGE)
        P_entry.grid(column=1, row=0, padx=25, pady=2)
        
        #!Q
        p_label = Label(middleframe, font=('arial', 15, 'bold'), text='q', relief=FLAT)
        p_label.grid(column=2, row=0, padx=5,pady=2)
        
        q_entry = Entry(middleframe, font=('arial', 13, 'italic'), textvariable='', relief=RIDGE)
        q_entry.grid(column=3, row=0, padx=25, pady=2)
        
        #!e
        p_label = Label(middleframe, font=('arial', 15, 'bold'), text='e', relief=FLAT)
        p_label.grid(column=4, row=0, padx=5,pady=2)
        
        q_entry = Entry(middleframe, font=('arial', 13, 'italic'), textvariable='', relief=RIDGE)
        q_entry.grid(column=5, row=0, padx=25, pady=2)
        
        #!e
        p_label = Label(middleframe, font=('arial', 15, 'bold'), text='d', relief=FLAT)
        p_label.grid(column=6, row=0, padx=5,pady=2)
        
        q_entry = Entry(middleframe, font=('arial', 13, 'italic'), textvariable='', relief=RIDGE)
        q_entry.grid(column=7, row=0, padx=25, pady=2)
        
        #?leftTop
        #!n
        pxq_label = Label(lefttop, font=('arial', 15, 'bold'), text="n=p x q", relief=FLAT)
        pxq_label.pack(padx=5, pady=5, side=LEFT)
        
        pxq_entry = Label(lefttop, font=('arial', 13, 'italic'), bg='#ffffff',width=15, textvariable='', relief=RIDGE)
        pxq_entry.pack(padx=5, pady=5, side=LEFT)
        
        #!m
        m_label = Label(lefttop, font=('arial', 15, 'bold'), text="m=(p-1)x(q-1)", relief=FLAT)
        m_label.pack(padx=5, pady=5, side=LEFT)
        
        m_entry = Label(lefttop, font=('arial', 13, 'italic'), bg='#ffffff',width=15, textvariable='', relief=RIDGE)
        m_entry.pack(padx=5, pady=5, side=LEFT)
        
        #?left
        #!message a chiffrer 
        message_label = Label(messagelabel, font=('arial', 15, 'italic'), text="message", relief=FLAT)
        message_label.pack(padx=5, pady=5, side=TOP)
        
        message_entry = ttk.Text(messagelabel, font=('arial', 13, 'italic'), width=30,height=12, relief=RIDGE)
        message_entry.pack(padx=5, pady=5, expand=True, fill=X)
        
        chiff_btn = Button(messagelabel, height=2, width=15, command=MessageInput(), text='chiffrer')
        chiff_btn.pack(side=BOTTOM)
        
        #!Message chiffré
        messagechiff_label = Label(messagechifflabel, font=('arial', 15, 'italic'), text="Message chiffré", relief=FLAT)
        messagechiff_label.pack(padx=5, pady=5, side=TOP)
        
        messagechiff_entry = ttk.Text(messagechifflabel, font=('arial', 13, 'italic'), width=30,height=12, relief=RIDGE)
        messagechiff_entry.pack(padx=5, pady=5, expand=True, fill=X)
        
        chiff_btn = Button(messagechifflabel, height=2, width=15, command='', text='dechiffrer')
        chiff_btn.pack(side=BOTTOM)
        
        #?right note 
        Note_label = Label(note_txt, font=('arial', 15, 'bold'), text="Note:", relief=FLAT)
        Note_label.pack(side=LEFT)
        
        Notecontent_label = Label(righttop, font=('arial', 15, 'italic'), text="les deux nombres p et q\n doivent etre les deux premiers!", relief=FLAT)
        Notecontent_label.pack(expand=True, fill=BOTH)
        
        
        
        
        
#!_______________________
if __name__ == '__main__':
    root = Tk()
    application = chiffrement_rsa_estk(root)
    root.mainloop()