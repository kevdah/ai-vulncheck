import re
import sys

def extract_changed_function(diff_file):
    with open(diff_file, 'r') as f:
        diff_content = f.read()

    # Assuming Python functions for now; adjust for other languages accordingly
    pattern = r'(def .*\(.*\):\n(?:    .*\n)+)'
    match = re.search(pattern, diff_content, re.MULTILINE)

    if match:
        return "{\"function\":\"" + match.group(1) + "\"}"
    else:
        return "No function changes detected."

if __name__ == "__main__":
    diff_file = sys.argv[1]
    changed_function = extract_changed_function(diff_file)
    print(changed_function)
