# Youtube_Download
A Python tool to Download Youtube Videos

# Installing Tool

To install this application follow the following instructions

Linux:
1. Install Python3 and Pip - Google It I don't have time to write this out 😂
3. Unzip the folder (See Instructions Below)
4. Change into the Directory ```cd Youtube-Download-main```
5. Install the requirements - ```pip install -r requirements.txt```
6. run the file! - ```python3 app.py```

Windows (GUI):
1. Install Python3 - This can be found in the Windows Store (Find instructions elsewhere on how to install.)
2. Install Pip
3. Unzip the folder (See Instructions Below)
4. Now you will need to open Powershell (Non-Admin.) Watch the video below to see how to do so:


https://github.com/OfficialJavaScript/Youtube-Download/assets/51689500/20f1ccdc-da9f-434b-88af-eb628b14342e


5. Run the command ```pip install -r requirements.txt```
6. Now you can either run the file using ```python3 app.py``` in the command line or you can just double click the file via the File Explorer.

# Unzip the Zip

Linux (CLI):
1. Change to the parent directory of the file (using ```cd``` or whatever)
2. ```apt-get install unzip```
3. ```unzip Youtube-Download-main.zip```

Windows (GUI):
1. Open your downloads folder
2. Find the file
3. Right click
4. Extract all
5. Press enter then proceed back to the earlier instructions to install

# Using the application
After doing the previous steps to be able to run the Python file, make sure it's running - It should put out something like this:

```
* Serving Flask app 'app'
* Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
* Restarting with stat
* Debugger is active!
```

This is a good sign, now you want to either go to http://127.0.0.1:5000 or localhost:5000 Both should work (Or just go to the address mentioned in your terminal.)

After navigating to that page you should be met with a nice web interface

Paste a Youtube link into the box, and press download - this process can take a while depending on internet speed and the length of the video.

# Future Updates
* Make logo load instantly (Well ASAP)
* Fix Progress Bar
* Maybe increase download speed
* Add an easier way to change the download location.
