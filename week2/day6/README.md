# Week 2 - Day 6: Prompt Engineering with Groq

## Overview

This project introduces the fundamentals of prompt engineering using the Groq API and Python. The goal is to demonstrate how a well-structured prompt can guide a Large Language Model (LLM) to perform a simple classification task.

In this exercise, the script sends a user complaint to a Groq-hosted model and asks it to classify the issue into one of the following categories:

- `billing`
- `technical`
- `return`
- `other`

The implementation highlights how prompt structure, constraints, examples, and fallback behavior influence the model's response.

## Project Purpose

This day is designed to help learners understand:

- how to build prompts with clear roles and objectives
- how to define task constraints and output expectations
- how to use examples to guide model behavior
- how to handle irrelevant or unsupported requests through fallback logic
- how to call an LLM API from Python using a secure API key

## Files Included

- `prompt_eng.py` — main script that loads the Groq API key, creates a client, and sends a structured prompt to the model
- `main.py` — simple starter script for the project
- `pyproject.toml` — project configuration and dependencies
- `README.md` — project documentation

## Technologies Used

- Python 3.13+
- Groq API
- `python-dotenv`
- `pydantic`

## Learning Objectives

By completing this exercise, you will learn how to:

1. configure a Python project for LLM integration
2. load sensitive credentials from a `.env` file
3. construct a structured prompt using role, task, constraints, and output format
4. evaluate model behavior against a controlled classification task
5. understand the importance of prompt clarity in real-world AI workflows

## Project Structure

```text
week2/
└── day6/
    ├── main.py
    ├── prompt_eng.py
    ├── pyproject.toml
    └── README.md
```

## Prerequisites

Before running the project, make sure you have:

- Python 3.13 or newer installed
- A valid Groq API key
- A `.env` file containing your environment variable

## Setup Instructions

### 1. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -e .
```

### 3. Add your Groq API key

Create a `.env` file in the project folder and add:

```env
GROQ_API_KEY=your_api_key_here
```

## Running the Project

Execute the prompt engineering example:

```powershell
python prompt_eng.py
```

This script:

1. loads the Groq API key from `.env`
2. creates a Groq client
3. defines a prompt that instructs the model to classify the issue
4. sends the prompt to the `llama-3.3-70b-versatile` model
5. prints the model's response in the terminal

## What the Prompt Demonstrates

The prompt in `prompt_eng.py` explicitly defines the following:

- the model's role: a support assistant
- the task: classify the issue into a category
- the constraint: use only one of `billing`, `technical`, or `return`
- the fallback rule: return `other` if the issue is unrelated
- the expected response format: one word only

This is a practical example of how instruction design affects model reliability.

## Example Scenario

The script sends a complaint such as:

```text
My marriage is broke
```

A well-behaved model should respond with:

```text
OTHER
```

## Profile Links

- LinkedIn: https://www.linkedin.com/in/waseemakramai/
- GitHub: https://github.com/buildwithwaseem

This shows how the prompt can be used to prevent the model from producing unrelated or unsupported outputs.

## Notes

- Keep your API key private and never commit it to version control.
- The prompt structure is intentionally simple, making it a strong starting point for prompt engineering practice.
- Output quality depends on the clarity and specificity of the prompt.

## Summary

Day 6 focuses on a practical prompt engineering pattern: providing the model with a clear role, constrained output rules, and a fallback strategy. It is an essential foundation for building safer and more predictable LLM-powered applications.
