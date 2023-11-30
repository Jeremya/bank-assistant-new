from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import AstraDB as LCAstraDB
from langchain.embeddings import OpenAIEmbeddings


def initialize_memory():
    return ConversationBufferMemory(memory_key="chat_history", return_messages=True)


def initialize_astradb(config):
    embeddings = OpenAIEmbeddings(openai_api_key=config['OPENAI_API_KEY'], model="text-embedding-ada-002")
    return LCAstraDB(
        embedding=embeddings,
        collection_name=config['ASTRA_DB_COLLECTION'],
        api_endpoint=config['ASTRA_DB_API_ENDPOINT'],
        token=config['ASTRA_DB_APPLICATION_TOKEN']
    )
