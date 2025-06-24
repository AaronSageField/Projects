# CRM Tagging Utility (Desktop GUI)

This lightweight Python application allows users to apply tags in bulk to CRM records via API with a minimal, single-screen interface. Built to support teams with no IT infrastructure, the tool simplifies a previously manual, multi-hour process into a one-click workflow.

## Overview

Due to limitations in the CRM's API (no bulk endpoint, no GUI), staff previously had to apply tags individually through the platform. This tool automates the process with a focus on:

- Minimal user input: one tag, one button
- Support for both Client and Lead record types
- Compatibility with manually exported CRM data

## Features

- Record type selection (Client / Lead)
- Free-text tag entry field
- Paste-in support using a text file (`records.txt`)
- Scrolled output field for status and error messages
- Input validation to ensure format compatibility with the CRM’s API
- Graceful handling of missing files and bad inputs

## How It Works

1. **Paste Record IDs**
   - Open `records.txt`
   - Paste CRM record IDs in the following format:  
     `"id1", "id2", "id3"`
   - Save and close the file

2. **Run the Application**
   - Launch the script via Python (`python remote_crm_tagging.py`)

3. **Use the GUI**
   - Choose record type: `Client` or `Lead`
   - Enter the tag name exactly as it exists in the CRM
   - Click **Apply Now**

4. **Review Output**
   - The bottom text window will show:
     - Status codes
     - Any API error messages
     - Which IDs were processed successfully

## Requirements

- Python 3.6+
- Internet access to reach the CRM API
- Valid API credentials (update `api_token` and `base_url` in the script)
- pip install requests

## Deployment Notes

- This tool is designed for operational teams with minimal technical background.
- It requires no installation, but assumes access to Python and basic file navigation.
- For teams unfamiliar with filesystem structure, a shortcut to `records.txt` and the script may be pinned in a shared folder (e.g., OneDrive).

## Limitations

- Does not create tags or workflows in the CRM; those must already exist
- Assumes all records in `records.txt` belong to the selected type
- No progress bar (output is printed to the console window)

## Next Steps

This tool was developed to address a narrow but high-friction process. Future plans may include:

- Adding drag-and-drop support for importing IDs
- Dropdown for recently used tags

---

