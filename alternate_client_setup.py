from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role":"user", "content":"Put the prompt here"}],
  max_completion_tokens=100
)

print(response.choices[0].message.content)
