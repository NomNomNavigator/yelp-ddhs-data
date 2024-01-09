# script.py

from fetch_data import fetch_and_save_data
from data_processing import process_data

# Call the function for Wilmington, Delaware
fetch_and_save_data("Wilmington, Delaware")

# Call the function for Philadelphia
fetch_and_save_data("Philadelphia")

# Load data into Pandas DataFrame and perform additional processing
process_data("Wilmington, Delaware")
process_data("Philadelphia")