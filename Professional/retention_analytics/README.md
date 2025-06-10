# MBOB Snapshot Generator (Work in Progress)

The MBOB (Merged Book of Business) Snapshot Generator is a Python-based desktop application designed to help small Medicare agencies consolidate and analyze carrier book of business reports.

Independent agents who sell for multiple insurance carriers often receive data in varied formats with inconsistent attributes, making unified analytics difficult without custom tools or a secure database. This application streamlines the process by generating standardized Excel snapshots and performing basic retention analysis, all within a lightweight interface.

## Features

- **Unified Snapshot Generation**  
  Merges book of business reports from multiple carriers into a single, standardized Excel file. Supports reports from UHC, Humana, Devoted, Cigna, and Aetna.

- **Retention Rate Calculation**  
  Compares historical snapshots to calculate both monthly and annual retention rates, output as a structured Excel report.

- **User Interface (Tkinter)**  
  Simple desktop GUI with buttons to:
  - Generate merged snapshots
  - Calculate retention rates
  - (Placeholder) Consolidate commission statements  
  A scrollable log displays real-time processing feedback and errors.

- **Data Validation**  
  Checks for required reports and column structures. Provides clear feedback when data is missing or improperly formatted.

- **File and Folder Management**  
  Automatically creates and manages necessary folders:
  - `Reports/` for input files  
  - `Snapshots/` for merged output  
  - `Program Data/` for temporary and supporting files

- **Threaded Processing**  
  Background threads keep the UI responsive during long-running tasks.

## Tech Stack

- **Language**: Python 3.8+
- **Libraries**:
  - `pandas`, `openpyxl` – for data processing and Excel output
  - `tkinter` – for the GUI
  - `threading` – for responsive execution
- **Supported File Formats**:
  - `.xlsx`, `.xls`, `.csv`, `.txt`  
    All non-Excel formats are converted internally.

## Setup and Usage

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)

Install required libraries (if no `requirements.txt` is provided):

```bash
pip install pandas openpyxl
```

### Preparing Files

1. Place your carrier reports (e.g., `.xlsx`, `.csv`) in the `Reports/` folder.
2. Include at least two of the following: UHC, Humana, Devoted, Cigna, or Aetna book of business files.
3. The application will generate `Snapshots/` and `Program Data/` as needed.

### Running the Tool

Run the main interface:

```bash
python ui.py
```

### Workflow

- **Generate Snapshot**  
  Merges the available reports into a normalized format and saves to `Snapshots/`.

- **Calculate Retention Rates**  
  Compares the most recent and prior snapshots to compute retention statistics.

- **Consolidate Commission Statements**  
  Not yet implemented. Currently returns a placeholder message.

Progress and error messages are displayed in the GUI’s output area.

## Limitations

- **Work in Progress**  
  Not ready for production use. Designed for demonstration and prototyping.

- **Commission Consolidation**  
  Feature is unimplemented and currently disabled.

- **CRM Integration**  
  Planned future capability; not available in this version.

- **Snapshot Comparison**  
  Direct policy-level comparison between snapshots is planned but not yet built.

- **Error Handling**  
  Reasonably robust, but edge cases may still fail silently or return incorrect output.

- **Performance**  
  Large reports may slow down processing. Optimization is under consideration.

## Roadmap

- Snapshot comparison: highlight new, terminated, or updated policies
- CRM integration using the unified snapshot as the single source of truth
- In-app visual analytics (e.g., retention trends, carrier mix)
- Expanded file format support and conversion improvements
- Optimized performance for larger datasets
- Cross-platform testing (Windows/macOS/Linux)
- Comprehensive user and developer documentation

## About This Project

This tool is an ongoing personal project developed to demonstrate practical Python development, UI design, and real-world data handling — especially in constrained environments without secure databases or IT support. It is tailored to the needs of small agencies that rely on manual data management and need accessible automation tools.
