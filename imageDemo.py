"""
Program: gui_template.py
Chapter 8
1/19/2024

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

Example of a GUI-based application that displays both an image and a text label
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
# Other imports go here

# Class header (class name will change project to project)
class imageDemo(EasyFrame):

    # Definition of our classes' constructor method
    def __init__(self):
        # Call to the Easy Frame class constructor
        EasyFrame.__init__(self, title = "Image Demo")
        self.setResizable(False)
        imageLabel = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")
        textLabel = self.addLabel(text = "Smokey The Cat", row = 1, column = 0, sticky = "NSEW")

        # Load the image data and associate it with the image label
        self.image = PhotoImage(file = "smokey.gif")
        imageLabel["image"] = self.image

        # Create the font object and apply it to the text label
        myFont = Font(family = "Verdana", size = 20, slant = "italic")
        textLabel["font"] = myFont
        textLabel["foreground"] = "blue"

# Global definition of the main() method
def main():
    # Instantiate an object from the class into mainloop()
    imageDemo().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
    main()