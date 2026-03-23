from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

load_dotenv()

model = init_chat_model("anthropic:MiniMax-M2.7")
# # 向聊天模型发问
# print(
#     model.invoke(
#         [
#             SystemMessage(content="You are a helpful assistant that translates English to Chinese."),
#             HumanMessage(content="Translate this sentence from English to Chinese: I love programming."),
#         ]
#     )
# )

# 批量向模型提问
print(
    model.batch(
        [
            [
                SystemMessage(content="You are a helpful assistant that translates English to Chinese."),
                HumanMessage(content="Translate this sentence from English to Chinese: I love programming."),
            ],
            [
                SystemMessage(content="You are a helpful assistant that translates English to Chinese."),
                HumanMessage(content="Translate this sentence from English to Chinese: I love programming."),
            ]
        ]
    )
)