# MongoDB Cluster Backup Script

## Introduction

This Python script allows you to take backups of a MongoDB cluster's secondary nodes in a consistent manner. It uses the `fsyncLock` and `fsyncUnlock` commands to lock the database during the backup process, ensuring data integrity. The script also makes use of the provided MongoDB connection string to connect to the cluster.

## Features

- Backup MongoDB secondary nodes with a single command.
- Utilizes the `pymongo` library to interact with MongoDB.
- Locks the database for consistent snapshots using `fsyncLock`.
- Unlocks the database after the backup using `fsyncUnlock`.
- Seamless integration with existing MongoDB deployments.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.x** installed on your system.

2. **Python Virtual Environment** (optional but recommended):
   - It's good practice to use Python virtual environments to isolate project dependencies.
   - To create a virtual environment, open your terminal/command prompt and run:

     ```bash
     python -m venv myenv
     ```

     Replace `myenv` with the desired name for your virtual environment.

   - Activate the virtual environment:

     **On Windows:**

     ```bash
     myenv\Scripts\activate
     ```

     **On macOS and Linux:**

     ```bash
     source myenv/bin/activate
     ```

   - With the virtual environment activated, any packages you install will be isolated to this project only.

3. **Dependencies (including pymongo)**:
   - If using virtual environment (recommended), ensure that it is activated before installing the dependencies.
   - To install the required packages (including pymongo with a specific version), run:

     ```bash
     pip install -r requirements.txt
     ```

     The `requirements.txt` file contains the necessary packages and versions. If pymongo version 3.12.0 is required, ensure it is specified in the `requirements.txt` file as `pymongo==3.12.0`.

## How to Use

1. Clone this repository to your local machine or download the `mongodb_backup.py` file.

2. Install the prerequisites as mentioned in the "Prerequisites" section.

3. Run the script using the following command:

   ```bash
   python mongodb_backup.py "mongodb://admin:password@vm-hostname1,vm-hostname2,vm-hostname3/admin?otherParams"
   ```

   Replace the provided MongoDB connection string with your actual connection details.

4. The script will lock the database, take backups of each secondary node using the specified `make-vm-snapshot` command, and then unlock the database.

## Important Note

- **Ensure that you have the correct permissions and credentials to access the MongoDB cluster and perform backups.**
- **Always verify the backup process on a test environment before using it in production.**

## Author

- Created by Zia
- GitHub: [Your GitHub Username](https://github.com/ZiaUrRehman786)

## License

This project is licensed under the [MIT License](LICENSE).

---