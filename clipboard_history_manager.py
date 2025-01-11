import os
import pyperclip
import time
import argparse
from datetime import datetime

HISTORY_DIR = 'clipboard_history'

VERSION = '1.0.0'

def create_history_dir():
    if not os.path.exists(HISTORY_DIR):
        os.makedirs(HISTORY_DIR)

def generate_filename():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S%f')
    return os.path.join(HISTORY_DIR, f"{timestamp}_text.txt")

def save_text(content):
    filename = generate_filename()
    with open(filename, 'w') as file:
        file.write(content)

def load_history():
    return [
        {'filename': f, 'content': open(os.path.join(HISTORY_DIR, f), 'r').read()}
        for f in os.listdir(HISTORY_DIR)
    ]

def show_history():
    history = load_history()
    if history:
        for idx, item in enumerate(history):
            print(f"{idx + 1}: {item['filename']} - Content: {item['content']}")
    else:
        print("No clipboard history found.")

def monitor_clipboard():
    previous_content = None
    while True:
        try:
            current_content = pyperclip.paste()
            if current_content != previous_content and current_content:
                print("Clipboard changed, saving text...")
                save_text(current_content)
                previous_content = current_content
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nClipboard monitoring stopped.")
            break

def clear_history():
    for filename in os.listdir(HISTORY_DIR):
        os.remove(os.path.join(HISTORY_DIR, filename))
    print("Clipboard history cleared.")

def parse_args():
    parser = argparse.ArgumentParser(
        description="Clipboard History Manager: A simple tool to manage and store clipboard content.",
        epilog="You can monitor your clipboard, view the saved history, or clear the clipboard history."
    )
    parser.add_argument(
        '-m', '--monitor',
        action='store_true',
        help="Monitor clipboard for changes and automatically save new clipboard content."
    )
    parser.add_argument(
        '-v', '--view',
        action='store_true',
        help="View the saved clipboard history (list of previously copied content)."
    )
    parser.add_argument(
        '-c', '--clear',
        action='store_true',
        help="Clear the entire clipboard history by deleting all saved files."
    )
    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s {VERSION}',
        help="Show the version of the program."
    )
    return parser.parse_args()

def main():
    create_history_dir()
    args = parse_args()
    if args.monitor:
        monitor_clipboard()
    elif args.view:
        show_history()
    elif args.clear:
        clear_history()
    else:
        print("Please specify an action: --monitor, --view, or --clear")

if __name__ == "__main__":
    main()
