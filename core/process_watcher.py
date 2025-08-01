# core/process_watcher.py

import psutil

def scan_processes():
    results = []
    flagged = ["cheat", "inject", "hook", "trainer", "engine", "table"]

    for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
        try:
            info = proc.info
            proc_str = f"{info['pid']:5} | {info['name']}"
            # Check for known sus keywords
            for word in flagged:
                if word in info['name'].lower() or ' '.join(info['cmdline']).lower().find(word) != -1:
                    proc_str += "  ⚠️ [SUSPICIOUS]"
                    break
            results.append(proc_str)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return results
