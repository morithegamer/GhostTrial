# games/tot_module.py

"""
Scans Outlast Trials memory for Murkoff Currencies & progression values.
Currency definitions from:
https://outlast.fandom.com/wiki/Murkoff_Currencies
"""

from core.memory_scanner import attach_to_process, scan_for_value

def scan_tot_memory():
    logs = []
    pm = attach_to_process("Outlast_Trials.exe")

    if not pm:
        logs.append("[ERROR] Could not find Outlast_Trials.exe running.")
        return logs

    logs.append("[TOT] Attached to Outlast Trials process successfully.")

    # Based on Outlast Trials wiki: https://outlast.fandom.com/wiki/Murkoff_Currencies
    target_values = {
        # 💰 Premium/soft currencies
        "Murkoff Coins (used for Program Advances, cosmetics)": 9999,
        "Tokens (granted during trials)": 999,
        "Stamps (account progression/leveling)": 1337,
        "RIG Unlock Flag (used to test if RIGs are enabled)": 1,
        "Suspected Dev Cheat Flag": 7777,

        # 🧱 Progression unlockables
        "Stamps (account progression/leveling)": 1337,
        "RIG Unlock Flag (used to test if RIGs are enabled)": 1,

        # 🧪 Extra test (used in some trainer scans)
        "Trial XP (Test 5555)": 5555,
        "RIG Progress Flag (Test)": 42,
        "Cosmetic Unlock Test (2222)": 2222,
        "Trial XP (Test 5555)": 5555,
        "RIG Progress Flag (Test)": 42,
        "Cosmetic Unlock Test (2222)": 2222,
        "Trial XP (Test 5555)": 5555,
        "RIG Progress Flag (Test)": 42,
        "Cosmetic Unlock Test (2222)": 2222,

    }

    for name, value in target_values.items():
        logs.append(f"[TOT] Scanning for {name}...")
        results = scan_for_value(pm, value, value_type='int')
        logs.extend(results)

    return logs