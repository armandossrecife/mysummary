#!/bin/bash

# Define the base URL (replace if needed)
base_url="https://raw.githubusercontent.com/armandossrecife/mysummary/refs/heads/main/pdfs/"

# Loop through each URL and download the file
for url in "$base_url"d{1..27}.pdf; do
  # Extract filename from URL
  filename=$(basename "$url")

  # Download the file with progress bar
  wget -O "$filename" -q --show-progress "$url"

  # Check for download success (optional)
  if [[ $? -eq 0 ]]; then
    echo "Downloaded: $filename"
  else
    echo "Error downloading: $filename"
  fi
done

echo "Download complete!"