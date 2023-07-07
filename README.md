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
  - Run the file named `console_compressor.py` Python file that is under `ProjectFiles` folder (create a configuration 
    with Python Interpreter if needed. I used PyCharm to do this project it both works with a configuration or selecting `Current File` as the run option.).


- If you are using the command prompt;
  - Go to the location of the project.\
    ```cd KOmpressor```
  
  - Then, run the `console_compressor.py` Python file inside ProjectFiles folder with `python` command.\
    ```python ProjectFiles\console_compressor.py```

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

> **_Note:_** There is no need to create a virtual environment for now so, I did not include a virtual environment installation in this version.


# Quick Explanation About How The Tool Works
- After you enter a command (or multiple commands if you entered '1' instead of '0' on the menu), it is split into keywords 
  in a function and passes it to another function as a list. In that function, a setting dictionary that holds all the setting data
  is created with these keywords. That settings dictionary is passed to command creator function. In this function each settings' FFMPEG 
  command is created with the corresponding FFMPEG flags. After all commands are created, all these commands returned as a list and passed 
  to the executor function. In this function, in a for loop, all commands taken by this function and this function executes them 
  one by one and while executing, it returns progress continuously and that is printed to the console. After all render(s) 
  are finished, output folder is opened with your operating system's file handler and operation finishes.

# Project Media
> Settings are given in the following table for the console version.

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

## Console Output Flag Names
![Console Output Flag Names](Resources/images(.png)/console_output_flag_names.png)


# Known Issues
- This section will be updated whenever a bug is discovered or fixed.

> 1. If you enter a command that has a file name or path that has a space in it, it will not work due 
     to the keywords are generated by splitting the entered line with spaces. For now, please prefer using a file path 
     that does not contain any spaces in it. There is a location for it that will be created at the first run and, 
     it is named as `ProjectFiles/TestIO`, then `Inputs` for input videos and `Outputs` for output videos followed by 
     the video name. Don't forget to copy & paste your video files to the location `ProjectFiles/TestIO/Inputs` or your 
     desired location before writing the command.


# License
 - The project is licensed under MIT License. If you want to use it, please check the [LICENSE](LICENSE.txt) file. 
 - Referencing to the project & author (as "Görkem 'Go4Real34' Sarıkaya") is enough for any reason.


### Feel free to use the project, make suggestions if you have any or report bugs maybe with their fixes if you found any.

# Thank you for using our KOmpressor Tool.