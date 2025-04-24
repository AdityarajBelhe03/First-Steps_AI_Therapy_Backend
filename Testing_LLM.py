from openai import OpenAI

# Initializing OpenRouter client
client = OpenAI(
    base_url="Put the url here",
    api_key="put the API here",
)

# First prompt to test LLM
completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout:free",
    messages=[
        {
            "role": "user",
            "content": "Hi, how are you?"
        }
    ]
)

# Printing the response
print(completion.choices[0].message.content)