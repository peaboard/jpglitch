try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
    from tkFileDialog import askopenfilename
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
    from tkinter.filedialog import askopenfilename

from jpglitch import Jpeg

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.image_button = Button(master, text="Image", command=self.image_load)
        self.image_button.pack()

        self.greet_button = Button(master, text="Glitch", command=self.glitch)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def glitch(self):
        print("Greetings!")

        with open(self.filename, "rb") as image:
            image_bytes = bytearray(image.read())

        jpeg = Jpeg(image_bytes, 99, 10, 10)
        print("\nScrambling your image with the following parameters:")
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

        jpeg.save_image(self.filename)

        output = "\nSucces! Checkout %s." % name
        print(output)

    def image_load(self):
        self.filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        print(self.filename)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
