from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_core.example_selectors import LengthBasedExampleSelector

load_dotenv()
model = init_chat_model("anthropic:MiniMax-M2.7")

# 定义生成商店的方法
def generate_store_names(store_features):
    prompt_template = "我正在开一家新的商店，它的主要特点是{}。请帮我想出10个商店的名字。"
    prompt = prompt_template.format(store_features)

    response = model.invoke(prompt)
    return response.content

store_features = "时尚、创意、独特"

store_names = generate_store_names(store_features)
print(store_names)