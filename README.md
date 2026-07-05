# AI Data Agent

An AI-powered data analysis agent built using **smolagents** and **Google Gemini**.

The agent analyzes datasets using **Python code generation** instead of relying on hardcoded analysis functions. It can answer natural language questions about CSV datasets by dynamically generating and executing pandas code.

## Features

- Analyze CSV datasets using natural language
- Generates Python (pandas) code automatically
- Interactive command-line interface
- Built using `smolagents` CodeAgent
- Easily extensible to support SQL databases, Excel files, APIs, and log files

---

## Dataset

Download the Olist Brazilian E-Commerce dataset from Kaggle:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Extract the downloaded archive and copy the **9 CSV files** into:

```
ai-data-agent/data/
```

---

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/SravanthiLC/ai-data-agent.git
cd ai-data-agent
```

### 2. Create a virtual environment

```bash
sudo apt update
sudo apt install python3-venv

python -m venv v1
```

### 3. Activate the virtual environment

```bash
source v1/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Create a `.env` file in the project root.

```text
GEMINI_API_KEY=your_api_key_here
```

---

## Run the Agent

```bash
python src/test_agent.py
```

Example:

```
============================================================
📊 AI Data Analyst
Type 'exit' to quit.
============================================================

Ask a question:
```

Example questions:

- How many customer records are there?
- Which dataset contains customer information?
- How many columns are present in the orders dataset?
- Which state has the highest number of customers?

---

## Tech Stack

- Python
- smolagents
- Google Gemini
- pandas
- python-dotenv

---

## Future Improvements

- Support Excel files
- Support SQL databases
- Support log file analysis
- Automatic report generation
- Data visualizations
- RAG integration for documentation