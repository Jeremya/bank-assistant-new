from langchain.tools import BaseTool

from dotenv import dotenv_values

from astradb_session import initialize_astradb

# Load configurations
config = dotenv_values('.env')

# Initialize AstraDB
vstore = initialize_astradb(config)

### TODO: Find a way to do a classic Cassandra query with LCAstraDB

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

# Get Client Information Tool Astra
# class GetClientInformationTool(BaseTool):
#     name = "Get Client Information"
#     description = "This tool will get the client information"
#
#     def _run(self, client_id):
#         query = f"SELECT client_id, surname, credit_score, location, gender, age, balance, has_credit_card, " \
#                 f"estimated_salary, satisfaction_score, card_type, point_earned FROM {ASTRA_KEYSPACE_NAME}.ClientById WHERE client_id = {client_id}"
#         rows = astraSession.execute(query)
#
#         client_list = []
#         for row in rows:
#             client_list.append({f"client id is {row.client_id}, current balance is {row.balance}, client's surname is {row.surname}, age is {row.age}, gender is {row.gender} , card type owned by client is {row.card_type}, credit score is {row.credit_score}, satisfaction score is {row.satisfaction_score}, point earned is {row.point_earned}, this client is located in {row.location}, client has a credit card is {row.has_credit_card}"})
#         return client_list
#
#     def _arun(self, query: str):
#         raise NotImplementedError("This tool does not support async")


