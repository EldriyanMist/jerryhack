# main.py
import os
import subprocess

# Step 1: Record audio using test.py
subprocess.run(["python", "test.py"])

# Step 2: Transcribe audio using ai.py
os.system("python ai.py")