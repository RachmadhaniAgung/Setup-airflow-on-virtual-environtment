# Project Description
## 1. Setup-airflow-on-virtual-environtment :
```
    Install Apache Airflow
    Install the Python package manager, and virtual environment :
    $ sudo apt-get install -y python3-pip python3-venv

    Create a new project directory :
    $ mkdir airflow-project

    Change to the directory :
    $ cd airflow-project

    Create a new virtual environment :
    $ python3 -m venv airflow-env

    ctivate the virtual environment :
    $ source airflow-env/bin/activate
    Your terminal prompt should change as below:
    (airflow-env) user@example:~/airflow-project$

    Using pip, install Airflow:
    $ pip install apache-airflow

    Initialize a new SQLite database to create the Airflow meta-store that 
    Airflow needs to run:
    $ airflow db init
    Output:
    ...
    DB: sqlite:////root/airflow/airflow.db
    [2023-02-05 17:08:48,821] {migration.py:205} INFO Context impl 
    SQLiteImpl.
    [2023-02-05 17:08:48,822] {migration.py:208} INFO - Will assume 
    non-transactional DDL.
    INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
    INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
    INFO  [alembic.runtime.migration] Running stamp_revision  -> ***
    WARNI [Airflow.models.crypto] empty cryptography key - values will not 
    be stored encrypted.
    Initialization done

    Create the administrative user and password used to access Airflow :
    $ airflow users create --role Admin --username admin --email admin 
    --firstname admin --lastname admin --password my-password

    Using nohup, start the Airflow scheduler to run in the background. 
    Airflow appends the output of running the scheduler to the scheduler.
    log file :
    $ airflow scheduler

    The Scheduler command starts the Airflow scheduler, queues, and runs 
    the workflows defined in the DAG code.

    Start the Airflow web server & Arflow scheculer in terminal local :
    $ airflow scheduler
    $ airflow webserver -p 8080
```
## 2. Create DAG CSV To JSON To CSV :
    - Membuat File .py pada directory dag yang tersedia.
    - Didalam file .py yang sudah anda buat, lakukan struktural seperti berikut: 
        1. Membuat proses penginputan file. 
        2. Membuat def atau definisi fungsi untuk membaca file. 
        3. Menentukan argumen default dari airflow DAG, untuk menentukan 
        parameter umum.
        4.Membuat DAG dan komponen DAG seperti (Nama DAG, Task, & Nama Task).
            1. untuk mengeksekusi callable python dalam DAG.
            2. untuk membuat peryataan bash menggunakan fungsi python dan 
            tersedia pada airflow.
            3. untuk urutan task.
