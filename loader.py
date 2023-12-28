from dotenv import dotenv_values

from langchain.document_loaders import CSVLoader
from astradb_session import initialize_astradb


# Function to load config and initialize AstraDB
def load_and_insert_data(config_path, csv_path):
    config = dotenv_values(config_path)
    vstore = initialize_astradb(config)

    loader = CSVLoader(csv_path)
    vstore.add_documents(documents=loader.load())
    print("Inserted clients into Astra DB")


# Call the function with paths
load_and_insert_data('.env', 'resources/clients-dataset.csv')
