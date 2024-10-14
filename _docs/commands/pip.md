# **PIP Commands**

This guide outlines common PIP commands for managing Python packages.

- **Install package:**
    ```bash
    pip install package-name
    ```

    This command installs the specified Python package.

- **Create or update a requirements file:**
    ```bash
    pip freeze > requirements.txt
    ```

    This command generates a requirements.txt file containing a list of installed packages and their versions. You can use this file to recreate the environment or share package dependencies with others.

- **Attempt to upgrade all packages:**
    ```bash
    pip install --upgrade $(pip freeze | cut -d '=' -f 1)
    ```

    This command attempts to upgrade all installed packages to their latest versions. It first generates a list of currently installed packages (excluding their versions) using `pip freeze`, then attempts to upgrade them using `pip install --upgrade`.

- **Install specific package version:**
    ```bash
    pip install package-name==version
    ```

    This command installs a specific version of a package. Replace `package-name` with the name of the package and `version` with the desired version.

- **Uninstall package:**
    ```bash
    pip uninstall package-name
    ```

    This command uninstalls the specified package from the Python environment.

- **List installed packages:**
    ```bash
    pip list
    ```
