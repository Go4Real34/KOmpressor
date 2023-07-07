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

# **_Latest Version: [v1.0.0.0] - 2023-07-07_**

<br>

# **_Change Log History_**

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