import os
import streamlit as st
from config import OPENAI_API_KEY
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# STEP 1: Setup Streamlit Page
st.set_page_config(page_title="CloudNova AI Assistant")
st.title("CloudNova AI Web Assistant")
st.write("Ask Anything to our CloudNova AI Assistant")

user_input = st.text_input("Please feel free to ask your question here")

# STEP 2: Configure LLM (The Brain)
llm = OpenAI(
    api_key=OPENAI_API_KEY,
    api_base="https://openrouter.ai/api/v1",
    model="openai/gpt-4o-mini",
    temperature=0
)

# STEP 3: Configure Embeddings (The Translator)
embed_model = OpenAIEmbedding(
    api_key=OPENAI_API_KEY,
    api_base="https://openrouter.ai/api/v1",
    model="openai/text-embedding-3-small"
)

# STEP 4: Set Global Settings
Settings.llm = llm
Settings.embed_model = embed_model
Settings.chunk_size = 800
Settings.chunk_overlap = 150

# STEP 5: Load Documents
folder_path = os.path.dirname(os.path.abspath(__file__))

documents = SimpleDirectoryReader(
    input_dir = folder_path,
    required_exts = [".txt"]
).load_data()

# STEP 6: Create Vector Index
index = VectorStoreIndex.from_documents(documents)

# STEP 7: Create Query Engine with System Prompt
SYSTEM_PROMPT = """You are the official AI assistant for CloudNova CRM.

Your responsibilities:
- Answer questions about CloudNova products and services
- Help users navigate CRM features
- Provide onboarding guidance
- Explain pricing and plans
- Assist with troubleshooting based on documentation

Rules:
- Only answer based on CloudNova documentation provided in the context
- If the question is not related to CloudNova CRM or cannot be answered from the context, politely say: "I'm sorry! I don't have idea about that. Please contact to CloudNova Support Team."
- Do not claim CloudNova is a real operating company
- Do not provide legal, financial, or medical advice
- Maintain a professional and friendly tone
- If user says "exit" or "goodbye" then says "Thank you! Have a great day!"
"""

query_engine = index.as_query_engine(
    similarity_top_k=3,
    system_prompt=SYSTEM_PROMPT
)

# STEP 8: Answer User Question
if user_input:
    with st.spinner("Getting the Information"):
        response = query_engine.query(user_input)
        st.write(str(response))