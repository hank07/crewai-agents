import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from tools import yt_tool

load_dotenv()

llm = LLM(
    model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
    api_key=os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL") or None,
)

blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, Machine Learning and Gen AI "
        "and providing suggestions on key insights."
    ),
    tools=[yt_tool] if yt_tool else [],
    allow_delegation=True,
    llm=llm
)

blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool] if yt_tool else [],
    allow_delegation=False,
    llm=llm
)
