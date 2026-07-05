from dotenv import load_dotenv
import os

from smolagents import CodeAgent, LiteLLMModel

# Load environment variables
load_dotenv()

# Find available datasets
DATA_DIR = "data"

datasets = "\n".join(
    f"- {file}"
    for file in os.listdir(DATA_DIR)
    if file.endswith(".csv")
)

# Initialize model
model = LiteLLMModel(
    model_id="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
)

# Create agent
agent = CodeAgent(
    tools=[],
    model=model,
    additional_authorized_imports=["pandas"],
)

# System context
context = f"""
You are an AI Data Analyst.

The CSV files available inside the data folder are:

{datasets}

Whenever required, write Python code using pandas to analyze these datasets.

The datasets are located inside the folder:

data/

Return concise, accurate answers.
"""

print("=" * 60)
print("📊 AI Data Analyst")
print("Type 'exit' to quit.")
print("=" * 60)

# Chat loop
while True:

    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    prompt = context + "\n\nUser Question:\n" + question

    answer = agent.run(prompt)

    print("\nAnswer:")
    print(answer)