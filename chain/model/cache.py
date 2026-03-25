from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.caches import InMemoryCache
from langchain_core.globals import set_llm_cache

load_dotenv()

set_llm_cache(InMemoryCache())

model = init_chat_model("anthropic:MiniMax-M2.7")

# 第一次向模型提问
result = model.invoke('tell me a joke')
print(result.content)

# 第二次向模型提问同样的问题（命中缓存，不会再调用 API）
result2 = model.invoke('tell me a joke')
print(result2.content)