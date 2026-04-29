import os

# YouTube tool for searching and getting video transcriptions
# Check if API key is set
if os.getenv('OPENAI_API_KEY'):
    try:
        from crewai_tools import YoutubeVideoSearchTool
        yt_tool = YoutubeVideoSearchTool()
        print("YouTube tool initialized successfully with API key.")
    except Exception as e:
        print(f"Error initializing YouTube tool: {e}")
        # Create a simple mock tool as fallback without using BaseTool
        yt_tool = None
else:
    print("Warning: OPENAI_API_KEY not set. YouTube tool not available.")
    # Set to None when no API key is available
    yt_tool = None
