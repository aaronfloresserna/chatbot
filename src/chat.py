import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": "que es chatgpt?"}]
)

print(completion.choices[0].message.content)