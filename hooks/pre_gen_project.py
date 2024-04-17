import re
import sys


PACKAGE_PATTERN = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

package_name = "{{ cookiecutter.package_name }}"

if not re.match(PACKAGE_PATTERN, package_name):
    print(f"ERROR: The package name ({package_name}) is not a valid Python package name. "
          f"Package names should start with a letter or underscore and be composed entirely "
          f"of letters, digits, and/or underscores.")

    # exit to cancel recipe
    sys.exit(1)
