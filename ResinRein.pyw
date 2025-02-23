import customtkinter as ctk
from datetime import datetime, timedelta
import time

# Function to calculate the time
def calculate_time():
    # Get the current and needed resin values from the inputs
    current_resin = int(entry_current_resin.get())
    needed_resin = int(entry_needed_resin.get())
    
    
    # resin_per_minute = 1
    
    # Calculate the difference in resin
    resin_needed = needed_resin - current_resin
    
    # Calculate time in minutes
    time_needed_minutes = resin_needed * 8  # 8 minutes per resin
    
    # Calculate the raw time to reach the needed resin
    # raw_time = str(timedelta(minutes=time_needed_minutes)) '''to display seconds too'''
    raw_time = str(timedelta(minutes=time_needed_minutes))[:5]
    
    # Calculate the local time at which resin will be full
    current_time = datetime.now()
    time_to_reach = current_time + timedelta(minutes=time_needed_minutes)
    local_time = time_to_reach.strftime('%H:%M')
    
    # Update the result labels using configure() instead of config()
    label_raw_time.configure(text=f"{raw_time}")
    label_local_time.configure(text=f"{local_time}")
    
# Function to add 20 to the needed resin
def add_resin():
    current_needed_resin = int(entry_needed_resin.get())
    new_needed_resin = current_needed_resin + 20
    entry_needed_resin.delete(0, ctk.END)
    entry_needed_resin.insert(0, str(new_needed_resin))
    calculate_time()  # Recalculate after the update

# Function to subtract 20 from the needed resin
def subtract_resin():
    current_needed_resin = int(entry_needed_resin.get())
    new_needed_resin = current_needed_resin - 20
    if new_needed_resin >= 0:  # Ensure it doesn't go below zero
        entry_needed_resin.delete(0, ctk.END)
        entry_needed_resin.insert(0, str(new_needed_resin))
        calculate_time()  # Recalculate after the update

# Create the main application window
root = ctk.CTk()

# Set the window size and title
root.geometry("300x350")
root.title("ResinRein")

# Add a label for "Current Resin"
label_current_resin = ctk.CTkLabel(root, text="CURRENT RESIN")
label_current_resin.pack(pady=1)

# Add an entry for the current resin value
entry_current_resin = ctk.CTkEntry(root, justify="center")
entry_current_resin.pack(pady=10)

# Add a label for "Needed Resin"
label_needed_resin = ctk.CTkLabel(root, text="NEEDED RESIN")
label_needed_resin.pack(pady=1)

# Add an entry for the needed resin value
entry_needed_resin = ctk.CTkEntry(root, width=60, justify="center")
entry_needed_resin.pack(pady=10)

# Add buttons to adjust the needed resin value
button_add_resin = ctk.CTkButton(root, text="+20", fg_color="darkred", hover_color="red", width=40, command=add_resin)
button_add_resin.pack(pady=5)
button_add_resin.place(x=185, y=118)


button_subtract_resin = ctk.CTkButton(root, text="-20", fg_color="darkred", hover_color="red", width=40, command=subtract_resin)
button_subtract_resin.pack(pady=5)
button_subtract_resin.place(x=75, y=118)


# Add a button to calculate the time
button_calculate = ctk.CTkButton(root, text=" ", fg_color="darkred", hover_color="red", command=calculate_time)
button_calculate.pack(pady=20)

# Label to display the raw time
label_raw_time = ctk.CTkLabel(root, font=("System", 30), text="00:00")
label_raw_time.pack(pady=5)

# Label to display the local time
label_local_time = ctk.CTkLabel(root, font=("System", 30), text="00:00")
label_local_time.pack(pady=5)

# Locking window size
root.resizable(False,False)

# Start the main event loop
root.mainloop()
