# https://www.geeksforgeeks.org/python-pip/

import os
os.system("cls")
# Package refers to a distribution of Python code that includes one or more modules or libraries. These packages are typically published on the Python Package Index (PyPI) and can be easily installed using pip. Python packages may contain modules, sub-packages, and additional resources such as documentation and data files.

# pip install package_name
# pip install package_name==version
# pip show package_name

# Get a list of locally installed Python Modules using Python PIP
# pip list

# Uninstall Packages with Python PIP
# pip uninstall package_name

# Using Requirement files with Python PIP
# Let’s suppose you want more than one package then instead of installing each package manually, you can install all the modules in a single go. This can be done by creating a requirements.txt file. Let’s suppose the requirements.txt file looks like this:
# pip install -r requirements.txt

# Upgrading Packages with Python PIP
# pip install --user --upgrade package_name
# pip install --user --upgrade package_name==version