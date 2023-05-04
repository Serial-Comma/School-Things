import os
import subprocess
import time
import pychrome
import shutil

# Search for the Chrome executable in the system's PATH environment variable
chrome_path = shutil.which('chrome.exe')
if chrome_path is None:
    raise Exception('Chrome browser is not installed or not in the PATH.')

# Start Chrome with remote debugging enabled
subprocess.Popen([chrome_path, "--remote-debugging-port=9222"])

# Wait for Chrome to start up
time.sleep(3)

# Connect to the remote debugging interface
from pychrome import Chrome
chrome = Chrome(port=9222)

# Get the list of open tabs
tabs = chrome.list_tabs()

# Extract the URLs from the tabs
urls = [tab.url for tab in tabs]

# Write the URLs to a file in space-separated format
with open("saved_links.txt", "w") as f:
    f.write(" ".join(urls))

# Close the connection to Chrome
chrome.close_tab(chrome.get_tabs()[0]["id"])
chrome.close()
