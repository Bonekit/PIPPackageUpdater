
# Title                 : PIP Package Updater v1.0
# Description           : PIP Package Updater v1.0
# Author                : Tobias Menzel
# Date                  : 09.10.2018
# Notes                 : Only for PIP Versions >= 10.0.1
# Python_version        : 3.7
# ==========================================================================================

# Import modules for the pip package updater.
from subprocess import call
import pkg_resources

# PIP Updater Function.


def main():
    packages = [dist.project_name for dist in pkg_resources.working_set]
    call("pip install --upgrade " + ' '.join(packages), shell=True)


# ===============================
#        APPLICATION START
# ===============================


if __name__ == "__main__":
    main()
