import tkinter as tk
from PILLOW import ImageTK

# initiallize app
root = tk.Tk()
root.title("Recipe Picker")
root.eval("tk::PlaceWindow . center")

#x = int(root.winfo_screenwidth() // 2)
#y = int(root.winfo_screenheight() ** 0.1)
#root.geometry('500x600 +' + str(x) + '+' + str(y))

frame1 = tk.Frame(root, width=500, height=600, bg='#3d6466')
frame1.grid(row=0,column=0)

ImageTK.PhotoImage(file="assets/RRecipe_logo.png")
# run app 
root.mainloop()
