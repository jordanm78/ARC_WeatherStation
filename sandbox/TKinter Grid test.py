from tkinter import *
from tkinter import ttk

master = Tk()
backgroundColor = "white"
normalFont = "Helvetica"
normalFontSize = 18

master.configure(background = backgroundColor)


myNumber = 3.1
myString1 = "%6.2f" % myNumber  #The .2 means that my string includes two decimal digits.
                                #If my number has fewer than two decimal digits, my string will be padded with trailing zeros.
                                #The 6 means that my string is six characters wide, including the decimal point.
                                #This leaves three places to the left of the decimal.
                                #If there are fewer than three characters to the left of the decimal, the extra places will be filled by spaces.
                                
                                
myNumber = 653.88
myString2 = "%.2f" % myNumber

currentRow = 0

#Create the title for the window
title = Label(master, text="ARC Weather Station",
              font = (normalFont, 36),
              background = backgroundColor)

#Place the title in the window
title.grid(columnspan = 4,
           padx = 10,
           pady = 10)

currentRow+=1

#Create the wind speed label
windSpeedLabel = Label(master, text="WindSpeed (MPH):",
                       font = (normalFont, normalFontSize),
                       background = backgroundColor)

#Place the wind speed label in the window
windSpeedLabel.grid(row = currentRow,
                    sticky=E)



#Create the wind speed indicator
windSpeedIndicator = Label(master, text=myString1,
                       font = (normalFont, normalFontSize),
                       background = backgroundColor)

#Place the wind speed indicator in the window
windSpeedIndicator.grid(row = currentRow,
                        column = 1,
                        sticky=W)


currentRow+=1


#Create the temperature label
temperatureLabel = Label(master, text="Temperature (Deg. F):",
                       font = (normalFont, normalFontSize),
                       background = backgroundColor)

#Place the temperature label in the window
temperatureLabel.grid(row = currentRow,
                      sticky=E)



#Create the temperature indicator
temperatureIndicator = Label(master, text=myString2,
                       font = (normalFont, normalFontSize),
                       background = backgroundColor)

#Place the temperature indicator in the window
temperatureIndicator.grid(row = currentRow,
                        column = 1,
                        sticky=W)

currentRow+=1

#Create the quit button
quitButton = Button(master, text = "Quit",
                       font = (normalFont, normalFontSize))

#Place the quit button in the window
quitButton.grid(row=currentRow, column=3, padx = 5, pady = 5)


master.mainloop()
