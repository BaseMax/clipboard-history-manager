import pyperclip
import time
import os
import json
import argparse

HISTORY_FILE = 'clipboard_history.json'

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as file:
            return json.load(file)
    return []

def save_history(history):
    with open(HISTORY_FILE, 'w') as file:
        json.dump(history, file)

def add_to_history(content, history):
    if not history or history[0] != content:
        history.insert(0, content)
        if len(history) > 10:
            history.pop()
        save_history(history)

def show_history(history):
    if not history:
        print("No clipboard history found.")
        return
    for idx, item in enumerate(history):
        print(f"{idx + 1}: {item}")

def monitor_clipboard():
    history = load_history()
    previous_content = ""

    print("Monitoring clipboard. Press Ctrl+C to stop.")
    while True:
        try:
            current_content = pyperclip.paste()

            if current_content != previous_content:
                add_to_history(current_content, history)
                previous_content = current_content
            time.sleep(1)

        except KeyboardInterrupt:
            print("\nClipboard monitoring stopped.")
            break

def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    print("Clipboard history cleared.")

def main():
    parser = argparse.ArgumentParser(description="Clipboard History Manager")
    parser.add_argument('-m', '--monitor', action='store_true', help="Monitor clipboard history.")
    parser.add_argument('-v', '--view', action='store_true', help="View clipboard history.")
    parser.add_argument('-c', '--clear', action='store_true', help="Clear clipboard history.")
    
    args = parser.parse_args()
    
    if args.monitor:
        monitor_clipboard()
    elif args.view:
        history = load_history()
        show_history(history)
    elif args.clear:
        clear_history()
    else:
        print("Please specify an action: --monitor, --view, or --clear")

if __name__ == "__main__":
    main()
