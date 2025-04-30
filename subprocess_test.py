import subprocess
from dotenv import load_dotenv
import os
import sys




load_dotenv()

tool_dir = os.environ['tool_dir']
# Create the command
# Command line: poetry run python src/our_main.py --tickers AAPL,MSFT,NVDA --ollama --agent technical_analyst --ollama-model gemma3:4b
command = [
    "poetry", "run", "python", "src/our_main.py",
    "--tickers", "AAPL,MSFT,NVDA",
    "--ollama",
    "--agent", "technical_analyst",
    "--ollama-model", "gemma3:4b"
]

# Run the process and capture output
result = subprocess.run(
    command,
    cwd=tool_dir,
    text=True,
    capture_output=True
)

# Print output and error (if any)
print("Output:")
print(result.stdout)

if result.stderr:
    print("Errors:")
    print(result.stderr)