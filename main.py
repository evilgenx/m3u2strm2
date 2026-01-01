import tools
import logger
import streamClasses
import wget
import sys
import os
import re

def is_url(string):
    """Check if the input string is a URL"""
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url_pattern.match(string) is not None

def process_local_m3u(file_path):
    """Process a local M3U file directly"""
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return False
    
    print(f"Processing local M3U file: {file_path}")
    stream_list = streamClasses.rawStreamList(file_path)
    return True

def process_url_m3u(base_url):
    """Process M3U files from a URL (original functionality)"""
    # Ensure m3u directory exists
    if not os.path.exists('m3u'):
        os.makedirs('m3u')
        print("Created 'm3u' directory")
    
    for i in range(1, 10):
        url = base_url + '/tvshows/' + str(i)
        filename = os.path.join('m3u', f'collection{i}')
        try:
            downloaded_file = wget.download(url, filename)
            print(f"\nDownloaded: {downloaded_file}")
            stream_list = streamClasses.rawStreamList(downloaded_file)
        except Exception as e:
            print(f"\nError downloading {url}: {e}")
            continue

    url = base_url + '/movies/'
    filename = os.path.join('m3u', 'movies')
    try:
        downloaded_file = wget.download(url, filename)
        print(f"\nDownloaded: {downloaded_file}")
        stream_list = streamClasses.rawStreamList(downloaded_file)
    except Exception as e:
        print(f"\nError downloading {url}: {e}")

def main(input_path=None):
    """Main function that handles both local files and URLs"""
    if input_path is None:
        print("Usage: python main.py <m3u_file_path_or_url>")
        print("Examples:")
        print("  python main.py ./ptgold.m3u          # Process local file")
        print("  python main.py http://example.com/   # Download from URL")
        return

    if is_url(input_path):
        print(f"Detected URL: {input_path}")
        process_url_m3u(input_path)
    else:
        # Assume it's a local file path
        process_local_m3u(input_path)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
    print('done')
    sys.exit()
