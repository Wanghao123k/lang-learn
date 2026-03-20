from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langgraph.prebuilt.chat_agent_executor import AgentState
from langchain_core.messages import AnyMessage
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import InMemorySaver
from pydantic import BaseModel
load_dotenv()


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


"""
init_chat_model 使用 provider:model 语法时，多余的 **kwargs 会直接传给底层的 ChatAnthropic 构造函数。
所以可以通过 base_url 和 api_key 参数覆盖默认值。但由于你的 .env 已经设置了 ANTHROPIC_BASE_URL 和 ANTHROPIC_API_KEY，ChatAnthropic 会自动读取，不需要额外传参。
"""
def prompt(state: AgentState, config: RunnableConfig) -> list[AnyMessage]:
    user_name = config["configurable"].get("user_name")
    system_msg = f"You are a helpful assistant. Address the user as {user_name}."
    return [{"role": "system", "content": system_msg}] + state["messages"]

class WeatherResponse(BaseModel):
    conditions: str

model = init_chat_model(
    "anthropic:MiniMax-M2.7",
    temperature=0,
)
checkpointer = InMemorySaver()

agent = create_react_agent(
    model=model,
    tools=[get_weather],
    # 静态提示
    # prompt="Never answer questions about the weather."
    # 动态提示
    prompt=prompt,
    # 添加记忆系统
    checkpointer=checkpointer,
    response_format=WeatherResponse,
)

# Run the agent
config = {"configurable": {"thread_id": "1"}}
sf_response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
    config
)
ny_response = agent.invoke(
    {"messages": [{"role": "user", "content": "what about new york?"}]},
    config
)
for msg in sf_response["messages"]:
    print(f"{msg.type}: {msg.content}")
for msg in ny_response["messages"]:
    print(f"{msg.type}: {msg.content}")