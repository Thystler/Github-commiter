import schedule
import time
import random
import subprocess
import os

# Function to execute shell commands
def run_command(command):
    subprocess.run(command, shell=True, check=True)

# Function to make commits
def make_commits():
    file_to_change = 'important.txt'       # Replace with the file you want to change
    num_commits = random.randint(1, 4)  # Random number of commits

    # Make random commits
    for i in range(num_commits):
        # Write to a file
        with open(file_to_change, 'a') as file:
            file.write(f"Adding line {i + 1}\n")

        # Stage the file
        run_command(f'git add {file_to_change}')

        # Commit the change
        run_command(f'git commit -m "Commit number {i + 1}"')

    run_command('git push')  # Push commits to GitHub

    print(f"Made {num_commits} commits.")

# Run once immediately
make_commits()

# Schedule the job
schedule.every().day.at("03:00").do(make_commits)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
