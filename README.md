# Get Data DAG Documentation

This `get_data` DAG is designed to query new data daily via Open-Meteo. By default, the data will have a delay of 48 hours and include a 2-year historical archive. These settings can be adjusted in `data_utils.py`.

## Setup Instructions

### 1. Install Dependencies
1. Install the required libraries listed in `requirements.txt` in your Airflow environment.
2. The library versions in `requirements.txt` can be modified as needed.

### 2. Add DAG Files
1. Place both `data_utils.py` and `getdata.py` into the Airflow DAG folder.

### 3. Database Connection
- The `getdata.py` script is not yet connected to a database.
- To enable database integration, add a database connection module to the `save_data()` function in `data_utils.py`.

## Notes
- Ensure that the Airflow environment is properly configured before running the DAG.
- Adjust the settings in `data_utils.py` to meet your specific requirements.
