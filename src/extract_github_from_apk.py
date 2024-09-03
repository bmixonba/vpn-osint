import os
import zipfile
import csv
import re
import sys
import pandas as pd

def extract_apk(apk_path, extract_to):
    with zipfile.ZipFile(apk_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def search_github_links(directory):
    github_links = []
    github_regex = re.compile(r'[https?://]*github\.com/[a-zA-Z0-9_\-]+/[a-zA-Z0-9_\-]+')
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    links = github_regex.findall(content)
                    for link in links:
                        github_links.append((file, link))
            except:
                continue
    return github_links

def analyze_apks(top_level_directory, output_csv):
    temp_extract_dir = 'temp_extracted'
    result = []
    print(f"analyze_apks(tld={top_level_directory}, o={output_csv}")
    for root, dirs, files in os.walk(top_level_directory):
        if False:
            print(f"analyze_apks(root={root}, len(dirs)={len(dirs)}, len(files)={len(files)}")
        for file in files:
            if False:
                print(f"analyze_apks(root={root}, len(dirs)={len(dirs)}, len(files)={len(files)}")
            if file.endswith('.apk'):
                print(f"analyze_apks= root={root}, file={file}")
                apk_path = os.path.join(root, file)
                extract_path = os.path.join(temp_extract_dir, file)
                os.makedirs(extract_path, exist_ok=True)

                extract_apk(apk_path, extract_path)
                links = search_github_links(extract_path)

                for file_containing_link, link in links:
                    result.append((file, file_containing_link, link))

                # Clean up extracted files
                for cleanup_root, cleanup_dirs, cleanup_files in os.walk(extract_path, topdown=False):
                    for name in cleanup_files:
                        os.remove(os.path.join(cleanup_root, name))
                    for name in cleanup_dirs:
                        os.rmdir(os.path.join(cleanup_root, name))
    result = pd.DataFrame(result)
    result.columns = ['APK Name', 'File Containing Link', 'GitHub Repository Link']
    result.drop_duplicates(inplace=True)
    result.to_csv(output_csv)

def main():
    if len(sys.argv) <= 1:
        # apk_directory = '/home/conntrack/git/vpn-osint/apks/MaliciousApks'
        apk_directory = '/home/conntrack/git/vpn-osint/apks'
    else:
        apk_directory = sys.argv[1] 
    output_csv = 'github_links.1.csv'
    analyze_apks(apk_directory, output_csv)

# Example usage
if __name__ == '__main__':
    main()
