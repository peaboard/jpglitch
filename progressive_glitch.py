try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
    from tkFileDialog import askopenfilename
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
    from tkinter.filedialog import askopenfilename

from PIL import ImageTk, Image

from jpglitch import Jpeg

import webbrowser



# The GUI component of the program
class imageGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("A simple GUI")

        self.label = Label(master, text="Let's Glitch Images")
        self.label.pack()

        self.image_button = Button(master, text="Image", command=self.image_load)
        self.image_button.pack()

        self.greet_button = Button(master, text="Glitch", command=self.glitch)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        # self.newWindow = Toplevel(self.master)
        # self.app = imageViewer(self.newWindow)


    # This function is called when the glitch button is pressed
    def glitch(self):

        # Read the slected image file
        with open(self.filename, "rb") as image:
            image_bytes = bytearray(image.read())

        # Initialize the Jpeg Class from jpglitch which scrambles the image
        # Use predefined values for glitch amount, start point and iterations
        jpeg = Jpeg(image_bytes, 99, 10, 10)
        print("\nScrambling your image")
        # for key, value in jpeg.parameters.items():
        #     click.echo(message=key + ': ' + str(value))
        output = 0
        if output:
            # TODO
            # make the extension here count as guide for what to save the file as
            # for now just ignore it if it's given
            name = output.rsplit('.')[0]
        else:
            name = image.name.rsplit('.')[0] + "_glitched"

        name += '%s' % ('.jpg')

        # Overwrite the original file with the glitched image so that we can continue glitching
        jpeg.save_image(self.filename)

        #self.app.loadImage(self.filename)

        self.image_view()

        output = "\nSuccess!"
        print(output)


        #webbrowser.open(self.filename)

        #self.current_glitched_image.show()



    def image_load(self):
        self.filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        #self.current_glitched_image = Image.open(self.filename)
        #self.current_glitched_image.show()
        print(self.filename)

        self.CharPhoto = ImageTk.PhotoImage(Image.open(self.filename))
        self.ChLabel = Label(self.master, image = self.CharPhoto)
        self.ChLabel.image = self.CharPhoto
        self.ChLabel.configure(image=self.CharPhoto)
        self.ChLabel.pack(side = "bottom", fill = "both", expand = "yes")

    def image_view(self):
        self.newImage = ImageTk.PhotoImage(Image.open(self.filename))
        self.ChLabel.image = self.newImage
        self.ChLabel.configure(image=self.newImage)





# class imageViewer:
#
#     def __init__(self, master):
#         # Window for viewing image
#         self.master = master
#
#         self.master.title("Join")
#         self.master.geometry("300x300")
#         self.master.configure(background='grey')
#
#     def loadImage(self, filename):
#
#         print(filename)
#         img = ImageTk.PhotoImage(Image.open(filename))
#         self.panel = Label(self.master, image = img)
#         self.panel.pack(side = "bottom", fill = "both", expand = "yes")
#         print("Image Loaded")
#         self.master.configure(background='black')

def main():
    root = Tk()
    my_gui = imageGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
