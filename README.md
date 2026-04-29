# CrewAI Multi-Agent Blog Generator

I built this to learn how CrewAI works — specifically how multiple agents can work together, each with a specific role, to complete a task that would be hard for a single agent.

The idea is simple: give it a YouTube topic, and two agents work together to produce a blog post about it.

## How it works

Two agents run in sequence:

1. **Blog Researcher** — searches YouTube for the given topic, reads the video transcription, and pulls out the key insights
2. **Blog Writer** — takes those insights and writes an engaging, readable blog post

## Project structure

```
crewai-project/
├── agents.py       # Agent definitions (researcher + writer)
├── tasks.py        # Task definitions for each agent
├── tools.py        # YouTube search tool setup
├── crew.py         # Wires everything together and runs it
├── firstcrew/      # A more structured CrewAI template project
│   └── src/firstcrew/
│       ├── crew.py       # CrewBase class with decorators
│       ├── llm.py        # LLM config
│       ├── main.py       # Entry point (run/train/test commands)
│       └── config/       # agents.yaml and tasks.yaml
```

## Setup

```bash
pip install crewai crewai-tools python-dotenv
```

Copy `.env.example` to `.env` and add your API key:

```
OPENAI_API_KEY=your-key-here
```

## Running it

```bash
python crew.py
```

It will research and write a blog post on `AI VS ML VS DL vs Data Science` by default. Change the `topic` in `crew.py` to whatever you want.

For the `firstcrew` subproject:

```bash
cd firstcrew
pip install -e .
firstcrew run
```

## Tech used

- [CrewAI](https://github.com/joaomdmoura/crewAI) for multi-agent orchestration
- CrewAI Tools for YouTube search
- OpenAI / any OpenAI-compatible LLM
