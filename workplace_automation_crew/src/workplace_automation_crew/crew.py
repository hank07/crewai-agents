import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import FileReadTool, DirectoryReadTool

from .llm import llm

KNOWLEDGE_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "knowledge")

# Shared tools: agents read from the local knowledge base of automation tools & patterns
knowledge_reader = FileReadTool()
knowledge_browser = DirectoryReadTool(directory=KNOWLEDGE_DIR)


@CrewBase
class WorkplaceAutomationCrew():
    """Two-agent crew that analyses a repetitive workplace task and produces
    a complete, costed automation blueprint with phased implementation roadmap."""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def process_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["process_analyst"],  # type: ignore[index]
            verbose=True,
            llm=llm,
            tools=[knowledge_browser, knowledge_reader],
        )

    @agent
    def automation_architect(self) -> Agent:
        return Agent(
            config=self.agents_config["automation_architect"],  # type: ignore[index]
            verbose=True,
            llm=llm,
            tools=[knowledge_browser, knowledge_reader],
        )

    @task
    def process_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["process_analysis_task"],  # type: ignore[index]
        )

    @task
    def automation_blueprint_task(self) -> Task:
        os.makedirs("output", exist_ok=True)
        return Task(
            config=self.tasks_config["automation_blueprint_task"],  # type: ignore[index]
            output_file="output/automation_blueprint.md",
        )

    @crew
    def crew(self) -> Crew:
        """Sequential: Process Analyst runs first, Automation Architect
        receives the full analysis as context before designing the blueprint."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
