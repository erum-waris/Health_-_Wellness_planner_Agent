# import streamlit as st
# import asyncio
# from health_agent import health_agent
# from context import get_user_context
# from agents import Runner
# from openai.types.responses import ResponseTextDeltaEvent
# from config import config
# st.set_page_config(page_title="Health & Wellness Planner AI")
# st.title("🧘 Health & Wellness Planner AI\nBy Erum Waris")

# user_input = st.chat_input("How can I support your wellness today?")

# # Setup context once
# if "context" not in st.session_state:
#     st.session_state.context = get_user_context("Erum Waris", 1)

# if user_input:
#     with st.chat_message("user"):
#         st.write(user_input)

#     with st.chat_message("assistant"):
#         placeholder = st.empty()

#         async def run_agent():
#             result = Runner.run_streamed(
#                starting_agent=health_agent,
#                input=user_input,
#                context=st.session_state.context,
#                run_config=config
#             )

#             output_text = ""  # ✅ Define inside async function
#             async for event in result.stream_events():
#                 if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
#                     output_text += event.data.delta or ""
#                     placeholder.markdown(output_text)

#         try:
#             asyncio.run(run_agent())  # ✅ Cleaner run
#         except RuntimeError:
#             loop = asyncio.new_event_loop()
#             asyncio.set_event_loop(loop)
#             loop.run_until_complete(run_agent())

import streamlit as st
import asyncio
import json

from health_agent import health_agent
from context import get_user_context
from agents import Runner
from tools.memory_tool import memory_tool  # ✅ Import this!
from openai.types.responses import ResponseTextDeltaEvent
from config import config

st.set_page_config(page_title="Health & Wellness Planner AI")
st.title("🌿Health & Wellness Planner AI🥗")
st.title("By Erum Waris")

user_input = st.chat_input("How can I support your wellness today?")

# Setup context once
if "context" not in st.session_state:
    st.session_state.context = get_user_context("Erum Waris", 1)

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()

        async def run_agent():
            # ✅ Save to memory before invoking agent
            await memory_tool(st.session_state.context, json.dumps({
                "input_text": user_input
            }))

            result = Runner.run_streamed(
                starting_agent=health_agent,
                input=user_input,
                context=st.session_state.context,
                run_config=config
            )

            output_text = ""
            async for event in result.stream_events():
                if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                    output_text += event.data.delta or ""
                    placeholder.markdown(output_text)

        try:
            asyncio.run(run_agent())
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(run_agent())
