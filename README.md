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

# Database Design
To design a production-grade database setup for microservices using MongoDB in the given case study, we need to consider factors like scalability, security, high availability, and manageability. Below is a proposal outlining key action items for the implementation:

### Proposal for Database Setup for Microservices with MongoDB

1. **Managed Cloud Database Service:**
   Consider using a managed cloud database service like MongoDB Atlas for both test and production environments. MongoDB Atlas provides automatic backups, scaling, monitoring, security features, and eliminates the need for manual maintenance.

2. **MongoDB Replica Set for High Availability:**
   Deploy a MongoDB Replica Set for both test and production environments. A Replica Set provides automatic failover, ensuring high availability in case of primary node failures.

3. **Data Isolation with Separate Databases:**
   Set up separate MongoDB databases for each environment (test and production). This ensures data isolation and avoids potential data interference between environments.

4. **ReadWrite Access in Test, ReadOnly Access in Production:**
   Create separate MongoDB users with read-write access for developers in the test environment and read-only access for applications in the production environment. This ensures that developers can test and modify data in the test environment while maintaining data integrity in production.

5. **Implement Role-Based Access Control (RBAC):**
   Utilize MongoDB's built-in Role-Based Access Control to manage access rights for different users and applications efficiently. Assign roles and permissions based on the specific needs of each microservice.

6. **Secret Management:**
   Use a secure secret management solution (e.g., HashiCorp Vault) to store sensitive MongoDB credentials and connection strings. This prevents exposure of credentials in code repositories or configuration files.

7. **Provisioning and Configuration Management:**
   Utilize Infrastructure-as-Code (IaC) tools like Terraform or Kubernetes Helm charts for provisioning and managing the MongoDB Replica Set and databases. Store configuration files in version control to track changes.

8. **Centralized Monitoring and Alerting:**
   Set up centralized monitoring and alerting for both test and production MongoDB environments. Use tools like MongoDB Cloud Manager or Prometheus and Grafana to monitor key metrics, detect performance issues, and set up alerting rules.

9. **Automated Backups and Disaster Recovery:**
   Configure automated backups for both environments to ensure data recoverability in case of data loss or corruption. Implement a disaster recovery plan to handle catastrophic failures.

10. **Continuous Integration and Deployment (CI/CD) Pipelines:**
    Integrate the database provisioning and configuration steps into the CI/CD pipelines for seamless deployments. This helps ensure consistency and automates the setup process.

11. **Regular Performance Tuning and Maintenance:**
    Schedule regular performance tuning and maintenance tasks to optimize MongoDB performance. Monitor query performance and address bottlenecks proactively.

12. **Horizontal Scaling with Sharding (If Required):**
    If the microservices generate significant data and need horizontal scaling, consider implementing sharding to distribute data across multiple MongoDB nodes for improved query performance.

By following these key action items, the proposed MongoDB database setup will provide a robust and scalable solution for microservices in both test and production environments. These measures ensure that the databases are secure, isolated, and efficiently managed, meeting the needs of modern microservices deployments in a production-grade environment.

## Author

- Created by Zia
- GitHub: [Your GitHub Username](https://github.com/ZiaUrRehman786)

## License

This project is licensed under the [MIT License](LICENSE).

---