import subprocess

# Выполнение команды sudo apt-get autoclean
autoclean_process = subprocess.run(['sudo', 'apt-get', 'autoclean'], capture_output=True, text=True)
print(autoclean_process.stdout)

# Выполнение команды sudo apt-get autoremove
autoremove_process = subprocess.run(['sudo', 'apt-get', 'autoremove'], capture_output=True, text=True)
print(autoremove_process.stdout)

# Выполнение команды sudo apt-get clean
clean_process = subprocess.run(['sudo', 'apt-get', 'clean'], capture_output=True, text=True)
print(clean_process.stdout)
