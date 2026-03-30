import json
import subprocess
import time

MAX_ACCOUNTS = 150
DELAY = 0.5

with open("accs.json", "r", encoding="utf-8") as f:
    accounts = json.load(f)

processes = []

for i, (uid, password) in enumerate(accounts.items()):
    if i >= MAX_ACCOUNTS:
        break
    p = subprocess.Popen(["python", "bot.py", uid, password])
    processes.append(p)
    time.sleep(DELAY)

for p in processes:
    p.wait()