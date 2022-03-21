#importing all of the processes
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

#Modify the do_command function:
#to use the new button as needed
def do_command(command):
        #Modify the do_command(command) function: 
    #to use the text box for input to the functions
    global command_textbox, url_entry

        #If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        #url_val = "127.0.0.1"
        url_val = "::1"
        
        #use url_val ping
    p = subprocess.Popen(command + ' ::1', stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    p = subprocess.Popen(command + ' ::1', stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)
#definition of root in the program (the base)
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="pink") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL: ", 
    compound="center",
    font=("Helvetica", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="circle",
    fg="light pink",
    bg="blue")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("times new roman", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="light pink") # change frame color
frame.pack()
# ping button
ping_btn = tk.Button(frame, text="ping", command=lambda:do_command("ping"))
ping_btn.pack()

#tracert button
tracert_btn = tk.Button(frame, text = "tracert", command=lambda:do_command("tracert"))
tracert_btn.pack()

#nslookup button
nslookup_btn = tk.Button(frame, text = "nslookup", command=lambda:do_command("nslookup"))
nslookup_btn.pack()

save_btn = tk.Button(frame, text = "save", command = lambda:mSave())
save_btn.pack()

#saving the function to a pre-existing or new file
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()

#a scrolled textbox in the gui program
command_textbox = tksc.ScrolledText(frame, height=10, width=50)
command_textbox.pack()

#end of the program
root.mainloop()