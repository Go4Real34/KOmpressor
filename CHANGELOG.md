# Change Log

All notable changes to this project will be documented in this file.\
The version format given as following.

> # [vX.Y.Z.W] - YYYY-MM-DD
> - Explanations
> 
> ### **_Additions_**
> - Any new features about the project.
> 
> ### **_Changes_**
> - Any changes about project.
> 
> ### **_Fixes_**
> - Any bug fixes about the project.
> 
> ### **_Deletions_**
> - Any deleted features about the project.
>
> ## **_Version Increment & Time Format_**
> #### - X: Major Change.
> #### - Y: New Feature.
> #### - Z: Bug Fix.
> #### - W: No Change in the Project
> #### - YYYY-MM-DD: Date of release (Year - Month - Day)

# **_Latest Version: [v1.2.0.1] - 2023-07-07_**

<br>

# **_Change Log History_**

# [v1.2.0.1] - 2023-07-07
- Updated README.md file.

### **_Additions_**
- **_Resources_**
  - **_'gifs(.gif)' Folder_**
    - Added with a gif that contains an animation of project banner.

### **_Changes_**
- **_Documentation_**
  - **_README.md_**
    - Animated project logo and banner are added.
    - Some [shields.io](https://shields.io) badges (4) (download count, last commit, repository size and license) are added.
  
  - **_CHANGELOG.md_**
      - Added new changes about **_[v1.2.0.1]_**.

### **_Fixes_**
 - No fixes were made.

### **_Deletions_**
- No deletions were made.

<br>

# [v1.2.0.0] - 2023-07-07
- Created menu for the project to navigate between functionalities.

### **_Additions_**
- **_Project Files_**
  - **_KOmpressor.py:_** The main start point of the menu version of the project. Functions handle folder creation, start 
    the console or web server depending on the user selection.


- **_Resources_**
  - **_'images(.png)' Folder_**
    - Added an image (1) that is used in the [README.md](README.md) file in `Project Media` section.

### **_Changes_**
- **_Project Files_**
  - **_extra_functions.py_**
    - Added code content for `KOmpressor` in `handle_first_run` function.


- **_Documentation_**
  - **_README.md_**
    - Added extra explanations about combined version in `Preparation, Usage & Deletion`, `Quick Explanation About How The Tools Work` and 
      `Project Media` sections.
  
  - **_CHANGELOG.md_**
    - Added new changes about **_[v1.2.0.0]_**.

  - **_.gitignore_**
    - Added a new folder (1) to ignore.

### **_Fixes_**
 - No fixes were made.

### **_Deletions_**
- No deletions were made.

<br>

# [v1.1.0.0] - 2023-07-07
- Created web version of the FFMPEG based compressor.

### **_Additions_**
- **_Project Files_**
  - **_web_compressor.py_**
    - The main start point of the web version of the project. Functions handle folder creation, start 
      the web server and include all redirection function for the web page.
  
  - **_web_handling.py_**
    - Includes the functions to handle web form. Functions fills missing keys and create a dictionary 
      before passing this dictionary to the console functions. 
      commands.
  
  - **_upload_page.html_**
    - Includes all HTML, CSS and JS code for the upload page. This page is the main entry page of the 
      web version. Make available to save uploaded videos and redirect to the video settings page.
  
  - **_video_settings.html_**
    - Includes all HTML, CSS and JS code for the video settings page. This page is reached after 
      uploading and selecting a video to proceed and contains all video render, save and reset operations.
  
  - **_upload.php_**
    - Includes PHP code to handle the upload process. This file is used to hold data of the video on upload 
      process to the server.
  
  - **_requirements.txt_**
    - Includes needed packages to run the project. This file is used by `pip` to install the packages 
      automatically.


- **_Resources_**
  - **_'images(.png)' Folder_**
    - Added images (8) that are used in the [README.md](README.md) file in `Project Media` section.

### **_Changes_**
- **_Project Files_**
  - **_console_compressor.py_**
    - Passed argument to the `handle_first_run` function.
  
  - **_render_handling.py_**
    - Added arguments to `run_renders` function for web version references and used them to pass 
      into the `update_progress` function.
    - Added a code block that determines the current stage number depending on `command2` to pass into 
      `update_progress` function.

  -  **_extra_functions.py_**
    - Added argument to the `handle_first_run` function and changed its code content to handle both 
       versions depending on the given argument.
    - Added arguments to the `update_progress` function and added a code block that connects to a SocketIO 
      connection and send a data about the progress using these and extra arguments.


- **_Documentation_**
  - **_README.md_**
    - Added extra explanations about web version in `Preparation, Usage & Deletion`, `Quick Explanation About How The Tools Work`,
      `Project Media` and `Known Issues` sections.
  
  - **_CHANGELOG.md_**
    - Added new changes about **_[v1.1.0.0]_**.

  - **_.gitignore_**
    - Added a new file (1) and a folder (1) to ignore.

### **_Fixes_**
 - No fixes were made.

### **_Deletions_**
- No deletions were made.

<br>

# [v1.0.0.0] - 2023-07-07
- First release of the project.
- Created console version of the FFMPEG based compressor.

### **_Additions_**
- **_Project Files_**
  - **_console_compressor.py_**
    - The main start point of the console command version of the project. Handles folder 
      creation, renders the video and opens the output folder.
  
  - **_render_handling.py_**
    - Includes function to handle render processes. Functions create corresponding FFMPEG commands 
      depending on the given setting dictionary, execute them while printing the progress to console.
  
  - **_input_handling.py_**
    - Includes functions to handle input. Functions create settings dictionary corresponding to 
      user input by passing arguments to each other.
  
  - **_extra_functions.py_**
    - Includes handy functions for the project. Functions were repeated in multiple files so, they 
      are moved to this file to prevent code repetition.


- **_Documentations_**
  - **_README.md_**
    - This file will be used to give information about the project and also includes quick explanations 
      about installation and run.
  
  - **_CHANGELOG.md_**
    - This file will be used to keep track of changes. Currently, includes **_[v1.0.0.0]_** version changes.
  
  - **_LICENSE.txt_**
    - This project is licenced with MIT License. The project is free to use everyone. When used, 
      referencing the project & author (as "Görkem 'Go4Real34' Sarıkaya") is enough for any reason.
  
  - **_.gitignore_**
    - This file includes the excluded folders and files from the project. It is used to prevent
    unnecessary files to be uploaded to the repository. Currently includes a file (1) and multiple folders (6).


- **_Resources_**
  - **_'images(.png)' Folder_**
    - Includes images (3) that are used in the [README.md](README.md) file in the `Project Media` section.

### **_Changes_**
- No changes were made.

### **_Fixes_**
 - No fixes were made.

### **_Deletions_**
- No deletions were made.