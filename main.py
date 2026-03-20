from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent

load_dotenv()


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

"""
问题在于 create_react_agent 接收纯字符串 "MiniMax-M2.7" 时，会尝试自动推断 provider，但 MiniMax 不在它的内置 provider 列表中。
解决方式是先构造一个 ChatAnthropic(model="MiniMax-M2.7") 实例（它会从 .env 读取 ANTHROPIC_BASE_URL 和 ANTHROPIC_API_KEY 指向 MiniMax），再把这个实例传给 agent。
"""
model = ChatAnthropic(model="MiniMax-M2.7")

agent = create_react_agent(
    model=model,
    tools=[get_weather],
    prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

for msg in result["messages"]:
    print(f"{msg.type}: {msg.content}")
