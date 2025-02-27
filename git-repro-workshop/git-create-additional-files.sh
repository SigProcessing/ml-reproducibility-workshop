#!/bin/bash
# Script to create additional Python files in git-repro-workshop

WORKSHOP_DIR="git-repro-workshop"

# Check if the script is being run from the correct directory
if [ "$(basename "$PWD")" != "$WORKSHOP_DIR" ]; then
  echo "Please run this script from the $WORKSHOP_DIR directory."
  exit 1
fi

# Create new Python files
echo 'def subtract(a, b): return a - b' > "subtraction.py"
echo 'print("Logging system initialized")' > "logger.py"
echo -e 'class DataProcessor:\n    def process(self, data): return data * 2' > "data-processor.py"

echo "Additional Python files have been created in $WORKSHOP_DIR."