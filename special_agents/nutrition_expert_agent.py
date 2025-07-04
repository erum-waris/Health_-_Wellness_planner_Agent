from agents import Agent
from config import model
from guardrails import medical_input_guardrail, medical_output_guardrail, GenericResponse

# 🍎 Nutrition Expert Agent
nutrition_expert_agent = Agent(
    name="NutritionExpertAgent",
   instructions=(
    "You are a certified Nutrition Expert.\n"
    "Provide balanced, culturally appropriate diet plans based on user needs.\n"
    "Use your tools to analyze food intake or generate personalized diet plans."
),

    model=model,
    tools=[],  # Add tools later if you define any (e.g., food_analysis_tool)
    hooks=None,
    input_guardrails=[medical_input_guardrail],
    output_guardrails=[medical_output_guardrail],
    output_type=GenericResponse
)
