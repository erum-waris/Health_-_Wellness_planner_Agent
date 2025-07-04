from agents import Agent
from config import model
from guardrails import (
    medical_input_guardrail,
    medical_output_guardrail,
    GenericResponse
)

injury_support_agent = Agent(
    name="InjurySupportAgent",
    instructions=(
"You are a compassionate assistant an injury support expert agent. When users mention injury, joint pain, or physical discomfort, you respond with empathy and understanding.\n"
"You may suggest common at-home care options like rest, ice packs, gentle stretches, or seeing a physiotherapist — but avoid any prescriptions or diagnoses.\n"
"Always encourage the user to consult a licensed healthcare professional for proper medical attention."

    ),
    model=model,
    tools=[],
    hooks=None,
    input_guardrails=[medical_input_guardrail],
    output_guardrails=[medical_output_guardrail],
    output_type=GenericResponse
)
