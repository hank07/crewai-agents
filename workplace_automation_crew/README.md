# Workplace Automation Crew — CrewAI Project

A two-agent CrewAI crew that takes any repetitive manual workplace task and produces a
**complete, costed automation blueprint** with a phased implementation roadmap and ROI calculation.

---

## What it does

Given a description of a repetitive manual task + team context + constraints, the crew:
1. Analyses the task step-by-step and maps every automation opportunity
2. Evaluates specific tools for each opportunity (with comparison tables)
3. Designs the full automation architecture and integration plan
4. Produces a phased roadmap, ROI calculation, and concrete next steps

---

## Two agents

| Agent | Role |
|-------|------|
| **Process Analyst** | Breaks the manual task into discrete steps, scores each for automation feasibility/impact/risk, evaluates 2-3 tool options per opportunity, identifies quick wins, and maps all data dependencies. Produces a structured Process Analysis Report. |
| **Automation Architect** | Receives the full analysis as context, then designs the recommended automation stack with integration architecture, a 3-phase implementation roadmap (Week 1-2 quick win → Week 3-8 core → Month 3-6 optimisation), ROI calculation at actual numbers, top-4 risk register, and 5 concrete next steps. |

The Automation Architect receives the Process Analyst's full report as `context` before
producing its blueprint — ensuring every tool choice is grounded in the evaluated landscape.

---

## Two tasks

| Task | Output |
|------|--------|
| `process_analysis_task` | Process breakdown + automation opportunity scoring table + tool comparison tables + quick wins + data dependency map |
| `automation_blueprint_task` | `output/automation_blueprint.md` — executive summary, ASCII architecture diagram, phased roadmap, ROI table, risk register, next steps |

---

## Knowledge base

The Process Analyst and Automation Architect both have access to a curated local knowledge base:

| File | Contents |
|------|----------|
| `knowledge/rpa_and_workflow_tools.md` | Power Automate, Zapier, n8n, UiPath, Python scripts, Make — with pricing, complexity ratings, best-fit scenarios |
| `knowledge/ai_automation_tools.md` | LLM APIs for document processing, Microsoft Copilot Studio, Azure Document Intelligence, python-pptx, Power BI |
| `knowledge/automation_patterns.md` | 7 proven patterns: email-to-data pipeline, report generation, data aggregation, reminder bot, RAG Q&A bot, meeting notes, scheduled sync |
| `knowledge/roi_framework.md` | Step-by-step ROI formula with example calculations, presentation tips, common mistakes to avoid |

Agents use `FileReadTool` and `DirectoryReadTool` to query these files during analysis.

---

## Project structure

```
workplace_automation_crew/
├── pyproject.toml                        # Project config + entry points
├── uv.lock                               # Pinned dependencies
├── output/                               # Generated blueprints land here
├── knowledge/                            # Domain knowledge base (4 files)
└── src/workplace_automation_crew/
    ├── crew.py                           # Agent + task wiring
    ├── llm.py                            # Gateway LLM config
    ├── main.py                           # Entry point + example inputs
    └── config/
        ├── agents.yaml                   # Agent personas + goals
        └── tasks.yaml                    # Task descriptions + expected outputs
```

---

## How to run

**From inside the project directory:**

```bash
cd /home/handa_k/projects/crewai-project/workplace_automation_crew
crewai run
```

**Or directly with uv:**

```bash
cd /home/handa_k/projects/crewai-project/workplace_automation_crew
uv run run_crew
```

The blueprint is saved to `output/automation_blueprint.md` when complete.

---

## Customise the inputs

Edit `src/workplace_automation_crew/main.py` → `run()` to describe your own task:

```python
inputs = {
    "task_description": "Describe the manual repetitive task in detail...",
    "team_context": "Team size, tools used, skills available...",
    "constraints": "Budget, timeline, tech restrictions, compliance requirements...",
    "current_year": "2026",
}
```

**Example use cases:**
- Weekly status report compiled from emails into PowerPoint
- Monthly invoice reconciliation across 3 systems
- Manual onboarding checklist run for every new joiner
- Daily data export from one system pasted into another
- Meeting notes written up and distributed after every call

---

## LLM configuration

Uses your internal LiteLLM-compatible gateway (OpenAI-compatible API):

```python
# src/workplace_automation_crew/llm.py
os.environ["OPENAI_API_KEY"] = "your-gateway-key"
os.environ["OPENAI_BASE_URL"] = "https://your-gateway/v1"

llm = LLM(model="claude-sonnet-4-5-20250929")
```

> **Note:** CrewAI detects `claude-` model names and tries the native Anthropic provider
> (which uses Anthropic's non-OpenAI API format). `llm.py` patches the provider detection
> to force the OpenAI native provider instead, which correctly routes to your
> OpenAI-compatible gateway.

---

## How it differs from the standard CrewAI tutorial

| Dimension | Tutorial (firstcrew) | This project |
|-----------|---------------------|--------------|
| Domain | General topic research | Workplace automation consulting |
| Agent 1 | Generic researcher | Process Analyst (task decomposition + tool evaluation) |
| Agent 2 | Generic analyst | Automation Architect (blueprint + roadmap + ROI) |
| Inputs | `{topic}` | `{task_description}` + `{team_context}` + `{constraints}` |
| Output | Generic markdown report | Costed automation blueprint with phased roadmap |
| Knowledge base | None | 4 domain files covering tools, patterns, ROI |
| Tools | None | `FileReadTool` + `DirectoryReadTool` on knowledge base |
| Context passing | Research → Report | Analysis → Blueprint (architect sees full analyst output) |
