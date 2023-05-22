# Title                 : PIP Package Updater v1.1
# Description           : Update all installed pip-packages
# Author                : Tobias Menzel
# Date                  : 09.10.2018
# Modified              : 22.05.2023
# Notes                 : Only for PIP Versions >= 10.0.1
# Tested:               : Python 3.7 or higher 
# ==========================================================================================

# Module dependencies
import subprocess
import pkg_resources
import pip

# Main function
def main():
    """ Get all packages and update """
    packages = [dist.project_name for dist in pkg_resources.working_set]
    subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade'] + packages, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# ===============================
#        APPLICATION START
# ===============================

if __name__ == "__main__":
    main()
