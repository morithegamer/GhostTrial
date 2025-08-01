# games/ttr_module.py

"""
Toontown Rewritten memory scanner.
Scans for basic progression values like laff, jellybeans, and gags.
Values are estimated for testing and learning purposes only.
"""

from core.memory_scanner import attach_to_process, scan_for_value

def scan_ttr_memory():
    logs = []
    pm = attach_to_process("ttr.exe")  # Adjust if process is named differently

    if not pm:
        logs.append("[ERROR] Could not find ttr.exe running.")
        return logs

    logs.append("[TTR] Attached to Toontown Rewritten process successfully.")

    target_values = {
        "Laff Points (max test: 137)": 137,
        "Jellybeans (common test: 5000)": 5000,
        "Throw XP (Test 600)": 600,
        "Squirt XP (Test 600)": 600,
        "Trap XP (Test 0)": 0,
    }

    for name, value in target_values.items():
        logs.append(f"[TTR] Scanning for {name}...")
        results = scan_for_value(pm, value, value_type='int')
        logs.extend(results)

    return logs
