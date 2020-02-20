from __future__ import print_function
import sys

if not (sys.version_info > (3, 0)):
    print("Uh oh! It looks like you're running an old version of Python. Python 2 is no longer supported, please install Python 3 instead.")
    sys.exit(0)

try:
    import fuzzywuzzy
    import pandas
except ImportError:
    print("Uh oh! It looks like you didn't install the required modules. Run the following command to install them.\n\n\t\033[1mpip -r requirements.txt\033[0m")
    sys.exit(0)
