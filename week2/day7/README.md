# ReAct Agent Demo

This folder introduces the idea of a ReAct-style AI agent: combining reasoning and action in a loop.

## What is ReAct?

ReAct stands for:

- Reasoning: the model thinks about what it needs to do.
- Acting: the model chooses an action, such as calling a tool.

In this demo, the agent does not directly answer everything by itself. Instead, it:

1. Reads the user question.
2. Decides which tool to call.
3. Executes that tool.
4. Receives an observation from the tool.
5. Uses that observation to continue reasoning.
6. Produces a final answer once the task is complete.

This is a simple example of how an LLM can act like an agent by using external tools.

## Project Goal

The goal of this example is to show how a language model can:

- answer a shopping question,
- call a pricing function,
- perform arithmetic using a calculator tool,
- and combine the results into a final answer.

## Files in This Folder

- `react_chain.py` – the main ReAct agent implementation.
- `.env` – expected to contain your `GROQ_API_KEY`.
- `README.md` – project explanation and usage instructions.

## Available Tools

The agent exposes two simple tools:

- `get_product_price(product)`
  - Returns a fixed product price.
  - Currently supports `iPhone 17` and `iPhone 15`.

- `calculator(expression)`
  - Evaluates a basic arithmetic expression.
  - Example: `5000 - 1000`

## How the Agent Works

The script uses a loop with the following pattern:

1. Build a message list with:
   - a system prompt describing the tools,
   - the user's question.
2. Send the prompt to the Groq model.
3. Read the model response.
4. If the model outputs an `Action:` line, run the matching tool.
5. Send the tool result back to the model as an `Observation:`.
6. Repeat until the model returns `Final Answer:`.

This is the core idea behind ReAct-style agents:

- the model reasons,
- chooses an action,
- observes the outcome,
- and continues.

## Example Prompt

The script currently uses a prompt like this:

> I have 5000 rupees. What is the price of an iphone 17? and how much money will I have left?

The agent should:

1. Look up the product price.
2. Subtract that price from 5000.
3. Return the final answer.

## Setup

1. Install the required Python packages:

```powershell
pip install python-dotenv groq
```

2. Create a `.env` file in this folder with your Groq API key:

```text
GROQ_API_KEY=your_api_key_here
```

## Run the Demo

From the `week2/day7` folder, run:

```powershell
python react_chain.py
```

## Important Notes

- The agent is designed to use exact action syntax, for example:

```text
Action: get_product_price("iPhone 17")
Action: calculator("5000 - 1000")
```

- The code currently limits the agent to 5 reasoning-action steps.
- The calculator uses Python `eval()`, so it should only be used with trusted input.

## Learning Outcome

By the end of this example, you should understand:

- what a ReAct agent is,
- how tool calling works,
- how the model can move through multiple reasoning-action steps,
- and how simple agent loops can be built with an LLM and external functions.

## Next Step

A natural next improvement would be to add more tools such as:

- product search,
- inventory lookup,
- order summary,
- or a more secure calculator implementation.

That would make the agent more realistic and capable of handling more complex task.