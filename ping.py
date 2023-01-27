import os
from tkinter import *
window = Tk()
hostname = "www.google.com" #example
response = os.system("ping " + hostname)

#and then check the response...
if response != "Request timed out.":
  b1=Button(window, text="?")
  b1.grid(row=0, column=0)
  window.mainloop()
  #print((hostname)+ " is up!")
else:
  print((hostname)+ " is down!")