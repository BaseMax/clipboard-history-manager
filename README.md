# Clipboard History Manager

Clipboard History Manager is a simple and efficient tool that allows users to manage and store clipboard content. The project provides a way to monitor clipboard changes, view saved clipboard history, and clear the entire clipboard history.

## Features

- **Monitor clipboard**: Detect changes in clipboard content and automatically save new clipboard entries.
- **View clipboard history**: View the list of previously copied content stored in the clipboard history.
- **Clear history**: Clear all saved clipboard history.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/BaseMax/clipboard-history-manager.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

- **Help message**:
    
    ```bash
    $ python clipboard_history_manager.py --help
    usage: clipboard_history_manager.py [-h] [-m] [-v] [-c] [--version]
    
    Clipboard History Manager: A simple tool to manage and store clipboard content.
    
    options:
      -h, --help     show this help message and exit
      -m, --monitor  Monitor clipboard for changes and automatically save new clipboard content.
      -v, --view     View the saved clipboard history (list of previously copied content).
      -c, --clear    Clear the entire clipboard history by deleting all saved files.
      --version      Show the version of the program.
    
    You can monitor your clipboard, view the saved history, or clear the clipboard history.
    ```

- **Monitor clipboard for changes**:

    ```bash
    python clipboard_history_manager.py --monitor
    ```

- **View clipboard history**:

    ```bash
    python clipboard_history_manager.py --view
    ```

- **Clear clipboard history**:

    ```bash
    python clipboard_history_manager.py --clear
    ```

- **Show version**:

    ```bash
    python clipboard_history_manager.py --version
    ```

## License

MIT License

© Copyright 2025, Max Base
