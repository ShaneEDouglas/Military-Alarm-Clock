from tkinter import *
import tkinter as tk
from pysound import *
import datetime as dt
import time
from threading import *
 
# Create Object
root = Tk()
 
# Set geometry
root.geometry("400x200")
 
# Use Threading
def Threading():
    t1=Thread(target=alarm)
    t1.start()
 
def alarm():
    # Infinite Loop
    while True:
        # Set Alarm
        setAlrm = f"{hour.get()}:{minute.get()}:{second.get()}"
 
        # Wait for one second delay
        time.sleep(1)
 
        # Get current time
        nowtime = datetime.datetime.now().strftime("%H:%M:%S")
        print(nowtime,setAlrm)
 
        # Check whether set alarm is equal to current time or not
        if setAlrm == nowtime:
            print("WAKE UP SOLDIER!!! TIME FOR PT!!!")
            # Playing sound (Reveille)
            winsound.PlaySound("",winsound.SND_ASYNC)
 
# Add Labels, Frame, Button, Optionmenus
Label(root,text="Military Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()
Background = PhotoImage(File = "FMJ.jpg") 
limg= Label(tk, i=bgimg)
limg.pack()
frame = Frame(root)
frame.pack()
 
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
 
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
 
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
 
second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
 
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)
 
Button(root,text="SET ALARM",font=("Helvetica 15"),command=Threading).pack(pady=20)
 
# Execute Tkinter
root.mainloop()

tk.mainloop()