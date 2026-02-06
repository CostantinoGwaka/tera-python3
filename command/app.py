import subprocess

# subprocess.call(['echo', 'Hello, World!'])
# subprocess.check_call(['echo', 'This will raise an error if it fails.'])
# subprocess.check_output(['echo', 'This will capture the output.'])
# subprocess.run(['echo', 'This is a more modern way to run subprocesses.'], check=True)
# subprocess.Popen(['echo', 'This will run in the background.'])

# result = subprocess.run(['python3', 'other.py'],
#                         capture_output=True, text=True)
# result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
try:
    result = subprocess.run(['false',],
                            capture_output=True, text=True, check=True)
    print(type(result))
    print("returncode", result.returncode)
    print("args", result.args)
    print("stderr", result.stderr)
    print("stdout", result.stdout)
except subprocess.CalledProcessError as e:
    print("An error occurred while running the subprocess:")
    print("Return code:", e.returncode)
    print("Output:", e.output)
    print("Error message:", e.stderr)
