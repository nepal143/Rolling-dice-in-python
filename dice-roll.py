import tkinter
import random
from PIL import Image, ImageTk

#Step 2
root = tkinter.Tk() 
root.geometry('400x400')
root.title('Ludo')
root.configure(bg= '#B9C6C9')


#Step 3
#Adding lable into the frame

#adding lable with different font and formatting 
l1 = tkinter.Label(root, text= "Hello world  ",
                    fg ="black" , bg = "#B9C6C9",
                    font = "Helvetica 16  italic")
l1.pack()

#step 4
#images 
dice = ['1.png' , '2.png' , '3.png' , '4.png' , '5.png' , '6.png']
# simulating the die with random number between 0 to 6 and generating images
# image2 = ImageTk.PhotoImage(file='6.png')
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice))) 
lable1 = tkinter.Label(root,image= image2)
lable1.image = image2
lable1.pack(expand = True)
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    #upldate image
    lable1.configure(image = image1, bg = '#B9C6C9')
    #keep a reference 
    lable1.image = image1
button  = tkinter.Button(root,text = "ROLL THE 🎲", font=('Arial,12,bold'),width=20 , height = 2 , bg = '#FE3939',fg='white' , command = rolling_dice)
button.pack(expand = True)


root.mainloop()
