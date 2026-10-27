import os
import openpyxl
import pyperclip
import tkinter as tk
from tkinter import messagebox

class TextScript:
    DEFAULT_PATTERN_FILE = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "mail_patterns.xlsx" #file name
    )
    
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Mail Answer Pattern Selector")
        self.root.geometry("500x600")
        self.root.configure(bg="#f5f5f5")


        # Read column data
        self.C_patterns = self.read_Column_C()
        

        # Create UI
        main_frame = tk.Frame(self.root, bg="#f5f5f5")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        top_frame = tk.Frame(main_frame, bg="#f5f5f5")
        top_frame.pack(fill="x", pady=(0, 10))

        action_row = tk.Frame(top_frame, bg="#f5f5f5")
        action_row.pack(fill="x")
        self.create_close_button(action_row)


        columns_frame = tk.Frame(main_frame, bg="#f5f5f5")
        columns_frame.pack(fill="both", expand=True)
        columns_frame.grid_columnconfigure(0, weight=1)
        columns_frame.grid_columnconfigure(1, weight=1)

        self.create_C_buttons(columns_frame)
        


    def read_Column_C(self):
        """Read all cells from column C until empty cell is found"""
        C_patterns = []
        
        try:
            # Check if file exists
            if not os.path.exists(self.DEFAULT_PATTERN_FILE):
                messagebox.showwarning("File Not Found", 
                                     f"Pattern file not found at:\n{self.DEFAULT_PATTERN_FILE}")
                return C_patterns
            
            # Open workbook and get active sheet
            workbook = openpyxl.load_workbook(self.DEFAULT_PATTERN_FILE)
            sheet = workbook.active
            
            # Read column C starting from row 1
            row = 1
            while True:
                cell_value = sheet.cell(row=row, column=3).value
                
                # Break when empty cell is found
                if cell_value is None or str(cell_value).strip() == "":
                    break
                    
                C_patterns.append(str(cell_value).strip())
                row += 1
            
            workbook.close()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read pattern file:\n{str(e)}")
        
        return C_patterns
    
    def create_C_buttons(self, parent):
        """Create buttons for each pattern found in column C"""
        if not self.C_patterns:
            label = tk.Label(parent, text="No C patterns found in file",
                           font=("Arial", 12), fg="red", bg="#f5f5f5")
            label.grid(row=0, column=0, padx=10, pady=10, sticky="n")
            return

        section = tk.Frame(parent, bg="#f5f5f5")
        section.grid(row=0, column=0, padx=(0, 10), pady=10, sticky="nsew")

        title_label = tk.Label(section, text="C Patterns", font=("Arial", 14, "bold"), bg="#f5f5f5")
        title_label.pack(pady=(0, 10))

        frame_canvas = tk.Frame(section, bg="#f5f5f5")
        frame_canvas.pack(fill="both", expand=True)

        canvas = tk.Canvas(frame_canvas, bg="#f5f5f5")
        scrollbar = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview , width=30)
        scrollable_frame = tk.Frame(canvas, bg="#f5f5f5")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for pattern in self.C_patterns:
            button = tk.Button(
                scrollable_frame,
                text=pattern,
                command=lambda p=pattern: (pyperclip.copy(p)),
                width=35,
                height=2,
                bg="#f0f0f0",
                relief="raised",
                cursor="hand2",
            )
            button.pack(pady=5, fill="x")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def create_close_button(self, parent):
        close_button = tk.Button(
            parent,
            text="Close",
            command=self.root.destroy,
            width=15,
            height=2,
            bg="#f0f0f0",
            relief="raised",
            cursor="hand2",
        )
        close_button.pack(side="left", pady=5)
    
    def run(self):
        """Start the Tkinter main loop"""
        self.root.mainloop()


if __name__ == "__main__":
    app = TextScript()
    app.run()