The CRM Record Updater is a Python application with a graphical user interface (GUI) that allows users to apply tags to CRM records in bulk via an API. It reads record IDs from a records.txt file and applies specified tags to either Client or Lead records, enabling automated workflows remotely.
Features

GUI Interface: Built with Tkinter for easy record type selection and tag input.
Bulk Processing: Processes multiple record IDs from a records.txt file.
API Integration: Sends PATCH requests to a CRM API to update records with tags.
Error Handling: Validates input file format and displays API response errors.
Scalable Output: Displays detailed logs of API responses and errors in a scrollable text area.

Prerequisites

Python 3.6 or higher
Required Python packages (see requirements.txt)
A valid API token for the CRM system
Access to the CRM API endpoint

Installation

Clone or download this repository to your local machine.
Install the required Python packages by running:pip install -r requirements.txt


Ensure a records.txt file exists in the same directory as the script (see Input File Format below).

Input File Format
The program reads record IDs from a records.txt file. The file must contain a comma-separated list of record IDs enclosed in double quotes, e.g.:
"id1","id2","id3"

To generate this format from a CRM report in Excel, use the following formula:
=TEXTJOIN(", ", TRUE, CHAR(34) & A1:A9999 & CHAR(34))

Copy the output to records.txt.
Configuration
Update the following variables in remote_crm_tagging.py with your CRM API details:

self.api_token: Replace 'example' with your actual API token.
self.base_url: Replace 'example' with the CRM API endpoint URL.

Example:
self.api_token = 'your_actual_api_token'
self.base_url = 'https://api.yourcrm.com/v1/records'

Usage

Run the script:python remote_crm_tagging.py


The GUI will open:
Select the record type (Client or Lead).
Enter the desired tag in the "Tag" field (default is "Test").
Click "Apply Now" to process the updates.


View the results in the output text area, which shows the API response codes and any errors for each record ID.

Notes

If records.txt is missing, the program will create an empty one and prompt you to add record IDs.
Invalid record ID formats or API errors (e.g., HTTP 400/422 for invalid tags) will be displayed in red in the output area.
Ensure your API token and endpoint are correctly configured to avoid authentication errors.

Troubleshooting

FileNotFoundError: Ensure records.txt exists in the same directory as the script.
Invalid format in records.txt: Verify the file follows the required format ("id1","id2","id3").
API errors: Check the API token, endpoint URL, and network connectivity.
GUI issues: Ensure Tkinter is installed (included with standard Python installations).

Dependencies
See requirements.txt for a list of required Python packages.
