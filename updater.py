
# Title                 : PIP Package Updater v1.0
# Description           : Update all installed pip-packages
# Author                : Tobias Menzel
# Date                  : 09.10.2018
# Modified              : 01.04.2021
# Notes                 : Only for PIP Versions >= 10.0.1
# Tested:               : Python 3.7 or higher 
# ==========================================================================================

# Module dependencies
from subprocess import call
import pkg_resources

# Main function


def main():
    """ Get all packages and update"""
    packages = [dist.project_name for dist in pkg_resources.working_set]
    call("pip install --upgrade " + ' '.join(packages), shell=True)


# ===============================
#        APPLICATION START
# ===============================


if __name__ == "__main__":
    main()
