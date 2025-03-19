""" Chapter 9 example (Page 228)
Program: labeldemo.py
3/10/25 
**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run properly  

Template code for any GUI based application in chapter 9.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports can go here

# Class Header (class name will change from project to project)
class Salarycalc(EasyFrame):
  # Definition of the classes' constructor method
  def __init__(self): #self is distinct that it is unique 
    
    # Call to the EasyFrame class consturctor
    EasyFrame.__init__(self, title = "Salary Demo", width = 280, height = 240, resizable = False, background = "DodgerBlue2")
    # Other components are added here
    self.addLabel(text = "Hourly Wage:", row= 0, column = 0, background = "dodgerblue2")
    self.addLabel(text = "Hours Worked:", row = 1, column = 0, background = "dodgerblue2")
    self.addLabel(text = "Weekly Salary:", row= 3, column = 0, background = "dodgerblue2")


    # Adding the panel for user input
    self.Wage = self.addFloatField(value = 0.0, row = 0, column = 1, precision = 2)
    self.Hours = self.addFloatField(value = 0.0, row = 1, column = 1, precision = 2)
    self.result = self.addFloatField(value = 0.0, row = 3, column = 1, precision = 2, state="readonly")
    # Using the bind function to bind the enter key to the button
    self.Hours.bind("<Return>", lambda event: self.totalWage())
    
    

    # Building the button
    self.button = self.addButton(text = "Calculate", row = 2, column = 0, columnspan = 2, command = self.totalWage)
    

    # Taking input and displaying total pay
  def totalWage(self):
    wage = self.Wage.getNumber()
    hours = self.Hours.getNumber()
    weeklySalary = wage * hours
    self.result.setNumber(weeklySalary)
      
      
      
      
  
      

      

    # End of class block
# Global definition of main function
def main():
  # Instantiate a object from the class into main loop
   Salarycalc().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
  main()
