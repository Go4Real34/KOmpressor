<div align="center">
  <img src="Resources/gifs(.gif)/project_banner.gif" alt="Project Banner">

  <p align="center">
    <img alt="GitHub all releases" src="https://img.shields.io/github/downloads/Go4Real34/KOmpressor/total?style=flat&logo=GitHub&label=Downloads" style="margin-right: 5px;">
    <img alt="GitHub last commit (by committer)" src="https://img.shields.io/github/last-commit/Go4Real34/KOmpressor?display_timestamp=committer" style="margin-right: 5px;">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Go4Real34/KOmpressor" style="margin-right: 5px;">
    <img alt="GitHub" src="https://img.shields.io/github/license/Go4Real34/KOmpressor">
  </p>
</div>

# KOmpressor
**_FFMPEG Based Web & Console Video Compression Tool with Next Gen Codecs (H.264, H.265, VP9, AV1) \
by Görkem Sarıkaya & Taha Berk Kuyruk for Computer Engineering III, Engineering Project III Course, 
3rd Year Project at Beykoz University (Istanbul, Turkey)_**


# Needed Installations for Windows 11
- **FFMPEG Version:** [5.1.2 Full Build for Windows 11](https://github.com/GyanD/codexffmpeg/releases/tag/5.1.2).
- **Python Version:** [3.11.3 for Windows 11](https://www.python.org/downloads/release/python-3113/).
- **WinRAR Version:** [6.22 for Windows 11](https://www.win-rar.com/download.html?&L=5)


# Installations
  ## Python Installation for Windows 11
  - Download the Python with `version '3.11.3'`.
  - Run the downloaded file.
  - Follow the instructions on the installation screen and complete installation.
    - Adding Python Path to the environment variables in the installation may be needed.
    - Not tested but can result in some errors especially for background processes and callbacks.

  ## WinRAR Installation for Windows 11
  - Download the WinRAR with `version '6.22'`.
  - Run the downloaded file.
  - Follow the instructions on the installation screen and complete installation.

  ## FFMPEG Installation for Windows 11
  - Download the FFMPEG with `version '5.1.2 Full Build'`.
  - Extract the ZIP file with using WinRAR.
    - Install WinRAR using the steps above if you did not.
    - After installing;
      - Right-click to the file.
      - Hover over `Show More Options`.
      - Hover over `WinRAR`.
      - Click to `Extract to "ffmpeg-5.1.2-full_build\"`.
      - You have successfully extracted the file.
  - After extracting the files to the folder, copy the path of the folder to a preferred location for you applications.
    - For simplicity, you can do the following steps that guarantee it to work;
      - Double click to the extracted folder once.
      - Rename it as `ffmpeg`.
      - Copy the folder and navigate to `C:` and paste it.


- After doing all installation operations;
  - Open your Windows Search Bar and type `Environment Variables`.
  - Click on the `Environment Variables` button that is bottom right of the opened window. 
  - For both User & System Variables tabs, find `Path` entry and open it by double-clicking on it or selecting it and clicking `Edit`.
  - Check that Python paths are there successfully. You should confirm that the following two entries exists in the following order;
    - `C:\{path_to_python}\Python311\Scripts`
    - `C:\{path_to_python}\Python311`
  - After that click `New` and paste the `ffmpeg\bin` path as new entry.
    - Example;
      - If you did the steps above, and extracted the files to `C:\ffmpeg`;
        - Add, `C:\ffmpeg\bin` to the PATH variable as the new entry.
      - After adding it, hit Enter on your keyboard and click 'OK' to every window you opened to close them.
  - After closing all windows, restart your computers for all these things to take effect.
  - After your computer opened again;
    - Open a command prompt (cmd).
    - Type `python --version`.
      - If you see the version number on the console output, that means you have successfully installed Python.
    - Type `ffmpeg -version`.
      - If you see the version number, that means you have successfully installed FFMPEG.
    - If you couldn't get right console output for any of them, try revert your changes back (delete files, uninstall, remove 
      variables from `Path`) and do the steps again or follow the instruction on the official websites of 
      [Python](https://www.python.org/downloads/) and [FFMPEG](https://ffmpeg.org/).

> Since the project is done in Windows 11, I don't specifically know how to install both FFMPEG & Python for the older version 
  of Windows, Linux, macOS or other operating systems. I did my best to make it easy for you to install them at least for 
  Windows 11.\
> If you still have any problems with the installation, as I said, definitely check official websites for solutions.\
> Thank you for your understanding.


# Preparation, Usage & Deletion
- Install Python, WinRAR and FFMPEG with the steps above if you don't have them or haven't done the steps.


- Download the project from `Code -> Download ZIP` and extract files or clone it in command the prompt.\
  ```git clone https://github.com/Go4Real34/KOmpressor.git```


- If you are using an IDE;
  - Create a virtual environment using your IDE.

  - Then, activate it and install the required packages with the following command via console or go and find them in your 
    IDE tabs if any exists.\
    ```.\venv\Scripts\activate```\
    ```pip install -r requirements.txt```
  
  - Finally, run the file named `KOmpressor.py` Python file that is under `KOmpressor` folder.
    - **_Note:_** If you want, you can run the files individually, this file just makes it easier to reach them both at once.

- If you are using the command prompt;
  - Go to the location of the project.\
    ```cd KOmpressor```
  
  - Run the following commands to create a virtual environment and activate it;
    - Create the virtual environment.\
      ```python -m venv venv```,
    
    - Activate the virtual environment.\
      ```.\venv\Scripts\activate```

  - After activating it, you should see a `(venv)` text at the start of the command line or if you changed its name 
    (2nd 'venv' in command above), you should see that name.
  
  - Then, install the required packages with the command via console:\
    ```pip install -r requirements.txt```
  
  - Finally, run the `KOmpressor.py` Python file with the following command:\
    ```python KOmpressor.py```
    - **_Note:_** If you want, you can run the files individually, this file just makes it easier to reach them both at once.\
    ```python ProjectFiles/console_compressor.py```\
    ```python ProjectFiles/web_compressor.py```
  
And you should be good to go.

- After your work is done with the project you can directly close the command prompt or; if you want to delete something, right-clicking 
  on it and deleting will be enough for the process.


- But if you want to clean it from the console, do the following steps.
  - First, deactivate the virtual environment.\
  ```deactivate```
  
  - Then, decide what you are going to delete.
    - If you are going to delete the virtual environment only for some problem use the following command.\
      ```rmdir /s /q venv``` (for 'venv', put your virtual environment's name if you have changed it.)
    
    - But if you want to completely get rid of the project itself, you can go back one directory and delete the project 
      folder completely by executing the following commands:
        - First go back one directory.\
          ```cd ..```
        
        - Then remove the project folder completely.\
          ```rmdir /s /q KOmpressor```


# Quick Explanation About How The Tools Work
## **_Start_**
  - Firstly, you select which version you are going to use from the menu.

## **_Console Tool_**
  - If you use console command, it will continue with the same command prompt.
  - After you enter a command (or multiple commands if you entered '1' instead of '0' on the menu), it is split into keywords 
    in a function and passes it to another function as a list. In that function, a setting dictionary that holds all the setting data
    is created with these keywords. That settings dictionary is passed to command creator function. In this function each settings' FFMPEG 
    command is created with the corresponding FFMPEG flags. After all commands are created, all these commands returned as a list and passed 
    to the executor function. In this function, in a for loop, all commands taken by this function and this function executes them 
    one by one and while executing, it returns progress continuously and that is printed to the console. After all render(s) 
    are finished, output folder is opened with your operating system's file handler and operation finishes.

## **_Web Tool_**
  - If you use web version, it will be started on your local computer at address 'http://127.0.0.1:5000' as default, and 
    even it is different, or you changed the host address and port; it will be printed to console by the package functions automatically. 
    Copying and pasting the address to your browser is enough to reach upload page.
  - Then you select a video to upload and press 'Continue' button to go to the video settings page.
  - After reaching the video settings page, you enter the settings however you want and press 'Compress' button to start rendering process.
  - Upon clicking on the 'Compress' button, all the input value objects are saved as a dictionary form and passed to a function. In 
    this function, since some of the input objects, like checkboxes, can be left untouched resulting in no key about it in the 
    dictionary; these keys are checked and added with default values. After that, this settings dictionary passed to another 
    function that creates Command Console Tool command. Then, this command passed to the same function in the console tool. Rest 
    of the process is the same as the console tool after this process. After render is finished, you can;
    - Save the video by pressing 'Save Video' button,
    
    - Reset the settings by pressing 'Reset Video Settings' and do another configuration with the same uploaded and selected video 
      - **_Note:_** _You need to press 'Compress' after doing new settings to render it again after resetting them with this button. Sometimes they are
        not registered so, restarting the website completely from scratch will solve the problem temporarily. Please check `Known Issues` section
        (end of the file) for details._ or,
    
    - Return back to the upload page by clicking 'Return Back to Upload Page' to do another configuration with another video.


# Project Media
> For both console & web examples, all settings are set as the same of each other.\
> Settings are given in the following table.

|              **_Setting_**               |       **_Value_**       |
|:----------------------------------------:|:-----------------------:|
|               _Resolution_               | `640x360 (360p) (16:9)` |
|                _Bitrate_                 |       `2048 kbps`       |
|              _Output Codec_              |         `H264`          |
|             _Output Format_              |         `.mp4`          |
|        _FPS (Frames Per Second)_         |          `10`           |
|     _Maximum File Size Compression_      |        `Enabled`        |
|           _Maximum File Size_            |         `50 MB`         |
|            _CRF Compression_             |        `Enabled`        |
|               _CRF value_                |          `30`           |
| Maximum Percentage File Size Compression |        `Enabled`        |
|      _Maximum percentage file size_      |          `60%`          |
|              _Speed Change_              |        `Enabled`        |
|              _Speed Ratio_               |          `2.5`          |
|             _Volume Change_              |        `Enabled`        |
|              _Volume Ratio_              |     `0 (0%) (Mute)`     |
|             _Cut Operation_              |        `Enabled`        |
|               _Cut Start_                |        `Enabled`        |
|             _Cut Start Time_             |      `60. second`       |
|                _Cut End_                 |        `Enabled`        |
|              _Cut End Time_              |      `120. second`      |
|            _Horizontal Flip_             |        `Enabled`        |
|             _Vertical Flip_              |        `Enabled`        |
|              _Rotate Side_               |       `Clockwise`       |
|              _Rotate Angle_              |       `30 degree`       |

### Be aware of I/O Structure (no spaces in file names or paths)

**Console Tool Command Example:** `COMPRESS ProjectFiles/TestIO/Inputs/input.mp4 ProjectFiles/TestIO/Outputs/output.mp4 640x360 2048 H264 .mp4 10 1 50 1 30 1 60 1 2.5 1 0 1 60 120 1 1 1 CW 30`

- Check `Known Issues` section (end of the file) for details.

## Input Video Frame Example
![Input Video Frame Example](Resources/images(.png)/input_video_frame_example.png)

## Output Video Frame Example
![Output Video Frame Example](Resources/images(.png)/output_video_frame_example.png)

## Full Menu
![Full Menu](Resources/images(.png)/full_menu.png)

## Console Output Flag Names
![Console Output Flag Names](Resources/images(.png)/console_output_flag_names.png)

## Web Console Output
![Web Console Output](Resources/images(.png)/web_console_output.png)

## Web Upload Page Idle
![Web Upload Page Idle](Resources/images(.png)/web_upload_page_idle.png)

## Web Upload Page Uploading
![Web Upload Page Uploading](Resources/images(.png)/web_upload_page_uploading.png)

## Web Upload Page Uploaded
![Web Upload Page Uploaded](Resources/images(.png)/web_upload_page_uploaded.png)

## Web Upload Page Selected
![Web Upload Page Selected](Resources/images(.png)/web_upload_page_selected.png)

## Web Video Settings Page
![Web Video Settings Page](Resources/images(.png)/web_video_settings_page.png)

## Web Video Settings Page Processing
![Web Video Settings Page Processing](Resources/images(.png)/web_video_settings_page_processing.png)

## Web Video Settings Page Preview
![Web Video Settings Page Preview](Resources/images(.png)/web_video_settings_page_preview.png)


# Known Issues
- This section will be updated whenever a bug is discovered or fixed.

### **_Console Tool_**
> 1. If you enter a command that has a file name or path that has a space in it, it will not work due 
     to the keywords are generated by splitting the entered line with spaces. For now, please prefer using a file path 
     that does not contain any spaces in it. There is a location for it that will be created at the first run and, 
     it is named as `ProjectFiles/TestIO`, then `Inputs` for input videos and `Outputs` for output videos followed by 
     the video name. Don't forget to copy & paste your video files to the location `ProjectFiles/TestIO/Inputs` or your 
     desired location before writing the command.

### **_Web Tool_**
> 1. If you upload a video, then select to upload another video again and exit without selecting any video (or canceling it); 
     after selecting  a video and clicking on 'Continue' button will result in a force page restart & refresh that will cause 
     all videos to be  uploaded again to show up on the upload page again. This is probably caused because of the way I save 
     the current selected file name to a file named `current_video.txt` by overwriting instead of appending.
> 2. If you upload multiple videos, and select one of them; only the last one is selected even though you select another. 
     This is again probably because of me saving the file by just overwriting to each other instead of appending to the file.
> 3. While rendering, there is no handling about disabling buttons so, all the buttons can be spammed resulting in slowing 
     down the computer, browser and rendering and addition to these; since while a render being processed it is written to 
     a temporary file named (temp.mp4) so, spamming it make this file overwritten and resulting in corruption of the video.
     For now, it is recommended to wait until the render is finished.
> 4. After a valid render, 'Save Video' will save the video to just `Downloads` folder. There is no option to select a 
     specific folder to save the video file and the video file is also saved with the same name as the input file.
> 5. After a valid render, pressing 'Reset Video Settings' will reset the page state but even after some setting is changed, 
     these changed settings sometimes cannot be captured, resulting in a render with the same settings as the last render.
> 6. Without doing anything, just after uploading a video and seeing the settings page, unless you fill 'Width', 'Height, 
     'Bitrate' and 'FPS' boxes, you cannot render a video.
> 7. All buttons are active at start. 'Reset Video Settings' and 'Return Back to Upload Page' doesn't affect the beginning 
     state of the page but since they are also connected to the same for as all buttons do, they cannot be work properly unless 
     the boxes in #6 are filled.
> 8. No multiple video can be selected to render at once like in the command tool.


# License
 - The project is licensed under MIT License. If you want to use it, please check the [LICENSE](LICENSE.txt) file. 
 - Referencing to the project & author (as "Görkem 'Go4Real34' Sarıkaya") is enough for any reason.


### Feel free to use the project, make suggestions if you have any or report bugs maybe with their fixes if you found any.

# Thank you for using our KOmpressor Tool.