import subprocess
import pytest

def run_behave_tests():
    print("Running Behave tests...")
    result = subprocess.run(["behave"], capture_output=True, text=True)
    print(result.stdout)