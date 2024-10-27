import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
import pygame
from pydub import AudioSegment
from pydub.playback import play
import threading

class AlarmClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Alarm Clock")
        self.master.geometry("400x300")

        # Initialize pygame for playing sound
        pygame.mixer.init()

        # Current time label
        self.label_time = tk.Label(master, font=("Arial", 30), fg="blue")
        self.label_time.pack(pady=20)

        # Alarm time entry
        self.label_alarm_time = tk.Label(master, text="Set Alarm Time (HH:MM:SS)")
        self.label_alarm_time.pack()

        self.entry_alarm_time = tk.Entry(master)
        self.entry_alarm_time.pack(pady=5)

        # Sound selection
        self.label_sound = tk.Label(master, text="Choose Alarm Sound")
        self.label_sound.pack(pady=5)

        self.selected_sound = tk.StringVar()
        self.sound_button = tk.Button(master, text="Select Sound", command=self.choose_sound)
        self.sound_button.pack(pady=5)

        # Set Alarm button
        self.btn_set_alarm = tk.Button(master, text="Set Alarm", command=self.set_alarm)
        self.btn_set_alarm.pack(pady=10)

        # Alarm list
        self.alarm_times = []

        # Start the time update loop
        self.update_time()

    def update_time(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.label_time.config(text=now)

        # Check for alarms
        self.check_alarms(now)

        self.master.after(1000, self.update_time)

    def check_alarms(self, current_time):
        for alarm_time in self.alarm_times.copy():
            if alarm_time['time'] == current_time:
                self.trigger_alarm(alarm_time['sound'])
                self.alarm_times.remove(alarm_time)

    def set_alarm(self):
        alarm_time_str = self.entry_alarm_time.get()
        try:
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M:%S").strftime("%H:%M:%S")
            if not self.selected_sound.get():
                messagebox.showerror("No Sound Selected", "Please select an alarm sound.")
                return

            self.alarm_times.append({
                'time': alarm_time,
                'sound': self.selected_sound.get()
            })
            messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
        except ValueError:
            messagebox.showerror("Invalid Time Format", "Please enter time in HH:MM:SS format")

    def choose_sound(self):
        sound_file = filedialog.askopenfilename(title="Select Alarm Sound", filetypes=(("MP3 files", "*.mp3"), ("WAV files", "*.wav")))
        if sound_file:
            self.selected_sound.set(sound_file)
            messagebox.showinfo("Sound Selected", f"Selected sound: {sound_file}")

    def trigger_alarm(self, sound):
        # Play the alarm sound in a separate thread
        threading.Thread(target=self.play_sound, args=(sound,)).start()

    def play_sound(self, sound):
        if sound.endswith('.mp3'):
            audio = AudioSegment.from_mp3(sound)
            play(audio)
        else:
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play(-1)  # Loop the sound until stopped

if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()
