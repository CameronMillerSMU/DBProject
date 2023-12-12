# Installation and User Manual
**Project Group 7:** Zakiya Caldwell, Morgan Glover, David Jiang, Cameron Miller

## Installation Manual:  

List of things to install: **Python IDE, MySQL, pip or Conda, mysql.connector, tkinter** 

1) For Python 

    * Download Python Installer: 

        * Go to the Python Downloads page. 

        * Download the latest version of Python for Windows. 
        
    * Run the Installer: 

        * Execute the downloaded installer (e.g., python-3.x.x-amd64.exe). 

        * Check the box that says "Add Python to PATH" during installation. 

    * Customize Installation (Optional): 

        * You can customize the installation by clicking on the "Customize installation" button. 

        * Ensure that the checkbox for "pip" and "Add Python to environment variables" is selected. 

    * Install Python: 

        * Click "Install Now" to start the installation process. 

        * The installer will install Python and set up the environment variables. 

    * Verify Installation: 

        * Open a command prompt. 

        * Type python --version or python -V and press Enter. You should see the installed Python version. 

2) For MySQL  

    * Download MySQL Installer: 

        * Go to the MySQL Downloads page. 

        * Download the MySQL Installer for Windows. 

    * Run the Installer: 

        * Execute the downloaded installer (e.g., mysql-installer-web-community-8.x.xx.xx.msi). 

        * Choose the "Developer Default" setup type for a standard installation. 

    * Installation Wizard: 

        * Follow the installation wizard, which will guide you through the process. 

        * Set up a MySQL Server instance and configure a root password. 

    * Installation Complete: 

        * Once the installation is complete, MySQL Server and other tools will be installed on your system. 

3) For pip or Conda 

    * Both pip and conda are package managers used in the Python ecosystem for managing and installing software packages, libraries, and dependencies. 

    * For most python 3, pip is included with the IDE installation. 

        * Example: python -m pip install <package_name> 

    * For Conda 

        * Download the Miniconda installer for Windows: 

            * Visit the Miniconda Downloads page. 

            * Download the installer for the right platform. 

        * Run the installer: 

            * Execute the downloaded installer (e.g., Miniconda3-latest-Windows-x86_64.exe). 

            * Follow the installation prompts. 

            * Choose to add Miniconda to your system PATH during installation. 

        * Example: conda install <package_name> 

4) For mysql.connector 

    * If you are using pip. 

        * pip install mysql-connector-python 

    * If you are using conda. 

        * conda activate <your_environment_name> 

        * conda install -c anaconda mysql-connector-python 

5) For tkinter 

    * If you are using pip. 

        * pip install tk 

    * If you are using conda. 

        * conda activate <your_environment_name> 

        * conda install -c conda-forge tk 

## User Manual: 

1) Install all necessary packages. 

2) Boot up your choice of Python IDE. 

3) Run the file ‘gui.py’, a window will pop up with the name “Database GUI”.  

4) When first running the program, only two action are given, Entry or Query.  

5) Click on the action you want to perform and a drop down will be given.  

6) Depending which option is picked, a number of text box will be given. 

7) Fill out all the requested input and press Execute 

    a.  For Entry, a message will be displayed under the Execute. It will either be success or failed, 

    b.  For Query, a message with the input query and a responds from the database will be displayed under the Execute. If query not found, a message will also display with an explanation.  