**Project Description**
Setup-airflow-on-virtual-environtment : 

Install Apache Airflow
Install the Python package manager, and virtual environment :
 $ sudo apt-get install -y python3-pip python3-venv

Create a new project directory :
 $ mkdir airflow-project

Change to the directory :
 $ cd airflow-project

Create a new virtual environment :
 $ python3 -m venv airflow-env

Activate the virtual environment :
 $ source airflow-env/bin/activate

Your terminal prompt should change as below:
 (airflow-env) user@example:~/airflow-project$

Using pip, install Airflow:
 $ pip install apache-airflow

Initialize a new SQLite database to create the Airflow meta-store that Airflow needs to run:
 $ airflow db init
Output:
 ...
 DB: sqlite:////root/airflow/airflow.db
 [2023-02-05 17:08:48,821] {migration.py:205} INFO - Context impl SQLiteImpl.
 [2023-02-05 17:08:48,822] {migration.py:208} INFO - Will assume non-transactional DDL.
 INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
 INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
 INFO  [alembic.runtime.migration] Running stamp_revision  -> ***
 WARNI [Airflow.models.crypto] empty cryptography key - values will not be stored encrypted.
 Initialization done

Create the administrative user and password used to access Airflow :
 $ airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password my-password

Using nohup, start the Airflow scheduler to run in the background. Airflow appends the output of running the scheduler to the scheduler.log file :
 $ nohup airflow scheduler > scheduler.log 2>&1 &

The Scheduler command starts the Airflow scheduler, queues, and runs the workflows defined in the DAG code.

Start the Airflow web server on port 8080:
$ nohup airflow webserver -p 8080 > webserver.log 2>&1 &