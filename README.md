# Converting Python Code to a Standalone Application (.exe)

This guide explains how to convert a Python project into a standalone Windows executable (.exe). Follow the steps below to complete the process easily.

## Requirements
1. **Python** must be installed on your system.
2. **PyInstaller** and **pyrcc5** libraries should be installed.
   - If not already installed, run the following commands:
     ```bash
     pip install pyinstaller
     pip install PyQt5
     ```

---

## Steps

### 1. Convert `.qrc` File to `.py` File
If your project includes a `.qrc` file (e.g., a Qt Resource file for managing assets), you need to convert it to a `.py` file using the following command:

```bash
pyrcc5 file_name.qrc -o file_name.py
