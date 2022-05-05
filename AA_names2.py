# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 16:10:20 2022

@author: xileioo
"""

import tkinter as tk

# =============================================================================
# AA_table = {}
# 
# def write():
#     with open('Amino_acid_names.csv') as file:
#         next(file)
#         for line in file:
#             line = line.rstrip('\n')
#             AA,ThreeCode,OneCode = line.split(',')
#             #print(AA,ThreeCode,OneCode)
#             AA_table[ThreeCode] = OneCode
#     
# =============================================================================
AA_table = {
  "ala": "A",
  "arg": "R",
  "asn": "N",
  "asp": "D",
  "asx": "B",
  "cys": "C",
  "glu": "E",
  "gln": "Q",
  "glx": "Z",
  "gly": "G",
  "his": "H",
  "ile": "I",
  "leu": "L",
  "lys": "K",
  "met": "M",
  "phe": "F", 
  "pro": "P",
  "ser": "S",
  "thr": "T",
  "trp": "W",
  "tyr": "Y",
  "val": "V"
}

def on_change(e):
    Ones = ""
    seq = e.widget.get()
    seq = seq.lower()
    #print(seq)
    n = 3
    # Using list comprehension
    out = [(seq[i:i+n]) for i in range(0, len(seq), n)]
    #print(out)
    for Three in out:
        if Three in AA_table:
            One = AA_table[Three]
            #print(One)
        else:
            One = "X"
        Ones = Ones + One
    print(Ones)
    ws = tk.Tk()
    ws.title("Amino acids, convert result")
    ws.geometry('500x200+700+200')  
    ws.configure(background='#5eba7d')
    text_box = tk.Text(ws, height=6,width=30)
    text_box.pack(expand=True)
    text_box.insert('end', Ones)
    text_box.config(state='disabled')



#write()
root = tk.Tk()
root.title("Amino acids, three letter codes to one letter codes")
root.geometry('500x200+100+200')   
e = tk.Entry(root, width=60)
e.place(x = 100,
        y = 20,
        width=300,
        height=30)
#e.pack(padx=10)    
# Calling on_change when you press the return key
e.bind("<Return>", on_change)  

root.mainloop()