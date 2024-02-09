# Delete Key Vault Script

This script allows you to delete an Azure Key Vault using the Azure SDK for Python.

## Prerequisites

Before running the script, ensure you have the following:

- An Azure subscription.
- Python installed on your machine.
- Azure CLI installed (for setting up credentials).

## Installation

Install the required Python packages using pip:

```bash
pip install azure-identity azure-mgmt-keyvault
```

## Usage

1. **Clone this repository** to your local machine:

    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the directory** containing the script:

    ```bash
    cd <repository-directory>
    ```

3. **Set up your Azure credentials** using Azure CLI:

    ```bash
    az login
    ```

4. **Run the script** by executing the following command:

    ```bash
    python delete.py
    ```

Replace `<repository-url>` and `<repository-directory>` with the URL and directory name of your Git repository where the `delete.py` script is located.

