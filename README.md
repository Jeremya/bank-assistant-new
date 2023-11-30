# bank-assistant-bot
Bank Assistant chat bot using LLM and AstraDB

This assistant is an adaptation of the [Bank Assistant](https://github.com/Jeremya/bank-assistant-bot) built on [AstraPy](https://github.com/datastax/astrapy)

It is using OpenAI to build embeddings and Astra to store the data.

## Pre-requisites

- Python 3.6+
- Launch an [AstraDB](https://astra.datastax.com/) database or use [Chroma](https://www.trychroma.com/)

## Setup

- Clone the repository
- Install the dependencies using `pip install -r requirements.txt`
- Add your Astra info and OpenAI token in `.env` file. (first, rename `.env.template` to `.env`)
- Run `loader.py` to import fake clients data in your Astra db collection from `resources/clients-dataset.csv`
- Run `main.py` using the command `streamlit run main.py`