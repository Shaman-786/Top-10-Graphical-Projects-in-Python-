import smtplib
import imaplib
import email
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from email.mime.text import MIMEText
from tkinter import messagebox, simpledialog, scrolledtext

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for a voice command and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            speak("Could not request results.")
            return None

def send_email(to_address, subject, message):
    """Send an email with the given parameters."""
    from_address = "your_email@gmail.com"  # Replace with your email
    password = "your_email_password"         # Replace with your email password

    # Create the email content
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    try:
        # Connect to the email server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_address, password)
            server.sendmail(from_address, to_address, msg.as_string())
            print("Email sent successfully.")
            speak("Email sent successfully.")
            messagebox.showinfo("Success", "Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
        speak("Failed to send email.")
        messagebox.showerror("Error", f"Failed to send email: {e}")

def read_emails():
    """Read emails from the inbox."""
    from_address = "your_email@gmail.com"  # Replace with your email
    password = "your_email_password"         # Replace with your email password

    try:
        # Connect to the email server using IMAP
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(from_address, password)
        mail.select('inbox')

        # Search for all emails
        result, data = mail.search(None, 'ALL')
        email_ids = data[0].split()

        email_history = ""

        for email_id in email_ids[-5:]:  # Read the last 5 emails
            result, message_data = mail.fetch(email_id, '(RFC822)')
            msg = email.message_from_bytes(message_data[0][1])
            subject = msg['subject']
            from_email = msg['from']
            email_history += f"From: {from_email}, Subject: {subject}\n"

        mail.logout()
        return email_history.strip() if email_history else "No emails found."
    except Exception as e:
        print(f"Failed to read emails: {e}")
        speak("Failed to read emails.")
        messagebox.showerror("Error", f"Failed to read emails: {e}")
        return ""

def show_email_history():
    """Display the email history in a text area."""
    email_history = read_emails()
    email_history_window = tk.Toplevel()
    email_history_window.title("Email History")
    
    text_area = scrolledtext.ScrolledText(email_history_window, width=50, height=20)
    text_area.pack(padx=10, pady=10)
    text_area.insert(tk.END, email_history)
    text_area.config(state=tk.DISABLED)  # Make the text area read-only

def main():
    """Main workflow for the voice email system."""
    speak("Welcome to the voice email system. Please tell me the recipient's email address.")
    to_address = listen()
    
    if to_address:
        speak("What is the subject of your email?")
        subject = listen()
        
        if subject:
            speak("Please dictate your message.")
            message = listen()
            
            if message:
                send_email(to_address, subject, message)
            else:
                speak("No message provided.")
                messagebox.showwarning("Warning", "No message provided.")
        else:
            speak("No subject provided.")
            messagebox.showwarning("Warning", "No subject provided.")
    else:
        speak("No recipient provided.")
        messagebox.showwarning("Warning", "No recipient provided.")

# Create a simple GUI
def create_gui():
    """Create a simple GUI for the email system."""
    window = tk.Tk()
    window.title("Voice Email System")

    tk.Label(window, text="Voice Email System", font=("Helvetica", 16)).pack(pady=10)

    send_email_button = tk.Button(window, text="Send Email", command=main, width=20)
    send_email_button.pack(pady=5)

    read_email_button = tk.Button(window, text="Show Email History", command=show_email_history, width=20)
    read_email_button.pack(pady=5)

    settings_button = tk.Button(window, text="Settings", command=lambda: messagebox.showinfo("Settings", "Settings feature is not implemented yet."), width=20)
    settings_button.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
