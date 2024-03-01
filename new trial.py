import openai
from apikey import api_data

openai.api_key=api_data

"""captain: how are you? 
openai: i am fine
"""

completion=openai.completion()

def Reply(question):
    prompt=f'captain: {question}\n Jarvis: '
    response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Chando'], max_tokens=200)
    answer=response.choices[0].text.strip()
    return answer

ans=Reply("what is ai")
print (ans)