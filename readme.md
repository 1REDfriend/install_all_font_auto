# Font Extractor

This Python script is designed to extract font files from ZIP archives and organize them into a designated folder. It provides a simple GUI interface built with Qt for selecting a folder containing ZIP files, extracting font files, and organizing them for installation.

## Prerequisites

- Python 3.x
- PySide6 library (Qt for Python)

## Installation

- Creating and activating an environment You can do this by running the following on a terminal:
  - Create environment (Your Python executable might be called python3):
  ```python
  python -m venv env
  ```
  - Activate the environment (Windows):
  ```python
  env\Scripts\activate.bat
  ```

- Installing PySide6
  - Now you are ready to install the Qt for Python packages using pip. From the terminal, run the following command:
    - For the latest version:
      ```python
      pip install pyside6
      ```
    - It is also possible to install a specific snapshot from our servers. To do so, you can use the following command:
      ```python
      pip install --index-url=https://download.qt.io/snapshots/ci/pyside/6.4/latest pyside6 --trusted-host download.qt.io
      ```

## Usage

1. Run the script using Python.
2. Click the "Select Folder" button to choose the folder containing ZIP files with font files.
3. Click the "Extract All" button to extract font files from the selected folder.
4. The extracted font files will be organized into a subfolder named "font_for_install" within the selected folder.
5. The script will display the progress and details of the extraction process in the text area.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
