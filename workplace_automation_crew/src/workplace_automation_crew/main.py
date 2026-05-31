#!/usr/bin/env python
import os
import sys
import warnings
from datetime import datetime

# Suppress CrewAI telemetry (unreachable without proxy in corporate network)
os.environ.setdefault("OTEL_SDK_DISABLED", "true")
# Set proxy for any remaining external calls (e.g. LiteLLM model cost map)
os.environ.setdefault("HTTP_PROXY", "http://proxy-fr-croissy.gemalto.com:8080")
os.environ.setdefault("HTTPS_PROXY", "http://proxy-fr-croissy.gemalto.com:8080")
os.environ.setdefault("NO_PROXY", "localhost,127.0.0.1,llm.synapse.thalescloud.io,*.gemalto.com")

from workplace_automation_crew.crew import WorkplaceAutomationCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """Run the Workplace Automation Crew."""
    inputs = {
        "task_description": (
            "Every week, our team manually compiles a project status report by: "
            "1) collecting updates from 6 team members via email, "
            "2) copy-pasting their updates into a shared Excel tracker, "
            "3) calculating RAG (Red/Amber/Green) status for each workstream based "
            "on rules we know by heart (e.g. >10% budget overrun = Red), "
            "4) building a PowerPoint slide deck from the Excel data, "
            "5) writing a 3-paragraph executive summary, "
            "6) emailing the final deck to 20 stakeholders every Friday at 5pm. "
            "This takes 5-7 hours every week and is error-prone when email updates arrive late."
        ),
        "team_context": (
            "Team of 10 project managers. The report is owned by 1 PM who rotates monthly. "
            "We use Microsoft 365 (Outlook, Excel, PowerPoint, Teams, SharePoint). "
            "Project data also lives in Jira (task tracking) and Confluence (documentation). "
            "Team has basic Python skills but no dedicated developer."
        ),
        "constraints": (
            "Budget: €300/month maximum for new tools. "
            "Must work within Microsoft 365 — no tools requiring separate CISO security review. "
            "Timeline: first automation live within 3 weeks, full solution in 2 months. "
            "Data stays within EU (GDPR). "
            "Solution must be maintainable by non-developers after handover."
        ),
        "current_year": str(datetime.now().year),
    }

    try:
        result = WorkplaceAutomationCrew().crew().kickoff(inputs=inputs)
        print("\n" + "=" * 60)
        print("Blueprint saved to: output/automation_blueprint.md")
        print("=" * 60)
        return result
    except Exception as e:
        raise Exception(f"Crew run failed: {e}")


def train():
    inputs = {
        "task_description": "Weekly status report compiled manually from emails into PowerPoint",
        "team_context": "Team of 10 PMs using Microsoft 365",
        "constraints": "€300/month budget, Microsoft 365 only, 3 weeks to first win",
        "current_year": str(datetime.now().year),
    }
    try:
        WorkplaceAutomationCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )
    except Exception as e:
        raise Exception(f"Training failed: {e}")


def replay():
    try:
        WorkplaceAutomationCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"Replay failed: {e}")


def test():
    inputs = {
        "task_description": "Weekly status report compiled manually from emails into PowerPoint",
        "team_context": "Team of 10 PMs using Microsoft 365",
        "constraints": "€300/month budget, Microsoft 365 only, 3 weeks to first win",
        "current_year": str(datetime.now().year),
    }
    try:
        WorkplaceAutomationCrew().crew().test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )
    except Exception as e:
        raise Exception(f"Test failed: {e}")
