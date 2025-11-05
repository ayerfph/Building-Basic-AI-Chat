# Define price per token
input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000

# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = max_completion_tokens

# Calculate cost
cost = (input_tokens * input_token_price + output_token * output_token_price)

# Show output
print(f"Estimate cost: ${cost}")
