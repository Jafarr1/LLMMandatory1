from crewai import Agent, Task, Crew, Process
from llm_config import coder_llm

deployment_agent = Agent(
    role="Deployment Engineer",
    goal="Repair the Docker deployment configuration based on real validation feedback.",
    backstory=(
        "You create and repair simple Docker deployment configurations "
        "based on actual build results."
    ),
    llm=coder_llm,
    verbose=True
)

deployment_task = Task(
    description="""
The Dockerfile you generated failed during real Docker validation.

Actual Docker build error:

ERROR [3/3] COPY ./APP.PY .
"/APP.PY": not found

The actual application file is named exactly:

app.py

Repair the Dockerfile.

Requirements:
- Use Python 3 slim.
- Install Flask.
- Copy the existing lowercase app.py.
- Expose port 5000.
- Start the application.
- Do not create additional infrastructure.
- Do not invent requirements.txt.
- Return ONLY valid Dockerfile contents.
- Do not use Markdown fences.
- Do not include explanations.
""",
    expected_output="Only the contents of a valid corrected Dockerfile.",
    agent=deployment_agent,
    output_file="Dockerfile"
)

crew = Crew(
    agents=[deployment_agent],
    tasks=[deployment_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print("\n--- DEPLOYMENT REPAIR RESULT ---")
print(result)