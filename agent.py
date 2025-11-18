from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool, FunctionTool, google_search
from google.genai import types

retry_config = types.HttpRetryoptions(
    attempts = 5,
    exp_base = 7,
    initial_delay = 1,
    http_status_codes = [429, 500, 503,504],
)

outline_agent = Agent(
    name="OutlineAgent",
    model=Gemini(
        name="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    output_key = "blog_outline",
)

draft_agent = Agent(
    name="DraftAgent",
    model=Gemini(
        name="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    output_key = "blog_draft",
)

final_agent = Agent(
    name="FinalAgent",
    model=Gemini(
        name="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    output_key = "final_blog",
)

root_agent = Agent(
    name="RootAgent",
    sub_agents = [outline_agent, draft_agent, final_agent],
)