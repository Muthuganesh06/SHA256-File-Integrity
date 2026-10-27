# File Integrity Verification Using SHA-256

## Project summary
A small Python desktop application that checks whether two files have identical contents by comparing their SHA-256 hash values.

## Features
- Select a reference file and a file to verify.
- Generate SHA-256 hashes using Python's built-in `hashlib` module.
- Compare the hashes and display MATCH or MISMATCH.
- Works with text, image, PDF, and other file types.

## Requirements
- Python 3.9 or newer
- Tkinter (usually included with standard Python installations)

No third-party Python packages are required.

## Run
1. Extract the ZIP file.
2. Open a terminal in the project folder.
3. Run:
   `python main.py`
4. Select the original/reference file.
5. Select the file to verify.
6. Click **COMPARE HASHES**.

## Result
- **MATCH:** The two files have identical contents.
- **MISMATCH:** The files have different contents.

## Important security note
SHA-256 is a cryptographic hash function, not encryption. Hash comparison can detect changes only when the reference hash is trustworthy. A hash by itself does not prove who created a file or keep its contents secret.
