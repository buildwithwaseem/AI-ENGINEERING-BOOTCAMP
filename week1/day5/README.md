# Day 5 Resume Match Analyzer

This project analyzes a job description and compares it against candidate resumes to produce a structured match score.

## What this project does

The script performs the following workflow:

1. Reads a job description and extracts structured fields using a Groq LLM.
2. Parses candidate resumes from `.pdf` or `.docx` files.
3. Uses the LLM to compare the parsed resume with the job requirements.
4. Outputs a score and a short reasoning summary for each candidate.

## Main features

- Job description parsing with `pydantic` models
- Resume extraction from PDF and DOCX files
- Candidate-to-job matching using Groq
- Top 2 and lowest 2 candidate summary output

## Project structure

- `resume_parser.py` — main script that runs the full pipeline
- `resume/` — sample resumes used for testing
- `pyproject.toml` — project dependencies and package configuration

## Required setup

This project uses `uv` and Python 3.13.

### 1. Install dependencies

```powershell
cd "C:\Users\wasee\AI-ENGINEER-BOOTCAMP\week1\day5"
uv sync
```

### 2. Set the API key

Create a `.env` file in the project root with your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

The script loads this key with `python-dotenv`.

## Running the project

The script expects a `resumes` folder containing `.pdf` or `.docx` resume files.

```powershell
cd "C:\Users\wasee\AI-ENGINEER-BOOTCAMP\week1\day5"
mkdir resumes
Copy-Item .\resume\*.pdf, .\resume\*.docx -Destination .\resumes\ -Force
uv run python resume_parser.py
```

## Output

The script prints:

- the candidate score for each resume
- the top 2 best-matching candidates
- the lowest 2 candidates

## Dependencies

The main libraries used are:

- `groq`
- `pydantic`
- `python-dotenv`
- `pypdf`
- `python-docx`

## Profile Links

- LinkedIn: https://www.linkedin.com/in/waseemakramai/
- GitHub: https://github.com/buildwithwaseem

## Notes

- The script currently uses the hardcoded model `openai/gpt-oss-120b`.
- The resume folder path is fixed as `resumes` in the script, so the files must be placed there before running.
- The program can take a few seconds per resume because it makes LLM calls for parsing and comparison.
