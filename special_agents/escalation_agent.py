from agents import Agent
from config import model
from guardrails import (
    medical_input_guardrail,
    medical_output_guardrail,
    GenericResponse
)

escalation_agent = Agent(
    name="EscalationAgent",
    instructions="You support users in sensitive or emergency health situations with empathy and redirect them to professionals.",
    model=model,
    input_guardrails=[medical_input_guardrail],
    output_guardrails=[medical_output_guardrail],
    output_type=GenericResponse
)
