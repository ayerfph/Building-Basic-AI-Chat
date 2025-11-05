# some code here...
prompt = "Generate a powerful tagline for a new electric vehicle that highlights innovation and sustainability"

# Generating response
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}]
)

# Show response
print(response.choice[0].message.content)
