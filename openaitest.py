from openai import OpenAI
import os
print(os.getenv("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"))

client = OpenAI()

client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "write an email to my boss for resignation?\n"
    },
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)