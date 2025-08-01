import customtkinter as ctk
import tkinter as tk
from datetime import datetime
from core.process_watcher import scan_processes
from core.honeypot import deploy_honeypot
from core.memory_scanner import attach_to_process, scan_for_value
from games.tot_module import scan_tot_memory
from games.ttr_module import scan_ttr_memory
from games.ttcc_module import scan_ttcc_memory
# GhostTrial GUI Application
# GUI Theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Main App
class GhostTrialApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("👻 GhostTrial v1.0 - Anti-Cheat Forensics")
        self.geometry("900x600")
        self.resizable(False, False)

        # === Sidebar: Game Selector ===
        self.sidebar = ctk.CTkFrame(self, width=200)
        self.sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(self.sidebar, text="🎮 Game Module", font=("Arial", 16, "bold")).pack(pady=(20, 10))

        self.game_var = tk.StringVar(value="TOT")
        ctk.CTkRadioButton(self.sidebar, text="Outlast Trials", variable=self.game_var, value="TOT").pack(pady=5)
        ctk.CTkRadioButton(self.sidebar, text="Toontown Rewritten", variable=self.game_var, value="TTR").pack(pady=5)
        ctk.CTkRadioButton(self.sidebar, text="Corporate Clash", variable=self.game_var, value="TTCC").pack(pady=5)

        # === Main Window Area ===
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Action Buttons
        ctk.CTkLabel(self.main_frame, text="🧪 GhostTrial Actions", font=("Arial", 18, "bold")).pack(pady=(10, 5))

        self.button_frame = ctk.CTkFrame(self.main_frame)
        self.button_frame.pack(pady=10)

        self.scan_button = ctk.CTkButton(self.button_frame, text="🔍 Scan Memory", command=self.dummy_action)
        self.scan_button.grid(row=0, column=0, padx=10)

        self.proc_button = ctk.CTkButton(self.button_frame, text="🧠 Watch Processes", command=self.watch_processes)
        self.proc_button.grid(row=0, column=1, padx=10)

        self.honeypot_button = ctk.CTkButton(self.button_frame, text="🎯 Drop Honeypot", command=self.drop_honeypot)
        self.honeypot_button.grid(row=0, column=2, padx=10)

        self.clear_button = ctk.CTkButton(self.button_frame, text="🧼 Clear Log", command=self.clear_log)
        self.clear_button.grid(row=0, column=3, padx=10)

        self.tot_button = ctk.CTkButton(self.button_frame, text="🧪 Scan TOT Memory", command=self.scan_tot)
        self.tot_button.grid(row=1, column=0, pady=5)

        self.ttr_button = ctk.CTkButton(self.button_frame, text="🎩 Scan TTR Memory", command=self.scan_ttr)
        self.ttr_button.grid(row=1, column=1, pady=5)

        self.ttcc_button = ctk.CTkButton(self.button_frame, text="🏢 Scan TTCC Memory", command=self.scan_ttcc)
        self.ttcc_button.grid(row=1, column=2, pady=5)

        # === Output Log Box ===
        ctk.CTkLabel(self.main_frame, text="📜 Output Log", font=("Arial", 16)).pack()
        self.log_box = ctk.CTkTextbox(self.main_frame, width=700, height=350, corner_radius=6)
        self.log_box.pack(pady=10)
        self.log("👻 GhostTrial launched successfully.\n")

    def dummy_action(self):
        self.log("🔧 [NOT IMPLEMENTED] This feature will be added in the next step.")

    def watch_processes(self):
        self.log("🧠 Scanning running processes...")
        results = scan_processes()
        for line in results:
            self.log(line)
        self.log("🧠 Process scan completed.")

    def drop_honeypot(self):
        self.log("🎯 Deploying honeypot trap files...")
        results = deploy_honeypot()
        for line in results:
            self.log(line)
        self.log("🎯 Honeypot deployment completed.")

    def scan_tot(self):
        self.log("🧪 Scanning Outlast Trials memory for coin/token/RIG values...")
        results = scan_tot_memory()
        for line in results:
            self.log(line)
        self.log("🧪 Outlast Trials memory scan completed.")

    def scan_ttr(self):
        self.log("🎩 Scanning Toontown Rewritten for laff/gags/beans...")
        results = scan_ttr_memory()
        for line in results:
            self.log(line)
        self.log("🎩 Toontown Rewritten memory scan completed.")

    def scan_ttcc(self):
        self.log("🏢 Scanning Corporate Clash for kudos/beans/gag XP...")
        results = scan_ttcc_memory()
        for line in results:
            self.log(line)
        self.log("🏢 Corporate Clash memory scan completed.")

    def clear_log(self):
        self.log_box.delete("0.0", tk.END)
        self.log("📛 Log cleared.")

    def log(self, msg):
        timestamp = datetime.now().strftime("[%H:%M:%S] ")
        self.log_box.insert(tk.END, f"{timestamp}{msg}\n")
        self.log_box.see(tk.END)

# === Run App ===
if __name__ == "__main__":
    app = GhostTrialApp()
    app.mainloop()
