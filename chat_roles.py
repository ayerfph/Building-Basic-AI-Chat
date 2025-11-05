# Single-turn tasks
# - Text Generation
# - Text transformation
# - Classification

# Multi-turn conversations
# - Build on previous prompts and responses

# Roles
# - System : Controls assistant's behavior
# - User : Instruct the assistant
# - Assistant : response to user instruction

# Can also be written by the developer to provide examples

# Just a note not included in the actual code
default_response_sample = """
response = client.chat.completions.create(
  model="gpt-4o-mini",
  message=[{"role": "user", "content": prompt}]
)
"""

# First Example : Prompt Setup (Putting The Roles In Messages)
messages=[{"role": "system", "content": "You are a Python programming tutor who speaks concisely."},
          {"role": "user", "content": "What is the difference between mutable and immutable objects?"}]

# Apply To Request Response
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "system", "content": "You are a Python programming tutor who speaks concisely."},
          {"role": "user", "content": "What is the difference between mutable and immutable objects?"}]
)

# Second Example : Mitigating Misuse With System Messages
sys_msg = """
You are finance education assistant that helps student study for exams.

If you are asked for specific, real-world financial advice with risk to their finances, respond with:

I'm sorry, I am not allowed to provide financial advice.
"""

# Adding the Mitigating Misuse With System Messages
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "system", "content": sys_msg},
          {"role": "user", "content": "Which stocks should I invest in?"}]
)

# Show output
print(response.choices[0].message.content)
