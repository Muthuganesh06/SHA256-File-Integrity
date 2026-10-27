import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path


def sha256_file(file_path):
    """Return the SHA-256 hash of a file, reading it in chunks."""
    digest = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            digest.update(chunk)
    return digest.hexdigest()


class IntegrityChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("File Integrity Verification - SHA-256")
        self.root.geometry("760x540")
        self.root.minsize(680, 500)
        self.root.configure(bg="#08111f")

        self.original_path = tk.StringVar()
        self.verify_path = tk.StringVar()
        self.original_hash = tk.StringVar(value="Not generated")
        self.verify_hash = tk.StringVar(value="Not generated")
        self.status = tk.StringVar(value="Choose two files to compare their integrity.")

        self._build_ui()

    def _build_ui(self):
        title = tk.Label(
            self.root, text="FILE INTEGRITY VERIFICATION",
            font=("Arial", 20, "bold"), fg="#46e6ff", bg="#08111f"
        )
        title.pack(pady=(18, 2))
        subtitle = tk.Label(
            self.root, text="Using SHA-256 Cryptographic Hashing",
            font=("Arial", 12), fg="#d9e8ff", bg="#08111f"
        )
        subtitle.pack(pady=(0, 18))

        self._file_row("Original/reference file", self.original_path, self.select_original)
        self._hash_box("Reference SHA-256 hash", self.original_hash)
        self._file_row("File to verify", self.verify_path, self.select_verify)
        self._hash_box("Verification SHA-256 hash", self.verify_hash)

        compare = tk.Button(
            self.root, text="COMPARE HASHES", command=self.compare,
            font=("Arial", 12, "bold"), bg="#00b8d9", fg="#04111d",
            activebackground="#63eaff", relief="flat", padx=18, pady=9
        )
        compare.pack(pady=14)

        status_box = tk.Label(
            self.root, textvariable=self.status, wraplength=680,
            font=("Arial", 11, "bold"), fg="#ffffff", bg="#13243a",
            padx=12, pady=14
        )
        status_box.pack(fill="x", padx=24, pady=(0, 12))

        footer = tk.Label(
            self.root, text="HASH  •  COMPARE  •  VERIFY",
            font=("Arial", 10, "bold"), fg="#8ca6c8", bg="#08111f"
        )
        footer.pack(side="bottom", pady=12)

    def _file_row(self, label, variable, command):
        frame = tk.Frame(self.root, bg="#08111f")
        frame.pack(fill="x", padx=24, pady=(4, 0))
        tk.Label(frame, text=label, font=("Arial", 10, "bold"),
                 fg="#d9e8ff", bg="#08111f").pack(anchor="w")
        row = tk.Frame(frame, bg="#08111f")
        row.pack(fill="x", pady=5)
        tk.Entry(row, textvariable=variable, state="readonly",
                 readonlybackground="#102039", fg="#ffffff",
                 insertbackground="#ffffff", relief="flat").pack(
                     side="left", fill="x", expand=True, ipady=7
                 )
        tk.Button(row, text="Browse", command=command, bg="#203957",
                  fg="#ffffff", activebackground="#31577d",
                  relief="flat", padx=14, pady=6).pack(side="left", padx=(8, 0))

    def _hash_box(self, label, variable):
        frame = tk.Frame(self.root, bg="#102039", padx=10, pady=8)
        frame.pack(fill="x", padx=24, pady=(2, 8))
        tk.Label(frame, text=label, font=("Arial", 9, "bold"),
                 fg="#71e8f5", bg="#102039").pack(anchor="w")
        tk.Label(frame, textvariable=variable, font=("Courier New", 9),
                 fg="#ffffff", bg="#102039", wraplength=680,
                 justify="left").pack(anchor="w", pady=(4, 0))

    def select_original(self):
        path = filedialog.askopenfilename(title="Select original/reference file")
        if path:
            self.original_path.set(path)
            try:
                self.original_hash.set(sha256_file(path))
            except OSError as exc:
                messagebox.showerror("File error", str(exc))

    def select_verify(self):
        path = filedialog.askopenfilename(title="Select file to verify")
        if path:
            self.verify_path.set(path)
            try:
                self.verify_hash.set(sha256_file(path))
            except OSError as exc:
                messagebox.showerror("File error", str(exc))

    def compare(self):
        first = self.original_path.get()
        second = self.verify_path.get()
        if not first or not second:
            messagebox.showwarning("Missing file", "Please select both files before comparing.")
            return
        try:
            hash1 = sha256_file(first)
            hash2 = sha256_file(second)
            self.original_hash.set(hash1)
            self.verify_hash.set(hash2)
        except OSError as exc:
            messagebox.showerror("File error", str(exc))
            return

        if hash1 == hash2:
            self.status.set("MATCH — The file contents are identical. Integrity verified.")
            messagebox.showinfo("Verification result", "MATCH: File integrity verified.")
        else:
            self.status.set("MISMATCH — The file contents differ. The file may have changed.")
            messagebox.showwarning("Verification result", "MISMATCH: The files are different.")


if __name__ == "__main__":
    root = tk.Tk()
    app = IntegrityChecker(root)
    root.mainloop()
