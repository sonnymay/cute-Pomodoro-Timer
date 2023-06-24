import tkinter as tk
from tkinter import messagebox
import time

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Cute Pomodoro Timer")
        self.master.geometry("300x200")
        
        # Customize the look of the window
        self.master.config(bg="pink")
        
        # Label
        self.label = tk.Label(self.master, text="Let's be productive!", font=('Helvetica', 15), bg="pink")
        self.label.pack()
        
        # Start button
        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer, bg="light green")
        self.start_button.pack()
        
        # Countdown Label
        self.time_left = tk.StringVar()
        self.countdown_label = tk.Label(self.master, textvariable=self.time_left, font=('Helvetica', 20), bg="pink")
        self.countdown_label.pack()

    def start_timer(self):
        # Pomodoro time is typically 25 minutes
        self.remaining_time = 25 * 60
        self.update_timer()
    
    def update_timer(self):
        # Calculate minutes and seconds
        minutes, seconds = divmod(self.remaining_time, 60)
        # Update the label
        self.time_left.set(f"{minutes:02}:{seconds:02}")
        
        # When time is up, show a pop-up message
        if self.remaining_time <= 0:
            messagebox.showinfo("Time's up!", "Take a short break!")
            return
        
        # Decrement the remaining time and update the label after 1 second
        self.remaining_time -= 1
        self.master.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    pomodoro_timer = PomodoroTimer(root)
    root.mainloop()
