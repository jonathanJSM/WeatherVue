# main.py
import tkinter as tk
import gui

def main():
    app = tk.Tk()
    app.title("Weather Dashboard")

    # Set background image
    background_image = tk.PhotoImage(file="ezgif.com-gif-maker.gif")  # Provide the path to your background image
    background_label = tk.Label(app, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = background_image

    gui.setup_ui(app)
    
    app.mainloop()

if __name__ == "__main__":
    main()
