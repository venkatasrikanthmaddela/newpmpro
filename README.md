# newpmpro

# Install Python 2.7
  Go to https://www.python.org/download/releases/2.7/
  Choose the appropriate package
  # Note: for the windows users set python 2.7 exceutable path in your system environment variable path called PATH.

# Install PIP
  Follow the Instructions provided here https://pip.pypa.io/en/stable/installing/
  (or)
  Get the pip from https://bootstrap.pypa.io/get-pip.py and run " python get-pip.py "
  # Note: for the windows users set pip exceutable path in your system environment variable path called PATH.
  

# Steps to install django with virtualenv

 # install virtualenv with pip
    follow the http://pymote.readthedocs.io/en/latest/install/windows_virtualenv.html
    
 # clone your project and get requirements.txt
    . Get into your created virtualenv and excecute the following command
    . pip install -r "path/to/requirements.txt"
    . It Will install all your project dependencies
    . Now open your pycharm. go to -> File -> Settings -> Project Interpreter
    . In the top right corner add click on settings symbol and select add local.
    . Select the virtualenv path here. and locate your python excecutable. for reference, check the below example path for windows.
   # For eg: C:\srikanth\softwares\venvs\pmpro\Scripts\python.exe
    . Yeah..! All caught up :) Good to go. Now you are ready to run your django project from pycharm
   
   # NOTE: For Windows Users python-MYSQL-db error will be rasied frequently while installing the dependencies. please look into the            following link and follow the instructions over there. this will definetly help you to get ready your project.
     # URL : http://www.swegler.com/becky/blog/2011/09/14/python-django-mysql-on-windows-7-part-5-installing-mysql/
     
 
 # Good Luck.
   
    
 
