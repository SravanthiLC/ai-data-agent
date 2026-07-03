from dotenv import load_dotenv
import os
from smolagents import CodeAgent, LiteLLMModel
from tools import list_csv_files

load_dotenv()

model = LiteLLMModel(
    model_id="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
)

agent = CodeAgent(
    tools=[list_csv_files],
    model=model,
)

print(agent.run("What CSV files are available?"))