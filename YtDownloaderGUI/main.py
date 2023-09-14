from pytube import YouTube
import customtkinter as ctk

ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry("500x400")
root.title("YtVideoDownloader")
root.grid_columnconfigure(0, weight=1)



# Create a label
label1 = ctk.CTkLabel(master=root, text="Enter the video URL",
                                font=("Arial", 20),
                                width=120,
                                height=25,
                                corner_radius=8)
label1.grid(row=1, column=0, padx=10, pady=20)

# Create an entry
entry = ctk.CTkEntry(master=root, 
                    width=1000, 
                    placeholder_text="Enter the video URL",
                    corner_radius=10)
entry.grid(row=2, column=0, padx=20, pady=1)

# Create a button
def button_callback():
    url = entry.get()
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension='mp4').first()
    try:
        if stream is not None:
            stream.download()
            label1.configure(text="Downloaded Successfully")
            button.destroy()
            entry.destroy()
    except Exception as e:
        print(e)
        label2 = ctk.CTkLabel(master=root, text="Error Occured")
        

button = ctk.CTkButton(root, 
                       text="Enter", 
                       fg_color="#4681f4",
                       command=button_callback,
                       width=100,
                       corner_radius=100,
                       hover_color = "purple"
                       )
button.grid(row=3, column=0, padx=20, pady=20)



root.mainloop()