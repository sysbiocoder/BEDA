from Tkinter import *
import unicodedata
import sys
master = Tk()
master.tk.call('encoding', 'system', 'utf-8')

Label(text="Batch Analysis",fg = "light blue",bg = "dark blue",width=100).pack()

separator = Frame(height=2, bd=1, relief=SUNKEN,bg = "dark green")
separator.pack(fill=X, padx=5, pady=5)

#label2 = Label(text="%s%s" % (u"\u2318","P"))
#label2.pack(padx=10, pady=10)
Label(text="Cell growth rate", anchor=W, compound =LEFT).pack()
#Label(master, text="%s"% (u"\u0119")).pack()
text = Text(master, width=80, height=12)
text.insert(INSERT," In Batch, the cells are dividing at a constant rate resulting in an exponential increase in the number of cells present.\n")

text.insert(INSERT,"%s%s%s"%("dx/dt=", u"\u03BC","X"))
text.insert(INSERT,"%s%s%s%s"%("\nwhere dx/dt is Exponential growth rate is First Order with respect to X, X is the cell concentration, ",u"\u03BC"," is the cell growth rate","\n"))
text.tag_configure("subscript", offset=-4)
text.insert(INSERT,"\nln(x/x","x","0","subscript",")=")
text.insert(INSERT,"%s%s%s"%("",u"\u03BC","t\n"))
text.insert(INSERT,"%s%s%s"%("where x and x","0"," are cell concentration at time t and t=0.\n"))

text.insert(INSERT,"\nDoubling time td(time required to double microbial mass or number) when x=2x","x","0","subscript", " \ntd = ln", "ln","2","subscript")
text.insert(INSERT,"%s%s"%("/",u"\u03BC"))
text.pack()
separator.pack(fill=X, padx=5, pady=5)
Label(text="Yield Coefficient").pack()
text1 = Text(master, width=80, height=8)
text1.insert(INSERT,"%s%s%s%s%s%s%s"%("Biomass formed per substrate consumed Ysx = ",u"\u03BC","/rs =",u"\u0394","x/",u"\u0394","s , where rs is substrate rate\n"))
text.tag_configure("subscript", offset=-4)
text1.insert(INSERT,"Product formed per substrate consumed Ysp = r","","p","subscript","/rs =")
text1.insert(INSERT,"%s%s%s%s"%(u"\u0394","p/",u"\u0394","s, where rp is product rate\n"))
text1.insert(INSERT,"%s%s%s"%("YO2x = X/(OUR/",u"\u03BC",")\n"))
text1.insert(INSERT,"where OUR is specific oxygen uptake rate\n")
text1.insert(INSERT,"%s%s%s"%("YCO2x = X/(CUR/",u"\u03BC",")\n"))
text1.insert(INSERT,"where CUR is specific carbon uptake rate\n")
text1.pack()
Label(text="Respiratory Quotient").pack()
text2 = Text(master, width=80, height=8)
text2.insert(INSERT, "Respiratory coefficient RQ=CTR/OTR\n")
text2.insert(INSERT, " where OTR and CTR stand for oxygen and carbon dioxide transfer rate\n")
text2.insert(INSERT, "CTR = P/RT(Fgas,out*yco2,out/Vw)\n")
text2.insert(INSERT, "OTR = P/RT(Fgas,in*yo2,in-Fgas,out*yo2,out/Vw)\n")
text2.insert(INSERT, "Where P is pressure, T is Temperature\n")
text2.pack()
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)


mainloop()