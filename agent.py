from phi.agent import Agent
# from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k
from dotenv import load_dotenv
import streamlit as st
import os 
from phi.model.google import Gemini


from knowledge_base import AgentKnowledge


load_dotenv()
st.title("Search Bar with phi agent")
input_text = st.text_input("Search")

gemini_api_key = os.getenv("GOOGLE_API_KEY")

def load_knowledge():
    knowledge = {}
    try:
        with open("info.txt", "r", encoding="utf-8") as file:
            for line in file:
                key, value = line.strip().split(": ")
                knowledge[key] = value
    except Exception as e:
        st.error(f"Error loading knowledge base: {e}")
    return knowledge

knowledge_data = load_knowledge()
knowledge_base = AgentKnowledge(data=knowledge_data)

agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    markdown=True,
    tools=[DuckDuckGo(), Newspaper4k()],
    description="You are a senior NYT researcher writing an article on a topic.",
    instructions=[
        "For a given topic, search for the top 5 links.",
        "Then read each URL and extract the article text, if a URL isn't available, ignore it.",
        "Analyse and prepare an NYT worthy article based on the information.",
    ],
    knowledge_base=knowledge_base.kb,
    search_knowledge=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    
)
if input_text:
    response = agent.run(input_text).content
    st.write(response)


