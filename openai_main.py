import openai

openai.api_key = "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"

# question = "what are the products"
# question = "what are your testimonials"
# question = "how many badges you have"
# question = "list all your badges"
# question = "list all your badges links"
# question = "what services do you offer"
# question = "tell me your HAPPY CUSTOMERS REVIEWS"
question = "what Support does EngageBay offer"


with open("gpt-input.txt", "r") as f:
    s_t = f.read()

prompt_text = f'{s_t}:{question}:'
message_log = [{"role": "user", "content": prompt_text}]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_log,
    max_tokens=150,
    stop=None,
    temperature=0.7,
)

print(response.choices[0].message.content)
