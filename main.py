import subprocess

prompt = ["journalctl", "-p", "-err", "-n", "-20"]
result = subprocess.run(prompt, capture_output=True, text=True)

print(result.stdout)