from openai import OpenAI

client = OpenAI(api_key="ENTER YOUR KEY HERE")

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role":"user", "content":"Put the prompt here"}]
)

print(response.choices[0].message.content)
