Log Parsing and Visualization Project:

This project involves parsing log files, extracting relevant data, and visualizing it through various graphs using Python. The log files may contain various types of log entries, including basic logs, JSON logs, and Base64-encoded logs. The goal of this project is to process these logs, perform analysis, and generate insightful visualizations such as action counts, action distributions, and logs over time.


  Before running the code, make sure you have the following installed:
  
->Python 3.x: You can download and install Python from the official website: python.org.

->Required Python Libraries:
                        pandas,
                        matplotlib,
                        seaborn,
                        json,
                        re .

To install the required libraries, run the following command in your terminal:

->pip install pandas matplotlib seaborn

Project Files

1. Log Parsing Code (log_parser.py)
   
This Python script reads log files, processes each log entry (including Base64 decoding), and stores the extracted data into a structured format (CSV or Excel).

Input: Log file in .log format.

Output: Parsed data stored in a CSV file (parsed_log_output.csv).

How to Run:
Place your log file in the same directory as the script or provide the file path in the code.
Run the script with the following command:
->python log_parser.py


2. Log Visualization Code (log_visualization.py)

This script uses the parsed data (in CSV format) to generate visualizations like action counts, action distributions, and logs over time using Matplotlib and Seaborn.

Input: Parsed CSV file (parsed_log_output.csv).

Output: Visualizations saved as an image (combined_visualizations.png).

How to Run:
After running log_parser.py, you will have a CSV file ready for visualization.
Run the script with the following command:

->python log_visualization.py

This will create and save visualizations as an image in the specified path.




How to Run the Entire Process:

Step 1: Install Python and required libraries as mentioned above.

Step 2: Run the log parsing script (log_parser.py) to parse the log data.

Step 3: Generate visualizations by running the log visualization script (log_visualization.py).


File Structure

/my_project
    ├── assessment.log 
    ├── log_parser.py             
    ├── log_visualization.py       
    ├── parsed_log_output.csv      
    ├── combined_visualizations.png 
    ├──README.md                  




Example Log File


An example log file (assessment.log) is expected to contain entries in different formats, such as:

Basic Log Format:

2024-11-01T12:30:00.123 user=John ip=192.168.1.1 action=login

JSON Log Format:

{"timestamp": "2024-11-01T12:30:00.123", "user": "John", "ip": "192.168.1.1", "action": "login"}

Base64 Encoded Log Format:

BASE64:eyJ0aW1lc3RhbXAiOiAiMjAyNC0xMS0wMVQxMjowMzowMy4xMjM5MCIsICJ1c2VyIjogIkpvaG4iLCAiaXAiOiAiMTkyLjE2OC4xLjEiLCAiYWN0aW9uIjogImxvZ2luIn0=

