import os
import pyentrp
from pyentrp.entropy import shannon_entropy
import argparse

def decompress_apk(apk_file):
    # Decompress APK using jadx
    jadx_cmd = f"/home/conntrack/cryptosluice/apks/bin/jadx -d output {apk_file}"
    os.system(jadx_cmd)

    # Get the decompiled directory path
    decompiled_dir = os.path.join(os.getcwd(), "output")

    return decompiled_dir

def calculate_entropy(directory):
    # Initialize entropy calculator
    

    # Calculate entropy for each file in the directory
    total_entropy = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                data = f.read()
                entropy_value = shannon_entropy(data)
                total_entropy += entropy_value

    return total_entropy

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='APK Decompression and Entropy Calculation')
    parser.add_argument('apk_file', help='Name of the Android APK file')
    args = parser.parse_args()

    apk_file = args.apk_file
    decompiled_dir = decompress_apk(apk_file)
    entropy_value = calculate_entropy(decompiled_dir)

    print(f"Entropy value for {apk_file}: {entropy_value:.4f}")
