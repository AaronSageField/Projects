# User Guide – Medicare Agent Analytics Tool (MVP)

**Version:** 1.0  
**Last Updated:** [Insert Date]  
**Created by:** [Your Name]

---

## Overview

The **Medicare Agent Analytics Tool** is a lightweight, GUI-based application that consolidates, cleans, and analyzes Medicare Book of Business and Commission Statement reports from four carriers: Aetna, Devoted, Humana, and UHC.

Designed for use in lean agency environments without dedicated data infrastructure, this tool provides leadership with the ability to validate commission payments, track client retention, and investigate suspicious or inconsistent data over time.

---

## Intended Users

- Agency executives (e.g., CEO)  
- Operations managers  
- Data analysts supporting business oversight  

---

## Feature Summary

| Feature           | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| Generate Snapshot| Consolidates Book of Business reports into a standardized data point.       |
| Generate CCS     | Merges Commission Statement reports into a raw format for analysis.          |
| View Analytics   | Opens a browser dashboard with trends, KPIs, and a correlation metric.       |
| Compare Data     | Diffs two snapshot data points and outputs all row-level differences.        |
| Help             | Provides usage guidance and carrier report requirements.                     |

---

## Folder Structure

The tool creates and manages the following directories automatically:

- `Reports/` – Input folder for downloaded carrier files  
- `Snapshots/` – Output folder for editable `.xlsx` files  
- `Program Data/` – Internal folder for versioned backup data points (no file extension)  

---

## Required Inputs

The user must manually download reports from each carrier’s vendor portal and place them into the `Reports/` folder. No formatting is necessary.

| Carrier  | Book of Business | Commission Statement |
|----------|------------------|----------------------|
| Aetna    | Required         | Required             |
| Devoted  | Required         | Not yet supported    |
| Humana   | Required         | Required             |
| UHC      | Required         | Required             |

---

## Instructions for Use

### Launching the Tool

1. Double-click the `LAUNCH.bat` file.  
2. The GUI will appear with a process log terminal on the right-hand side.

### Step 1: Generate Data Points

- **Generate Snapshot**:  
  - Scans the `Reports/` folder for Book of Business reports.  
  - Cleans and merges them into a `.xlsx` file saved in `Snapshots/`.  
  - Saves a backup copy (without extension) in `Program Data/`.

- **Generate CCS**:  
  - Performs the same process for Commission Statement files.  
  - CCS data is not deduplicated but is prepared for analysis.

If a required file is missing or malformed, the terminal will identify the issue and stop the process safely.

### Step 2: View Analytics

Click `View Analytics` to open a browser dashboard. The dashboard displays:

- All-time average retention rate  
- All-time average commission delta  
- Pearson correlation coefficient (between the two metrics)  
- Line graph showing delta trends over time  
- Tables listing snapshot and CCS data by date, sum, and change

### Step 3: Compare Data Points

Click `Compare Data` to select any two snapshot backups from the `Program Data/` folder. The tool will output a list of all differences between them in the terminal window.

Use this feature to investigate unusual shifts in client or payment data.

---

## Internal Logic

- **Deduplication**: Snapshot data is deduplicated and standardized across carriers.  
- **Column Structuring**: Policy data is stored using dynamic suffixes (e.g., `carrier_1`, `product_1`).  
- **CCS Normalization**: Commission data is processed directly for statistical analysis, not modified.  
- **Correlation**: Statistical analysis uses Pearson’s r to assess the relationship between retention and commissions over time.  

---

## Troubleshooting and Error Handling

| Problem                        | Resolution                                                |
|-------------------------------|-----------------------------------------------------------|
| Tool does not launch          | Ensure Python is installed. Use `LAUNCH.bat` to restart. |
| Permission denied errors      | Run the tool as Administrator.                           |
| Missing or wrong carrier files| Ensure correct files are downloaded into `Reports/`.      |
| Unexpected or blank results   | Check source data; contact developer if problem persists. |

All major errors are caught and reported in the terminal. When an issue occurs, the tool will stop operations and clean up incomplete files automatically.

---

## System Requirements

The following Python packages are required. The tool checks for them on launch and installs any missing packages automatically:

- `pandas`  
- `openpyxl`  
- `scipy`  
- `win32com`  

The tool is designed for Windows 11 and does not require administrative installation or third-party databases.

---

## Future Features

- Addition of Devoted to the CCS workflow (pending fix to carrier report format)  
- Improved error messaging and flagging of data anomalies  
- Exportable change logs for snapshot comparisons  

---

## Notes

- This is a minimum viable product (MVP) and has not undergone formal QA.  
- Users should not alter or delete files in the `Program Data/` directory.  
- `.xlsx` outputs in `Snapshots/` are provided for convenience and can be modified for ad hoc reporting.  

---

