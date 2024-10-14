# **VSCode Settings**

This guide outlines common VSCode settings for Python development, along with the requirement to install Python and Ruff.

**Note:** Before applying these settings, Python and Ruff must be installed on the system.

**Extensions Needed:**
- **Python**: Provides support for Python language features and tools.
- **Ruff**: A code formatter for Python that enforces PEP 8 style guide recommendations.

### create ``.vscode/settings.json`` in project root and add the json code below.

```json
{
"[python]": {
    // Automatically format the code when saving a file
    "editor.formatOnSave": true,
    // Configure code actions to perform on save
    "editor.codeActionsOnSave": {
        // Perform all available fixes on save
        "source.fixAll": "explicit",
        // Organize imports on save
        "source.organizeImports": "explicit",
    },
    // Set the default code formatter to Ruff, assuming it is installed
    "editor.defaultFormatter": "charliermarsh.ruff"
},
// Display a vertical ruler at column 88 to help maintain PEP 8 style guide recommendations
"editor.rulers": [88]
}
