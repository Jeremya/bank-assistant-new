from dotenv import dotenv_values
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
import streamlit as st
from langchain_core.messages import SystemMessage

from tools import ClientSimilarityTool
from astradb_session import initialize_memory, initialize_astradb

# Load configurations
config = dotenv_values('.env')

# Initialize AstraDB
vstore = initialize_astradb(config)

# Initialize Tools
tools = [ClientSimilarityTool()]

# Initialize Memory
message_history = initialize_memory()

# Initialize Chat Model
llm = ChatOpenAI(openai_api_key=config['OPENAI_API_KEY'], temperature=0)

# Initialize System Message
system_message = SystemMessage(content="You are Bankflix, a sophisticated bank assistant, specialized in credit "
                                       "scores and currency transactions. With expert knowledge and precision, "
                                       "you are here to provide accurate information and solutions to banking "
                                       "queries.")

# Initialize Agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=message_history,
    agent_kwargs={
        "system_message": system_message.content
    }
)

# Streamlit UI
st.title("🏦 Bankflix, the future of banking 🏦")
st.header("Welcome dear bank employee!")
user_question = st.text_input('Ask a question here:')

if len(user_question) > 5:
    with st.spinner(text="In progress..."):
        response = agent.run(input=user_question)
        st.write(response)
