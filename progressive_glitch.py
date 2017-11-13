try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
    from tkFileDialog import askopenfilename, asksaveasfilename
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
    from tkinter.filedialog import askopenfilename, asksaveasfilename

from PIL import ImageTk, Image

from jpglitch import Jpeg

# TODO: If user opens new image after glitching it appends to window but old one is used again
#       So basically currently works with only one image at a time

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

        self.greet_button = Button(master, text="Save", command=self.save_image)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    # This function is called when the glitch button is pressed
    def glitch(self):

        # Read the slected image file
        with open(self.filename, "rb") as image:
            image_bytes = bytearray(image.read())

        # Initialize the Jpeg Class from jpglitch which scrambles the image
        # Use predefined values for glitch amount, start point and iterations
        self.jpeg = Jpeg(image_bytes, 99, 10, 10)
        print("\nScrambling your image")

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
        self.jpeg.save_image(self.filename)

        self.image_view()

        output = "\nSuccess!"
        print(output)

    def image_load(self):
        self.filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        print(self.filename)

        #Open and display Image in GUI window
        self.CharPhoto = ImageTk.PhotoImage(Image.open(self.filename))
        self.ChLabel = Label(self.master, image = self.CharPhoto)
        # Make an instance of the image or it greys out
        self.ChLabel.image = self.CharPhoto
        self.ChLabel.configure(image=self.CharPhoto)
        self.ChLabel.pack(side = "bottom", fill = "both", expand = "yes")

    # Option to save the image as a separate file
    def save_image(self):
        self.save_as_name = asksaveasfilename(   #this will make the file path a string
        defaultextension=".png",                 #so it's easier to check if it exists
        filetypes = (("JPEG Image", "*.jpg"),    #in the save function
                     ("PNG Image", "*.png")))    #Thank-You atlasologist (stackoverflow.com)
        self.jpeg.save_image(self.save_as_name)

    # Upgate the displayed image on every glitch
    def image_view(self):
        self.newImage = ImageTk.PhotoImage(Image.open(self.filename))
        self.ChLabel.image = self.newImage
        self.ChLabel.configure(image=self.newImage)

def main():
    root = Tk()
    my_gui = imageGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
