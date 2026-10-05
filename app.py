import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

token = os.getenv("HF_TOKEN")

client = InferenceClient(
    provider="novita",
    api_key=token
)

print("Hugging Face connected!")

topic = input("Enter your topic: ")

response = client.chat.completions.create(
    model="zai-org/GLM-5.3",
    messages=[
        {
            "role": "user",
            "content": f"""
Create exactly 5 flashcards about {topic}.

Use this format:

1. Q: What is ...?
   A: ...

2. Q: What is ...?
   A: ...

3. Q: ...
   A: ...

4. Q: ...
   A: ...

5. Q: ...
   A: ...

Rules:
- Give exactly 5 flashcards.
- Each flashcard must have a question and an answer.
- Keep answers short and simple.
- Do not give any introduction or extra text.
"""
        }
    ],
    max_tokens=800
)

print("\n" + response.choices[0].message.content)