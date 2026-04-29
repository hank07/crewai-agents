from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# Research task for the blog researcher
research_task = Task(
    description=(
        "Identify the video {topic} in the provided YouTube channel."
        "Focus on identifying key points, insights, and main concepts."
        "Your final answer MUST be a comprehensive analysis ready for blog writing."
        "Use the YouTube tool to search for relevant videos and extract transcription."
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the video content.',
    tools=[yt_tool] if yt_tool else [],
    agent=blog_researcher,
)

# Writing task for the blog writer  
write_task = Task(
    description=(
        "Using the insights provided, develop an engaging blog post"
        "that highlights the most significant aspects of {topic}."
        "Your post should be informative yet accessible, catering to a tech-savvy audience."
        "Make it sound cool, avoid complex words so it doesn't sound like AI."
    ),
    expected_output='A compelling 4 paragraph blog post formatted as markdown.',
    tools=[yt_tool] if yt_tool else [],
    agent=blog_writer,
    async_execution=False,
    output_file='blog_post.md'
)
