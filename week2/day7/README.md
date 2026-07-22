# React Chain Agent Demo

This folder contains a simple tool-enabled agent demo using the Groq `llama-3.3-70b-versatile` model.

## Overview

The script `react_chain.py` implements a small agent loop that:
- sends a system prompt describing available tools,
- calls the LLM to decide what to do next,
- executes exactly one tool per step,
- returns the tool observation to the LLM,
- repeats until the agent returns a `Final Answer:`.

The agent is designed as a shopping assistant that can answer product pricing questions and perform basic arithmetic.

## Files

- `react_chain.py` - main agent script
- `.env` - expected to contain `GROQ_API_KEY`
- `README.md` - this documentation

## Tools

The agent exposes two tools:

- `get_product_price(product)`
  - returns a price for selected products.
  - currently supports `iPhone 17` and `iPhone 15`.
- `calculator(expression)`
  - evaluates a simple arithmetic expression using Python `eval()`.

## Setup

1. Install dependencies:
   ```powershell
   pip install python-dotenv groq
   ```
2. Add your API key to a `.env` file:
   ```text
   GROQ_API_KEY=your_api_key_here
   ```

## Run

Execute the script from `week2/day7`:

```powershell
python react_chain.py
```

The default prompt asks:

- "I have 5000 rupees. What is the price of an iphone 17?"
- "and how much money will I have left?"

## How it works

1. The script loads the Groq API key from `.env`.
2. It initializes the LLM client and builds a system prompt describing the tools.
3. It sends the user question to the model.
4. For each step, it reads the model response:
   - if the model returns an `Action: ...`, the script runs the tool,
   - appends the observation back into the conversation,
   - continues until the model returns `Final Answer:`.

## Notes

- The prompt requires exact tool syntax, for example:
  - `Action: get_product_price("iPhone 17")`
  - `Action: calculator("5000 - 1000")`
- The current implementation limits the agent to 5 steps.
- `calculator()` uses `eval()`, so only trusted inputs should be used in real applications.
