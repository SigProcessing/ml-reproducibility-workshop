#!/bin/bash
# Script to create initial Python files in git-repro-workshop

WORKSHOP_DIR="git-repro-workshop"

# Check if the script is being run from the correct directory
if [ "$(basename "$PWD")" != "$WORKSHOP_DIR" ]; then
  echo "Please run this script from the $WORKSHOP_DIR directory."
  exit 1
fi

# Create initial Python files
echo 'print("Hello, World!")' > "hello.py"
echo 'def add(a, b): return a + b' > "math-utils.py"
echo 'if __name__ == "__main__": print("This is the main script.")' > "main.py"

echo "Initial Python files have been created in $WORKSHOP_DIR."