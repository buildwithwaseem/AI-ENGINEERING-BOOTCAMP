# Week 1 - Day 2: System Prompt and Temperature Control

## Overview
This project introduces two important concepts in LLM interaction:

- the use of a system message to guide the model's behavior
- the role of `temperature` in controlling response creativity and variability

The implementation in `sys_temp.py` uses the Groq API to generate a brand name suggestion for a clothing company. It demonstrates how a well-structured system prompt can shape the output and how a temperature setting of `0` encourages predictable, stable responses.

## Learning Objectives
By completing this exercise, you will learn how to:

- load environment variables securely from a `.env` file
- initialize a Groq client in Python
- send a system message and a user prompt to a language model
- configure the model's `temperature` parameter
- interpret the generated response from the API

## Project Structure
- `sys_temp.py` — the main script demonstrating system prompt usage and temperature control
- `main.py` — a simple starter script that prints a basic greeting
- `pyproject.toml` — project metadata and dependencies
- `README.md` — project documentation

## What the Script Demonstrates
The program in [week1/day2/sys_temp.py](week1/day2/sys_temp.py) performs the following steps:

1. Loads the environment variables using `dotenv`
2. Reads the `GROQ_API_KEY` from the environment
3. Raises an error if the API key is missing
4. Creates a Groq client instance
5. Defines a system message that instructs the model to act as a brand manager
6. Sends a user prompt asking for a clothing company name
7. Calls the Groq chat completion API with `temperature=0`
8. Prints the model's final answer

## Key Concept: System Prompt
A system prompt defines the model's role and constraints. In this project, the system message tells the model to:

- act as a brand manager
- suggest a one-word name
- provide only one name for a clothing brand

This is an example of how prompt design can strongly influence the tone, format, and quality of the response.

## Key Concept: Temperature
The `temperature` parameter controls the randomness of the model's output.

- `temperature = 0` makes the response more deterministic and focused
- higher values increase creativity and variability

In this exercise, the temperature is set to `0` to keep the output stable and suitable for a constrained naming task.

## Prerequisites
Before running the project, make sure you have:

1. Python 3.13 or later installed
2. A valid Groq API key
3. A `.env` file containing your environment variable

## Setup Instructions
1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install the required dependencies:

   ```powershell
   pip install -e .
   ```

3. Create a `.env` file in the project folder and add your API key:

   ```env
   GROQ_API_KEY=your_api_key_here
   ```

## Running the Project
To execute the system prompt and temperature example, run:

```powershell
python sys_temp.py
```

The script will send the prompt to the Llama model through Groq and print the generated company name.

## Expected Behavior
The script is designed to produce a single, one-word brand name suggestion based on the system instruction and the user prompt. The exact output may vary depending on the model version and the API response, but the response should remain consistent because the temperature is set to `0`.

## Notes
- The system message is essential for controlling the model's behavior.
- `temperature=0` is ideal for tasks that require predictability and consistency.
- Keep your API key private and avoid committing it to version control.

## Summary
This Day 2 exercise demonstrates a practical introduction to prompt engineering with LLMs. It shows how a system message can define the model's role and how temperature can be used to control the balance between determinism and creativity.
