from anthropic.types import MessageParam, TextBlock
from anthropic import Anthropic


def add_user_message(messages: list[MessageParam], content):
    message = {"role": "user", "content": content}
    messages.append(message)


# LLM Generated message
def add_assistant_message(messages: list[MessageParam], content):
    message = {"role": "assistant", "content": content}
    messages.append(message)


def chat(
    model_name: str,
    client: Anthropic,
    messages: list[MessageParam],
    system_prompt=None,
    temperature=0.5,
    stop_sequences=[],
) -> str:

    params = {
        "model": model_name,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
        "stop_sequences": stop_sequences,
    }

    if system_prompt:
        params["system"] = system_prompt

    reply = client.messages.create(**params)
    return reply.content[0].text
