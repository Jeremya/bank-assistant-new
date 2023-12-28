from langchain.tools import BaseTool

from dotenv import dotenv_values

from astradb_session import initialize_astradb

# Load configurations
config = dotenv_values('.env')

# Initialize AstraDB
vstore = initialize_astradb(config)

### Client Similarity Tool Astra #########
class ClientSimilarityTool(BaseTool):
    name = "Client Similarity Tool"
    description = "This tool is used to search for client information like balance, credit score, has a credit card, " \
                  "gender, surname, location, point earned and satisfaction score. " \
                  "Note this does not contains user names or emails." \
                  "Example query: what is the top 3 client in alabama ranked by credit score?"

    def _run(self, user_question):
        print(user_question)
        client_list = vstore.similarity_search(user_question, k=5)

        return client_list

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")



