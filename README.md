# AI-Powered CLI Summarizer Tool

This project is a **command-line interface (CLI) tool** that leverages a **large language model (LLM)** (via Amazon Bedrock) to **automatically summarize `.txt` files** dropped into a monitored directory.

When you add a `.txt` file to the `input/` folder, a summary is automatically generated and saved under the `summaries/` folder with the same name suffixed by `_summary.txt`.

---

## Use Cases

- Automated meeting or lecture note summarization
- Real-time content simplification or compression
- Drop-folder automation for editorial pipelines
- Hands-free summarization assistant for journalists and researchers

---

## Folder Structure

```bash
AIPoweredCliTool/
├── input/               # Drop your .txt files here
├── summaries/           # Summaries will be saved here
├── logs/                # Event and error logs
│   └── events.log
├── src/                 # Core codebase
│   ├── cli.py           # CLI entrypoint using Click
│   ├── config.py        # Config and environment loader
│   ├── summarizer.py    # LLM interface to generate summaries
│   ├── watcher.py       # Watches input/ and triggers summarization
│   └── __init__.py
├── tests/               # Unit and integration tests
│   ├── test_cli_runs.py
│   ├── test_summarizer.py
│   └── test_watcher.py
├── .env                 # AWS keys and Bedrock config
├── .gitignore
├── README.md
├── requirements.txt
└── venv/                # Your Python virtual environment
```
---

## Setup & Installation

1. Clone the Repo
```
git clone https://github.com/your-username/AIPoweredCliTool.git
cd AIPoweredCliTool
```
2. Install Dependencies
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Configure Environment Variable
```
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1
BEDROCK_MODEL_ID=your-model-id-of-choice
```
---

## Usage Guide
1. Run The CLI
```
python src/cli.py
```
The CLI will:
- Monitor the input/ directory for new ``.txt`` files.
- Upon detecting a file, call the LLM and save the summary as a new file in ``summaries/``


