import os
import shutil
import tkinter as tk
from tkinter import filedialog, Listbox, Scrollbar, messagebox
from moviepy.editor import VideoFileClip
import threading

class VideoGalleryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Gallery")
        self.root.geometry("800x600")

        # Set the directory for storing video files (change this to your desired path)
        self.external_video_directory = "C:/Videos"  # Specify your external folder here
        os.makedirs(self.external_video_directory, exist_ok=True)  # Create directory if it doesn't exist

        # Create a listbox to display video files
        self.video_listbox = Listbox(self.root, selectmode=tk.MULTIPLE)  # Allow multiple selection
        self.video_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.video_listbox.bind("<Double-Button-1>", self.play_selected_videos)  # Add double-click event to play videos

        # Add a scrollbar to the listbox
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.video_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.video_listbox.yview)

        # Create buttons for uploading, deleting, viewing, and playing files
        self.upload_button = tk.Button(self.root, text="Upload Files", command=self.upload_files)
        self.upload_button.pack(side=tk.TOP, fill=tk.X)

        self.delete_button = tk.Button(self.root, text="Delete File", command=self.delete_file)
        self.delete_button.pack(side=tk.TOP, fill=tk.X)

        self.view_button = tk.Button(self.root, text="View Files", command=self.view_files)
        self.view_button.pack(side=tk.TOP, fill=tk.X)

        self.play_button = tk.Button(self.root, text="Play Selected", command=self.play_selected_videos)
        self.play_button.pack(side=tk.TOP, fill=tk.X)

        # Variable to store currently playing clips
        self.playing_threads = []  # List to keep track of playing threads

        # Bind the closing event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def view_files(self):
        # Clear the listbox
        self.video_listbox.delete(0, tk.END)

        # List all video files in the external directory
        video_extensions = ('.mp4', '.avi', '.mov', '.mkv')
        for filename in os.listdir(self.external_video_directory):
            if filename.lower().endswith(video_extensions):
                self.video_listbox.insert(tk.END, filename)

    def upload_files(self):
        # Prompt user to select multiple video files to upload
        video_files = filedialog.askopenfilenames(title="Select Video Files",
                                                  filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")])
        for video_file in video_files:
            if video_file:
                # Construct the destination file path
                destination = os.path.join(self.external_video_directory, os.path.basename(video_file))
                
                try:
                    shutil.copy2(video_file, destination)  # Copies the file instead of moving it
                    self.video_listbox.insert(tk.END, os.path.basename(destination))  # Update the listbox
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to upload file: {e}")
        
        if video_files:
            messagebox.showinfo("Success", "Files uploaded successfully.")

    def delete_file(self):
        try:
            selected_index = self.video_listbox.curselection()[0]  # Get the selected item index
            selected_video = self.video_listbox.get(selected_index)
            full_path = os.path.join(self.external_video_directory, selected_video)

            # Confirm deletion
            if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{selected_video}'?"):
                os.remove(full_path)  # Remove the file
                self.video_listbox.delete(selected_index)  # Remove from the listbox
                messagebox.showinfo("Success", "File deleted successfully.")

        except IndexError:
            messagebox.showwarning("Warning", "Please select a file to delete.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete file: {e}")

    def play_selected_videos(self, event=None):
        try:
            selected_indices = self.video_listbox.curselection()  # Get all selected items
            if not selected_indices:
                messagebox.showwarning("Warning", "Please select at least one video to play.")
                return

            for index in selected_indices:
                selected_video = self.video_listbox.get(index)
                full_path = os.path.join(self.external_video_directory, selected_video)
                # Start a new thread to play each selected video
                playing_thread = threading.Thread(target=self.play_video, args=(full_path,))
                playing_thread.start()
                self.playing_threads.append(playing_thread)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to play videos: {e}")

    def play_video(self, full_path):
        try:
            clip = VideoFileClip(full_path)
            clip.preview()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to play video: {e}")

    def on_closing(self):
        # Stop currently playing videos if any
        for thread in self.playing_threads:
            if thread.is_alive():
                thread.join()  # Wait for all threads to finish
        self.root.destroy()  # Close the application window

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoGalleryApp(root)
    root.mainloop()
