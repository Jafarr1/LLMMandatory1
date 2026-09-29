from crewai import Agent, Task, Crew, Process
from llm_config import architect_llm, coder_llm

architect = Agent(
    role="Software Architect",
    goal="Respond as the architecture agent.",
    backstory="You are responsible for software architecture.",
    llm=architect_llm,
    verbose=True
)

coder = Agent(
    role="Software Developer",
    goal="Respond as the coding agent.",
    backstory="You are responsible for software implementation.",
    llm=coder_llm,
    verbose=True
)

architect_task = Task(
    description="Reply with exactly: ARCHITECT_AGENT_OK",
    expected_output="ARCHITECT_AGENT_OK",
    agent=architect
)

coder_task = Task(
    description="Reply with exactly: CODER_AGENT_OK",
    expected_output="CODER_AGENT_OK",
    agent=coder
)

crew = Crew(
    agents=[architect, coder],
    tasks=[architect_task, coder_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print("\n--- FINAL RESULT ---")
print(result)