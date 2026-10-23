# Internet Speed Test Logger

About the Project

Internet Speed Test Logger is a Python-based application that measures internet download speed, upload speed, and ping. It also saves test results in a CSV file so users can review their internet speed history later.

# Features

- Test internet download speed
- Test internet upload speed
- Measure ping latency
- Display a speed test report
- Save results with date and time
- Store history in a CSV file
- View previous speed test results
- Menu-driven interface

# Technologies Used

- Python
- "speedtest-cli"
- CSV File Handling
- "datetime"
- "os"

# Requirements

- Python 3.x
- Active internet connection
- "speedtest-cli" library

# Installation

Install the required library using:

pip install speedtest-cli

# How to Run

1. Download or clone this repository.
2. Open the project folder in your terminal.
3. Run the Python file:

python InternetSpeedLogger.py

4. Select an option from the menu.

# Menu Options

Option| Description
1| Test Internet Speed
2| View Speed History
3| Exit

# Output Information

The application displays:

- Download speed in Mbps
- Upload speed in Mbps
- Ping in milliseconds
- Date and time of the test

# Data Storage

Test results are stored in "speed_history.csv". The file contains the test date, download speed, upload speed, and ping.

The CSV file is created automatically when the first speed test is completed.

# Project Structure

Internet-Speed-Test-Logger/
├── InternetSpeedLogger.py
├── speed_history.csv
└── README.md

The "speed_history.csv" file is generated automatically by the program.

# Learning Objectives

This project helps beginners practice:

- Python functions
- External library installation
- Exception handling
- CSV file operations
- Date and time handling
- Working with internet speed test results

# Limitations

- An active internet connection is required.
- Speed test results may vary depending on network conditions and the selected server.
- The "speedtest-cli" library may not work in every mobile Python environment.

# Future Improvements

- Display speed history as a graph
- Calculate average download and upload speeds
- Export reports with additional statistics
- Add automatic periodic speed tests
- Create a graphical user interface

# Author

Ayush Singh

GitHub: https://github.com/ayush893singh

License

This project is available for educational and personal use.
