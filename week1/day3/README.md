# Week 1 - Day 3: Understanding Token Usage with Groq

## Overview
This project demonstrates how to interact with the Groq API using Python and inspect the token consumption of several chat completions. It is a beginner-friendly example focused on:

- loading the API key securely from a `.env` file
- initializing the Groq client
- sending multiple user prompts to a chat model
- printing token usage statistics returned by the API

The script in `tokens.py` is designed as a practical introduction to token counting, model usage monitoring, and response analysis in LLM applications.

## Project Purpose
Day 3 introduces a key operational concept in LLM development: token usage.

When building AI-powered applications, it is important to understand how many tokens are consumed for:

- input prompt tokens
- generated completion tokens
- total request cost and usage

This example helps you observe these metrics directly from the Groq API response.

## What the Script Does
The program performs the following sequence:

1. Loads environment variables from a `.env` file.
2. Reads the `GROQ_API_KEY` value.
3. Creates a Groq API client.
4. Defines a model name and a user role.
5. Sends three prompts one by one:
   - `Hi!`
   - `Explain time travel in Detail but under 100 words`
   - `Write a 1000 word essay on Machine learning`
6. Prints the following response metadata for each request:
   - prompt tokens
   - completion tokens
   - total tokens
   - finish reason

## Learning Objectives
By working through this exercise, you will learn how to:

- secure API credentials using environment variables
- connect Python to the Groq API
- assemble a chat message payload
- submit prompt requests to a language model
- inspect usage details from the API response

## Project Structure
- `tokens.py` — the main script that sends prompts and logs token usage
- `pyproject.toml` — project metadata and dependencies
- `README.md` — project documentation

## Technologies Used
- Python 3.13+
- Groq SDK
- `python-dotenv`

## Prerequisites
Before running the project, ensure that you have:

1. Python installed on your machine
2. A valid Groq API key
3. A `.env` file containing your key

## Setup Instructions
1. Open a terminal in the project directory.
2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```powershell
   pip install -e .
   ```

4. Create a `.env` file in the project folder with the following content:

   ```env
   GROQ_API_KEY=your_api_key_here
   ```

## Running the Project
Execute the script with:

```powershell
python tokens.py
```

The program will call the Groq chat completion endpoint for each prompt and display the token usage summary in the terminal.

## Expected Output
The script prints a line per prompt with values similar to:

```text
Prompt: Hi! --> your tokens: X completion_tokens: Y total tokens: Z Finish Reason: stop
```

The exact numbers depend on the selected model, request length, and API response.

## Key Notes
- Keep your API key private and do not commit it to version control.
- This example emphasizes usage inspection rather than response content generation.
- The `max_tokens` parameter can be adjusted depending on your application needs.
- The `Path` import is currently unused in the script and can be removed for cleanliness.

## Summary
This exercise provides a practical introduction to LLM API interaction in Python, with a focus on understanding the token usage returned by the model provider. It serves as a useful foundation for building more advanced AI applications that require monitoring, optimization, and cost awareness.
