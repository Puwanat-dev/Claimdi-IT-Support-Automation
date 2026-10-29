import tkinter as tk
from aig_claim_workflow import AIGWorkflow


class PolicyUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Page Switch")
        self.geometry("300x200")
        self.configure(bg="#f5f5f5")

        self.aig_workflow = AIGWorkflow()

        self.container = tk.Frame(self, bg="#f5f5f5")
        self.container.pack(fill="both", expand=True)

        self.show_page("policy_ui_home")

    def run_aig(self):
        try:
            self.aig_workflow.run()
        except SystemExit:
            pass 

    def show_page(self, page_name):
        for widget in self.container.winfo_children():
            widget.destroy()

        if page_name == "policy_ui_home":
            self.create_policy_home_page()

    def create_policy_home_page(self):
        label = tk.Label(self.container, text="Insurance Selector", font=("Arial", 14))
        label.pack(pady=(30, 10))

        aig_runflow_button = tk.Button(
            self.container,
            text="AIG",
            command=self.run_aig,
            width=20,
            height=2,
        )
        aig_runflow_button.pack()


if __name__ == "__main__":
    app = PolicyUI()
    app.mainloop()     # this keeps the window alive