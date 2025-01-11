import os
import pyperclip
import time
import base64
import argparse
from datetime import datetime
from PIL import Image
import io
import magic

HISTORY_DIR = 'clipboard_history'

if not os.path.exists(HISTORY_DIR):
    os.makedirs(HISTORY_DIR)

def generate_filename(content_type):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S%f')
    return os.path.join(HISTORY_DIR, f"{timestamp}_{content_type}")

def save_text(content):
    filename = generate_filename('text.txt')
    with open(filename, 'w') as file:
        file.write(content)
    return filename

def save_image(image_data, file_type):
    if file_type == 'image/png':
        extension = '.png'
    elif file_type == 'image/jpeg':
        extension = '.jpg'
    else:
        extension = '.img'

    filename = generate_filename(f'image{extension}')
    image = Image.open(io.BytesIO(image_data))
    image.save(filename)
    return filename

def save_binary(content):
    filename = generate_filename('binary.bin')
    with open(filename, 'wb') as file:
        file.write(content)
    return filename

def detect_content_type(content):
    if isinstance(content, str):
        return 'text'
    
    file_type = magic.Magic(mime=True).from_buffer(content)
    
    if file_type.startswith('image/'):
        return 'image'
    else:
        return 'binary'

def save_content(content):
    content_type = detect_content_type(content)
    
    if content_type == 'text':
        return save_text(content)
    elif content_type == 'image':
        return save_image(content, magic.Magic(mime=True).from_buffer(content))
    elif content_type == 'binary':
        return save_binary(content)

def load_history():
    history = []
    for filename in os.listdir(HISTORY_DIR):
        filepath = os.path.join(HISTORY_DIR, filename)
        with open(filepath, 'rb') as file:
            history.append({
                'filename': filename,
                'content': file.read()
            })
    return history

def show_history():
    history = load_history()
    if not history:
        print("No clipboard history found.")
        return
    for idx, item in enumerate(history):
        print(f"{idx + 1}: {item['filename']}")

def monitor_clipboard():
    previous_content = None
    while True:
        try:
            current_content = pyperclip.paste()

            if current_content != previous_content:
                if current_content:
                    print(f"Clipboard changed, saving text...")
                    save_content(current_content)
                previous_content = current_content

            time.sleep(1)

        except KeyboardInterrupt:
            print("\nClipboard monitoring stopped.")
            break

def clear_history():
    for filename in os.listdir(HISTORY_DIR):
        file_path = os.path.join(HISTORY_DIR, filename)
        os.remove(file_path)
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
        show_history()
    elif args.clear:
        clear_history()
    else:
        print("Please specify an action: --monitor, --view, or --clear")

if __name__ == "__main__":
    main()
