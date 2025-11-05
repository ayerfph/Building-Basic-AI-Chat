# some code here...
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content":"Put some words here."}],
  # Temperature is the one controls on determinism where 0 is highly deterministic and 2 is very random
  temperature=2
)

print(response.choice[0].message.content)
