# Laptop-Charging-Notification
A Python script that monitors the charging status of your laptop and plays a sound when charging starts or stops. The script logs charging events to a file for review.
## Features
- Monitors battery charging status.
- Plays a sound when charging starts or stops.
- Logs charging events to a file with timestamps.
## Prerequisites
- Python 3.x
- Required Python libraries: -psutil
                             -playsound
## Installation
1.Clone the Repository:
```bash
git clone https://github.com/yourusername/laptop-charging-notification.git
cd laptop-charging-notification
```
2.Install Required Libraries:
```bash
pip install psutil playsound

```
3. Download Sound File:
-Ensure you have a sound file (e.g., charging_sound.wav) to be played when charging status changes. Place it in the project directory.

4.Configure Log File Path:
- Edit main.py to set the log_file and sound_file paths as needed.

  ## Usage
1.Run the Script:
```bash
python main.py

```
2. Convert to Executable (Optional):
- To run the script without displaying the Command Prompt window, you can convert it to an executable using PyInstaller:
  ```bash
pip install pyinstaller
pyinstaller --onefile main.py

```
-The executable will be located in the dist folder.
3.Create a Batch File to Run the Script Continuously in the backgroung:
-Create a batch file named run_charging_notification.bat in the project directory with the following content:
```bash
@echo off
python D:\projects\charge_sound\main.py
pause

```
- This batch file will execute the Python script and keep the Command Prompt window open for debugging
4. Add Batch File to Startup (Optional) For Windows Users Only:
To ensure the script runs automatically at startup, move the batch file or executable to the Startup folder:
-Press Win + R, type shell:startup, and press Enter.
-Place a shortcut to the run_charging_notification.bat file or the executable in this folder.
  
## Logging
The script logs charging events to log.txt in the project directory. Review this file for details on charging status changes.
## Troubleshooting
- Script Not Running: Ensure that Python is correctly installed and the required libraries are installed. Check if the script runs correctly from the Command Prompt.
- Sound Not Playing: Verify that the sound file path is correct and that the file is accessible. Ensure the sound file format is supported by the playsound library.
- Logs Not Updating: Check the log.txt file path and permissions. Ensure the script has write access to the log file.
- Batch File Not Executing: Verify the path in the batch file is correct. Ensure you have permissions to execute the file.
    


    
  
