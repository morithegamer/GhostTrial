# core/honeypot.py

import os
from datetime import datetime

def deploy_honeypot():
    bait_dir = os.path.expanduser("~/.ghosttrial_honeypot")
    os.makedirs(bait_dir, exist_ok=True)

    bait_files = {
        "steam_pass.txt": "steam_user=mori\nsteam_password=123456",
        "discord_token.txt": "NTg4...FAKETOKEN",
        "microsoft_key.txt": "MICROSOFT_KEY=XXXX-XXXX-XXXX-XXXX",
        "inject_logs.log": "[Injection trace log begins here...]\n\n",
        "ghosttrial_config.bait": "autoexec=true\ninternal_mode=on",
    }

    results = []
    for filename, content in bait_files.items():
        path = os.path.join(bait_dir, filename)
        try:
            with open(path, "w") as f:
                f.write(content)
            results.append(f"[HONEYPOT] Created bait file: {path}")
        except Exception as e:
            results.append(f"[ERROR] Failed to create {filename}: {e}")

    return results
