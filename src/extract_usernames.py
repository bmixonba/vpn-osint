## Basic imports
import re
import subprocess
import json
import sys

## ML imports 
from sklearn.feature_extraction.text import TfidfTransformer

def printdbg(s, dbg=False):
    """ """
    if dbg:
        print(s)

def extract_urls_file_paths_and_email_addresses(input_strings):
    """
    Extracts strings that look like URLs, file paths, and email addresses from a list of strings.

    Args:
        input_strings (list): A list of strings to process.

    Returns:
        A dictionary with three keys: 'urls', 'file_paths', and 'email_addresses', each containing a list of extracted strings.
    """
    if input_strings == None:
        # raise Exception(f"extract_urls_file_paths_and_email_addresses - invalid input")
        printdbg(f"extract_urls_file_paths_and_email_addresses - invalid input", dbg=True)
    result = {'urls': [], 'file_paths': [], 'email_addresses': []}

    # Regular expressions for URL, file path, and email address patterns
    url_pattern = r'https?://[^\s]+|www\.[^\s]+'
    file_path_pattern = r'/[^/]+'
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    printdbg(f"input_strings={input_strings}", dbg=True)

    for string in input_strings:
        # Extract URLs
        urls = re.findall(url_pattern, string)
        result['urls'].extend(urls)

        # Extract file paths
        file_paths = re.findall(file_path_pattern, string)
        result['file_paths'].extend(file_paths)

        # Extract email addresses
        email_addresses = re.findall(email_pattern, string)
        result['email_addresses'].extend(email_addresses)
        # rest = set(input_strings)

    return result


def run_strings_command(f):
    printdbg(f"BEFORE: run_strings_command - {f} ") #, dbg=True)
    process = subprocess.Popen(['strings', '-n', '10', f],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    printdbg(f"returncode={process.returncode}, output={type(output)}")
    if process.returncode != 0:
        print(f"Error running strings command: {error.decode()}")
    else:
        printdbg(output.decode())
        return output.decode()

# Example usage:

def get_input_strings(f):
    """ """
    printdbg(f"BEFORE: get_input_strings - {f} ") # , dbg=True)
    strings = run_strings_command(f)
    printdbg(f"AFTER: get_input_strings - {strings} ") #, dbg=True)
    return strings

def main():
    # Example usage:
    with open(f"{sys.argv[1]}") as f:
        files = [l[:-1] for l in f.readlines()]
    printdbg(f"files={files}") # , dbg=True) # 
    results = []
    for f in files:
        printdbg(f)
        input_strings = get_input_strings(f)
        if input_strings != None and len(input_strings) > 0:
            input_strings = input_strings.split('\n')
            printdbg(f"FINISHED get_input_strings({f})={len(input_strings)}, {type(input_strings)}")
            result = extract_urls_file_paths_and_email_addresses(input_strings)
            results.append({"data_source" :  f, "strings" : input_strings, "other" : result})
    print(json.dumps(results, indent=4))
    if True:
        with open(f"data.json", "w") as f:
            json.dump(results, f)

if __name__ == '__main__':
    main()
