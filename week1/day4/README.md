# Week 1 - Day 4: Structured JSON Output with Pydantic and Groq

## Overview

This project introduces a very practical and important workflow in AI application development: turning unstructured text into clean, validated structured data.

Instead of asking a model to return free-form text and then manually extracting fields, we define a strict schema first and let the model generate JSON that matches that schema. Then we validate the JSON using Pydantic before using it in Python.

This day focuses on three connected ideas:

- structured output from an LLM
- schema-driven prompt design
- runtime validation with Pydantic

The sample script in `json_pydantic.py` demonstrates how to:

1. load a Groq API key from a `.env` file
2. send a ticket-like message to a language model
3. request a JSON object response
4. convert the result into a Python object
5. validate the extracted fields using a Pydantic model

---

## Why This Topic Matters

Most real-world AI systems do not operate on plain text alone. They need clean machine-readable data.

Examples include:

- extracting customer details from support tickets
- parsing resumes into structured fields
- converting form responses into typed records
- building AI pipelines where downstream code expects reliable JSON

Without structure, the model may return inconsistent text, missing fields, or slightly different formats each time. That makes it harder to build dependable systems.

This is where structured output becomes essential.

---

## Learning Objectives

By the end of this exercise, you should understand:

- how to define a schema for LLM output
- why JSON object responses are useful in production workflows
- how to use `pydantic.BaseModel` for validation
- how to convert a raw JSON string into a typed Python object
- how prompt design influences extraction quality
- how to handle extracted data safely in application code

---

## Core Concepts

### 1. Structured Output from an LLM

An LLM is powerful because it can understand natural language, but it is not automatically a database or a formal data extractor.

If you ask it for a free-form answer, the output may vary. For example, the model might return:

- different names for the same field
- inconsistent capitalization
- extra commentary around the JSON
- slightly malformed output

To make this more reliable, we ask the model to return a JSON object.

In the example, the API call uses:

```python
response_format = {
    "type": "json_object"
}
```

This tells the model to produce JSON in object form rather than a free-form paragraph.

---

### 2. Schema Design with Pydantic

Pydantic is a Python library for defining data models and validating inputs.

The script builds a `Ticket` class like this:

```python
from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    email: str
    issue: str
```

This gives us a strict shape for the data:

- `name` must be a string
- `email` must be a string
- `issue` must be a string

That means we can be confident that downstream code is working with the expected fields.

---

### 3. JSON Schema Generation

Pydantic can automatically generate a JSON schema from the model:

```python
schema = Ticket.model_json_schema()
```

This schema acts like a contract. It tells the LLM what fields to produce and what their types are.

The schema is inserted into the system prompt so the model knows what structure to follow.

---

### 4. Prompt Engineering for Extraction

A strong system prompt should tell the model:

- what kind of task it is doing
- what output format it must return
- what the schema is
- what information to extract

In the script, the system prompt is:

```python
system_prompt = f"""
Extract the personal information from the ticket strictly based on this schema and give a json output.
{schema}
"""
```

This prompt is designed to reduce hallucination and keep the model aligned with the expected output format.

The user message then provides the actual ticket text.

---

### 5. Parsing and Validation

The API returns a response string. That string is then parsed using Python's `json` module:

```python
raw_json = answer
data_file = json.loads(raw_json)
```

Once we have a Python dictionary, we can instantiate the Pydantic model:

```python
ticket = Ticket(**data_file)
```

This step is important because it validates the output before we use it.

If the model returns something missing, malformed, or unexpectedly typed, Pydantic will raise a validation error instead of letting broken data flow into the next stage.

---

## Deep Dive into the Script

### Step 1: Load the API Key

The script reads the Groq API key from the environment:

```python
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
```

This follows a common secure pattern:

- keep secrets out of source code
- store them in `.env`
- load them only at runtime

---

### Step 2: Initialize the Groq Client

```python
client = Groq(api_key=my_api_key)
```

The Groq client is the bridge between your Python code and the language model.

---

### Step 3: Define the Schema

```python
class Ticket(BaseModel):
    name: str
    email: str
    issue: str
```

The schema describes the exact form of the data we expect from the model.

---

### Step 4: Build a Prompt That Guides Extraction

The system prompt tells the model precisely what to do:

- extract personal information
- follow the schema strictly
- return JSON

The user prompt contains the actual text to parse.

This separation is important:

- the system message sets behavior
- the user message provides the data

---

### Step 5: Send the Request

The request includes:

- the selected model
- the system and user messages
- a JSON response format

This is the point where the model is asked to transform free text into structured information.

---

### Step 6: Parse the Response and Validate It

The raw answer is a JSON string. We parse it into Python and then validate it against the `Ticket` model.

This is the critical step that turns a model response into reliable application data.

---

## Why `response_format` Alone Is Not Enough

A common misunderstanding is that `response_format={"type": "json_object"}` guarantees perfect structure.

It helps, but it does not completely guarantee that:

- every required field will be present
- the field names will always match your schema
- the content will be semantically correct
- the response will never contain extra or missing values

So the best practice is:

1. ask for JSON output
2. validate it with Pydantic
3. fail loudly if the output is invalid

That combination is much stronger than relying on the model alone.

---

## Real-World Use Cases

This technique is widely used in AI workflows such as:

- support ticket triage
- customer onboarding extraction
- lead form parsing
- document-to-JSON pipelines
- resume screening
- HR data extraction from applicant forms

A typical pipeline looks like this:

1. raw text enters the system
2. LLM extracts structured fields
3. schema validation confirms correctness
4. the validated object is stored or processed by business logic

---

## Practical Notes

### Stronger Prompting Tips

To improve result quality, you can add more instruction to the system prompt, such as:

- return only valid JSON
- do not add explanations
- use the exact field names from the schema
- if data is missing, use an empty string or `null` according to your policy

### Validation Strategy

In production systems, you should also consider:

- checking that emails look like valid email addresses
- normalizing names and issue text
- handling missing fields gracefully
- logging malformed responses for debugging

---

## Project Structure

- `json_pydantic.py` — the main script demonstrating schema-based extraction
- `main.py` — simple starter file
- `pyproject.toml` — project dependencies
- `README.md` — project documentation

---

## Setup Instructions

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install the dependencies:

   ```powershell
   pip install -e .
   ```

3. Create a `.env` file with your Groq API key:

   ```env
   GROQ_API_KEY=your_api_key_here
   ```

---

## Running the Example

Run the script:

```powershell
python json_pydantic.py
```

What happens:

- the ticket text is sent to the LLM
- the model is asked to return JSON
- the JSON is parsed
- the result is validated with the `Ticket` schema
- the extracted `name`, `email`, and `issue` values are printed

---

## Expected Outcome

If the model performs well, you will see a structured JSON object that contains fields such as:

```json
{
  "name": "Waseem",
  "email": "buildwithwasu@gmail.com",
  "issue": "iphone is not working"
}
```

Once validated, these values can be used safely in Python code.

---

## Key Takeaways

This exercise shows a foundational pattern in AI engineering:

- define the target schema
- ask the model to produce structured output
- validate the output using Pydantic
- use that validated data in the rest of your program

This is one of the most important building blocks for trustworthy AI-powered applications.

---

## Homework

A very good next step for this topic is to build a real extraction workflow using resume data.

### Suggested challenge

Take a resume in PDF or Word format and:

1. extract fields such as skills, experience, and projects
2. compare those extracted fields with a list provided by HR
3. compute a match percentage or similarity score
4. return a structured result for downstream review

This extends the same skill set into a more realistic AI automation scenario.

---

## Summary

Day 4 is about moving from raw LLM output to reliable structured data.

The important lesson is not just “ask the model for JSON,” but also:

- define a clear schema
- guide the model with strong prompts
- validate the response before using it

That is what makes LLM-based systems much more production-ready.
