import subprocess
from pymongo import MongoClient

def lock_secondary_node_backup(connection_string):
    # Connect to the MongoDB cluster using the provided connection string
    client = MongoClient(connection_string)

    # Get the admin database
    admin_db = client.admin

    # Lock the database to make a consistent snapshot
    admin_db.command("fsyncLock")

    # Get the list of secondary node hostnames from the connection string
    secondary_nodes = client.nodes

    for hostname in secondary_nodes:
        # Run the make-vm-snapshot command to take a VM snapshot
        snapshot_command = f"make-vm-snapshot {hostname}"
        subprocess.run(snapshot_command, shell=True, check=True)

    # Unlock the database
    admin_db.command("fsyncUnlock")

    # Close the MongoDB connection
    client.close()

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python your_script.py \"mongodb://admin:password@vm-hostname1,vm-hostname2,vm-hostname3/admin?otherParams\"")
        sys.exit(1)

    connection_string = sys.argv[1]
    lock_secondary_node_backup(connection_string)
