import json
from typing import Any
from agents.tool import FunctionTool

# ✅ Async and correct parameter order
async def schedule_checkin_tool(context: Any, params_json: str):
    # Parse the params if any (currently none expected)
    # You can add future parameters like 'note' or 'date' later
    if not hasattr(context.context, "progress_logs") or context.context.progress_logs is None:
        context.context.progress_logs = []

    context.context.progress_logs.append({
        "date": "Weekly",  # or use actual datetime
        "note": "Scheduled weekly check-in"
    })

    return {"result": "✅ Weekly check-in has been successfully scheduled!"}

# ✅ Register with FunctionTool
scheduler_tool = FunctionTool(
    name="CheckinSchedulerTool",
    description="Schedules a weekly check-in for the user.",
    params_json_schema={
        "type": "object",
        "properties": {},
        "required": []
    },
    on_invoke_tool=schedule_checkin_tool,
    strict_json_schema=True,
    is_enabled=True,
)
