#Michael Zhang, Reece Mason and Owen Lehtovaara, and Jared Dobbyn
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox 

class CafFinance(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Dover Bay Cafeteria Finance Calculator")
    self.geometry("1000x768")
    self.configure(background="#44505A")
    self.separator = ttk.Separator(self, orient="horizontal").place(relx=0., rely=0.38, relwidth=1, relheight=0.003)
    self.register1 = tk.Label(self, text="Register A", bg="#44505A", fg='white', font='timesnewroman').place(relx=0,rely=0)
    self.register2 = tk.Label(self, text="Register B", bg="#44505A", fg="white", font="timesnewroman",).place(relx=0.34, rely=0)
    self.register3 = tk.Label(self, text="Register C", bg="#44505A", fg="white", font="timesnewroman").place(relx=0.67, rely=0)
    self.widgets()

  def delete(self):
    #register A 
    self.nickelEntry.delete(0, 'end')
    self.dimeEntry.delete(0, 'end')
    self.quarterEntry.delete(0, 'end')
    self.loonieEntry.delete(0, 'end')
    self.toonieEntry.delete(0, 'end')
    self.fiveEntry.delete(0, 'end')
    self.tenEntry.delete(0, 'end')
    self.twentyEntry.delete(0, 'end')
    self.fiftyEntry.delete(0, 'end')
    self.punchCardEntry.delete(0, 'end')
    #register B
    self.nickelBEntry.delete(0, 'end')
    self.dimeBEntry.delete(0, 'end')
    self.quarterBEntry.delete(0, 'end')
    self.loonieBEntry.delete(0, 'end')
    self.toonieBEntry.delete(0, 'end')
    self.fiveBEntry.delete(0, 'end')
    self.tenBEntry.delete(0, 'end')
    self.twentyBEntry.delete(0, 'end')
    self.fiftyBEntry.delete(0, 'end')
    self.punchCardBEntry.delete(0, 'end')
    #register C
    self.nickelCEntry.delete(0, 'end')
    self.dimeCEntry.delete(0, 'end')
    self.quarterCEntry.delete(0, 'end')
    self.loonieCEntry.delete(0, 'end')
    self.toonieCEntry.delete(0, 'end')
    self.fiveCEntry.delete(0, 'end')
    self.tenCEntry.delete(0, 'end')
    self.twentyCEntry.delete(0, 'end')
    self.fiftyCEntry.delete(0, 'end')
    self.punchCardCEntry.delete(0, 'end')
    
  def widgets(self): #interface
#register A
    #nickels-----------------------------
    self.nickels = tk.DoubleVar()
    self.nickels.trace_add("write", self.calculate)
    self.nickelEntry = tk.Entry(self, textvariable=self.nickels, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.nickelEntry.place(relx=0, rely=0.03)
    self.nickelLab = tk.Label(self, text="Nickels:", bg="#44505A", fg='white').place(relx=0.07, rely=0.03)
    self.nickelWorthLab = tk.Label(self, text=self.nickels.get())
    self.nickelWorthLab.place(relx=0.14, rely=0.03)
    #dimes----------------------------------
    self.dimes = tk.DoubleVar()
    self.dimes.trace_add("write", self.calculate)
    self.dimeEntry = tk.Entry(self, textvariable=self.dimes, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.dimeEntry.place(relx=0, rely=0.06)
    self.dimeLabel = tk.Label(self, text="Dimes:", bg="#44505A", fg='white').place(relx=0.07, rely=0.06)
    self.dimeWorthLab = tk.Label(self, text=self.dimes.get())
    self.dimeWorthLab.place(relx=0.14, rely=0.06)
    #quarter----------------------------------
    self.quarters = tk.DoubleVar()
    self.quarters.trace_add("write", self.calculate)
    self.quarterEntry = tk.Entry(self, textvariable=self.quarters, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.quarterEntry.place(relx=0, rely=0.09)
    self.quarterLabel = tk.Label(self, text="Quarters:", bg="#44505A", fg='white').place(relx=0.07, rely=0.09)
    self.quarterWorthLab = tk.Label(self, text=self.quarters.get())
    self.quarterWorthLab.place(relx=0.14, rely=0.09)
    #loonies----------------------------------
    self.loonies = tk.DoubleVar()
    self.loonies.trace_add("write", self.calculate)
    self.loonieEntry = tk.Entry(self, textvariable=self.loonies, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.loonieEntry.place(relx=0, rely=0.12)
    self.loonieLabel = tk.Label(self, text="Loonies:", bg="#44505A", fg='white').place(relx=0.07, rely=0.12)
    self.loonieWorthLab = tk.Label(self, text=self.loonies.get())
    self.loonieWorthLab.place(relx=0.14, rely=0.12)
    #toonies----------------------------------
    self.toonies = tk.DoubleVar()
    self.toonies.trace_add("write", self.calculate)
    self.toonieEntry = tk.Entry(self, textvariable=self.toonies, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.toonieEntry.place(relx=0, rely=0.15)
    self.toonieLabel = tk.Label(self, text="Toonies:", bg="#44505A", fg='white').place(relx=0.07, rely=0.15)
    self.toonieWorthLab = tk.Label(self, text=self.toonies.get())
    self.toonieWorthLab.place(relx=0.14, rely=0.15)
    #$5 bill----------------------------------
    self.five = tk.DoubleVar()
    self.five.trace_add("write", self.calculate)
    self.fiveEntry = tk.Entry(self, textvariable=self.five, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiveEntry.place(relx=0, rely=0.18)
    self.fiveLabel = tk.Label(self, text="$5 Bill:", bg="#44505A", fg='white').place(relx=0.07, rely=0.18)
    self.fiveWorthLab = tk.Label(self, text=self.five.get())
    self.fiveWorthLab.place(relx=0.14, rely=0.18)
    #$10 bill----------------------------------
    self.ten = tk.DoubleVar()
    self.ten.trace_add("write", self.calculate)
    self.tenEntry = tk.Entry(self, textvariable=self.ten, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.tenEntry.place(relx=0, rely=0.21)
    self.tenLabel = tk.Label(self, text="$10 Bill:", bg="#44505A", fg='white').place(relx=0.07, rely=0.21)
    self.tenWorthLab = tk.Label(self, text=self.ten.get())
    self.tenWorthLab.place(relx=0.14, rely=0.21)
    #$20 bill----------------------------------
    self.twenty = tk.DoubleVar()
    self.twenty.trace_add("write", self.calculate)
    self.twentyEntry = tk.Entry(self, textvariable=self.twenty, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.twentyEntry.place(relx=0, rely=0.24)
    self.twentyLabel = tk.Label(self, text="$20 Bill:", bg="#44505A", fg='white').place(relx=0.07, rely=0.24)
    self.twentyWorthLab = tk.Label(self, text=self.twenty.get())
    self.twentyWorthLab.place(relx=0.14, rely=0.24)
    #$50 bill----------------------------------
    self.fifty = tk.DoubleVar()
    self.fifty.trace_add("write", self.calculate)
    self.fiftyEntry = tk.Entry(self, textvariable=self.fifty, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiftyEntry.place(relx=0, rely=0.27)
    self.fiftyLabel = tk.Label(self, text="$50 Bill:", bg="#44505A", fg='white').place(relx=0.07, rely=0.27)
    self.fiftyWorthLab = tk.Label(self, text=self.fifty.get())
    self.fiftyWorthLab.place(relx=0.14, rely=0.27)
    #total-----------------------------------
    self.totalWord = tk.Label(self, text="     Total:", bg="#44505A", fg='white').place(relx=0.07, rely=0.30)
    self.totalA = self.nickels.get() + self.dimes.get() + self.quarters.get() + self.loonies.get() + self.toonies.get() + self.five.get()  + self.ten.get() + self.twenty.get()  + self.fifty.get() 
    self.totalLab = tk.Label(self.totalA)
    self.totalLab.place(relx=0.14, rely=0.30)
    #punchcard----------------------------------
    self.punchCard = tk.DoubleVar()
    self.punchCardEntry = tk.Entry(self, textvariable=self.punchCard, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.punchCardEntry.place(relx=0.11, rely=0.34)
    self.punchCardLab = tk.Label(self, text="Punch Cards: $", bg="#44505A", fg='white').place(relx=0, rely=0.34)
    
#Register B
    #nickels B-----------------------------
    self.nickelsB = tk.DoubleVar()
    self.nickelsB.trace_add("write", self.calculate)
    self.nickelBEntry = tk.Entry(self, textvariable=self.nickelsB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.nickelBEntry.place(relx=0.34, rely=0.03)
    self.nickelBLab = tk.Label(self, text="Nickels:", bg="#44505A", fg='white').place(relx=0.41, rely=0.03)
    self.nickelBWorthLab = tk.Label(self, text=self.nickelsB.get())
    self.nickelBWorthLab.place(relx=0.48, rely=0.03)
    #dimes B----------------------------------
    self.dimesB = tk.DoubleVar()
    self.dimesB.trace_add("write", self.calculate)
    self.dimeBEntry = tk.Entry(self, textvariable=self.dimesB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.dimeBEntry.place(relx=0.34, rely=0.06)
    self.dimeBLabel = tk.Label(self, text="Dimes:", bg="#44505A", fg='white').place(relx=0.41, rely=0.06)
    self.dimeBWorthLab = tk.Label(self, text=self.dimesB.get())
    self.dimeBWorthLab.place(relx=0.48, rely=0.06)
    #quarter----------------------------------
    self.quartersB = tk.DoubleVar()
    self.quartersB.trace_add("write", self.calculate)
    self.quarterBEntry = tk.Entry(self, textvariable=self.quartersB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.quarterBEntry.place(relx=0.34, rely=0.09)
    self.quarterBLabel = tk.Label(self, text="Quarters:", bg="#44505A", fg='white').place(relx=0.41, rely=0.09)
    self.quarterBWorthLab = tk.Label(self, text=self.quartersB.get())
    self.quarterBWorthLab.place(relx=0.48, rely=0.09)
    #loonies----------------------------------
    self.looniesB = tk.DoubleVar()
    self.looniesB.trace_add("write", self.calculate)
    self.loonieBEntry = tk.Entry(self, textvariable=self.looniesB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.loonieBEntry.place(relx=0.34, rely=0.12)
    self.loonieBLabel = tk.Label(self, text="Loonies:", bg="#44505A", fg='white').place(relx=0.41, rely=0.12)
    self.loonieBWorthLab = tk.Label(self, text=self.looniesB.get())
    self.loonieBWorthLab.place(relx=0.48, rely=0.12)
    #toonies----------------------------------
    self.tooniesB = tk.DoubleVar()
    self.tooniesB.trace_add("write", self.calculate)
    self.toonieBEntry = tk.Entry(self, textvariable=self.tooniesB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.toonieBEntry.place(relx=0.34, rely=0.15)
    self.toonieBLabel = tk.Label(self, text="Toonies:", bg="#44505A", fg='white').place(relx=0.41, rely=0.15)
    self.toonieBWorthLab = tk.Label(self, text=self.tooniesB.get())
    self.toonieBWorthLab.place(relx=0.48, rely=0.15)
    #$5 bill----------------------------------
    self.fiveB = tk.DoubleVar()
    self.fiveB.trace_add("write", self.calculate)
    self.fiveBEntry = tk.Entry(self, textvariable=self.fiveB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiveBEntry.place(relx=0.34, rely=0.18)
    self.fiveBLabel = tk.Label(self, text="$5 Bill:", bg="#44505A", fg='white').place(relx=0.41, rely=0.18)
    self.fiveBWorthLab = tk.Label(self, text=self.fiveB.get())
    self.fiveBWorthLab.place(relx=0.48, rely=0.18)
    #$10 bill----------------------------------
    self.tenB = tk.DoubleVar()
    self.tenB.trace_add("write", self.calculate)
    self.tenBEntry = tk.Entry(self, textvariable=self.tenB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.tenBEntry.place(relx=0.34, rely=0.21)
    self.tenBLabel = tk.Label(self, text="$10 Bill:", bg="#44505A", fg='white').place(relx=0.41, rely=0.21)
    self.tenBWorthLab = tk.Label(self, text=self.tenB.get())
    self.tenBWorthLab.place(relx=0.48, rely=0.21)
    #$20 bill----------------------------------
    self.twentyB = tk.DoubleVar()
    self.twentyB.trace_add("write", self.calculate)
    self.twentyBEntry = tk.Entry(self, textvariable=self.twentyB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.twentyBEntry.place(relx=0.34, rely=0.24)
    self.twentyBLabel = tk.Label(self, text="$20 Bill:", bg="#44505A", fg='white').place(relx=0.41, rely=0.24)
    self.twentyBWorthLab = tk.Label(self, text=self.twentyB.get())
    self.twentyBWorthLab.place(relx=0.48, rely=0.24)
    #$50 bill----------------------------------
    self.fiftyB = tk.DoubleVar()
    self.fiftyB.trace_add("write", self.calculate)
    self.fiftyBEntry = tk.Entry(self, textvariable=self.fiftyB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiftyBEntry.place(relx=0.34, rely=0.27)
    self.fiftyBLabel = tk.Label(self, text="$50 Bill:", bg="#44505A", fg='white').place(relx=0.41, rely=0.27)
    self.fiftyBWorthLab = tk.Label(self, text=self.fiftyB.get())
    self.fiftyBWorthLab.place(relx=0.48, rely=0.27)
    #total-----------------------------------
    self.totalBWord = tk.Label(self, text="     Total:", bg="#44505A", fg='white').place(relx=0.41, rely=0.30)
    self.totalB = self.nickelsB.get() + self.dimesB.get() + self.quartersB.get() + self.looniesB.get() + self.tooniesB.get() + self.fiveB.get()  + self.tenB.get() + self.twentyB.get()  + self.fiftyB.get()
    self.totalBLab = tk.Label(self.totalB)
    self.totalBLab.place(relx=0.48, rely=0.30)
    #punchcard----------------------------------
    self.punchCardB = tk.DoubleVar()
    self.punchCardBEntry = tk.Entry(self, textvariable=self.punchCardB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.punchCardBEntry.place(relx=0.41, rely=0.34)
    self.punchCardBLab = tk.Label(self, text="Punch Cards: $", bg="#44505A", fg='white').place(relx=0.30, rely=0.34)
    
#Register C
    #nickels-----------------------------
    self.nickelsC = tk.DoubleVar()
    self.nickelsC.trace_add("write", self.calculate)
    self.nickelCEntry = tk.Entry(self, textvariable=self.nickelsC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.nickelCEntry.place(relx=0.67, rely=0.03)
    self.nickelCLab = tk.Label(self, text="Nickels:", bg="#44505A", fg='white').place(relx=0.74, rely=0.03)
    self.nickelCWorthLab = tk.Label(self, text=self.nickelsC.get())
    self.nickelCWorthLab.place(relx=0.81, rely=0.03)
    #dimes----------------------------------
    self.dimesC = tk.DoubleVar()
    self.dimesC.trace_add("write", self.calculate)
    self.dimeCEntry = tk.Entry(self, textvariable=self.dimesC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.dimeCEntry.place(relx=0.67, rely=0.06)
    self.dimeCLabel = tk.Label(self, text="Dimes:", bg="#44505A", fg='white').place(relx=0.74, rely=0.06)
    self.dimeCWorthLab = tk.Label(self, text=self.dimesC.get())
    self.dimeCWorthLab.place(relx=0.81, rely=0.06)
    #quarter----------------------------------
    self.quartersC = tk.DoubleVar()
    self.quartersC.trace_add("write", self.calculate)
    self.quarterCEntry = tk.Entry(self, textvariable=self.quartersC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.quarterCEntry.place(relx=0.67, rely=0.09)
    self.quarterCLabel = tk.Label(self, text="Quarters:", bg="#44505A", fg='white').place(relx=0.74, rely=0.09)
    self.quarterCWorthLab = tk.Label(self, text=self.quartersC.get())
    self.quarterCWorthLab.place(relx=0.81, rely=0.09)
    #loonies----------------------------------
    self.looniesC = tk.DoubleVar()
    self.looniesC.trace_add("write", self.calculate)
    self.loonieCEntry = tk.Entry(self, textvariable=self.looniesC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.loonieCEntry.place(relx=0.67, rely=0.12)
    self.loonieCLabel = tk.Label(self, text="Loonies:", bg="#44505A", fg='white').place(relx=0.74, rely=0.12)
    self.loonieCWorthLab = tk.Label(self, text=self.looniesC.get())
    self.loonieCWorthLab.place(relx=0.81, rely=0.12)
    #toonies----------------------------------
    self.tooniesC = tk.DoubleVar()
    self.tooniesC.trace_add("write", self.calculate)
    self.toonieCEntry = tk.Entry(self, textvariable=self.tooniesC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.toonieCEntry.place(relx=0.67, rely=0.15)
    self.toonieCLabel = tk.Label(self, text="Toonies:", bg="#44505A", fg='white').place(relx=0.74, rely=0.15)
    self.toonieCWorthLab = tk.Label(self, text=self.tooniesC.get())
    self.toonieCWorthLab.place(relx=0.81, rely=0.15)
    #$5 bill----------------------------------
    self.fiveC = tk.DoubleVar()
    self.fiveC.trace_add("write", self.calculate)
    self.fiveCEntry = tk.Entry(self, textvariable=self.fiveC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiveCEntry.place(relx=0.67, rely=0.18)
    self.fiveCLabel = tk.Label(self, text="$5 Bill:", bg="#44505A", fg='white').place(relx=0.74, rely=0.18)
    self.fiveCWorthLab = tk.Label(self, text=self.fiveC.get())
    self.fiveCWorthLab.place(relx=0.81, rely=0.18)
    #$10 bill----------------------------------
    self.tenC = tk.DoubleVar()
    self.tenC.trace_add("write", self.calculate)
    self.tenCEntry = tk.Entry(self, textvariable=self.tenC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.tenCEntry.place(relx=0.67, rely=0.21)
    self.tenCLabel = tk.Label(self, text="$10 Bill:", bg="#44505A", fg='white').place(relx=0.74, rely=0.21)
    self.tenCWorthLab = tk.Label(self, text=self.tenC.get())
    self.tenCWorthLab.place(relx=0.81, rely=0.21)
    #$20 bill----------------------------------
    self.twentyC = tk.DoubleVar()
    self.twentyC.trace_add("write", self.calculate)
    self.twentyCEntry = tk.Entry(self, textvariable=self.twentyC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.twentyCEntry.place(relx=0.67, rely=0.24)
    self.twentyCLabel = tk.Label(self, text="$20 Bill:", bg="#44505A", fg='white').place(relx=0.74, rely=0.24)
    self.twentyCWorthLab = tk.Label(self, text=self.twentyC.get())
    self.twentyCWorthLab.place(relx=0.81, rely=0.24)
    #$50 bill----------------------------------
    self.fiftyC = tk.DoubleVar()
    self.fiftyC.trace_add("write", self.calculate)
    self.fiftyCEntry = tk.Entry(self, textvariable=self.fiftyC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiftyCEntry.place(relx=0.67, rely=0.27)
    self.fiftyCLabel = tk.Label(self, text="$50 Bill:", bg="#44505A", fg='white').place(relx=0.74, rely=0.27)
    self.fiftyCWorthLab = tk.Label(self, text=self.fiftyC.get())
    self.fiftyCWorthLab.place(relx=0.81, rely=0.27)
    #total-----------------------------------
    self.totalCWord = tk.Label(self, text="     Total:", bg="#44505A", fg='white').place(relx=0.74, rely=0.30)
    self.totalC = self.nickelsC.get() + self.dimesC.get() + self.quartersC.get() + self.looniesC.get() + self.tooniesC.get() + self.fiveC.get()  + self.tenC.get() + self.twentyC.get()  + self.fiftyC.get()
    self.totalCLab = tk.Label(self.totalC)
    self.totalCLab.place(relx=0.81, rely=0.30)
    #punchcard----------------------------------
    self.punchCardC = tk.DoubleVar()
    self.punchCardCEntry = tk.Entry(self, textvariable=self.punchCardC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.punchCardCEntry.place(relx=0.74, rely=0.34)
    self.punchCardCLab = tk.Label(self, text="Punch Cards: $", bg="#44505A", fg='white').place(relx=0.63, rely=0.34)
    #grand total------------------------------
    self.registerTotal = tk.Label(self, text="Total of all registers:", bg="#44505A", fg='white').place(relx=0, rely=0.39)
    self.grandTotal = self.totalA + self.totalB + self.totalC
    self.registerTotalLab = tk.Label(self, text = self.grandTotal)
    self.registerTotalLab.place(relx=0.15, rely=0.39)
    #float-------------------------------------
    self.floatAndNet = tk.DoubleVar()
    self.floatAndNet.trace_add("write", self.calculate)
    self.NetProfitText = tk.Label(self, text = "Net Profit (-$489 float): ", bg="#44505A", fg='white').place(relx=0, rely=0.45)
    self.NetProfitLab = tk.Label(self, text=(self.floatAndNet.get()))
    self.NetProfitLab.place(relx=0.17, rely=0.45)
    self.delete()
    #punch card total-----------------------------
    self.punchCardTotal = tk.Label(self, text="Punch Cards Total:", bg="#44505A", fg='white').place(relx=0, rely=0.5)
    self.punchCardsABC = self.punchCard + self.punchCardB + self.punchCardC
    self.punchCardTotalLab = tk.Label(self, text=self.punchCardsABC, bg="#44505A", fg='white').place(relx=0, rely=0.5)

    #self.clearButton = tk.Button(self, text="Clear All", command=(self.delete()))
    #self.clearButton.place(relx=0.042, rely=0.47)


  def calculate(self, *args): #calculations  
  #Register A
    #nickels
    try: nickelAmount = self.nickels.get()
    except: nickelAmount = 0
    self.nickelWorthLab['text'] = round((nickelAmount * 0.05), 2)
    #dimes
    try: dimeAmount = self.dimes.get()
    except: dimeAmount = 0
    self.dimeWorthLab['text'] = round((dimeAmount * 0.10), 2)
    #quarters
    try: quarterAmount = self.quarters.get()
    except: quarterAmount = 0
    self.quarterWorthLab['text'] = round((quarterAmount * 0.25), 2)
    #loonies
    try: loonieAmount = self.loonies.get()
    except: loonieAmount = 0
    self.loonieWorthLab['text'] = round((loonieAmount * 1.0), 2)
    #toonies
    try: toonieAmount = self.toonies.get()
    except: toonieAmount = 0
    self.toonieWorthLab['text'] = round((toonieAmount * 2.0), 2)
    #5 dollar bill
    try: fiveAmount = self.five.get()
    except: fiveAmount = 0
    self.fiveWorthLab['text'] = round((fiveAmount * 5.0), 2)
    #10 dollar bill
    try: tenAmount = self.ten.get()
    except: tenAmount = 0
    self.tenWorthLab['text'] = round((tenAmount * 10.0), 2)
    #20 dollar bill
    try: twentyAmount = self.twenty.get()
    except: twentyAmount = 0
    self.twentyWorthLab['text'] = round((twentyAmount * 20.0), 2)
    #50 dollar bill
    try: fiftyAmount = self.fifty.get()
    except: fiftyAmount = 0
    self.fiftyWorthLab['text'] = round((fiftyAmount * 50.0), 2)
    #total

    self.CalculateTotalA = self.nickelWorthLab['text'] + self.dimeWorthLab['text'] + self.quarterWorthLab['text'] + self.loonieWorthLab['text'] + self.toonieWorthLab['text'] + self.fiveWorthLab['text'] + self.tenWorthLab['text'] + self.twentyWorthLab['text'] + self.fiftyWorthLab['text']

    self.totalLab['text'] = round((self.CalculateTotalA), 2)
#Register B
    #nickels
    try: nickelBAmount = self.nickelsB.get()
    except: nickelBAmount = 0
    self.nickelBWorthLab['text'] = round((nickelBAmount * 0.05), 2)
    #dimes
    try: dimeBAmount = self.dimesB.get() 
    except: dimeBAmount = 0
    self.dimeBWorthLab['text'] = round((dimeBAmount * 0.10), 2)
    #quarters
    try: quarterBAmount = self.quartersB.get()
    except: quarterBAmount = 0
    self.quarterBWorthLab['text'] = round((quarterBAmount * 0.25), 2)
    #loonies
    try: loonieBAmount = self.looniesB.get()
    except: loonieBAmount = 0
    self.loonieBWorthLab['text'] = round((loonieBAmount * 1.0), 2)
    #toonies
    try: toonieBAmount = self.tooniesB.get()
    except: toonieBAmount = 0
    self.toonieBWorthLab['text'] = round((toonieBAmount * 2.0), 2)
    #5 dollar bill
    try: fiveBAmount = self.fiveB.get()
    except: fiveBAmount = 0
    self.fiveBWorthLab['text'] = round((fiveBAmount * 5.0), 2)
    #10 dollar bill
    try: tenBAmount = self.tenB.get()
    except: tenBAmount = 0
    self.tenBWorthLab['text'] = round((tenBAmount * 10.0), 2)
    #20 dollar bill
    try: twentyBAmount = self.twentyB.get()
    except: twentyBAmount = 0
    self.twentyBWorthLab['text'] = round((twentyBAmount * 20.0), 2)
    #50 dollar bill
    try: fiftyBAmount = self.fiftyB.get()
    except: fiftyBAmount = 0
    self.fiftyBWorthLab['text'] = round((fiftyBAmount * 50.0), 2)
    #total
    self.CalculateTotalB = self.nickelBWorthLab['text'] + self.dimeBWorthLab['text'] + self.quarterBWorthLab['text'] + self.loonieBWorthLab['text'] + self.toonieBWorthLab['text'] + self.fiveBWorthLab['text'] + self.tenBWorthLab['text'] + self.twentyBWorthLab['text'] + self.fiftyBWorthLab['text'] 

    self.totalBLab['text'] = round((self.CalculateTotalB), 2)
#Register C
    #nickels
    try: nickelCAmount = self.nickelsC.get()
    except: nickelCAmount = 0
    self.nickelCWorthLab['text'] = round((nickelCAmount * 0.05), 2)
    #dimes
    try: dimeCAmount = self.dimesC.get() 
    except: dimeCAmount = 0
    self.dimeCWorthLab['text'] = round((dimeCAmount * 0.10), 2)
    #quarters
    try: quarterCAmount = self.quartersC.get()
    except: quarterCAmount = 0
    self.quarterCWorthLab['text'] = round((quarterCAmount * 0.25), 2)
    #loonies
    try: loonieCAmount = self.looniesC.get()
    except: loonieCAmount = 0
    self.loonieCWorthLab['text'] = round((loonieCAmount * 1.0), 2)
    #toonies
    try: toonieCAmount = self.tooniesC.get()
    except: toonieCAmount = 0
    self.toonieCWorthLab['text'] = round((toonieCAmount * 2.0), 2)
    #5 dollar bill
    try: fiveCAmount = self.fiveC.get()
    except: fiveCAmount = 0
    self.fiveCWorthLab['text'] = round((fiveCAmount * 5.0), 2)
    #10 dollar bill
    try: tenCAmount = self.tenC.get()
    except: tenCAmount = 0
    self.tenCWorthLab['text'] = round((tenCAmount * 10.0), 2)
    #20 dollar bill
    try: twentyCAmount = self.twentyC.get()
    except: twentyCAmount = 0
    self.twentyCWorthLab['text'] = round((twentyCAmount * 20.0), 2)
    #50 dollar bill
    try: fiftyCAmount = self.fiftyC.get()
    except: fiftyCAmount = 0
    self.fiftyCWorthLab['text'] = round((fiftyCAmount * 50.0), 2)
    #total
    self.CalculateTotalC = self.nickelCWorthLab['text'] + self.dimeCWorthLab['text'] + self.quarterCWorthLab['text'] + self.loonieCWorthLab['text'] + self.toonieCWorthLab['text'] + self.fiveCWorthLab['text'] + self.tenCWorthLab['text'] + self.twentyCWorthLab['text'] + self.fiftyCWorthLab['text']
    self.totalCLab['text'] = round((self.CalculateTotalC), 2)
    #grand total
    self.registerTotalLab['text'] = round((self.CalculateTotalA + self.CalculateTotalB + self.CalculateTotalC), 2)
    #float/net profit
    self.NetProfitLab['text'] = round((self.registerTotalLab['text'] - 489), 2)
    #punchcards
    self.CalculatePunchCards = self.punchCardEntry['text'] + self.punchCardBEntry['text'] + self.punchCardCEntry['text'] 
  
if __name__ == "__main__":
  app = CafFinance()
  app.mainloop()
  
#Hit Us Up @veryepicprogrammers@gmail.com
#VEP inc since 2021
