import json
from agents.tool import FunctionTool
from agents.run_context import RunContextWrapper
from typing import Any

# 🧠 Memory Tool Implementation
async def memory_tool(context: RunContextWrapper[Any], params_json: str):
    params = json.loads(params_json)
    input_text = params.get("input_text", "")

    # Initialize history if not set
    if not hasattr(context.context, "history") or not isinstance(context.context.history, list):
        context.context.history = []

    # 🧾 Show history if asked
    if "show" in input_text.lower() and "history" in input_text.lower():
        history = context.context.history
        if history:
            formatted = "\n".join([f"{i+1}. {msg}" for i, msg in enumerate(history)])
            return {"result": f"🧠 Your message history:\n{formatted}"}
        else:
            return {"result": "No message history recorded yet."}

    # 💾 Save input
    context.context.history.append(input_text)
    return {"result": f"💾 Got it! I’ve saved: '{input_text}'"}

# ✅ Define tool
memory_tool_fn = FunctionTool(
    name="MemoryExampleTool",
    description="Stores user messages in context and can show message history.",
    params_json_schema={
        "type": "object",
        "properties": {
            "input_text": {"type": "string", "description": "The user's message to save."}
        },
        "required": ["input_text"]
    },
    on_invoke_tool=memory_tool,
    strict_json_schema=True,
    is_enabled=True,
)
