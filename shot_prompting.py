# Shot Prompting : Including examples to guide
# - Zero-Shot : No examples, just instructions
# - One-Shot : One example guides the response
# - Few-Shot : Multiple examples provide more context

# Zero-Shot Prompting
zero_shot_prompt = """Classify sentiment as 1-5 (bad-good) in the following statements:
1. Meal was decent, but I've had better
2. My food was delayed, but drinks were good.
"""

# One-Shot Prompting
one_shot_prompt = """Classify sentiment as 1-5 (bad-good) in the following statements:
1. The service was very slow -> 1
2. Meal was decent, but I've had better. ->
3. My food was delayed, but drinks were good. ->
"""

#Few-Shot Prompting
few_shot_prompt = """Classify sentiment as 1-5 (bad-good) in the following statements:
1. The service was very slow -> 1
2. The steak was awfully good -> 5
3. It was ok, no massive complaints. -> 3
2. Meal was decent, but I've had better. ->
3. My food was delayed, but drinks were good. ->
"""
