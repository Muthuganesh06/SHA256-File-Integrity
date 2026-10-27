# MINI PROJECT REPORT

## Title
**File Integrity Verification Using SHA-256**

## 1. Abstract
This project implements a simple file integrity verification system using the SHA-256 cryptographic hash algorithm. The application generates a hash value for a reference file and a second file, then compares the values. Matching hashes indicate that the file contents are identical; different hashes indicate that the contents differ.

## 2. Introduction
File integrity is important when sharing documents, storing backups, downloading software, and preserving digital evidence. Even a small change in a file normally produces a different SHA-256 hash. Hashing therefore provides a practical way to check whether two files contain the same data.

## 3. Problem Statement
Users need a simple way to check whether a file has changed or differs from a trusted reference copy.

## 4. Objectives
- Generate SHA-256 hashes for selected files.
- Compare hash values automatically.
- Display a clear integrity verification result.
- Provide a simple graphical user interface.

## 5. Tools and Technologies
- Language: Python
- Hash algorithm: SHA-256
- Library: `hashlib`
- GUI: `tkinter`
- IDE: IDLE or Visual Studio Code

## 6. Proposed System
The user selects a reference file and a file to verify. The program reads each file in binary mode, calculates its SHA-256 hash, and compares the two hash strings. It displays MATCH if they are equal and MISMATCH otherwise.

## 7. Algorithm
1. Start the application.
2. Select the reference file.
3. Read the file in binary chunks and calculate its SHA-256 hash.
4. Select the file to verify.
5. Calculate its SHA-256 hash.
6. Compare the two hash values.
7. If equal, display “File integrity verified.”
8. Otherwise, display “Files are different.”
9. Stop.

## 8. Implementation
The `hashlib.sha256()` function creates the hash object. File data is read in chunks to avoid loading large files entirely into memory. The `tkinter` library provides the file selection buttons and result window.

## 9. Expected Output
- If the files are identical: **MATCH — The file contents are identical. Integrity verified.**
- If the files differ: **MISMATCH — The file contents differ. The file may have changed.**

## 10. Advantages
- Easy to use.
- Supports many file types.
- No third-party package installation is required.
- Can process large files in chunks.

## 11. Limitations
- A trusted reference hash or reference file is required.
- Hashing does not encrypt data.
- A matching hash alone does not prove the identity of the file's author.
- The application compares two files; it does not maintain a protected history of hashes.

## 12. Applications
- Checking downloaded files.
- Comparing backup copies.
- Document integrity verification.
- Basic digital forensics and data integrity checks.

## 13. Conclusion
The project demonstrates how SHA-256 hashing can be used to compare file contents and identify differences. It offers a simple introduction to cryptographic hashing and file integrity verification.

## 14. Future Enhancement
The project can be extended with folder scanning, batch file verification, a saved reference-hash database, and digitally signed hash manifests.
