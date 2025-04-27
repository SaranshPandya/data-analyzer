# Data Analyzer

**Data Analyzer** is a Python-based tool that leverages AI agents to analyze data from PostgreSQL databases. It provides an interactive command-line interface for querying and exploring database data, using powerful libraries  `LangChain` for AI-driven insights.  
This tool is ideal for developers, data analysts, and researchers who need to extract meaningful information from databases using natural language queries.

## Features
>**Note** All processing is performed locally on your machine, with the exception of AI model inference, which is executed remotely via Google's Gemini API.
- Connects to PostgreSQL databases for seamless data access.
- Uses AI agents (powered by Google's Gemini model) to analyze and interpret data.
- Interactive command-line interface for entering queries and receiving insights.
- Built with Python 3.11, pandas, LangChain, and other modern libraries.

## Installation

### Prerequisites

- Python 3.11 or higher
- Poetry (version 1.7.1 or higher) for dependency management
- PostgreSQL database
- Gemini API Key for AI functionality

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/SaranshPandya/data-analyzer.git
    cd data-analyzer
    ```

2. Install dependencies using Poetry:
    ```bash
    poetry install
    ```

3. Ensure you have:
   - A PostgreSQL database
   - A Gemini API

## Usage

1. Activate the Poetry virtual environment:
    ```bash
    poetry shell
    ```

2. Run the main script:
    ```bash
    python src/main.py
    ```

3. Follow the prompts to:
    - Enter your PostgreSQL database parameters (e.g., user, host, database name, port, password)
    - Enter your Gemini API key
    - Input your data analysis queries (e.g., `"Summarize sales data by region"`)

4. Type `q` to exit the interactive session.

### Build a Docker Image
```bash
docker build -t data-analyzer:latest .
```

### Run the Docker Image
```bash
docker run -it data-analyzer:latest
```

> **Note**: Adding support for more models, including local ones, is definitely on the roadmap.

> **Note**: Enhancing agent performance with LangGraph is currently in active development.
