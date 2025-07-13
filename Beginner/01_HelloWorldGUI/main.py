import tkinter as tk

#🐥 STEP 2: Create the Main Window
# Think of this as creating an empty canvas where we can draw:
root = tk.Tk()#it creates a window
root.title("Hello World GUI")  # Set the title of the window

#Step 3: Add a label
label = tk.Label(root, text="Hello, World!", font=("Helvetica",16))
label.pack(pady=20)
# .pack() tells Tkinter to actually place it in the window.
#  pady adds padding so it doesn’t stick to the edges.

# STEP 4: Start the Event Loop
root.mainloop()
#  This line makes your program “live” and interactive.

