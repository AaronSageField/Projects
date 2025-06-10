Status: Work in Progress (WIP)


The MBOB (Merged Book of Business) Snapshot Generator is a Python-based desktop application designed to assist small Medicare agencies in managing and analyzing carrier book of business reports. Agents selling on behalf of multiple insurance carriers often receive reports in varying formats with inconsistent attributes, making it challenging to consolidate data for analytics. This tool automates the creation of a unified book of business snapshot, reducing manual effort and enabling data-driven insights without requiring a secure database or advanced technical expertise.
Built with a user-friendly Tkinter interface, the application processes reports from multiple carriers (e.g., UHC, Humana, Devoted, Cigna, Aetna), merges them into a standardized Excel snapshot, and provides functionality for calculating retention rates. Future enhancements will include snapshot comparison, CRM integration, and additional analytics features.
This project is a work in progress and is being developed to demonstrate my skills in Python, data processing, and UI development while addressing a real-world business problem. Feedback and contributions are welcome!
Features

Unified Snapshot Generation: Merges book of business reports from multiple carriers into a single, standardized Excel file with consistent attributes (e.g., member details, plan information).
Retention Rate Calculation: Analyzes historical snapshots to compute monthly and annual retention rates, saved as an Excel report.
User-Friendly Interface: Tkinter-based GUI with buttons for generating snapshots, consolidating commission statements (placeholder), and calculating retention rates, plus a log area for real-time feedback.
Data Validation: Checks for required reports and columns, providing clear error messages if data is missing or invalid.
File Management: Automatically creates necessary folders (Reports, Snapshots, Program Data) and handles various file formats (e.g., .xlsx, .csv).
Threaded Operations: Runs time-consuming tasks in background threads to keep the UI responsive.

Tech Stack

Python 3.8+
Libraries:
pandas and openpyxl for Excel data processing
tkinter for the graphical user interface
threading for asynchronous task execution


File Formats: Supports .xlsx, .xls, .csv, and .txt (with conversion to .xlsx)

Installation and Setup
Prerequisites

Python 3.8 or higher
pip (Python package manager)

Note: If no requirements.txt exists, install the required packages manually:
pip install pandas openpyxl

Prepare Input Files:

Place carrier book of business reports (e.g., .xlsx, .csv) in the Reports folder.
Ensure at least two of the following reports are present: UHC, Humana, Devoted, Cigna, or Aetna Book of Business.
The application will create Snapshots and Program Data folders if they don't exist.

Run the Application:
python ui.py

Usage:

Click Generate Snapshot to create a merged book of business snapshot.
Click Calculate Retention Rates to analyze historical snapshots and generate a retention report.
The Consolidate Commission Statements feature is a placeholder and not yet implemented.
Logs and errors are displayed in the UI's text area.

Project Structure
mbob-snapshot-generator/
├── ui.py                # Tkinter GUI and main application logic
├── business.py          # Core data processing and business logic
├── Reports/             # Input folder for carrier reports
├── Snapshots/           # Output folder for generated snapshots
└── Program Data/        # Storage for processed data files

Current Limitations

WIP Status: The project is under active development and not production-ready.
Commission Consolidation: The "Consolidate Commission Statements" feature is a placeholder and currently outputs a "Not available" message.
CRM Integration: Remote CRM updates are planned but not yet implemented.
Snapshot Comparison: Direct comparison of snapshots is a future feature.
Error Handling: While robust, edge cases (e.g., malformed files) may require additional validation.
Performance: Large reports may slow down processing; optimization is planned.

Future Plans

Snapshot Comparison: Add functionality to compare two snapshots and highlight changes (e.g., new/terminated policies).
CRM Integration: Enable remote updates to a CRM system using a single snapshot as the source of truth.
Enhanced Analytics: Introduce visualizations (e.g., retention trends, carrier distribution) within the UI.
File Format Support: Expand support for additional report formats and improve conversion reliability.
Performance Optimization: Optimize pandas operations for faster processing of large datasets.
Cross-Platform Testing: Ensure compatibility across Windows, macOS, and Linux.
Documentation: Add detailed user guides and developer documentation.

This project is a portfolio piece demonstrating my ability to solve real-world problems with Python and data processing. It is not intended for production use in its current state.
