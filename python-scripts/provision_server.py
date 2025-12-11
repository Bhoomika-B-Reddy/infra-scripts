import os
import subprocess

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

# Update packages
run("sudo apt update -y")
run("sudo apt upgrade -y")

# Create user
run("sudo useradd -m automation -s /bin/bash")

# Install tools
run("sudo apt install -y nginx python3-pip")

print("Python-based provisioning complete!")
